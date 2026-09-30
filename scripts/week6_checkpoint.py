#!/usr/bin/env python3
"""Atomic per-rank checkpoints for the Week 6 article pipeline."""
from __future__ import annotations

import argparse
import fcntl
import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


STEPS = (
    "read_docs",
    "verify_higgsfield",
    "inspect_row",
    "duplicate_check",
    "serp_intelligence",
    "fact_check",
    "keyword_map",
    "structure_visuals",
    "draft",
    "product_media",
    "publish_wordpress",
    "generate_type3",
    "patch_type3",
    "live_qa",
    "update_status",
    "final_report",
)
VALID_STATUSES = {"pending", "running", "done", "failed", "skipped"}


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def atomic_save(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data["updated_at"] = now()
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(data, handle, indent=2, ensure_ascii=False)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def parse_details(values: list[str]) -> dict[str, Any]:
    details: dict[str, Any] = {}
    for value in values:
        if "=" not in value:
            raise SystemExit(f"Invalid --detail {value!r}; expected key=value")
        key, raw = value.split("=", 1)
        try:
            details[key] = json.loads(raw)
        except json.JSONDecodeError:
            details[key] = raw
    return details


def mutate(path: Path, callback) -> dict[str, Any]:
    lock_path = path.with_suffix(path.suffix + ".lock")
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open("a+", encoding="utf-8") as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        data = load(path)
        callback(data)
        atomic_save(path, data)
        return data


def init_checkpoint(args: argparse.Namespace) -> None:
    path = Path(args.path)

    def update(data: dict[str, Any]) -> None:
        data.setdefault("pipeline", "week6")
        data.setdefault("rank", args.rank)
        data.setdefault("slug", args.slug)
        data.setdefault("primary", args.primary)
        data.setdefault("created_at", now())
        data.setdefault("status", "pending")
        steps = data.setdefault("steps", {})
        for step in STEPS:
            steps.setdefault(step, {"status": "pending"})

    data = mutate(path, update)
    print(json.dumps(data, indent=2, ensure_ascii=False))


def mark_checkpoint(args: argparse.Namespace) -> None:
    if args.step not in STEPS:
        raise SystemExit(f"Unknown step {args.step!r}; choose from {', '.join(STEPS)}")
    if args.status not in VALID_STATUSES:
        raise SystemExit(f"Invalid status {args.status!r}")
    details = parse_details(args.detail)
    path = Path(args.path)

    def update(data: dict[str, Any]) -> None:
        steps = data.setdefault("steps", {})
        entry = steps.setdefault(args.step, {})
        entry["status"] = args.status
        if args.status == "running":
            entry["started_at"] = now()
        if args.status in {"done", "failed", "skipped"}:
            entry["finished_at"] = now()
        entry.update(details)
        if args.status == "failed":
            data["status"] = "failed"
        elif all(steps.get(step, {}).get("status") in {"done", "skipped"} for step in STEPS):
            data["status"] = "complete"
            data["completed_at"] = now()
        elif data.get("status") != "failed":
            data["status"] = "running"

    data = mutate(path, update)
    print(json.dumps(data["steps"][args.step], ensure_ascii=False))


def show_checkpoint(args: argparse.Namespace) -> None:
    path = Path(args.path)
    print(json.dumps(load(path), indent=2, ensure_ascii=False))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init")
    init.add_argument("--path", required=True)
    init.add_argument("--rank", type=int, required=True)
    init.add_argument("--slug", required=True)
    init.add_argument("--primary", required=True)
    init.set_defaults(func=init_checkpoint)

    mark = sub.add_parser("mark")
    mark.add_argument("--path", required=True)
    mark.add_argument("--step", required=True)
    mark.add_argument("--status", required=True)
    mark.add_argument("--detail", action="append", default=[])
    mark.set_defaults(func=mark_checkpoint)

    show = sub.add_parser("show")
    show.add_argument("--path", required=True)
    show.set_defaults(func=show_checkpoint)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
