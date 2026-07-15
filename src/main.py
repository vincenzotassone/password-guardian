from generator import PasswordGenerator
from analyzer import PasswordAnalyzer
from rules import RegolaLunghezza, RegolaMaiuscola, RegolaNumero
from report import ReportManager


def risposta_si_no(domanda):
    risposta = input(domanda).strip().lower()
    return risposta == "s"


def main():

    generatore = PasswordGenerator()
    analyzer = PasswordAnalyzer()
    report = ReportManager()

    print("===================================")
    print("      PASSWORD GUARDIAN")
    print("===================================")
    print("1 - Genera password")
    print("2 - Genera passphrase")
    print("3 - Analizza password")
    print("0 - Esci")

    scelta = input("\nScelta: ")

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

        regole = [
            RegolaLunghezza(),
            RegolaMaiuscola(),
            RegolaNumero()
        ]

        print("\nVerifica password:")

        for regola in regole:
            if regola.verifica(password):
                print(f"{type(regola).__name__}: OK")
            else:
                print(f"{type(regola).__name__}: NON OK")

    elif scelta == "2":

        numero_parole = int(input("Quante parole vuoi nella passphrase? "))

        passphrase = generatore.genera_passphrase(numero_parole)

        print("\nPassphrase generata:")
        print(passphrase)

    elif scelta == "3":

        password = input("Inserisci la password da analizzare: ")

        risultato = analyzer.analizza(password)

        # Aggiunge la password al report JSON
        risultato["password"] = password

        # Salva il report
        report.salva_report(risultato)

        print("\n===== ANALISI PASSWORD =====")
        print("Lunghezza :", risultato["lunghezza"])
        print("Entropia  :", risultato["entropia"])
        print("Livello   :", risultato["livello"])
        print("Maiuscole :", risultato["maiuscole"])
        print("Minuscole :", risultato["minuscole"])
        print("Numeri    :", risultato["numeri"])
        print("Simboli   :", risultato["simboli"])

        print("\nReport JSON salvato nella cartella 'reports'.")

    elif scelta == "0":

        print("Programma terminato.")

    else:

        print("Scelta non valida.")


if __name__ == "__main__":
    main()
