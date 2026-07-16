# Devlog

## Entry 1 – 25 giugno – 7 luglio 2026

In questa prima fase abbiamo definito l'idea del progetto e preparato tutto il necessario per iniziare lo sviluppo. Abbiamo creato il repository GitHub, scritto la proposta iniziale e organizzato la struttura delle cartelle e dei file. Prima di iniziare a programmare abbiamo discusso su come suddividere il progetto in moduli, evitando di concentrare tutto in un unico file.

Successivamente abbiamo iniziato a sviluppare il generatore di password, che rappresenta la funzionalità principale del progetto. Dopo aver valutato diverse possibilità, abbiamo deciso di utilizzare il modulo `secrets` invece di `random`, perché offre una generazione casuale più adatta alla sicurezza. Abbiamo implementato una prima versione del generatore e verificato che producesse password sempre diverse.

Durante questa fase abbiamo anche iniziato a ragionare sull'organizzazione delle classi e su come mantenere il codice semplice ma facilmente estendibile. Alcune prove iniziali non funzionavano come previsto, ma ci hanno aiutato a capire meglio come strutturare il progetto prima di aggiungere nuove funzionalità.

---

## Entry 2 – 9 – 10 luglio 2026

Abbiamo ampliato il progetto introducendo il generatore di passphrase e il sistema di regole per la validazione delle password. Per le passphrase abbiamo creato un file contenente un elenco di parole e implementato la lettura del file tramite `pathlib`, così da evitare problemi con i percorsi.

Successivamente abbiamo realizzato la gerarchia delle classi dedicata alle regole di sicurezza. Dopo un confronto abbiamo deciso di utilizzare una classe base (`RegolaPassword`) e più sottoclassi, applicando ereditarietà e polimorfismo, invece di creare semplici funzioni indipendenti. Questa soluzione ci è sembrata più ordinata e facilmente estendibile.

Abbiamo aggiornato il menu principale per integrare le nuove funzionalità e svolto diversi test manuali. Alcuni errori nella gestione degli import e nei percorsi dei file ci hanno fatto perdere tempo, ma una volta individuati siamo riusciti a risolverli senza modificare la struttura generale del progetto.

---

## Entry 3 – 13 – 16 luglio 2026

Nell'ultima fase abbiamo completato il progetto sviluppando il modulo di analisi delle password. Abbiamo implementato il calcolo dell'entropia, la valutazione del livello di sicurezza e il controllo della presenza di maiuscole, minuscole, numeri e simboli.

Successivamente abbiamo creato il modulo dedicato all'esportazione dei risultati in formato JSON, facendo in modo che il programma generasse automaticamente un report dopo ogni analisi. Abbiamo integrato tutti i moduli nel menu principale e verificato il corretto funzionamento dell'intera applicazione.

Infine abbiamo realizzato i test automatici con `pytest`, aggiornato il file `.gitignore`, corretto alcuni piccoli problemi riscontrati durante le prove e completato tutta la documentazione richiesta, compresi il manuale utente, il manuale tecnico, le scelte implementative e la dichiarazione sull'utilizzo dell'Intelligenza Artificiale. Prima della consegna abbiamo eseguito un controllo finale dell'intero progetto per verificare che tutte le funzionalità fossero operative.
