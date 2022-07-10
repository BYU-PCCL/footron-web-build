import argparse
import json
from pathlib import Path
from .build import WebBuilder

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build a Footron web app.")
    parser.add_argument("web_source_path", type=Path)
    parser.add_argument("output_path", type=Path)
    parser.add_argument("experience_paths", nargs="+", type=Path)
    parser.add_argument("--color-output-path", type=Path)
    parser.add_argument("--debug", action="store_true")

    args = parser.parse_args()
    color_output_path = args.color_output_path
    builder = WebBuilder(
        args.web_source_path,
        args.output_path,
        args.experience_paths,
        generate_colors=bool(color_output_path),
        debug=args.debug,
    )
    output = builder.build()

    if color_output_path:
        with open(color_output_path, "w") as color_file:
            color_data = {}
            for experience in output.experiences:
                if not hasattr(experience, "colors"):
                    continue

                color_data[experience.id] = {
                    "primary": experience.colors.primary,
                    "secondary_light": experience.colors.secondary_light,
                    "secondary_dark": experience.colors.secondary_dark,
                }
            json.dump(color_data, color_file)
