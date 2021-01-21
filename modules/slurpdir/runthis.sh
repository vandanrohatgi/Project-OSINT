#!/bin/bash

./modules/slurpdir/slurp domain -p ./modules/slurpdir/permutations.json -c 50 -t $1 &> ./modules/slurpdir/slurp.txt
