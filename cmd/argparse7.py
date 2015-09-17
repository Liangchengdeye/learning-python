
# python argparse7.py 4
# python argparse7.py 4 -v
# python argparse7.py 4 -v 1
# python argparse7.py 4 -v 2

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, help="display a square of a given number")
parser.add_argument("-v","--verbose", type=int, help="increase output verbose")

args = parser.parse_args()
answer = args.square ** 2

if args.verbose == 2:
    print("the square of {} equals {}".format(args.square, answer))
elif args.verbose == 1:
    print("{}^2 == {}".format(args.square, answer))
else:
    print(answer)
