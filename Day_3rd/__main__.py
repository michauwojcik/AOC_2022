
import sys
import os
import argparse

sys.path.append("Day_3rd/src")
sys.path.append("Common")

from src.main import main

parser = argparse.ArgumentParser()
parser.add_argument("--filepath", help="a relative path to filename with rucksacks inventory", type=str)
args = parser.parse_args()

main(args.filepath)