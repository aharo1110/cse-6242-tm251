from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
import csv

app = Flask(__name__)
bootstrap = Bootstrap5(app)

paths = {
    "csv": "data/fifa_tweets_sentiment.csv"
}

def read_data():
    rows = []
    labels = {}

    with open(paths["csv"], 'r') as file:
        reader = csv.reader(file)
        l_temp = next(reader)

        for i in range(len(l_temp)):
            labels[l_temp[i]] = i

        for i in reader:
            rows.append(i)
    
    return rows, labels

r, l = read_data()

@app.route("/")
def main():

    matches = list(set([i[l["nearest_event_match"]] for i in r if i[l["nearest_event_match"]] != "none"]))
    matches.sort()

    return render_template('index.html', matches=matches)

@app.route("/match", methods=['GET'])
def match():
    if request.method != 'GET':
        return render_template('match-no.html')
    match_data = [i for i in r if i[l["nearest_event_match"]] == request.args["match"]]

    timestamps = [i[l["datetime"]] for i in match_data]

    return render_template('match.html', name=request.args["match"], times=timestamps)