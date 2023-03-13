import time
import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta

def time_inquiry():
    f = open(r'/opt/time.txt','r')
    tmp_time = f.read()
    f.close()

    blood_cc = tmp_time[0:3]
    next_strptime = tmp_time[4:]
    if blood_cc == '250':
        shift = 2
    else :
        shift = 3
    next_strptime = datetime.fromtimestamp(int(next_strptime))
    strptime_time = next_strptime - relativedelta(months=shift)


    return '上次捐血時間為 : '+str(strptime_time)[0:10] + '\n上次捐血cc數為 : ' + blood_cc +'\n下次捐血時間 : ' + str(next_strptime)[0:10]



    
