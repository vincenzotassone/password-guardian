import secrets
import string


class PasswordGenerator:

    def genera_password(self, lunghezza, maiuscole=True, minuscole=True,
                         numeri=True, simboli=True):

        caratteri = ""

        if maiuscole:
            caratteri += string.ascii_uppercase

        if minuscole:
            caratteri += string.ascii_lowercase

        if numeri:
            caratteri += string.digits

        if simboli:
            caratteri += "!@#$%^&*"

        if caratteri == "":
            raise ValueError("Seleziona almeno un tipo di carattere.")

        password = ""

        for _ in range(lunghezza):
            password += secrets.choice(caratteri)

        return password

    def genera_passphrase(self, numero_parole=4):

        with open("words.txt", "r", encoding="utf-8") as file:
            parole = file.read().splitlines()

        scelta = []

        for _ in range(numero_parole):
            scelta.append(secrets.choice(parole))

        return "-".join(scelta)
