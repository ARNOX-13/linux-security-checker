from flask import Flask, render_template, request
from checks.file_scan import scan_file
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        file = request.files.get("file")

        if file and file.filename:
            filepath = file.filename
            file.save(filepath)

            result = scan_file(filepath)

            os.remove(filepath)

    return render_template("index.html", result=result)


# Required for Vercel
app = app
