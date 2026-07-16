# Scelte Implementative

## Organizzazione del progetto

Abbiamo suddiviso il progetto in moduli per separare le responsabilità e rendere il codice più ordinato e facilmente estendibile.

## Utilizzo delle classi

Abbiamo scelto di utilizzare la programmazione orientata agli oggetti per rappresentare le diverse funzionalità del progetto.

Ogni classe svolge un compito specifico:

* PasswordGenerator genera password e passphrase;
* PasswordAnalyzer analizza le password;
* ReportManager salva i report;
* le classi delle regole verificano i requisiti di sicurezza.

## Perché l'ereditarietà

Le regole di controllo condividono tutte lo stesso comportamento generale: verificare una password.

Per questo motivo abbiamo creato una classe base `RegolaPassword` dalla quale derivano le varie regole.

Questa scelta rende semplice aggiungere nuove regole senza modificare il codice già esistente.

## Perché non funzioni separate

Una soluzione alternativa sarebbe stata utilizzare semplici funzioni.

Abbiamo preferito l'ereditarietà perché era uno degli argomenti principali del corso e permette di applicare il polimorfismo tramite il metodo `verifica()`.

## Alternative scartate

Abbiamo valutato una struttura più complessa con numerose classi e configurazioni avanzate, ma l'abbiamo scartata per mantenere il progetto semplice, leggibile e coerente con gli obiettivi didattici.
