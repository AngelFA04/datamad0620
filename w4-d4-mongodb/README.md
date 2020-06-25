# Comandos

## Importar datos en mongdb desde un json

`mongoimport --db datamad0620 --collection companies ./companies.json`

## Importar datos desde una API via `curl`

`curl https://pokeapi.co/api/v2/pokemon/1 | mongoimport -d datamad0620 -c pokemons`


## Importart y procesar datos con `jq`

`curl https://pokeapi.co/api/v2/pokemon/25 | jq "{name: .name, image: .sprites.front_default}" | mongoimport -d datamad0620 -c pokemons`

# Operadores

- [https://docs.mongodb.com/manual/reference/operator/query/]

## Queries

- `"name":{"$eq":"Facebook"}`
- `{"founded_year":{"$gt":2010}}`
- `{$and:[{"founded_year":{"$gte":2010}}, {"founded_year":{"$lte":2011}}]}`
- `{category_code:{$in:["web","software"]}}`
- `{name:/^Face/i}`
- `{"offices":{$elemMatch:{"state_code":"CA"}}}`
- Compañias con como minimo una oficina en CA, y con mas de 1 oficina en total:

```json
  {
  "$and": [
    { "offices": { "$elemMatch": { "state_code": "CA" } } },
    { "offices": { "$not":{"$size": 1 } }}
  ]
}
```
