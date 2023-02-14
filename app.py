from flask import Flask, request, render_template
import openai

app = Flask(__name__)
# 请在此处输入openai平台申请的key
openai.api_key = "YOUR_API_KEY_HERE"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/prompt", methods=["POST"])
def prompt():
    prompt_str = request.form.get("text")
    
    print(prompt_str)

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt_str,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()


if __name__ == "__main__":
    app.run()
