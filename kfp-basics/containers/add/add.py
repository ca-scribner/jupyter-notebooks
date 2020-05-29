import argparse


def parse_args():
	parser = argparse.ArgumentParser(description="Add one or more numbers")
	parser.add_argument(
		"output_file",
		type=str,
		help="Filename to write result to"
		)
	parser.add_argument(
		"numbers", 
		type=float, 
		nargs="+",
		help="One or more numbers"
	)
	args = parser.parse_args()
	return args


def main(args):
	x = sum(args.numbers)
	with open(args.output_file, 'w') as fout:
		fout.write(str(x))


if __name__ == "__main__":
	args = parse_args()
	main(args)