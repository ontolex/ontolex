#!/bin/bash

for f in `find . -name \*.ttl`
do
    NAME=${f/%.ttl/}
    NAME=${NAME:2}
    echo $NAME
    rapper -i turtle -o dot -I "http://www.w3.org/ns/lemon/$NAME#" $f | dot -Tpng > ${f/%ttl/png}
done
