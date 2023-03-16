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
>更新軟體包(?)
>  
>```sudo apt update && sudo apt upgrade```
>
>把專案抓回來
>
>```sudo git clone https://github.com/jayceh99/donate_blood_linebot.git```
>
>(或是要把專案叉回去![擷取](https://user-images.githubusercontent.com/104083191/225216495-589561e5-4113-477e-8016-079df7ee23df.PNG)
自己的git hub也可以！ 建議叉回去後續想要自己修改也會比較方便 ！)
>
>更改資料夾讀寫權限
>
>```sudo chmod 777 /opt/ ```
>
>移到專案資料夾內
>
>```cd donate_blood_linebot/```
>
>安裝套件管理器
>
>```sudo apt install pip```
>
>安裝所需套件
>
>```sudo pip install flask line-bot-sdk python-dateutil lxml apscheduler```
>
>修改設定檔
>
>```sudo vim config.xml```
>
>按i進入編輯,前三項資訊可以在LINE Developers裡面找到
>
>Channel secret跟Your user ID 在Basic settings裡面
>
>>![擷取](https://user-images.githubusercontent.com/104083191/225235275-e0bcda2c-8f97-4725-9e63-7413b8fefece.PNG)
>
>Channel access token在Messaging API裡面
>
>>![擷取](https://user-images.githubusercontent.com/104083191/225235795-bab81cd7-8ae0-4d13-b349-db8301f4ac9a.PNG)
>
>最後location就填上你最常出沒的區域,像我住在林口我就填    
>```新北市林口區```
>
>整份文件填起來像這樣
>```
> <?xml version="1.0"?>
> <data>
>        <channel_secret>xxxxxxxxxxxxxxxxxxxxxxxxxx</channel_secret>
>        <channel_access_token>xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx</channel_access_token>
>        <your_user_ID>xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx</your_user_ID>
>        <location>新北市林口區</location>
> </data>
>```
>
>填完後按鍵盤左上角的esc退出編輯,並輸入```:wq```儲存並離開
## Step4 啟動line bot
>直接輸入
>```sudo nohup python3 main.py & ```
>
>讓主程式在背景運作
>
>下載ngrok

>``` curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok ```
>
>[並到官網申請一組金鑰](https://ngrok.com/ "Title") 
>
>![擷取](https://user-images.githubusercontent.com/104083191/225240083-d518d5d2-40d5-42f3-9aa1-17ac0a868c6b.PNG)
>
>記住被碼掉的部分(這個是金鑰)
>
>回到GCP的VM裡,輸入
>
>```ngrok authtoken 你的金鑰 ```
>
>啟動ngrok 並放到背景運行
>
>```nohup ngrok http 5000 &```
>
>將ngrok連線資訊抓出來
>
>```sudo wget 127.0.0.1 http://127.0.0.1:4040/api/tunnels```
>
>查看外部https網址
>
>```cat tunnels```
>
>從裡面找到```public_url```後面的https網址
>
>把他貼到line bot 內Messaging API 的 Webhook URL
>
>如下圖
>
>![擷取](https://user-images.githubusercontent.com/104083191/225245052-13941756-b4ff-4092-b0f4-74ccae9bdb25.PNG)
>
>好了之後點update再點Verify驗證,跳出Success的視窗,代表機器人已經上線囉
>
>之後就可以打開line開始初始化囉~

## step5 讓line bot自動推播

>初始化過後,只要能夠再次捐血的時間一到,每個禮拜天早上8點就會開始自動推播(auto_push_info.py內可更改時間)接下來一個禮拜(日~六)
>
>最常出沒的區域(設定檔內可以更改)哪裡有捐血車囉
>
>回到專案資料夾內
>
>``` cd donate_blood_linebot/ ```
>
>把自動推播的程式叫起來並放到背景運行
>
>```nohup python3 auto_push_info.py & ```


以上就大功告成囉~
捐血一袋,救人一命,每次捐完血都要給自己一個讚
