#!/usr/bin/env python3
"""Atomic per-rank checkpoints for the Week 7 article pipeline."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import week6_checkpoint as base


STEPS = base.STEPS
VALID_STATUSES = base.VALID_STATUSES
load = base.load
mutate = base.mutate
now = base.now


def init_checkpoint(args: argparse.Namespace) -> None:
    def update(data: dict[str, Any]) -> None:
        data.setdefault("pipeline", "week7")
        data.setdefault("rank", args.rank)
        data.setdefault("slug", args.slug)
        data.setdefault("primary", args.primary)
        data.setdefault("created_at", now())
        data.setdefault("status", "pending")
        steps = data.setdefault("steps", {})
        for step in STEPS:
            steps.setdefault(step, {"status": "pending"})

    data = mutate(Path(args.path), update)
    print(json.dumps(data, indent=2, ensure_ascii=False))


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
    mark.set_defaults(func=base.mark_checkpoint)

    show = sub.add_parser("show")
    show.add_argument("--path", required=True)
    show.set_defaults(func=base.show_checkpoint)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
