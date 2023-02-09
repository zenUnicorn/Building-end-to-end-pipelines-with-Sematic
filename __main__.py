"""
This is the entry point of your pipeline.

This is where you import the pipeline function from its module and resolve it.
"""
# Sematic
import argparse
from .pipeline import pipeline

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Hello World")
    parser.add_argument("--name", type=str, required=True)

    args = parser.parse_args()

    pipeline(args.name).resolve()
