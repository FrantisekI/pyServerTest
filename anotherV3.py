from flask import Flask, render_template
from requests import get
#import googleapiclient.discovery
#api_key = 'AIzaSyDbVmYfDx_GALgXTRgbAydqPMun4FKQaF4'

app = Flask(__name__)
@app.route('/')

def home():
    user = get_user()
    user_name = user["name"]
    uesr_trophies = str(user['trophies'])
    league = user['league']['iconUrls']['medium']

    return render_template('index.html', league=league, name=user_name, trophies=uesr_trophies)




#the code that accualy do something
headers = {
    'Accept': 'application/json',
    #for server
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjM4ZTcyOTAzLTIxOTEtNGE4Yy04Y2VhLTliMzUxNzNlODQwZiIsImlhdCI6MTcwMDgzNTM1NSwic3ViIjoiZGV2ZWxvcGVyL2ZlMjViNjQ3LTliNjEtZGMzYi1hMzBlLTQ0ODIwMjdjMGFjZCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjMuNzUuMTU4LjE2MyJdLCJ0eXBlIjoiY2xpZW50In1dfQ.oWEzkzAYOZJeQiKqoCBEowd50emdfEwh1Kq01l6klkWAuqnQyrEhFbUCADqilVU-zfElKSBs1VSdGnkGqm8MIg'
    #from home
    #'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImJmYWQwNTNhLTE1NDktNDE5YS05ZWUwLWY3NjA2OTdmNGMzOCIsImlhdCI6MTY5NDA5NjUwNiwic3ViIjoiZGV2ZWxvcGVyL2ZlMjViNjQ3LTliNjEtZGMzYi1hMzBlLTQ0ODIwMjdjMGFjZCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjgxLjI1LjI4LjIwIl0sInR5cGUiOiJjbGllbnQifV19.vO5eDkILD2fLdCDWfPeaB5EOVUIMu8QY0FxxV5fSA_U6osVAAxFjSGuBO1DY6kF-v0s-xM6MuyPcJrxb8JFYxQ' 
}

def get_user():
    response = get('https://api.clashofclans.com/v1/players/%23QQ2YYYQV2', headers=headers)
    user_json = response.json()
    return(user_json)





test = 0
if test==1:
    print(home())
else:
    if __name__ == '__main__':
        app.run(host='0.0.0.0')

