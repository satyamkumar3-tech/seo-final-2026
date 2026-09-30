#!/usr/bin/env python3
"""Generate Type 3 Higgsfield images through the CLI with a small concurrency limit."""
from __future__ import annotations

import concurrent.futures
import json
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def raw_path_for(final_path: str) -> Path:
    path = ROOT / final_path
    return path.with_suffix(".raw.png")


def run_slot(manifest_path: Path, slot: str, force: bool = False) -> dict[str, object]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    cfg = manifest["slots"][slot]
    final_path = ROOT / manifest["output"][slot]
    output_raw = raw_path_for(manifest["output"][slot])
    output_raw.parent.mkdir(parents=True, exist_ok=True)
    job_key = f"{slot}_accepted_cli_candidate"
    existing = manifest.get("higgsfield_jobs", {}).get(job_key)
    if not force and existing and (output_raw.exists() or final_path.exists()):
        return {
            "manifest": str(manifest_path.relative_to(ROOT)),
            "slot": slot,
            "job_id": existing.get("job_id"),
            "status": "reused",
            "result_url": existing.get("result_url"),
            "local_raw": existing.get("local_raw") or str(output_raw.relative_to(ROOT)),
            "reused": True,
        }
    cmd = [
        "higgsfield",
        "generate",
        "create",
        manifest.get("higgsfield", {}).get("model", "nano_banana_pro"),
        "--prompt",
        cfg["prompt"],
        "--aspect_ratio",
        manifest.get("higgsfield", {}).get("aspect_ratio", "16:9"),
        "--resolution",
        manifest.get("higgsfield", {}).get("resolution", "2k"),
    ]
    for image in cfg["local_reference_images"]:
        cmd += ["--image", str(ROOT / image)]
    cmd += ["--wait", "--wait-timeout", "20m", "--wait-interval", "5s", "--json"]

    last_error = ""
    for attempt in range(2):
        proc = subprocess.run(cmd, text=True, capture_output=True)
        if proc.returncode == 0:
            data = json.loads(proc.stdout)
            job = data[0] if isinstance(data, list) else data
            url = job["result_url"]
            with urllib.request.urlopen(url, timeout=180) as response:
                output_raw.write_bytes(response.read())
            return {
                "manifest": str(manifest_path.relative_to(ROOT)),
                "slot": slot,
                "job_id": job.get("id"),
                "status": job.get("status"),
                "result_url": url,
                "local_raw": str(output_raw.relative_to(ROOT)),
                "reused": False,
            }
        last_error = (proc.stderr or proc.stdout or "").strip()
        if attempt == 0:
            time.sleep(45)
    raise RuntimeError(f"{manifest_path.name}:{slot} failed: {last_error}")


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit(
            "Usage: generate_type3_cli_batch.py manifest.json [manifest2.json...] "
            "[--slots hero,lifestyle] [--force]"
        )
    args = list(sys.argv[1:])
    force = "--force" in args
    if force:
        args.remove("--force")
    slots = ("hero", "flatlay", "lifestyle")
    if "--slots" in args:
        index = args.index("--slots")
        if index + 1 >= len(args):
            raise SystemExit("--slots requires a comma separated value")
        requested = tuple(value.strip() for value in args[index + 1].split(",") if value.strip())
        invalid = [value for value in requested if value not in slots]
        if invalid:
            raise SystemExit(f"Invalid slots: {invalid}")
        slots = requested
        del args[index : index + 2]
    manifests = [Path(arg) if Path(arg).is_absolute() else ROOT / arg for arg in args]
    tasks = [(manifest, slot) for manifest in manifests for slot in slots]
    results: list[dict[str, object]] = []
    failures: list[str] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        futures = {
            executor.submit(run_slot, manifest, slot, force): (manifest, slot)
            for manifest, slot in tasks
        }
        for future in concurrent.futures.as_completed(futures):
            manifest, slot = futures[future]
            try:
                result = future.result()
                results.append(result)
                action = "REUSED" if result.get("reused") else "GENERATED"
                print("DONE", action, result["manifest"], slot, result["job_id"], result["local_raw"], flush=True)
            except Exception as exc:  # noqa: BLE001
                failures.append(str(exc))
                print("FAILED", manifest, slot, exc, flush=True)
    by_manifest: dict[str, list[dict[str, object]]] = {}
    for result in results:
        by_manifest.setdefault(str(result["manifest"]), []).append(result)
    for manifest_rel, items in by_manifest.items():
        manifest = json.loads((ROOT / manifest_rel).read_text(encoding="utf-8"))
        jobs = manifest.setdefault("higgsfield_jobs", {})
        for item in items:
            jobs[f"{item['slot']}_accepted_cli_candidate"] = {
                "job_id": item["job_id"],
                "result_url": item["result_url"],
                "local_raw": item["local_raw"],
            }
        (ROOT / manifest_rel).write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        prefix = manifest.get("output_prefix") or Path(manifest_rel).stem
        results_path = ROOT / f"output/{prefix}_type3_generation_results_cli.json"
        previous = json.loads(results_path.read_text(encoding="utf-8")) if results_path.exists() else []
        merged = {str(item.get("slot")): item for item in previous}
        merged.update({str(item.get("slot")): item for item in items})
        results_path.write_text(
            json.dumps(list(merged.values()), indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    if failures:
        raise SystemExit("\n".join(failures))


if __name__ == "__main__":
    main()
