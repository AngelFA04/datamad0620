import requests

def get_poke_data(poke_id):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke_id}")
    data = response.json()
    poke_data = {"name":data.get("name"),
                 "sprite":data.get("sprites").get("front_default"),
                 "stats":{stat.get("stat").get("name"):stat.get("base_stat") for stat in data.get("stats")},
                 "types":list(zip(*sorted([[typ,order] for order,typ in {typ.get("slot"):typ.get("type").get("name") for typ in data.get("types")}.items()],key=lambda x: x[1])))[0]
                }
    return poke_data

def get_evolutions(chain):
    evolution = {}
    poke_id = int(chain.get("species").get("url").split("/")[-2])
    evolution[poke_id] = get_poke_data(poke_id)
    if chain.get("evolves_to"):
        for evol in [get_evolutions(evol) for evol in chain.get("evolves_to")]:
            evolution = {**evolution, **evol}
    return evolution

def pokedex(poke_id):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke_id}")
    data = response.json()
    species = requests.get(data.get("species").get("url"))
    species_data = species.json()
    evolution_chain = requests.get(species_data.get("evolution_chain").get("url"))
    evolution_chain_data = evolution_chain.json()
    species_data
    pokedex_data = {
                    "id":species_data.get("id"),
                    "capture_rate":species_data.get("capture_rate"),
                    "flavor_text":species_data.get("flavor_text_entries")[0].get("flavor_text").replace("\n", " ").replace("\x0c"," ").strip(),
                    "evolution_chain":get_evolutions(evolution_chain_data.get("chain"))
                   }
    return pokedex_data      