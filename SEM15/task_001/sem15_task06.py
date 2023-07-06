from hw15_utils import walk_dir
import argparse


def parse_ars():
    parser = argparse.ArgumentParser(description='sem15t001_s15t06')
    parser.add_argument('-p', metavar='path', type=str, nargs='*', default='.', help='Enter a path(s) to directory(s) to list')
    args = parser.parse_args()
    return args.p


def main():
    for place in parse_ars():
        for item in (walk_dir(place)):
            print(repr(item))


if __name__ == '__main__':
    # CLI example: -p hw15_utils ../task01
    main()