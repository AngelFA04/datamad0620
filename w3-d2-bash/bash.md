# Bash terminal

- `<command> --help` Ver ayuda
- `man <command>` Ver ayuda
- `wc -l` cuenta lineas de stdout
- `grep` filtra stdout
- `cut` recorta stdout por filas y campos
- `sort` ordena los resultados de stdout


## Some bash commands:

- `cat ../data/pokemon.csv | grep "Pikachu"`
- `cat ../data/pokemon.csv | cut -d , -f 2,3 | grep "Water" > pokemon_water.csv`

## Running our own pipe 
- `python3 mypipe.py | say`


## Other commands
- `cat videos.txt | xargs youtube-dl -o "videos/%(id)s.%(ext)s" -x --audio-format "mp3"`

## Utils
- https://code.visualstudio.com/docs/editor/codebasics
- https://github.com/ytdl-org/youtube-dl