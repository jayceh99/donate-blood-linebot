import time
import datetime
from dateutil.relativedelta import relativedelta

def  update_time():
    nowtime = datetime.datetime.now() + relativedelta(months=3)
    unixtime = int(time.mktime(nowtime.timetuple()))
    f = open(r'/opt/time.txt','w')
    f.write(str(unixtime))
    f.close()
    tmp = '下次捐血時間 : ' + str(nowtime)[0:10]
    del nowtime , unixtime
    return tmp 

