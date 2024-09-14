from flask import Flask, request, jsonify
import langid
from googletrans import Translator

app = Flask(__name__)
translator = Translator()


@app.route('/detect_language', methods=['POST'])
def detect_language():
    data = request.get_json()
    text = data.get('text')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    try:
        language, confidence = langid.classify(text)
        return jsonify({'language': language, 'confidence': confidence})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    text = data.get('text')
    target_language = data.get('target_language')

    if not text or not target_language:
        return jsonify({'error': 'No text or target language provided'}), 400

    try:
        translation = translator.translate(text, dest=target_language)
        return jsonify({'translated_text': translation.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
