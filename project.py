from flask import  Flask, jsonify, request
import csv
allarticles=[]
with open("articles.csv",encoding="UTF-8")as f:
    reader=csv.reader(f)
    data=list(reader)
    allarticles=data[1:]
liked_articles=[]
notliked_articles=[]

app=Flask(__name__)
@app.route("/get-article")
def get_article():
    return jsonify({
        "data":allarticles[0],
        "status":"success"
    })
@app.route("/liked-article",methods=["POST"])
def liked_articles():
    article=allarticles[0]
    allarticles=allarticles[1:]
    liked_articles.append(article)
    return jsonify({
        "status":"success"
    }),201
   
@app.route("/notliked-article",methods=["POST"])
def notliked_articles():
    article=allarticles[0]
    allarticles=allarticles[1:]
    notliked_articles.append(article)
    return jsonify({
        "status":"success"
    }),201

if __name__=="__main__":
    app.run()