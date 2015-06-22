def main():
    input_file_path = 'bugtrk.in'
    output_file_path = 'bugtrk.out'

    n, w, h = read_data(input_file_path)
    side = get_square_side(n, w, h)

    write_solution_to_file(output_file_path, side)


def get_square_side(n, w, h):
    s = w if w > h else h
    sn = n
    while n != 0:
        j = s
        while n > 0 and j - h >= 0:
            j -= h
            i = s
            while n > 0 and i - w >= 0:
                i -= w
                n -= 1
        if n > 0:
            s += 1
            n = sn
    return s


def read_data(filename):
    with open(filename, 'r') as input_file:
        return [int(x) for x in input_file.readline().split()]


def write_solution_to_file(filename, solution):
    with open(filename, 'w') as output_file:
        output_file.write(str(solution))


if __name__ == '__main__':
    main()
