from flask import Flask, request, abort, redirect, json , jsonify

from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage

from tokens import handler  # token
from command import command

from tokens import cred, default_app, db, todo_ref

app = Flask(__name__)


@app.route('/add', methods=['POST'])
def create():
    """
            create() : Add document to Firestore collection with request body
            Ensure you pass a custom ID as part of json body in post request
            e.g. json={'id': '1', 'title': 'Write a blog post'}
    """
    try:
        id = request.json['id']
        todo_ref.document(id).set(request.json)
        return jsonify({"success": True}), 200

    except Exception as e: return f"An Error occured : {e}"


@app.route('/')
def hello_world():
    return redirect("http://farhandika.work/")


@app.route('/callback', methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    command(event)


if __name__ == '__main__':
    app.run()
