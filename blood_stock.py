import requests
from lxml import html

def blood_stock():
    r = requests.get('https://www.blood.org.tw/Internet/main/index.aspx')
    data = html.fromstring(r.content.decode('UTF-8'))

    last_time = '/html/body/div[3]/div/form/table[3]/tr[1]/td[2]/div[2]/table[1]/tr/th/span/text()'
    last_time = str(data.xpath(last_time))
    last_time = last_time.replace('[\'','').replace('\']','')
    data_tmp = []
    for i  in range (2,6):
        blood_xpath = '/html/body/div[3]/div/form/table[3]/tr[1]/td[2]/div[2]/table[2]/tr['+str(i)+']/th/text()'
        blood_type = str(data.xpath(blood_xpath))
        blood_type = blood_type.replace('[\'','').replace('\']','')
        data_tmp.append(blood_type)
        for j in range(1,5):
            blood_xpath = '/html/body/div[3]/div/form/table[3]/tr[1]/td[2]/div[2]/table[2]/tr['+str(i)+']/td['+str(j)+']/img/@alt'
            blood_tmp = str(data.xpath(blood_xpath))
            blood_tmp = blood_tmp.replace('[\'','').replace('\']','')
            data_tmp.append(blood_tmp)

    tpe = '台北\n%s %s\n%s %s\n%s %s\n%s %s\n\n' % (data_tmp[0],data_tmp[1],data_tmp[5],data_tmp[6],data_tmp[10],data_tmp[11],data_tmp[15],data_tmp[16])
    hch = '新竹\n%s %s\n%s %s\n%s %s\n%s %s\n\n' % (data_tmp[0],data_tmp[2],data_tmp[5],data_tmp[7],data_tmp[10],data_tmp[12],data_tmp[15],data_tmp[17])
    tch = '台中\n%s %s\n%s %s\n%s %s\n%s %s\n\n' % (data_tmp[0],data_tmp[3],data_tmp[5],data_tmp[8],data_tmp[10],data_tmp[13],data_tmp[15],data_tmp[18])
    khs = '高雄\n%s %s\n%s %s\n%s %s\n%s %s\n\n' % (data_tmp[0],data_tmp[4],data_tmp[5],data_tmp[9],data_tmp[10],data_tmp[14],data_tmp[15],data_tmp[19])
    blood_table = tpe+hch+tch+khs+last_time
    del r , data , last_time , data_tmp , blood_xpath , blood_type , blood_tmp ,tpe ,hch , tch , khs
    return blood_table