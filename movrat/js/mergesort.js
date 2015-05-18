function sort(array){
    mergesort_internal(array, 0, array.length - 1)
}

var mergesort_internal = function(array, p, r) {
    if ( r > p ) {
        var q = Math.floor( (r - p)/2 ) + p;
        mergesort_internal(array, p, q);
        mergesort_internal(array, q+1, r);
        linear_merge(array, p, q, r);
    }
};

var linear_merge = function(array, p, q, r) {
    var lowHalf = [];
    var highHalf = [];
    var k = p; var i; var j;

    for (i = 0; k <= q; i++, k++) {
        lowHalf[i] = array[k];
    }
    for (j = 0; k <= r; j++, k++) {
        highHalf[j] = array[k];
    }
    k = p; i = 0; j = 0;

    while ( i < lowHalf.length && j < highHalf.length ){
        if ( lowHalf[i] < highHalf[j] ) {
            array[k] = lowHalf[i];
            i++;
        } else {
            array[k] = highHalf[j];
            j++;
        }
        k++;
    }

    while (i < lowHalf.length){
        array[k] = lowHalf[i];
        k++; i++;
    }

    while (j < highHalf.length){
        array[k] = highHalf[j];
        k++; j++;
    }

};

module.exports = sort;
