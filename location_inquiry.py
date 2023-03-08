from lxml import html
import requests

def location_inquiry(location):
    tpe_url = 'https://www.tp.blood.org.tw/Internet/taipei/LocationWeek.aspx?site_id=2'
    hch_url = 'https://www.sc.blood.org.tw/Internet/hsinchu/LocationWeek.aspx?site_id=3'
    tch_url = 'https://www.tc.blood.org.tw/Internet/Taichung/LocationWeek.aspx?site_id=4'
    khs_url = 'https://www.ks.blood.org.tw/Internet/Kaohsiung/LocationWeek.aspx?site_id=6'
    tpe_location = ('台北市,臺北市,新北市,宜蘭縣,花蓮縣,金門縣,連江縣,基隆市')
    hch_location = ('桃園市,新竹縣,苗栗縣,新竹市')
    tch_location = ('台中市,臺中市,彰化縣,南投縣,雲林縣')
    khs_location = ('嘉義縣,台南市,臺南市,高雄市,屏東縣,台東縣,臺東縣,澎湖縣,嘉義市')
    if location[0:3] in tpe_location :
        url = tpe_url
    elif location[0:3] in hch_location :
        url = hch_url
    elif location[0:3] in tch_location :
        url = tch_url
    elif location[0:3] in khs_location :
        url = khs_url
    else:
        return '格式錯誤 請輸入正確縣市名稱 e.g. 台北市 or 臺北市 '
    r = requests.get(url)
    data = html.fromstring(r.content.decode('UTF-8'))
    day_stack = [0]*7
    addr = [0]*7
    typo = False
    if '台' in location or '臺' in location :
        location_1 = '臺'+location[1:]
        location_2 = '台'+location[1:]
        typo = True
    for i in range(1,8):
        tmp = ''
        day = data.xpath('/html/body/div[2]/div/form/div/div[2]/div[2]/div[3]/div[3]/div[2]/div/div[2]/table/tr['+str(i)+']/td[1]/text()')
        day = str(day).replace('\\r\\n','').replace(' ','').replace('[\'','').replace('\']','')
        day_stack[i-1] = day
        count = data.xpath('/html/body/div[2]/div/form/div/div[2]/div[2]/div[3]/div[3]/div[2]/div/div[2]/table/tr['+str(i)+']/td[2]/table/tr')
        for  j in range(1,len(count)+1):
            k = data.xpath('/html/body/div[2]/div/form/div/div[2]/div[2]/div[3]/div[3]/div[2]/div/div[2]/table/tr['+str(i)+']/td[2]/table/tr['+str(j)+']/td/span/text()')
            if typo == True :
                if location_1 in str(k)  or location_2 in str(k):
                    k = str(k).replace('[\'','').replace('\']','')
                    tmp = tmp + k +'\n'
            
            elif location in str(k) :
                k = str(k).replace('[\'','').replace('\']','')
                tmp = tmp + k +'\n'

        addr[i-1] = tmp
    tmp = ''
    for i in range (0,7):
        if addr[i] != '':
            tmp  = tmp + day_stack[i]+'\n'+addr[i]+'\n'
    if tmp == '':
        tmp = '這週\n'+day_stack[0]+'~'+day_stack[6]+'\n'+location+'沒有捐血車'
    if typo == False :
        del tpe_url , hch_url , tch_url , khs_url , tpe_location ,hch_location , tch_location , khs_location , location , url , r , data , day_stack , addr , day , count , i , j , k  , typo 
    else :
        del tpe_url , hch_url , tch_url , khs_url , tpe_location ,hch_location , tch_location , khs_location , location , url , r , data , day_stack , addr , day , count , i , j , k  , typo , location_1 , location_2
    return tmp
