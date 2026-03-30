from flask import Flask, render_template, request
from checks.file_scan import scan_file
import tempfile
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        file = request.files.get("file")

        if file:
            try:
                temp = tempfile.NamedTemporaryFile(delete=False)
                file.save(temp.name)

                result = scan_file(temp.name)

                temp.close()
                os.remove(temp.name)

            except:
                result = "[!] File upload failed (server restriction)"

    return render_template("index.html", result=result)


app = app
