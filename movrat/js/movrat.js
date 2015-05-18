var fs = require('fs');
var mergesort = require('./mergesort');

input_file  = '../testdata/movrat.in'
output_file = '../testdata/movrat.out'

var file_data = fs.readFileSync(input_file, 'utf8').split('\n');

var n = +file_data[0];
var rates = file_data[1].split(' ').map(function(rate){ return +rate });
var lowIgnoreCount = +file_data[2];
var highIgnoreCount = +file_data[3];

// inplace sort
mergesort(rates);

var stripped_rates = rates.slice(lowIgnoreCount, n - highIgnoreCount);
var sum = stripped_rates.reduce(function(a,b){return a + b}, 0);
var average = Math.floor( sum / stripped_rates.length );

// write out
fs.writeFileSync(output_file, ''+average);
