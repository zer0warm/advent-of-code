#! /bin/sh

grep -oE 'mul\([0-9]+?,[0-9]+?\)' input | sed -e 's/mul//' -e 's/,/*/' | paste -sd+ | bc

grep -oE "(mul\([0-9]+?,[0-9]+?\)|do\(\)|don't\(\))" input | awk "
BEGIN { enabled=1 }
/don't/ { enabled=0; next }
/do/ { enabled=1; next }
{ if ( enabled ) print }
" | sed -e 's/mul//' -e 's/,/*/' | paste -sd+ | bc
