from pymongo import MongoClient
from flask import Flask, request #import main Flask class and request object
import datetime

app = Flask(__name__) #create the Flask app 


@app.route('/datetime')
def process_date():
    now = datetime.datetime.utcnow()
    return 'UTC:'+str(now.year)+','+str(now.month)+','+str(now.day)+','+str(now.hour)+','+str(now.minute)+','+str(now.second)+'#'


@app.route('/add', methods=['PUT'])
def process_data():        
    data = eval(request.headers['X-Smartcitizendata'][1:-1])
    data['panel'] = int(data['panel'])
    data['co'] = int(data['co'])
    data['nets'] = int(data['nets'])
    data['hum'] = int(data['hum'])
    data['temp'] = int(data['temp'])
    data['bat'] = int(data['bat'])
    data['no2'] = int(data['no2'])
    data['noise'] = int(data['noise'])
    data['light'] = int(data['light'])
    data['macaddr'] = request.headers['X-Smartcitizenmacaddr']
    data['_id'] = datetime.datetime.strptime(data['timestamp'], "%Y-%m-%d %H:%M:%S")
    data['version'] = request.headers['X-Smartcitizenversion']
    myclient = MongoClient("mongodb://localhost:27017/")
    mydb = myclient['smartcitizen']
    mycol = mydb['data']
    try:
        print(data)
        #mycol.insert_one(data)
    except:
        print("mongoproblemo")
    return "200"
