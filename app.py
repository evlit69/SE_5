from flask import Flask, render_template, request
from cipher import process_cipher

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    original_text = ""
    shift = 3
    mode = "encrypt"
    brute_results = []

    if request.method == "POST":
        original_text = request.form.get("text", "")
        mode = request.form.get("mode", "encrypt")

        try:
            shift = int(request.form.get("shift", 3))
            if not 0 <= shift <= 25:
                raise ValueError
        except ValueError:
            shift = 3

        try:
            result, brute_results = process_cipher(original_text, shift, mode)
        except ValueError:
            result = ""
            brute_results = []

    return render_template(
        "index.html",
        result=result,
        original_text=original_text,
        shift=shift,
        mode=mode,
        brute_results=brute_results,
    )


if __name__ == "__main__":
    app.run(debug=True)
