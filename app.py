from flask import Flask, render_template, url_for, jsonify, request
from config import Config


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/translate-text', methods=['POST'])
def translate_text():
    data = request.get_json()
    text_input = data['text']
    translation_output = data['to']
    response = translate.get_translation(text_input, translation_output)
    return jsonify(response)


@app.route('/sentiment-analysis', methods=['POST'])
def sentiment_analysis():
    data = request.get_json()
    input_text = data['inputText']
    input_lang = data['inputLanguage']
    output_text = data['outputText']
    output_lang =  data['outputLanguage']
    response = sentiment.get_sentiment(input_text, input_lang, output_text, output_lang)
    print(response)
    return jsonify(response)


import translate, sentiment
