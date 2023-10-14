from flask import Flask, request, jsonify
# from pymongo import MongoClient
# import json, sys, certifi, openai
# from typing import List
# from datetime import datetime, date
# from dotenv import dotenv_values

app = Flask(__name__)

# mongo_pwd = dotenv_values()["MONGO_PWD"]
# uri = f"mongodb+srv://admin:{ mongo_pwd }@hackathon.otz1cym.mongodb.net/?retryWrites=true&w=majority"
# client = MongoClient(uri, tlsCAFile=certifi.where())
# db = client["Rewind"]
# col = db["Test"]

# def get_embedding(entry, model="text-embedding-ada-002"):
#     entry = entry.replace("\n", " ")
#     return openai.Embedding.create(input = [entry], model=model)['data'][0]['embedding']

@app.route("/")
def test_func():
    return "hello world"

# #pn is phone number
# @app.route("/getToday/<int:pn>", methods=['GET'])
# def get_today(pn):
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

# @app.route("/getAll/<int:pn>", methods=['GET'])
# def get_all(pn):
#     query = {
#         "phoneNumber": pn
#     }
#     cursor = col.find(query)
#     document_list = [doc for doc in cursor]
#     json_data = json.dumps(document_list, default=str, indent=2)
#     return json_data

# @app.route("/postEntry", methods=['POST'])
# def post_entry():
#     input_string = request.json['payload']
#     items = parse_payload(input_string)
#     date_time, phone_no, entry = items
#     fixed = {
#         "dateTime" : date_time,
#         "phoneNumber" : phone_no,
#         "entry" : entry,
#         "embedding": get_embedding(entry)
#     }
#     result = col.insert_one(fixed)
#     return f"Inserted document ID: {result.inserted_id}"

# @app.route("/getMonth/<int:pn>", methods=['GET'])
# def get_month(pn):
#     today = str(datetime.now())
#     pattern = today[0:7]

#     query = {
#         "phoneNumber" : pn,
#         "dateTime": {"$regex": pattern}
#     }
#     cursor = col.find(query)
#     document_list = [doc for doc in cursor]
#     json_data = json.dumps(document_list, default=str, indent=2)
#     print(len(document_list))
#     return json_data

# def parse_payload(s: str) -> List:
#     ret = []
#     if(len(s) > 21):
#         unix_time = int(s[0:10])
#         normal_time = datetime.utcfromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S')
#         phone_no = int(s[10:21])
#         message = s[21:]
#         ret.append(normal_time)
#         ret.append(phone_no)
#         ret.append(message)
#     return ret


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
