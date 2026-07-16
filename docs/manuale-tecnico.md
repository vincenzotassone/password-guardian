# Manuale Tecnico

## Architettura del progetto

Il progetto è suddiviso in moduli indipendenti.

```
main.py
│
├── generator.py
├── analyzer.py
├── rules.py
└── report.py
```

Ogni modulo ha una responsabilità specifica.

## Moduli

### main.py

Gestisce il menu e coordina tutte le operazioni.

### generator.py

Contiene la classe `PasswordGenerator`.

Responsabilità:

* generazione password;
* generazione passphrase.

### analyzer.py

Contiene la classe `PasswordAnalyzer`.

Responsabilità:

* analisi password;
* calcolo entropia;
* classificazione della sicurezza.

### report.py

Contiene la classe `ReportManager`.

Responsabilità:

* esportazione dei risultati in formato JSON.

### rules.py

Contiene il sistema di validazione delle password.

## Gerarchia delle classi

```
                RegolaPassword
                     │
     ┌───────────────┼───────────────┐
     │               │               │
RegolaLunghezza RegolaMaiuscola RegolaNumero
```

Ogni sottoclasse implementa il metodo:

```
verifica(password)
```

Il programma utilizza il polimorfismo per applicare automaticamente tutte le regole senza conoscere il tipo concreto della classe.

## Estensioni future

È possibile aggiungere nuove regole creando una nuova sottoclasse di `RegolaPassword` e implementando il metodo `verifica()`.
