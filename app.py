from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
import csv

app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.config['TEMPLATES_AUTO_RELOAD'] = True

paths = {
    "csv_events": "data/fifa_event_detection_results.csv",
    "csv_sentiment": "data/fifa_tweets_sentiment.csv"
}

def read_data():
    rows = []
    labels = {}

    with open(f"static/{paths["csv_events"]}", 'r') as file:
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
    dates = ["2018-07-01", "2018-07-03", "2018-07-15"]
    return render_template('index.html', matches=dates)

@app.route("/match", methods=['GET'])
def match():
    if request.method != 'GET':
        return render_template('match-no.html')

    return render_template('match.html', name=request.args["match"], path=paths["csv_sentiment"])

@app.route("/events")
def events():
    detected_events = [i[l["event_name"]] for i in r if i[l["window_tweet_total"]] != "0"]
    
    return render_template('events.html', path_sentiment=paths["csv_sentiment"], path_event=paths["csv_events"], events=detected_events)