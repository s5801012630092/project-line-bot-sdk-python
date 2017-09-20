from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('FSEBgU182d0T8KamxSpYxvU+5ZALoEi/cCPHNTwQSCPKkdPY2rGFFgyJht3QGeWZTv8NtDsPUaE2mzUVQYuwtO31WMCgk7VS8U32JGF8wIxn+b/r8fwPrIU6jL1qflm+8K/hVBQUd7vTMLypOyvjPAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('8e6a8972aeb270d3ba26167cd9c57096')


@app.route("/callback", methods=['POST'])
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
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
