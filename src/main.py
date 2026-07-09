from generator import PasswordGenerator


def risposta_si_no(domanda):
    risposta = input(domanda).strip().lower()
    return risposta == "s"


def main():

    generatore = PasswordGenerator()

    print("PASSWORD GUARDIAN")
    print()

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


if __name__ == "__main__":
    main()
