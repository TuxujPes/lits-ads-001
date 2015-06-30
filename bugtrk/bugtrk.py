def main():
    input_file_path = 'bugtrk.in'
    output_file_path = 'bugtrk.out'

    n, width, height = read_data(input_file_path)
    side = get_square_side(n, width, height)

    write_solution_to_file(output_file_path, side)


def get_square_side(n, width, height):
    square_side = max(width, height)

    while True:
        elems_in_row = square_side / width
        rows_in_square = square_side / height

        if elems_in_row * rows_in_square >= n:
            break
        # make sure we fill at least one more
        square_side += min(width, height)

    return square_side


def read_data(filename):
    with open(filename, 'r') as input_file:
        return [int(x) for x in input_file.readline().split()]


def write_solution_to_file(filename, solution):
    with open(filename, 'w') as output_file:
        output_file.write(str(solution))


if __name__ == '__main__':
    main()
