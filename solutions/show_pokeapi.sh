#!/bin/bash

# This script uses jq -> https://stedolan.github.io/jq/download/

for q in $(seq 1 9)
do
    url=$(curl -s https://pokeapi.co/api/v2/pokemon/$q | jq -r ".sprites.front_default")
    ./imgcat --url $url
done
