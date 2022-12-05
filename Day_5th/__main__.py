
import sys
import os
import argparse

sys.path.append("Day_5th/src")
sys.path.append("Common")

from src.main import main

parser = argparse.ArgumentParser()
parser.add_argument("--filepath", help="a relative path to filename with a drawing of crates", type=str)
args = parser.parse_args()

main(args.filepath)