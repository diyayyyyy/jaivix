from flask import Flask, request, redirect, render_template
from flask_cors import CORS
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
CORS(app)

EMAIL_ADDRESS = "sanikashete164@gmail.com"
EMAIL_PASSWORD = "vybhexkmqtnwqmed"

# ================= HOME PAGE =================
@app.route("/")
def index():
    return render_template("index.html")

# ================= ABOUT PAGE =================
@app.route("/about")
def about():
    return render_template("about.html")

# ================= SERVICES PAGE =================
@app.route("/services")
def services():
    return render_template("services.html")

# ================= CONTACT PAGE =================
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        msg = EmailMessage()
        msg["Subject"] = f"Contact Form: {subject}"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS
        msg.set_content(
            f"Name: {name}\n"
            f"Email: {email}\n\n"
            f"Message:\n{message}"
        )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        return redirect("/contact")

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
