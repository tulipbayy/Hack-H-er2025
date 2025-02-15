from flask import Flask, render_template, request, jsonify
import openai
import config 

app = Flask(__name__, template_folder="templates")

# Set your OpenAI API Key here
OPENAI_API_KEY = "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"

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
        client = openai.OpenAI(api_key=config.OPENAI_API_KEY)
        response = response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a linguistic and etymology expert."},
                {"role": "user", "content": prompt}
            ]
        )
        etymology_info = response.choices[0].message.content  
        return jsonify({"etymology": etymology_info})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
