#!/usr/bin/env python3
"""Collect audio file paths and store them in a manifest file."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Iterable, Iterator, Optional, Set

DEFAULT_EXTENSIONS = {
    ".aif",
    ".aiff",
    ".alac",
    ".ape",
    ".flac",
    ".m4a",
    ".mp3",
    ".ogg",
    ".opus",
    ".wav",
    ".wma",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Scan directories for audio files and write absolute or relative paths "
            "to an inventory file (default: aalleaudio.txt)."
        )
    )
    parser.add_argument(
        "roots",
        nargs="+",
        help="One or more directory roots to scan for audio files.",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="aalleaudio.txt",
        help="Path to the output manifest file (default: %(default)s).",
    )
    parser.add_argument(
        "-e",
        "--extensions",
        help=(
            "Comma-separated list of file extensions to include. "
            "Defaults to common audio formats."
        ),
    )
    parser.add_argument(
        "-r",
        "--relative-to",
        help=(
            "Emit relative paths with respect to the provided directory. "
            "By default absolute paths are written."
        ),
    )
    parser.add_argument(
        "--follow-symlinks",
        action="store_true",
        help="Follow symbolic links when traversing directories.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print matches to stdout instead of writing to a file.",
    )
    return parser.parse_args()


def normalize_extensions(raw: str | None) -> Set[str]:
    if not raw:
        return DEFAULT_EXTENSIONS
    entries = {entry.strip().lower() for entry in raw.split(",") if entry.strip()}
    return {f".{ext[1:]}" if ext.startswith(".") else f".{ext}" for ext in entries}


def iter_audio_files(roots: Iterable[str], extensions: Set[str], follow_symlinks: bool) -> Iterator[Path]:
    seen: Set[Path] = set()
    for root in roots:
        root_path = Path(root).expanduser()
        if not root_path.exists():
            raise FileNotFoundError(f"Root path does not exist: {root_path}")
        if not root_path.is_dir():
            raise NotADirectoryError(f"Root path is not a directory: {root_path}")

        for dirpath, dirnames, filenames in os.walk(root_path, followlinks=follow_symlinks):
            current_dir = Path(dirpath)
            for filename in filenames:
                path = current_dir / filename
                if path.suffix.lower() not in extensions:
                    continue
                resolved = path.resolve()
                if resolved in seen:
                    continue
                seen.add(resolved)
                yield resolved


def format_path(path: Path, relative_to: Optional[Path]) -> str:
    if relative_to is None:
        return str(path)
    base = relative_to
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(base))
    except ValueError:
        # Fall back to absolute paths if the file is not located beneath the base.
        return str(resolved)


def main() -> int:
    args = parse_args()
    extensions = normalize_extensions(args.extensions)
    try:
        matches = list(iter_audio_files(args.roots, extensions, args.follow_symlinks))
    except (FileNotFoundError, NotADirectoryError) as error:
        print(error)
        return 1

    base: Optional[Path]
    if args.relative_to:
        base_candidate = Path(args.relative_to).expanduser()
        if not base_candidate.exists():
            print(f"relative-to path does not exist: {args.relative_to}")
            return 1
        base = base_candidate.resolve()
    else:
        base = None

    formatted = [format_path(path, base) for path in matches]

    formatted.sort()

    if args.dry_run:
        for line in formatted:
            print(line)
        return 0

    output_path = Path(args.output).expanduser()
    output_path.write_text("\n".join(formatted) + ("\n" if formatted else ""), encoding="utf-8")
    print(f"Wrote {len(formatted)} audio paths to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
