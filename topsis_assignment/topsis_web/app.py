from flask import Flask, render_template, request
import os
import re
from topsis.topsis import run_topsis
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ---------- Email validation ----------
def valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

# ---------- Send email ----------
def send_email(receiver_email, attachment_path):
    sender_email = "goyalnishtha888@gmail.com"
    sender_password = "nishtha"

    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Result File"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content("Please find attached the TOPSIS result file.")

    with open(attachment_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename=os.path.basename(attachment_path)
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)

# ---------- Routes ----------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("file")
        weights = request.form.get("weights")
        impacts = request.form.get("impacts")
        email = request.form.get("email")

        if not file or not weights or not impacts or not email:
            return "All fields are required"

        if not valid_email(email):
            return "Invalid email format"

        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        output_path = os.path.join(UPLOAD_FOLDER, "result.csv")
        file.save(input_path)

        try:
            run_topsis(input_path, weights, impacts, output_path)
            send_email(email, output_path)
        except Exception as e:
            return str(e)

        return "Result sent successfully to your email"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
