import time
import datetime
from dateutil.relativedelta import relativedelta

def  update_time(blood_cc):   
    blood_cc = blood_cc[1:4]
    if blood_cc == '250':
        shift = 2
    else :
        shift = 3
    strptime_time = datetime.datetime.now()
    next_strptime = strptime_time + relativedelta(months=shift)
    next_unixtime = int(time.mktime(next_strptime.timetuple()))
    f = open(r'/opt/time.txt','w')
    f.write(blood_cc +','+str(next_unixtime))
    f.close()


    del next_unixtime , shift
    return '這次捐血時間為 : '+str(strptime_time)[0:10]+'\n捐血cc數為 : '+blood_cc+'\n下次捐血時間 : ' + str(next_strptime)[0:10]


