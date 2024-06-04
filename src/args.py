import argparse
import os

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("out_dir", type=str, help="path to output directory")
    args = parser.parse_args()
    if not os.path.isdir(args.out_dir):
        print(f"\nDirectory \"{args.out_dir}\" not found.\n")
        parser.print_help()
        exit(1)
    return args