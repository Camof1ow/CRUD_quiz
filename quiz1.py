from flask import Flask, render_template, request, jsonify, redirect
from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.7nr2yln.mongodb.net/?retryWrites=true&w=majority')
app = Flask(__name__)

db = client.dbsparta

#Q1 역대대통령 이름을 db로 저장
doc = ([
    {'name': '이승만'},
    {'name': '윤보선'},



#Q2 저장한 데이터를
        #이승만
        #윤보선
        #박정희
#순으로 데이터 출력
all_users = list(db.president.find({},{'_id':False}))
for name in all_users:



#Q3 저장한 데이터를 update로 취임순서 집어넣기
all_users = list(db.president.find({},{'_id':False}))
place = 1
for name in all_users:









