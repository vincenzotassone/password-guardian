# Manuale Utente

## Introduzione

Password Guardian è un'applicazione Python che permette di generare password sicure, creare passphrase memorizzabili e analizzare la robustezza di una password.

## Avvio del programma

Aprire un terminale nella cartella principale del progetto ed eseguire:

```bash
python src/main.py
```

## Menu principale

All'avvio viene mostrato il seguente menu:

```
PASSWORD GUARDIAN

1 - Genera password
2 - Genera passphrase
3 - Analizza password
0 - Esci
```

## Opzione 1 - Genera password

L'utente può scegliere:

* lunghezza della password;
* utilizzo di lettere maiuscole;
* utilizzo di lettere minuscole;
* utilizzo di numeri;
* utilizzo di simboli.

Il programma genera una password casuale rispettando le opzioni selezionate e verifica automaticamente alcune regole di sicurezza.

### Esempio

```
Lunghezza password: 12
Usare lettere maiuscole? s
Usare lettere minuscole? s
Usare numeri? s
Usare simboli? s

Password generata:
A9!kLm4@Qr2P
```

---

## Opzione 2 - Genera passphrase

Il programma genera una passphrase composta da parole casuali prese dal file `words.txt`.

### Esempio

```
Quante parole vuoi? 4

mare-cane-luna-computer
```

---

## Opzione 3 - Analizza password

L'utente inserisce una password già esistente.

Il programma mostra:

* lunghezza;
* entropia;
* livello di sicurezza;
* presenza di maiuscole;
* presenza di minuscole;
* presenza di numeri;
* presenza di simboli.

Inoltre viene creato automaticamente un file JSON nella cartella `reports`.

---

## Report

Il file `reports/report.json` contiene il risultato dell'ultima analisi effettuata.
