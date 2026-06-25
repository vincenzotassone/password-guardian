Password Guardian - Generatore e Analizzatore di Password Sicure

Componenti del gruppo

Vincenzo Tassone
Gabriele Rosso

Descrizione del progetto

Password Guardian è un’applicazione sviluppata in Python che consente di generare password sicure e di analizzarne la robustezza. Il programma permette all’utente di creare password personalizzabili in base a lunghezza e complessità, verificare la sicurezza di password esistenti e ottenere suggerimenti per migliorarle.

L’applicazione fornisce inoltre un punteggio complessivo di sicurezza, una stima dell’entropia della password e la possibilità di salvare report in formato JSON.

Problema che risolve

Molti utenti utilizzano password deboli e facilmente individuabili tramite attacchi brute-force o dizionario. Questo progetto aiuta a creare password più sicure e a comprendere il livello di protezione offerto dalle proprie credenziali.

Lo strumento può essere utilizzato sia in ambito personale sia come supporto didattico per comprendere i principi della sicurezza delle password.

Competenze del corso utilizzate

Programmazione orientata agli oggetti (OOP)
Ereditarietà e polimorfismo
Espressioni regolari (Regex)
Gestione di file e JSON
Hashing
Argparse per la realizzazione di una CLI

Gerarchia di ereditarietà prevista

Classe base:

RegolaPassword

Sottoclassi:

RegolaLunghezza
RegolaCaratteri
RegolaPattern
RegolaDizionario

Metodo polimorfico:

verifica(password)

Ogni sottoclasse implementerà il metodo verifica() in modo differente. Il valutatore applicherà tutte le regole senza conoscere il tipo concreto della regola utilizzata, sfruttando così il polimorfismo.

Piano di sviluppo

Fase 1

Creazione repository GitHub
Definizione struttura del progetto
Implementazione generatore di password
Implementazione della gerarchia delle regole

Fase 2

Sistema di valutazione delle password
Calcolo dell’entropia
Salvataggio dei report in formato JSON

Fase 3

Realizzazione dei test automatici con pytest
Stesura della documentazione
Correzione bug e rifinitura del progetto

Obiettivo intermedio

Entro metà sviluppo prevediamo di completare il generatore di password, la struttura ad oggetti e il sistema base di valutazione.

Possibili estensioni

Controllo di password compromesse tramite hash
Miglioramento del sistema di valutazione
Esportazione avanzata dei report
