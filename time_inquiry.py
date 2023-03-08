import time
import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta

def time_inquiry():
    f = open(r'/opt/time.txt','r')
    tmp_time = f.read()
    f.close()
    tmp_time = datetime.fromtimestamp(int(tmp_time))
    tmp_time = tmp_time - relativedelta(months=3)
    return '上次捐血時間為 : '+str(tmp_time)[0:10]


    
