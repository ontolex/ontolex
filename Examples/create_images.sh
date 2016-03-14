#!/bin/bash

for f in `find . -name \*.ttl`
do
    NAME=${f/%.ttl/}
    NAME=${NAME:2}
    if [[ $NAME != lime-old* ]]
    then
        if [[ $f -nt ${f/%ttl/png} || (-e ${f/%ttl/LR} && ${f/%ttl/LR} -nt ${f/%ttl/png}) ]]
        then
            echo $NAME
            if [ -e ${f/%ttl/LR} ]
            then
                python3 convert_to_dot.py $f | dot -Tpng -Grankdir=LR > ${f/%ttl/png}
            else
                python3 convert_to_dot.py $f | dot -Tpng > ${f/%ttl/png}
            fi
        fi
    fi
done
