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

    # GPT-3を使用してレシピを生成
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"I want to cook a {dish_type}. What is the recipe?",
        temperature=0.5,
        max_tokens=200
    )

    # レスポンスをJSONとして返す
    return jsonify(response['choices'][0]['message']['content'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)