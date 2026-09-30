import json
import os
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import week6_checkpoint
import week6_pipeline


rank = 5
row = week6_pipeline.load_week6_rows()[rank]
checkpoint_path = ROOT / "output/checkpoints/week6_rank5.json"
checkpoint = week6_checkpoint.load(checkpoint_path)

week6_pipeline.upsert_status_record(
    row,
    checkpoint,
    status="published",
    notes=(
        "Gift guide; categories Gift and Wedding Jewellery; live QA passed; "
        "supporting phrases inferred; competitor URL absent; facts not applicable; "
        "carousel SKUs BVPJ0935C06, BIAR0097R07, BISA0255D05, BIIP0550P16, "
        "BIAV0865V25, BIAV0987N78; Type 3 SKUs BVPJ0935C06, BIPM0017R18, BIAV0865V24"
    ),
)

rotation_path = ROOT / "output/product_rotation.json"
rotation = json.loads(rotation_path.read_text(encoding="utf-8"))
rank_label = "Week6 Rank 5"

trio = {
    "rank": rank_label,
    "hero": "BVPJ0935C06 The Shubhlatika Mangalsutra Necklace",
    "flatlay": "BIPM0017R18 The Malibu Ring",
    "lifestyle": "BIAV0865V24 The Pervinca Charm Holder Bracelet",
}
rotation["recent_type3_trios"] = [
    item for item in rotation.get("recent_type3_trios", []) if item.get("rank") != rank_label
] + [trio]

setting = {
    "rank": rank_label,
    "setting": "marble-vanity",
    "note": "wedding gifts for girls The Malibu Ring",
}
rotation["recent_flatlay_settings"] = [
    item for item in rotation.get("recent_flatlay_settings", []) if item.get("rank") != rank_label
] + [setting]
rotation["updated"] = "2026-08-18"

file_descriptor, temporary_name = tempfile.mkstemp(
    prefix=f".{rotation_path.name}.", dir=rotation_path.parent
)
try:
    with os.fdopen(file_descriptor, "w", encoding="utf-8") as handle:
        json.dump(rotation, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temporary_name, rotation_path)
finally:
    if os.path.exists(temporary_name):
        os.unlink(temporary_name)

print("status_csv_upserted rank 5")
print("product_rotation_upserted Week6 Rank 5")
