from datetime import datetime
import time

def init_time(tmp_time):
    try:
        tmp_time = str(tmp_time)
        yy , mm , dd  = tmp_time[0:4] , tmp_time[4:6] , tmp_time[6:8]
        tmp_time = yy+'-'+mm+'-'+dd
        date_time = yy+'-'+mm+'-'+dd
        tmp_time = time.strptime(tmp_time, '%Y-%m-%d')
        tmp_time = int(time.mktime(tmp_time)) 
        f = open(r'/opt/time.txt','w')
        f.write(str(tmp_time))
        f.close()
        del tmp_time
        return '時間已更新為 '+date_time
    except Exception :
        return '日期輸入錯誤 請再輸入一次'

    

