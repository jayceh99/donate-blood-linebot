from linebot import LineBotApi
from linebot.models import TextSendMessage
from lxml import etree , html
import xml.dom.minidom
from apscheduler.schedulers.blocking import BlockingScheduler
import location_inquiry
import time


def auto_push_info(channel_access_token,your_user_ID,location):

    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.push_message(your_user_ID, TextSendMessage(text=location_inquiry.location_inquiry(location)))


def main():
    f = open(r'/opt/time.txt','r')
    time_q = f.read()
    if float(time_q[4:]) < time.time():
        path = r'config.xml'
        element = xml.dom.minidom.parse(path)
        root = element.documentElement
        channel_access_token =  root.getElementsByTagName('channel_access_token')[0].firstChild.data
        your_user_ID =  root.getElementsByTagName('your_user_ID')[0].firstChild.data
        location = root.getElementsByTagName('location')[0].firstChild.data
        auto_push_info(channel_access_token , your_user_ID , location)

sched = BlockingScheduler()
@sched.scheduled_job('cron', day_of_week='sun', hour=8)
def scheduled_job():
    main()
sched.start()


    