# Devlog

## Entry – 7 luglio 2026

Oggi abbiamo iniziato concretamente il progetto. Dopo aver definito l'idea nella proposta, abbiamo creato la struttura iniziale del repository GitHub e iniziato a sviluppare il modulo dedicato alla generazione delle password. Prima di scrivere il codice abbiamo ragionato su come suddividere il progetto in più file invece di concentrare tutto in un unico programma. Questa scelta ci è sembrata più ordinata e ci avrebbe facilitato nelle fasi successive.

Abbiamo creato la classe `PasswordGenerator`, che rappresenta il cuore del progetto. All'inizio avevamo pensato di utilizzare il modulo `random`, ma documentandoci abbiamo scoperto che `secrets` è più indicato per generare password sicure. Abbiamo quindi modificato l'implementazione scegliendo questa soluzione.

La parte più delicata è stata capire come costruire dinamicamente l'insieme dei caratteri in base alle scelte dell'utente (maiuscole, minuscole, numeri e simboli). Dopo alcune prove il generatore ha iniziato a produrre password corrette. Abbiamo effettuato diversi test manuali per verificare che ogni esecuzione producesse risultati differenti.

---

## Entry – 10 luglio 2026

In questa fase abbiamo ampliato il progetto introducendo nuove funzionalità. Abbiamo implementato il sistema delle regole creando una classe base `RegolaPassword` e alcune sottoclassi dedicate ai diversi controlli. Questa scelta ci ha permesso di applicare concretamente l'ereditarietà e il polimorfismo, argomenti affrontati durante il corso.

Abbiamo discusso se utilizzare semplici funzioni oppure una gerarchia di classi. Alla fine abbiamo preferito la seconda soluzione perché rende il codice più estendibile e permette di aggiungere facilmente nuove regole senza modificare quelle esistenti.

Successivamente abbiamo lavorato sul menu principale, aggiornando `main.py` per permettere all'utente di interagire con il programma. Durante questa fase abbiamo dedicato diverso tempo ai test, perché alcuni controlli non restituivano il risultato previsto. Una volta corrette le verifiche, il programma ha iniziato a comportarsi come previsto.

---

## Entry – 13–16 luglio 2026

Negli ultimi giorni abbiamo completato il progetto integrando tutte le funzionalità previste. Abbiamo sviluppato il generatore di passphrase utilizzando un elenco di parole contenuto nel file `words.txt`. Per leggere correttamente il file indipendentemente dalla cartella di esecuzione abbiamo utilizzato la libreria `pathlib`.

Successivamente abbiamo implementato l'analizzatore delle password, aggiungendo il calcolo dell'entropia e una classificazione della sicurezza in livelli. Abbiamo poi realizzato il modulo dedicato all'esportazione dei risultati in formato JSON, così da salvare automaticamente l'analisi effettuata.

Una parte del lavoro è stata dedicata all'integrazione dei vari moduli. Alcuni errori negli import e nella gestione dei percorsi dei file ci hanno fatto perdere tempo, ma ci hanno permesso di comprendere meglio come organizzare un progetto Python suddiviso in più moduli.

Nella fase finale abbiamo creato i test automatici con `pytest`, aggiornato il README, completato la documentazione tecnica e preparato tutti i documenti richiesti per la consegna. Prima della chiusura del progetto abbiamo eseguito ulteriori test manuali per verificare che tutte le opzioni del menu funzionassero correttamente e che il report JSON venisse generato senza errori.
