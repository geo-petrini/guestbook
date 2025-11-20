from flask import Blueprint, render_template, request, flash, redirect, url_for
from models import Message

app = Blueprint("guestbook", __name__)


@app.route("/")
def root():

    messages = Message.select().order_by(Message.created_at.desc())
    return render_template("guestbook.html", messages=messages)

@app.route("/", methods=["POST"])
def post():
    name = request.form["name"]
    message = request.form["message"]

    #check if user (name) already posted a message
    message = Message.get(Message.name == name)
    if message:
        flash('Hai già lasciato un messaggio')
    else:
        Message.create(name=name, message=message)  #crea l'istanza e salva il record 
        flash( "Messaggio inviato con successo" )

    return redirect(url_for('guestbook.root'))
