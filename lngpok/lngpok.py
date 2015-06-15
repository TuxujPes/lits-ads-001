from quicksort import QuickSortAlgorithm

qsort = QuickSortAlgorithm()


def main():
    input_file_path = "testdata/lngpok2.in"
    output_file_path = "testdata/lngpok.out"

    cards = read_cards_from_file(input_file_path)
    qsort.sort(cards)  # O(n log n)
    jokers = get_jokers(cards)  # O( zeros n )

    uniques = get_unique_list(cards)  # O( n )
    longest_streak = get_longest_streak(uniques, jokers) + jokers  # O(n^2)
    write_solution_to_file(output_file_path, longest_streak)
    print longest_streak


def get_longest_streak(cards, jokers):
    n = len(cards)
    start = 1 if jokers > 0 else 0
    longest_streak = 1
    for i in xrange(start, n):
        for j in xrange(i + 1, n):
            if is_enough_jokers_to_fill(cards, i, j, jokers):
                streak = j - i + 1
                if streak > longest_streak:
                    longest_streak = streak
            else:
                break
    return longest_streak


def is_enough_jokers_to_fill(cards, start, end, jokers):
    return (cards[end] - cards[start]) - (end - start) <= jokers


def get_unique_list(cards):
    uniques = []
    for card in cards:
        if card not in uniques:
            uniques.append(card)
    return uniques


def get_jokers(cards):
    count = 0
    for card in cards:
        if card > 0:
            break
        else:
            count += 1
    return count


def read_cards_from_file(filename):
    with open(filename, "r") as input_file:
        return [int(x) for x in input_file.readline().split()]


def write_solution_to_file(filename, solution):
    with open(filename, 'w') as output_file:
        output_file.write(str(solution))


if __name__ == "__main__":
    main()
