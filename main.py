import requests,os 
import smtplib,ssl 
import time
import json
import datetime
from webserer import keep_alive
import tolu
from pytz import timezone
secret = os.environ['pssd']
sender= 'ddkscowin@hotmail.com'
recevier = os.environ['recev']
def Status():
   ind_time = datetime.datetime.now(timezone("Asia/Kolkata")).strftime('%d-%m-%y ,%H:%M:%S')
   return ind_time
def Vaccine(X):
    GBH = []
    mil = 0
    DDKS = []
    count = 0
    hnio = 0
    today_date = datetime.date.today()

    new_date = today_date.strftime('%d-%m-%y')
  


    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

    fgh = X
    if len(str(fgh)) == 6:
        pincode = str(fgh)
    else:
        pincode = '247001'

    

    s = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode='+pincode+'&date='+new_date+'new.json',headers=headers)

    json_response = s.json()

    d = json.dumps(s.json(),sort_keys = True , indent = 4)

    gl = ''
    LIST15 = []
    for i in json_response['centers']:
        d = i['name']
        for k in i['sessions']:
            cap = k['available_capacity']
            dat = k['date']
            age = k['min_age_limit']
            dose=k['available_capacity_dose1']
            name = i['name']
            j = [d,dat,age,cap,dose,name]
            if int(j[2]) == 15 and int(j[4]) !=0:
              LIST15.append(j)
            DDKS.append(j)

    for n in DDKS:
        if n[3] == 0 :
            count+= 1

    if count == len(DDKS):
        print('Not Available')
        gl = 'Hello Sorry Not Available'

    else:
        for n in DDKS:
            if n[3] != 0 and n[4] !=0 :
                v = n
                GBH.append(n[2])
            
                hb = 'Appointment available at',v[0],'of date',v[1],'min age : ',v[2],'Available Appointment :',v[3]
                gl+='\n'
                gl+=str(hb)
    
    if gl != 'Hello Sorry Not Available':
        for i in GBH:
            if i == 15:
                hnio += 1
                tolu.telegram_bot_sendtext('Total Available Centres Which are not Fully Booked !(in Next 7 Days) : '+str(len(LIST15))+'\n\nChecked At :'+Status())

    
                """
                port = 587
                context = ssl.create_default_context()

                with smtplib.SMTP('smtp.office365.com',port) as server:
                    server.starttls()
                    server.login('ddkscowin@outlook.in',secret)
                    server.sendmail('ddkscowin@outlook.in',recevier,gl)
                    """
                mil = 1
                return mil
        if hnio == 0:
            print('Not Available for 18+')
            time.sleep(300)
 
           
keep_alive()
while True:
    mil= Vaccine(247001)
    if mil == 1:
        print( 'YO')
        time.sleep(3600)
    time.sleep(5)
         

