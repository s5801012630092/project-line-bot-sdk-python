from flask import Flask, request
import json
import requests

# �ç YOURSECRETKEY ��ͧ��������ͧ��Ѻ�С���Ƕ֧㹢�鹵͹���� �
global LINE_API_KEY
LINE_API_KEY = '8e6a8972aeb270d3ba26167cd9c57096'

app = Flask(__name__)
 
@app.route('/')
def index():
    return 'This is chatbot server.'
@app.route('/bot', methods=['POST'])

def bot():
    # ��ͤ�������ͧ����觡�Ѻ
    replyStack = list()
   
    # ��ͤ���������Ѻ��
    msg_in_json = request.get_json()
    msg_in_string = json.dumps(msg_in_json)
    
    # Token ����Ѻ�ͺ��Ѻ (���繵�ͧ��㹡�õͺ��Ѻ)
    replyToken = msg_in_json["events"][0]['replyToken']

    # ���ͧ Echo ��ͤ�����Ѻ���ٻẺ������-�� (Ẻ json)
    replyStack.append(msg_in_string)
    reply(replyToken, replyStack[:5])
    
    return 'OK',200
 
def reply(replyToken, textList):
    # Method ����Ѻ�ͺ��Ѻ��ͤ��������� text ��Ѻ��Ѻ ��¹Ẻ�����¡����Ѻ
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': LINE_API_KEY
    }
    msgs = []
    for text in textList:
        msgs.append({
            "type":"text",
            "text":text
        })
    data = json.dumps({
        "replyToken":replyToken,
        "messages":msgs
    })
    requests.post(LINE_API, headers=headers, data=data)
    return

if __name__ == '__main__':
    app.run()
