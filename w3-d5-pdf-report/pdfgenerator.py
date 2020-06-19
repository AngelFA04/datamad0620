# https://pyfpdf.readthedocs.io/en/latest/
# !pip3 install fpdf
from fpdf import FPDF 
from api.pokedex import pokedex
import pandas as pd

# FPDF('P', 'mm', 'A4')
pdf = FPDF()
pdf.add_page()

# fpdf.set_font(family, style = '', size = 0)
pdf.set_font("Arial", "B", 12)

# fpdf.text(x: float, y: float, txt: str)
pdf.text(10,10,"Hello, World!")
pdf.text(10,15,"Hola, Mundillo!")

# fpdf.set_xy(x: float, y: float)
pdf.set_xy(10, 20)

# fpdf.cell(w, h = 0, txt = '', border = 0, ln = 0, align = '', fill = False, link = '')
pdf.cell(0, h=10, txt = 'Snorlax Evolutive Line', border = 1, ln = 1, align = 'C', fill = False, link = '')

poke_data = pokedex("snorlax")
data = {pokemon.get("name"):pokemon.get("stats") for pokemon in poke_data["evolution_chain"].values()}
data = pd.DataFrame.from_dict(data)

columns = [""] + list(data.columns)
for col in columns:
    pdf.cell(63.3, 10, col.title(), 1, 0, "C")
pdf.ln()
for ind,row in data.iterrows():
    val = [ind] + [row[col] for col in data.columns]
    for v in val:
        pdf.cell(63.3, 10, str(v), 1, 0, "C")
    pdf.ln()

# fpdf.image(name, x = None, y = None, w = 0, h = 0, type = '', link = '')
pdf.image(poke_data["evolution_chain"][poke_data["id"]]["sprite"],pdf.get_x()+35.001,pdf.get_y() )



pdf.output("output/primerito_pdf.pdf")