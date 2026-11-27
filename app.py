
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
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024

@app.errorhandler(413)
def request_entity_too_large(error):
    return render_template(
        "index.html",
        result="",
        original_text="",
        shift=3,
        mode="encrypt",
        brute_results=[],
        error="Request is too large. Maximum request size is 16 KB.",
        input_char_count=0,
        input_word_count=0,
        result_char_count=0,
        result_word_count=0
    ), 413

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    original_text = ""
    shift = 3
    mode = "encrypt"
    brute_results = []
    error = ""

    # Initialize counters
    input_char_count = 0
    input_word_count = 0
    result_char_count = 0
    result_word_count = 0

    if request.method == "POST":
        original_text = request.form.get("text", "")

        # Calculate counts for the original input
        input_char_count = len(original_text)
        input_word_count = len(original_text.split())

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

                    # Calculate counts for the generated result
                    if mode in ("encrypt", "decrypt"):
                        result_char_count = len(result)
                        result_word_count = len(result.split())

                except ValueError:
                    error = "Invalid operation."

    return render_template(
        "index.html",
        result=result,
        original_text=original_text,
        shift=shift,
        mode=mode,
        brute_results=brute_results,
        error=error,
        input_char_count=input_char_count,
        input_word_count=input_word_count,
        result_char_count=result_char_count,
        result_word_count=result_word_count
    )


if __name__ == "__main__":
    app.run(debug=True)