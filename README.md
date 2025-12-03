# Guestbook Flask App

Un'applicazione Guestbook realizzata con **Flask** e **Peewee ORM**, con supporto automatico per **MySQL** oppure **SQLite** come fallback.
L'app inizializza automaticamente il database e crea la tabella necessaria se non esiste.

---

## Funzionalità principali

* API/rotte fornite tramite Blueprint (`routes.py`)
* Modello `Message` gestito tramite Peewee ORM
* Database selezionato automaticamente:

  * **MySQL** se sono presenti le variabili d’ambiente
  * **SQLite** in assenza di configurazione
* Creazione automatica delle tabelle al primo avvio
* Supporto a `.env` tramite `python-dotenv`

---

## Struttura del progetto

```
.
├── app.py
├── models.py
├── routes.py
├── requirements.txt
├── README.md
└── guestbook.db (creato solo in modalità SQLite)
```

---

## Requisiti

* Python 3.9+
* Pip
* (Opzionale) Server MySQL

Installazione dipendenze:

```bash
pip install -r requirements.txt
```

---

## Configurazione ambiente

L'app usa automaticamente MySQL **solo se** sono presenti queste variabili d'ambiente:

| Variabile           | Descrizione           |
| ------------------- | --------------------- |
| `DATABASE_HOST`     | Host del server MySQL |
| `DATABASE_NAME`     | Nome del database     |
| `DATABASE_USER`     | Username MySQL        |
| `DATABASE_PASSWORD` | Password MySQL        |

Esempio `.env` per MySQL:

```
DATABASE_HOST=localhost
DATABASE_NAME=guestbook_db
DATABASE_USER=root
DATABASE_PASSWORD=secret
```

### Uso con SQLite (default)

Se `DATABASE_HOST` **non è impostata**, Flask userà SQLite.

Puoi opzionalmente definire:

```
SQLITE_DB=instance/guestbook.db
```

Il programma crea automaticamente il path per il db SQLite.

---

## Come funziona la scelta del database

```python
if os.getenv("DATABASE_HOST"):
    # usa MySQL
else:
    # fallback SQLite
```

---

## Avvio dell'applicazione

```bash
python app.py
```

L'app sarà disponibile su:

```
http://127.0.0.1:5000
```

---

## Creazione automatica delle tabelle

Al primo avvio, il codice:

```python
db.create_tables([Message])
```

crea automaticamente le tabelle se non esistono.

**Attenzione:** Peewee non gestisce migrazioni complesse.
Se modifichi i campi del modello, devi aggiornare la tabella manualmente.

---

## Rotte API

Le rotte sono definite in:

```
routes.py
```

e registrate tramite:

```python
app.register_blueprint(guestbook_bp)
```

---

## Docker (opzionale)

Il progetto è compatibile con un ambiente Docker + MySQL.
Puoi usare un `docker-compose.yaml` come:

```yaml
environment:
  DATABASE_HOST: db
  DATABASE_USER: your_user
  DATABASE_PASSWORD: your_pass
  DATABASE_NAME: guestbook_db
```

### Build dell'immagine

```shell
docker build --pull --rm -f "dockerfile" -t "guestbook:latest" .
```

### Run dell'immagine

Il comando seguente permette di eseguire l'immagine come container, utilizzando il db interno SQLite.

Attenzione, se il container viene chiuso verranno persi tutti i dati.
```shell
docker run -d \
  --name guestbook \
  -p 5000:5000 \
  guestbook:latest
```

Per garantire la persistenza usare l'opzione -v per creare un volume e associarlo al db SQLite
```shell
docker run -d \
  --name guestbook \
  -p 5000:5000 \
  -v db:/app/instance \
  guestbook:latest
```

Compose per il servizio standalone
```yaml
version: '3.9'
services:
    guestbook:
        image: 'guestbook:latest'
        container_name: guestbook
        volumes:
            - 'db:/app/instance'
        ports:
            - '5000:5000'
volumes:
  db:

```
---

## Licenza

MIT