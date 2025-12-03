from flask import Blueprint, render_template, request, flash, redirect, url_for
from models import Message, get_message_by_name

app = Blueprint("guestbook", __name__)


@app.route("/")
def root():

    messages = Message.select().order_by(Message.created_at.desc())
    return render_template("guestbook.html", messages=messages)

@app.route("/", methods=["POST"])
def post():
    name = request.form.get("name")
    message = request.form.get("message")

    if not name:
        flash("Il campo 'Nome' è obbligatorio")
        return redirect(url_for('guestbook.root'))
    if not message:
        flash("Il campo 'Messaggio' è obbligatorio")
        return redirect(url_for('guestbook.root'))

    #check if user (name) already posted a message
    record = get_message_by_name(name)
    if record:
        flash('Hai già lasciato un messaggio')
    else:
        Message.create(name=name, message=message)  #crea l'istanza e salva il record 
        flash( "Messaggio inviato con successo" )

    return redirect(url_for('guestbook.root'))
