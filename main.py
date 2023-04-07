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
#import requests
import os
import xml.dom.minidom
import init_time , location_inquiry , time_inquiry , update_time , blood_stock
app = Flask(__name__)

path = r'config.xml'
element = xml.dom.minidom.parse(path)

root = element.documentElement
channel_secret =  root.getElementsByTagName('channel_secret')[0].firstChild.data
channel_access_token =  root.getElementsByTagName('channel_access_token')[0].firstChild.data
your_user_ID =  root.getElementsByTagName('your_user_ID')[0].firstChild.data
location = root.getElementsByTagName('location')[0].firstChild.data

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    input_text = event.message.text

    if input_text == '初始時間':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='第一次使用請輸入上一次捐血量以及日期並用,分開 e.g. 500,20230307'))


    elif (input_text[0:3] == "250"  or input_text[0:3] == "500") and (str.isdigit(input_text[4:]) == True  and len(input_text[4:]) == 8):
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=init_time.init_time(input_text)))
        


    elif input_text == '更新時間':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請輸入這次的@捐血量 e.g. @250'))


    elif input_text == "@250"  or input_text == "@500":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=update_time.update_time(input_text)))


    elif input_text == '查詢預設地點':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=location_inquiry.location_inquiry(location)))
        

    elif input_text == '查詢特定地點':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請輸入縣市名稱 e.g. 臺北市 or 台北市'))


    elif input_text[0:3] in ('台北市,臺北市,新北市,宜蘭縣,花蓮縣,金門縣,連江縣,基隆市,桃園市,新竹縣,苗栗縣,新竹市,台中市,臺中市,彰化縣,南投縣,雲林縣,嘉義縣,台南市,臺南市,高雄市,屏東縣,台東縣,臺東縣,澎湖縣,嘉義市'):
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=location_inquiry.location_inquiry(input_text)))    


    elif input_text == '查詢時間':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=time_inquiry.time_inquiry()))
    
    elif input_text == '查詢血液庫存':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=blood_stock.blood_stock()))
        
    elif input_text == '?':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='使用說明:\n第一次使用請輸入  初始時間\n若當日捐完血請輸入  更新時間\n若想查詢上次捐血時間請輸入 查詢時間\n若想查詢特定捐血地點請輸入  查詢特定地點\n若想查詢預設的捐血地點請輸入 查詢預設地點\n若想查詢血液庫存量請輸入 查詢血液庫存'))
        
    else :
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='格式輸入錯誤\n或輸入?取得使用說明'))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
