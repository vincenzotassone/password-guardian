# Password Guardian – Generatore Avanzato e Analizzatore di Password Sicure

## Componenti del gruppo

* Vincenzo Tassone
* Gabriele Rosso

---

# Descrizione del progetto

**Password Guardian** è un'applicazione sviluppata in Python che ha come obiettivo principale la **generazione di password e passphrase sicure**, completamente personalizzabili secondo politiche di sicurezza configurabili dall'utente.

Il programma permette di:

* generare password casuali ad alta sicurezza;
* generare **passphrase memorizzabili** ispirate al metodo Diceware;
* definire regole personalizzate (lunghezza minima, caratteri obbligatori, simboli, numeri, maiuscole, esclusione di caratteri ambigui, ecc.);
* verificare automaticamente che la password generata rispetti tutte le politiche impostate;
* analizzare password già esistenti per valutarne la robustezza;
* calcolare il livello di entropia;
* assegnare un punteggio di sicurezza;
* esportare un report dettagliato in formato JSON.

L'obiettivo è realizzare uno strumento che **prima genera password robuste** e successivamente ne verifica automaticamente la conformità alle regole di sicurezza.

---

# Problema che risolve

Molti utenti utilizzano password deboli oppure creano password casuali che risultano difficili da ricordare.

Password Guardian risolve questo problema offrendo due modalità di generazione:

* password casuali ad alta entropia;
* passphrase lunghe e facilmente memorizzabili.

Ogni password generata viene immediatamente controllata per garantire il rispetto delle politiche di sicurezza configurate dall'utente.

L'applicazione può essere utilizzata sia in ambito personale sia come supporto didattico per comprendere le tecniche di creazione e valutazione delle password.

---

# Competenze del corso utilizzate

* Programmazione orientata agli oggetti (OOP)
* Ereditarietà
* Polimorfismo
* Espressioni regolari (Regex)
* Gestione di file JSON
* Calcolo dell'entropia
* Hashing
* Argparse per la realizzazione della CLI

---

# Gerarchia di ereditarietà prevista

## Classe base

**RegolaPassword**

### Sottoclassi

* RegolaLunghezza
* RegolaCaratteri
* RegolaPattern
* RegolaDizionario

### Metodo polimorfico

```python
verifica(password)
```

Ogni sottoclasse implementa il metodo `verifica()` in modo differente.

Il sistema di validazione applica automaticamente tutte le regole senza conoscere il tipo concreto della regola, sfruttando il polimorfismo.

Questa struttura permette di aggiungere facilmente nuove regole senza modificare il codice esistente.

---

# Funzionalità principali

### Generatore di password

* lunghezza configurabile;
* scelta dei caratteri utilizzabili;
* esclusione dei caratteri ambigui;
* password casuali ad alta entropia;
* verifica automatica del rispetto delle regole.

### Generatore di passphrase

* generazione di passphrase tramite liste di parole;
* stile Diceware;
* maggiore facilità di memorizzazione;
* elevata sicurezza grazie alla lunghezza.

### Analizzatore

* verifica della robustezza;
* controllo delle regole;
* calcolo dell'entropia;
* valutazione complessiva della sicurezza;
* suggerimenti per il miglioramento.

### Report

* esportazione dei risultati in formato JSON.

---

# Piano di sviluppo

## Fase 1

* Creazione del repository GitHub
* Definizione della struttura del progetto
* Implementazione del generatore di password
* Implementazione del generatore di passphrase
* Realizzazione della gerarchia delle regole

## Fase 2

* Sistema di verifica automatica delle password generate
* Analizzatore di password
* Calcolo dell'entropia
* Esportazione dei report JSON

## Fase 3

* Test automatici con pytest
* Documentazione completa
* Correzione bug
* Ottimizzazione del codice

---

# Obiettivo intermedio

Entro metà dello sviluppo prevediamo di completare:

* il generatore di password;
* il generatore di passphrase;
* la struttura a oggetti;
* il sistema di verifica delle regole;
* una prima versione dell'analizzatore.

---

# Possibili estensioni

* Controllo delle password compromesse tramite database di hash (es. Have I Been Pwned tramite k-anonymity).
* Introduzione di nuove politiche di sicurezza configurabili.
* Esportazione avanzata dei report.
* Interfaccia grafica (GUI).
* Supporto a file di configurazione per definire policy personalizzate.

