import os
import json
import requests
import argparse
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
response = requests.get(
    "https://tennis-api-atp-wta-itf.p.rapidapi.com/tennis/v2/extend/api/events/live",
    headers={
        "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),
        "X-RapidAPI-Host": "tennis-api-atp-wta-itf.p.rapidapi.com",
    },
)

parser = argparse.ArgumentParser()
parser.add_argument("jogador", nargs="?", default="Alcaraz")
args = parser.parse_args()

jogador_playing = False
jogador_recebido = args.jogador.lower()

resultado = {
    "checado_em": datetime.now().isoformat(),
    "jogador": "",
    "jogando_agora": False,
    "adversario": "",
    "liga": "",
    "tourType": "",
    "score": "",
}

for match in response.json()["results"]:
    p1 = match["participant1"].lower()
    p2 = match["participant2"].lower()
    if match.get("status") == "InPlay" and (
        jogador_recebido in p1 or jogador_recebido in p2
    ):
        jogador = (
            match["participant1"] if jogador_recebido in p1 else match["participant2"]
        )
        adversario = (
            match["participant2"] if jogador_recebido in p1 else match["participant1"]
        )
        print(f"{jogador} is playing against {adversario}")
        jogador_playing = True
        resultado["jogador"] = jogador
        resultado["jogando_agora"] = True
        resultado["adversario"] = adversario
        resultado["liga"] = match["league"]
        resultado["tourType"] = match["tourType"]
        resultado["score"] = match["score"]

if not jogador_playing:
    print(f"{args.jogador} is not playing at the moment")

with open("resultado.json", "w") as f:
    json.dump(resultado, f, indent=4)

print(json.dumps(resultado, indent=4))
