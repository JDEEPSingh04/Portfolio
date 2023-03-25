from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)
download_desktop = "https://docs.google.com/document/d/1-4o2M_YJY1axbgIV8oZ2PMzQtMCpMCpTFGPmyngkep0/edit?usp=sharing"
download_apk = "https://docs.google.com/document/d/1-4o2M_YJY1axbgIV8oZ2PMzQtMCpMCpTFGPmyngkep0/edit?usp=sharing"

@app.route("/", methods=["POST","GET"])
def homepage():
    return render_template("homepage.html")

@app.route("/qualifications", methods=["POST","GET"])
def qualifications():
    return render_template("qualifications.html")

@app.route("/skills", methods=["POST","GET"])
def skills():
    return render_template("skills.html")

@app.route("/connect", methods=["POST","GET"])
def connect():
    return render_template("connect.html")

if __name__ == "__main__":
    app.run(debug=True)
