import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/englishToFrench', methods=['GET'])
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translation = translator.englishToFrench(textToTranslate)
    return translation


@app.route('/frenchToEnglish', methods=['GET'])
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translation = translator.frenchToEnglish(textToTranslate)
    return translation


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
