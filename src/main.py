from generator import PasswordGenerator
from rules import RegolaLunghezza, RegolaMaiuscola, RegolaNumero


def risposta_si_no(domanda):
    risposta = input(domanda).strip().lower()
    return risposta == "s"


def main():

    generatore = PasswordGenerator()

    print("PASSWORD GUARDIAN")
    print("1 - Genera password")
    print("2 - Genera passphrase")

    scelta = input("Scelta: ")

    if scelta == "1":

        lunghezza = int(input("Lunghezza password: "))

        maiuscole = risposta_si_no("Usare lettere maiuscole? (s/n): ")
        minuscole = risposta_si_no("Usare lettere minuscole? (s/n): ")
        numeri = risposta_si_no("Usare numeri? (s/n): ")
        simboli = risposta_si_no("Usare simboli? (s/n): ")

        password = generatore.genera_password(
            lunghezza,
            maiuscole,
            minuscole,
            numeri,
            simboli
        )

        print("\nPassword generata:")
        print(password)

        # Verifica delle regole
        regole = [
            RegolaLunghezza(),
            RegolaMaiuscola(),
            RegolaNumero()
        ]

        print("\nVerifica password:")

        for regola in regole:
            if regola.verifica(password):
                print(type(regola).__name__, "OK")
            else:
                print(type(regola).__name__, "NON OK")

    elif scelta == "2":

        numero_parole = int(input("Quante parole vuoi nella passphrase? "))

        passphrase = generatore.genera_passphrase(numero_parole)

        print("\nPassphrase generata:")
        print(passphrase)

    else:
        print("Scelta non valida.")


if __name__ == "__main__":
    main()
