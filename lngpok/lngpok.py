from quicksort import QuickSortAlgorithm

qsort = QuickSortAlgorithm()

def main():
    input_file_path = "testdata/lngpok.in"
    output_file_path = "testdata/lngpok.out"

    cards = read_cards_from_file(input_file_path)
    qsort.sort(cards)
    jokers = get_jokers(cards)

    get_longest_streak(cards, jokers)
    write_solution_to_file(output_file_path, jokers)
    print cards
    print jokers

def get_longest_streak(cards, jokers):
    n = len(cards)
    for i in xrange(jokers, n):
        for j in xrange(jokers+1, n):
            print cards[j] - cards[i]

def get_needed_jokers_to_fill(cards, start, end, jokers):
    for

def get_unique_list(cards):
    unique = [for card in cards]

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
