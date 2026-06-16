import random

# IMPOSSIBLE-werkwoorden (12 stuks)
verbs = [
    "ir", "ser", "decir", "venir", "dormir", "morir",
    "ver", "poner", "hacer", "oír", "leer", "construir"
]

persons = ["yo", "tú", "él/ella", "nosotros", "vosotros", "ellos"]
tenses = ["presente", "perfecto", "imperfecto", "gerundio"]

def conjugate(verb, person, tense):

    # === PRESENTE ===
    if tense == "presente":

        # ir
        if verb == "ir":
            forms = {
                "yo": "voy", "tú": "vas", "él/ella": "va",
                "nosotros": "vamos", "vosotros": "vais", "ellos": "van"
            }
            return f"{person} {forms[person]}"

        # ser
        if verb == "ser":
            forms = {
                "yo": "soy", "tú": "eres", "él/ella": "es",
                "nosotros": "somos", "vosotros": "sois", "ellos": "son"
            }
            return f"{person} {forms[person]}"

        # decir
        if verb == "decir":
            forms = {
                "yo": "digo", "tú": "dices", "él/ella": "dice",
                "nosotros": "decimos", "vosotros": "decís", "ellos": "dicen"
            }
            return f"{person} {forms[person]}"

        # venir
        if verb == "venir":
            forms = {
                "yo": "vengo", "tú": "vienes", "él/ella": "viene",
                "nosotros": "venimos", "vosotros": "venís", "ellos": "vienen"
            }
            return f"{person} {forms[person]}"

        # dormir (o→ue)
        if verb == "dormir":
            forms = {
                "yo": "duermo", "tú": "duermes", "él/ella": "duerme",
                "nosotros": "dormimos", "vosotros": "dormís", "ellos": "duermen"
            }
            return f"{person} {forms[person]}"

        # morir (o→ue)
        if verb == "morir":
            forms = {
                "yo": "muero", "tú": "mueres", "él/ella": "muere",
                "nosotros": "morimos", "vosotros": "morís", "ellos": "mueren"
            }
            return f"{person} {forms[person]}"

        # ver
        if verb == "ver":
            forms = {
                "yo": "veo", "tú": "ves", "él/ella": "ve",
                "nosotros": "vemos", "vosotros": "veis", "ellos": "ven"
            }
            return f"{person} {forms[person]}"

        # poner
        if verb == "poner":
            forms = {
                "yo": "pongo", "tú": "pones", "él/ella": "pone",
                "nosotros": "ponemos", "vosotros": "ponéis", "ellos": "ponen"
            }
            return f"{person} {forms[person]}"

        # hacer
        if verb == "hacer":
            forms = {
                "yo": "hago", "tú": "haces", "él/ella": "hace",
                "nosotros": "hacemos", "vosotros": "hacéis", "ellos": "hacen"
            }
            return f"{person} {forms[person]}"

        # oír
        if verb == "oír":
            forms = {
                "yo": "oigo", "tú": "oyes", "él/ella": "oye",
                "nosotros": "oímos", "vosotros": "oís", "ellos": "oyen"
            }
            return f"{person} {forms[person]}"

        # leer
        if verb == "leer":
            forms = {
                "yo": "leo", "tú": "lees", "él/ella": "lee",
                "nosotros": "leemos", "vosotros": "leéis", "ellos": "leen"
            }
            return f"{person} {forms[person]}"

        # construir (i→y)
        if verb == "construir":
            forms = {
                "yo": "construyo", "tú": "construyes", "él/ella": "construye",
                "nosotros": "construimos", "vosotros": "construís", "ellos": "construyen"
            }
            return f"{person} {forms[person]}"

    # === PERFECTO ===
    if tense == "perfecto":
        aux = {
            "yo": "he", "tú": "has", "él/ella": "ha",
            "nosotros": "hemos", "vosotros": "habéis", "ellos": "han"
        }
        participios = {
            "decir": "dicho",
            "hacer": "hecho",
            "poner": "puesto",
            "ver": "visto",
            "morir": "muerto",
            "escribir": "escrito",
            "abrir": "abierto",
            "volver": "vuelto",
            "romper": "roto",
            "leer": "leído",
            "oír": "oído"
        }
        participio = participios.get(verb, verb[:-2] + ("ado" if verb.endswith("ar") else "ido"))
        return f"{person} {aux[person]} {participio}"

    # === IMPERFECTO ===
    if tense == "imperfecto":
        if verb == "ir":
            forms = {
                "yo": "iba", "tú": "ibas", "él/ella": "iba",
                "nosotros": "íbamos", "vosotros": "ibais", "ellos": "iban"
            }
            return f"{person} {forms[person]}"

        if verb == "ser":
            forms = {
                "yo": "era", "tú": "eras", "él/ella": "era",
                "nosotros": "éramos", "vosotros": "erais", "ellos": "eran"
            }
            return f"{person} {forms[person]}"

        if verb == "ver":
            forms = {
                "yo": "veía", "tú": "veías", "él/ella": "veía",
                "nosotros": "veíamos", "vosotros": "veíais", "ellos": "veían"
            }
            return f"{person} {forms[person]}"

        # regular fallback
        stem = verb[:-2]
        ending = verb[-2:]
        if ending == "ar":
            endings = {
                "yo": "aba", "tú": "abas", "él/ella": "aba",
                "nosotros": "ábamos", "vosotros": "abais", "ellos": "aban"
            }
        else:
            endings = {
                "yo": "ía", "tú": "ías", "él/ella": "ía",
                "nosotros": "íamos", "vosotros": "íais", "ellos": "ían"
            }
        return f"{person} {stem}{endings[person]}"

    # === GERUNDIO ===
    if tense == "gerundio":
        if verb == "decir":
            return f"{person} diciendo"
        if verb == "venir":
            return f"{person} viniendo"
        if verb == "dormir":
            return f"{person} durmiendo"
        if verb == "morir":
            return f"{person} muriendo"
        if verb == "leer":
            return f"{person} leyendo"
        if verb == "oír":
            return f"{person} oyendo"
        if verb == "construir":
            return f"{person} construyendo"

        stem = verb[:-2]
        ending = verb[-2:]
        if ending == "ar":
            return f"{person} {stem}ando"
        else:
            return f"{person} {stem}iendo"


print("=== IMPOSSIBLE TRAINER — PILOT v1 ===")

while True:
    verb = random.choice(verbs)
    person = random.choice(persons)
    tense = random.choice(tenses)

    print("\n----------------------------------")
    print(f"Infinitief: {verb}")
    print(f"Persoon: {person}")
    print(f"Tijd: {tense}")
    print("----------------------------------")

    correct = conjugate(verb, person, tense)

    user_form = input("Typ de juiste vorm: ").strip().lower()

    if user_form == correct.lower():
        print("✔ Correct!")
    else:
        print(f"✖ Fout. Correct is: {correct}")

    input("Spreek het hardop uit en druk op Enter...")

    print("\nMaak nu een zin met deze vorm.")
    user_sentence = input("Jouw zin: ").lower()

    if correct.split()[1] in user_sentence or correct in user_sentence:
        print("✔ Zin lijkt correct!")
    else:
        print("⚠ Ik zie de vorm niet terug in je zin.")

    input("Spreek de zin hardop uit en druk op Enter...")

    input("\nDruk op Enter voor de volgende opdracht...")
