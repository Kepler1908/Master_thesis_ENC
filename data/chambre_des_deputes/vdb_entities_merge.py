#!/usr/bin/env python3
import argparse, glob, os, re, sys
def natural_key(s):
    return [int(t) if t.isdigit() else t for t in re.findall(r'\d+|\D+', s)]
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pattern", required=True, help="e.g. vdb_entities.json.part_*")
    ap.add_argument("--output", default="vdb_entities.json")
    args = ap.parse_args()

    parts = sorted(glob.glob(args.pattern), key=natural_key)
    if not parts:
        print("No parts matched.", file=sys.stderr); sys.exit(1)

    with open(args.output, "wb") as out:
        for p in parts:
            with open(p, "rb") as f:
                while True:
                    chunk = f.read(1024*1024)
                    if not chunk: break
                    out.write(chunk)
    print(f"Merged {len(parts)} parts -> {args.output}")

if __name__ == "__main__":
    main()
