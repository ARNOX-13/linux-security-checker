from flask import Flask, render_template, request, send_file
from checks.firewall_check import check_firewall
from checks.port_check import check_ports
from checks.ssh_check import check_ssh
from checks.file_scan import scan_file

import os
import json

app = Flask(__name__)


# ---------------- HOME PAGE ---------------- #
@app.route("/", methods=["GET", "POST"])
def index():
    results = []

    if request.method == "POST":

        # System scan
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

        # File scan
        elif "scan_file" in request.form:
            file = request.files.get("file")

            if file:
                filepath = file.filename
                file.save(filepath)

                results.append(scan_file(filepath))

                os.remove(filepath)  # cleanup

    return render_template("index.html", results=results)


# ---------------- DOWNLOAD JSON ---------------- #
@app.route("/download")
def download():
    report = {}

    msg, _ = check_firewall()
    report["firewall"] = msg

    msg, _ = check_ports()
    report["ports"] = msg

    msg, _ = check_ssh()
    report["ssh"] = msg

    with open("report.json", "w") as f:
        json.dump(report, f, indent=4)

    return send_file("report.json", as_attachment=True)


# ---------------- RUN APP ---------------- #
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
