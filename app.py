import os
from dotenv import load_dotenv
import openai
import requests
from flask import Flask, render_template, request, jsonify

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_recipe', methods=['POST'])
def generate_recipe():
    # リクエストから料理の名前を取得
    dish_name = request.form.get('dish_name')

    # GPT-4を使用してレシピを生成
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{dish_name}のレシピを教えてください。"}
        ]
    )

    # レスポンスをJSONとして返す
    return jsonify(response['choices'][0]['message']['content'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)