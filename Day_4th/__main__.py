
import sys
import os
import argparse

sys.path.append("Day_4th/src")
sys.path.append("Common")

from src.main import main

parser = argparse.ArgumentParser()
parser.add_argument("--filepath", help="a relative path to filename with game's strategy", type=str)
args = parser.parse_args()

main(args.filepath)