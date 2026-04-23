from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
import csv
from collections import defaultdict

app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.config['TEMPLATES_AUTO_RELOAD'] = True

paths = {
    "csv": "static/data/fifa_tweets_sentiment.csv",
    "csv_indir": "data/fifa_tweets_sentiment.csv",
    "network_nodes": "data/network/nodes.json",
    "network_edges": "data/network/edges.json",
    "network_homogeneity": "data/network/homogeneity.json",
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

def build_matchdate_index(rows, labels):
    """Return a list of {date, matches_label} derived from rows with a known event."""
    date_to_matches = defaultdict(set)
    for row in rows:
        match = row[labels["nearest_event_match"]]
        if match == "none" or not match:
            continue
        dt = row[labels["datetime"]]
        if len(dt) >= 10:
            date_to_matches[dt[:10]].add(match)

    index = []
    for date in sorted(date_to_matches):
        matches = sorted(date_to_matches[date])
        index.append({"date": date, "label": f"{date} — {' · '.join(matches)}"})
    return index

r, l = read_data()
matchdate_index = build_matchdate_index(r, l)

@app.route("/")
def main():
    return render_template('index.html', matchdates=matchdate_index)

@app.route("/match", methods=['GET'])
def match():
    if request.method != 'GET':
        return render_template('match-no.html')

    date = request.args.get("match")
    if not date or not any(md["date"] == date for md in matchdate_index):
        return render_template('match-no.html')

    return render_template(
        'match.html',
        name=date,
        path=paths["csv_indir"],
        network_nodes_path=paths["network_nodes"],
        network_edges_path=paths["network_edges"],
        network_homogeneity_path=paths["network_homogeneity"],
    )