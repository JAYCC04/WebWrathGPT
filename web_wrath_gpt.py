from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Replace with your actual OpenAI API Key
openai.api_key = "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"

@app.route('/generate_website', methods=['POST'])
def generate_website():
    data = request.get_json()
    prompt = data.get("prompt", "Build a basic responsive website with a homepage, about, and contact pages.")
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Generate a complete HTML and CSS code for the following website idea: {prompt}. "
                   "Make it responsive and visually appealing.",
            max_tokens=1000
        )
        website_code = response.choices[0].text.strip()
        return jsonify({"status": "success", "website_code": website_code})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "online", "message": "Web Wrath GPT is ready."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
