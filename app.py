from flask import Flask
from dotenv import load_dotenv
from models import db, Message
from routes import app as guestbook_bp
from peewee import MySQLDatabase, SqliteDatabase
import os


def create_app():
    load_dotenv()

    app = Flask(__name__)

    if os.getenv("DATABASE_HOST"):  # Se è configurato usa MySQL
        print("Inizializzo MySQL")

        mysql_host = os.getenv("DATABASE_HOST")
        mysql_db = os.getenv("DATABASE_NAME", "guestbook")
        mysql_user = os.getenv("DATABASE_USER", "root")
        mysql_password = os.getenv("DATABASE_PASSWORD", "")

        database = MySQLDatabase(
            mysql_db,
            host=mysql_host,
            user=mysql_user,
            password=mysql_password,
            port=3306
        )

    else:  # Altrimenti fallback con SQLite
        print("MySQL non configurato, fallback a SQLite")
        sqlite_name = os.getenv("SQLITE_DB", "guestbook.db")
        database = SqliteDatabase(sqlite_name)

    # Inizializza il proxy
    db.initialize(database)

    # Inizializza DB e crea tabelle
    # attenzione non ci sono migrazioni, peewee non le supporta
    with app.app_context():
        if db.is_closed():
            db.connect()
        db.create_tables([Message])

    # Registra il Blueprint
    app.register_blueprint(guestbook_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
