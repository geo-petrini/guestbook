from flask import Blueprint, render_template, request
from models import Message

app = Blueprint("guestbook", __name__)


@app.route("/", methods=["GET", "POST"])
def guestbook():
    if request.method == "POST":
        name = request.form["name"]
        message = request.form["message"]

        Message.create(name=name, message=message)
        return "Messaggio inviato con successo!"

    messages = Message.select().order_by(Message.created_at.desc())
    return render_template("guestbook.html", messages=messages)
