from flask import Flask
#import googleapiclient.discovery
#api_key = 'AIzaSyDbVmYfDx_GALgXTRgbAydqPMun4FKQaF4'


app = Flask(__name__)

@app.route("/")


def index():
    #print(response)
    return '<button type="button">Click Me!</button>'

if __name__ == '__main__':
   app.run(host='127.0.0.1', port=80)
