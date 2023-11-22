from flask import Flask
#import googleapiclient.discovery
#api_key = 'AIzaSyDbVmYfDx_GALgXTRgbAydqPMun4FKQaF4'


app = Flask(__name__)

@app.route("/")




def index():

    '''api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=api_key)
    request = youtube.channels().list(
        part="snippet,statistics",
        id="UChFur_NwVSbUozOcF_F2kMg"
    )
    response = request.execute()'''
    
    #print(response)
    return '<button type="button">Click Me!</button>'

if __name__ == '__main__':
   app.run(host='127.0.0.1', port=80)