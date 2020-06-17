#!/bin/bash

echo "hola"

for i in {1..10}
do
    echo "Hola $i"
done

for f in $(cat nombres.txt)
do
    echo "Hola $f"
done

for q in $(seq 1 2 10)
do
    echo "El numero es el $q"
done