import os
import json
from datetime import datetime
import requests
from dotenv import load_dotenv

load_dotenv()
response = requests.get(
    "https://tennis-api-atp-wta-itf.p.rapidapi.com/tennis/v2/extend/api/events/live",
    headers={
        "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),
        "X-RapidAPI-Host": "tennis-api-atp-wta-itf.p.rapidapi.com",
    },
)

# print(response.status_code)  # Exibe o código de status (ex: 200)
# print(response.json())

alcaraz_playing = False
# check if alcaraz is playing
resultado = {
    "checado_em": datetime.now().isoformat(),
    "jogando_agora": False,
    "adversario": "",
    "liga": "",
    "tourType": "",
    "score": "",
}
for match in response.json()["results"]:
    if match.get("status") == "InPlay" and (
        "Alcaraz" in match["participant1"] or "Alcaraz" in match["participant2"]
    ):
        print(
            f"Alcaraz is playing against {match['participant2'] if 'Alcaraz' in match['participant1'] else match['participant1']}"
        )
        alcaraz_playing = True
        resultado["jogando_agora"] = True
        resultado["adversario"] = (
            match["participant2"]
            if "Alcaraz" in match["participant1"]
            else match["participant1"]
        )
        resultado["liga"] = match["league"]
        resultado["tourType"] = match["tourType"]
        resultado["score"] = match["score"]
if not alcaraz_playing:
    print("Alcaraz is not playing at the moment")

with open("resultado.json", "w") as f:
    json.dump(resultado, f, indent=4)
