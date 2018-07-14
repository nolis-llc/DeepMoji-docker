from flask import Flask, make_response, request, jsonify
from emoji_function import *
app = Flask(__name__)

@app.route('/', methods=["POST"])
def emoji_api():
    sentences = request.get_json(force=True)["sentences"]
    emoji = get_emoji(sentences)
    emoji_string = '{\"emoji\":['+','.join(map(lambda y: "[" + (','.join(map(lambda x: "{\"emoji\": \"" + x[0] + "\", \"prob\": " + '{:.20f}'.format(x[1]) + "}",y))) + "]",emoji))+']}'
    to_be_returned = make_response(emoji_string)
    to_be_returned.mimetype ='application/json;charset=utf-8'
    return to_be_returned
    #return jsonify(sentences=sentences, emoji=emoji)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("80"), debug=True)