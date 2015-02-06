#!/bin/bash

for f in `find . -name \*.ttl`
do
    NAME=${f/%.ttl/}
    NAME=${NAME:2}
    echo $NAME
    if [[ $NAME != lime-old* ]]
    then
        python3 convert_to_dot.py $f | dot -Tpng > ${f/%ttl/png}
    fi
done
