from dateutil.parser import parse as parse_date
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--infile", type=argparse.FileType("r"), default="-")
    args = parser.parse_args()

    start = None
    for line in args.infile:
        line = line.strip()

        try:
            d = line.split()[0]
        except IndexError:
            continue

        dt = parse_date(d)
        if not dt:
            print(f"-1 {line}")

        if start is None:
            start = dt

        delta = dt - start
        print(f"{delta} {line}")
