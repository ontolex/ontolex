#!/bin/bash

for f in `find . -name \*.ttl`
do
    NAME=${f/%.ttl/}
    NAME=${NAME:2}
    if [[ $NAME != lime-old* ]]
    then
        if [[ $f -nt ${f/%ttl/png} ]]
        then
            echo $NAME
            python3 convert_to_dot.py $f | dot -Tpng > ${f/%ttl/png}
        fi
    fi
done
