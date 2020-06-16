#!/usr/bin/env python3

import random 
import sys
import os

def saluda(lugar, lang="es"):
    a = random.choice(["Felipe","Amanda","Marc"])
    if lang == "es":
        return f"Hola {a} desde {lugar}"
    elif lang == "en":
        return f"Hello {a} from {lugar}"
    else:
        return "Unrecognized language"

print(sys.argv)
lang = sys.argv[2]
lugar = sys.argv[4] if len(sys.argv) >=4 else os.getenv("LUGAR")

data = saluda(lugar, lang)
print(data)


