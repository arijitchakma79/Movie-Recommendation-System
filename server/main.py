from recommender import Recommender

import json
from flask import Flask, jsonify, request

recommender = Recommender()
app = Flask(__name__)

@app.route('/', methods=['GET'])
def movies_by_name():
 movieName = request.args.get('name')
 
 try:
    movies = recommender.recommend(movieName)
    return jsonify({'movies':movies, 'status':'ok'})
 except:
   return jsonify({'status':'error'})

print("Listening...")
app.run(port=5000)