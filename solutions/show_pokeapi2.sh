#!/bin/bash

# This script uses jq -> https://stedolan.github.io/jq/download/
echo "Showing pokemons"
for q in $(seq 1 9)
do
    data=$(curl -s https://pokeapi.co/api/v2/pokemon/$q)
    url=$(echo "$data" | jq -r ".sprites.front_default")
    name=$(echo "$data" | jq -r ".name")
    echo "Hello $name"
    ./imgcat --url $url
done
