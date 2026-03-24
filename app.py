from flask import Flask, render_template, request
from checks.firewall_check import check_firewall
from checks.port_check import check_ports
from checks.ssh_check import check_ssh
from checks.file_scan import scan_file
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []

    if request.method == "POST":

        if "scan_system" in request.form:
            score = 0

            msg, pts = check_firewall()
            results.append(msg)
            score += pts

            msg, pts = check_ports()
            results.append(msg)
            score += pts

            msg, pts = check_ssh()
            results.append(msg)
            score += pts

            results.append(f"Security Score: {score}/10")

        elif "scan_file" in request.form:
            file = request.files["file"]
            if file:
                filepath = file.filename
                file.save(filepath)

                results.append(scan_file(filepath))

                os.remove(filepath)  # cleanup

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
