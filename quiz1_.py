from flask import Flask, render_template, request, jsonify, redirect
from pymongo import MongoClient

client = MongoClient('')
app = Flask(__name__)

db = client.dbsparta

doc = ([
    {'name': '이승만'},
    {'name': '윤보선'},
    {'name': '박정희'},
    {'name': '최규하'},
    {'name': '전두환'},
    {'name': '노태우'},
    {'name': '김영삼'},
    {'name': '김대중'},
    {'name': '노무현'},
    {'name': '이명박'},
    {'name': '박근혜'},
    {'name': '문재인'}
])

db.president.insert_many(doc)








