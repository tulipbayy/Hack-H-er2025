from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__, template_folder="templates")

# Set your OpenAI API Key here
openai.api_key = "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"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_etymology", methods=["POST"])
def get_etymology():
    word = request.json.get("word")
    if not word:
        return jsonify({"error": "No word provided"}), 400

    prompt = f"Please give the linguistic and etymological roots of the word '{word}'."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are a linguistic and etymology expert."},
                      {"role": "user", "content": prompt}]
        )
        etymology_info = response["choices"][0]["message"]["content"]
        return jsonify({"etymology": etymology_info})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
