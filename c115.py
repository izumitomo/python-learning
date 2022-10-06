import sys

def main(lines):
	first_line = lines.pop(0).split()
	N = int(first_line[0])
	W = int(first_line[1])
	distance = 0

	number_list = list(map(int, lines))
	for i in number_list:
		if i <= W:
			distance += i
	print(distance)

if __name__ == '__main__':
	lines = []
	for l in sys.stdin:
		lines.append(l.rstrip('\r\n'))
	main(lines)
