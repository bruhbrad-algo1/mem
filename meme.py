memes = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "ROFL": "una respuesta a una broma",
    "SHEESH": "ligera desaprobación",
    "CREEPY": "aterrador, siniestro",
    "AGGRO": "ponerse agresivo/enojado",
}

palabra = input("Escribe una palabra que no entiendas (con mayusculas por favor!): ").upper()

if palabra in memes.keys():
    print(memes[palabra])
else:
    print("no se")
