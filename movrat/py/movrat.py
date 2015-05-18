# import sys
import os

from mergesort import merge_sort

input_file  = '../testdata/movrat.in'
output_file = '../testdata/movrat.out'

file_data = [line.strip() for line in open(input_file)]

n = int( file_data[0] )
rates = [ int(x) for x in file_data[1].split() ]
lowIgnoreCount = int( file_data[2] )
highIgnoreCount = int( file_data[3] )

sorted_rates = merge_sort( rates )
stripped_rates = sorted_rates[ lowIgnoreCount : (n - highIgnoreCount) ]

average = sum(stripped_rates)/len(stripped_rates)

print average

# write result
os.remove(output_file) # not sure how to overwrite instead of appending
with open (output_file, 'a') as f: f.write ( str(average) )
