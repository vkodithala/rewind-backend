from flask import Flask, request, jsonify
from pymongo import MongoClient
import json, sys
import certifi
from datetime import datetime, date

app = Flask(__name__)

uri = "mongodb+srv://admin:Rewind1234!@hackathon.otz1cym.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, tlsCAFile=certifi.where())
db = client["Rewind"]
col = db["Test"]

#pn is phone number
@app.route("/getToday/<int:pn>", methods=['GET'])
def get_today(pn):
    today = str(datetime.now())
    pattern = today[0:10]

    query = {
        "phoneNumber" : pn,
        "dateTime": {"$regex": pattern}
    }
    cursor = col.find(query)
    document_list = [doc for doc in cursor]
    json_data = json.dumps(document_list, default=str, indent=2)
    return json_data

@app.route("/getAll/<int:pn>", methods=['GET'])
def get_all(pn):
    query = {
        "phoneNumber": pn
    }
    cursor = col.find(query)
    document_list = [doc for doc in cursor]
    json_data = json.dumps(document_list, default=str, indent=2)
    return json_data

@app.route("/postEntry", methods=['POST'])
def post_entry():
    input_string = request.json['payload']
    items = parse_payload(input_string)
    fixed = {
        "dateTime" : items[0],
        "phoneNumber" : items[1],
        "text" : items[2]
    }
    result = col.insert_one(fixed)
    return f"Inserted document ID: {result.inserted_id}"

# # def parse_payload(s: str) -> []:
# #     ret = []
# #     if(len(s) > 21):
# #         unix_time = int(s[0:10])
# #         normal_time = datetime.utcfromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S')
# #         phone_no = int(s[10:21])
# #         message = s[21:]
# #         ret.append(normal_time)
# #         ret.append(phone_no)
# #         ret.append(message)
# #     return ret

# @app.route("/getMonth/<int:pn>", methods=['GET'])
# def get_month(pn):
#     today = str(datetime.now())
#     pattern = today[0:10]

#     query = {
#         "phoneNumber" : pn,
#         "dateTime": {"$regex": pattern}
#     }
#     cursor = col.find(query)
#     document_list = [doc for doc in cursor]
#     json_data = json.dumps(document_list, default=str, indent=2)
#     return json_data


# # @app.route("/getPast7/<int:pn>", methods=['GET'])
# # def getPast7(pn):
# #     today = str(datetime.now())
# #     pattern = today[0:10]
# #     currDay = int(pattern[-2:])
# #     longString = ""
# #     for i in range(currDay - 6, currDay + 1):
# #         currPatt = today[0:8] + str(i)
# #         if (i < (currDay)):
# #             currPatt += "|"
# #         longString += currPatt
# #     query = {
# #         "phoneNumber" : pn,
# #         "dateTime": {"$regex": longString}
# #     }
# #     cursor = col.find(query)
# #     document_list = [doc for doc in cursor]
# #     json_data = json.dumps(document_list, default=str, indent=2)
# #     return json_data
