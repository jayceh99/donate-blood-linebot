from datetime import datetime
import time
from dateutil.relativedelta import relativedelta
def init_time(tmp_time):
    try:
        blood_cc = tmp_time[0:3]
        if blood_cc == '250':
            shift = 2
        else :
            shift = 3
        tmp_time = tmp_time[4:]
        tmp_time = str(tmp_time)
        yy , mm , dd  = tmp_time[0:4] , tmp_time[4:6] , tmp_time[6:8]
        tmp_time = yy+'-'+mm+'-'+dd
        this_time = yy+'-'+mm+'-'+dd
        tmp_time = datetime.strptime(tmp_time, '%Y-%m-%d') + relativedelta(months=shift)
        date_time = tmp_time
        tmp_time = int(time.mktime(tmp_time.timetuple())) 
        f = open(r'/opt/time.txt','w')
        f.write(blood_cc+','+str(tmp_time))
        f.close()

        del tmp_time  , shift
        return '這次捐血時間為 : '+str(this_time)+'\n捐血cc數為 : '+blood_cc+'\n下次捐血時間 : ' + str(date_time)[0:10]
    except Exception :
        return '日期輸入錯誤 請再輸入一次'

    

