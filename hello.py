import os
import sys
import argparse

def parse_args():
    parser = argparse.ArgumentParser("hello")
    parser.add_argument("-s", type=str, default='hello world!')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    print(args.s)