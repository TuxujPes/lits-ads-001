from quicksort import QuickSortAlgorithm

input_file = 'discnt.in'
output_file = 'discnt.out'
disc_nth = 3
qsort = QuickSortAlgorithm()
# prepare data
file_data = [line.strip() for line in open(input_file)]
item_prices = [int(x) for x in file_data[0].split()]
discount = int(file_data[1]) * 0.01

items_q = len(item_prices)
disc_pivot = items_q - items_q / disc_nth
price_sum = 0

# sort so we discount only most expensive ones
qsort.sort(item_prices)

# sum based on nth and discount
for idx, price in enumerate(item_prices):
    price_sum += price if idx < disc_pivot else price * (1 - discount)

# write to file
with open(output_file, 'w') as f:
    f.write('%.2f' % price_sum)
