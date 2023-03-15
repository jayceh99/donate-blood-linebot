# Ubuntu 20.04
# Python 3.10.9
*****
## Step1 建立自己的雲端主機
>[可參考這裡建立免費的GCP雲端主機](https://ithelp.ithome.com.tw/articles/10276289?sc=iThomeR "Title") 

>或是參考我的作法
>
>[按這裡前往GCP首頁](https://console.cloud.google.com/ "Title") 
>點選
![建立](https://user-images.githubusercontent.com/104083191/224921561-d305e544-8e8a-4ee9-a51f-96186119dea2.PNG)
>建立VM
>
>
>相關設定如下
>
>
>>![VM](https://user-images.githubusercontent.com/104083191/224922827-7d48441e-bbd3-4132-a453-9f8356ebdff4.PNG)
>
>
>點選變更更改硬碟大小與系統
>
>>![before](https://user-images.githubusercontent.com/104083191/224927851-92f7bd37-1911-49ce-9f56-f3c16f9f8acf.PNG)
>
>
>更改硬碟大小與系統如下圖
>
>
>>![after](https://user-images.githubusercontent.com/104083191/224925120-32d91f02-f4d4-4d28-ae19-33e10d78e072.PNG)
>
>
>允許HTTP與HTTPS流量
>
>>![https](https://user-images.githubusercontent.com/104083191/224925334-d3d27bb7-176d-4161-89f3-2e22b360d009.PNG)
>
>
>點選建立,到這裡已經成功建立屬於自己的VM囉~
>
>
>GCP免費政策如下，可以自己選喜歡的地區，也要注意不要玩過頭網路流量爆掉囉～
>>![FREE](https://user-images.githubusercontent.com/104083191/224926236-c4dbecc6-c219-486d-b68e-09707f427128.PNG)
>
>
*****
## Step2 申請屬於自己的line bot 
>[可參考這裡建立line bot](https://ithelp.ithome.com.tw/articles/10215268 "title")
>
>網路上有相當多教學就不再贅述
>
*****
## Step3 建立環境
>[按這裡前往GCP首頁](https://console.cloud.google.com/ "Title") 
>
>選擇VM執行個體
>
>>![2](https://user-images.githubusercontent.com/104083191/225214892-2e97bd37-dceb-48a7-8c1a-21146ea73574.PNG)
>
>點選SSH
>
>>![3](https://user-images.githubusercontent.com/104083191/225215179-83ed0a55-dc66-4b8a-97f6-00e3419580c4.PNG)
>>
>更新軟體包(?)在視窗中輸入
>  
>```sudo apt update && sudo apt upgrade```
>
>在視窗中輸入把專案抓回來
>
>```sudo git clone https://github.com/jayceh99/donate_blood_linebot.git```
>
>(或是要把專案叉回去![擷取](https://user-images.githubusercontent.com/104083191/225216495-589561e5-4113-477e-8016-079df7ee23df.PNG)
自己的git hub也可以！ 建議叉回去後續想要自己修改也會比較方便 ！)
>
>更改專案佔存的資料夾讀寫權限,在視窗中輸入
>
>```sudo chmod 755 /opt/ ```




