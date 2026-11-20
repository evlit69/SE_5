from flask import Flask, render_template, request
from cipher import process_cipher

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = Flask(__name__)

MAX_LENGTH = 5000

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    original_text = ""
    shift = 3
    mode = "encrypt"
    brute_results = []
    error = ""

    if request.method == "POST":
        original_text = request.form.get("text", "")
        mode = request.form.get("mode", "encrypt")
        if len(original_text) > MAX_LENGTH:
            error = "Message too long"
        else:
            try:
                shift = int(request.form.get("shift", 3))
                if not 0 <= shift <= 25:
                    raise ValueError
            except ValueError:
                error = "Shift must be an integer between 0 and 25."

            if not error:
                try:
                    result, brute_results = process_cipher(
                        original_text, shift, mode
                    )
                except ValueError:
                    error = "Invalid operation."

    return render_template(
        "index.html",
        result=result,
        original_text=original_text,
        shift=shift,
        mode=mode,
        brute_results=brute_results,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
