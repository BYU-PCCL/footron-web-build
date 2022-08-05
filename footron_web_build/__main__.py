import argparse
import json
from pathlib import Path
from .build import WebBuilder

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build a Footron web app.")
    parser.add_argument("web_source_path", type=Path)
    parser.add_argument("output_path", type=Path)
    parser.add_argument("experience_paths", nargs="+", type=Path)
    parser.add_argument("--debug", action="store_true")

    args = parser.parse_args()
    builder = WebBuilder(
        args.web_source_path,
        args.output_path,
        args.experience_paths,
        debug=args.debug,
    )
    output = builder.build()
