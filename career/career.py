def main():
    input_file_path = 'career.in'
    output_file_path = 'career.out'

    n, exps = read_data(input_file_path)

    for y in range((len(exps) - 2), -1, -1):
        for x in xrange(len(exps[y])):
            left = exps[y + 1][x]
            right = exps[y + 1][x + 1]
            best = max(left, right)
            exps[y][x] += best

    solution = exps[0][0]

    write_solution_to_file(output_file_path, solution)

def read_data(filename):
    with open(filename, 'r') as input_file:
        n = int(input_file.readline())
        arr = []
        for line in input_file:
            arr.append([int(x) for x in line.rstrip('\n').split()])
        return n, arr


def write_solution_to_file(filename, solution):
    with open(filename, 'w') as output_file:
        output_file.write(str(solution) + '\n')


if __name__ == '__main__':
    main()
