import re
import math


class PasswordAnalyzer:

    def analizza(self, password):

        pool = 0

        if re.search(r"[a-z]", password):
            pool += 26

        if re.search(r"[A-Z]", password):
            pool += 26

        if re.search(r"\d", password):
            pool += 10

        if re.search(r"[^A-Za-z0-9]", password):
            pool += 8

        if pool == 0:
            entropia = 0
        else:
            entropia = round(len(password) * math.log2(pool), 2)

        if entropia < 40:
            livello = "Debole"
        elif entropia < 70:
            livello = "Media"
        else:
            livello = "Forte"

        return {
            "lunghezza": len(password),
            "entropia": entropia,
            "livello": livello,
            "maiuscole": bool(re.search(r"[A-Z]", password)),
            "minuscole": bool(re.search(r"[a-z]", password)),
            "numeri": bool(re.search(r"\d", password)),
            "simboli": bool(re.search(r"[^A-Za-z0-9]", password))
        }
