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

        if file and file.filename:

            try:
                # 🔥 Create temporary file (safe for Vercel)
                with tempfile.NamedTemporaryFile(delete=False) as temp:
                    file.save(temp.name)
                    temp_path = temp.name

                # Run scan
                result = scan_file(temp_path)

                # Cleanup
                os.remove(temp_path)

            except Exception as e:
                result = "[!] File processing failed (server restriction)"

    return render_template("index.html", result=result)


# Required for Vercel
app = app
