from bs4 import BeautifulSoup
import requests
import json
from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
s = requests.Session()
nfl_season = '2023'

@app.route('/draft-picks')
def get_draft_picks():
    url = 'https://www.pff.com/api/mock_draft_simulator/draft_picks'

    result_draft_picks = s.get(url)
    json_draft_picks = json.loads(result_draft_picks.text)
    return json_draft_picks

@app.route('/needs')
def get_needs():
    url = 'https://www.nflmockdraftdatabase.com/team-needs-'+nfl_season

    result_needs = s.get(url)
    doc_needs = BeautifulSoup(result_needs.text, "lxml")
    list_needs = doc_needs.find_all('li', class_='mock-list-item')

    json_needs = { }
    teams_id = {}
    f = open('NFL_teams.json')
    data_teams = json.load(f)

    for i in data_teams:
        teams_id[i['team_abbr']] = i['id']

    for item in list_needs:
        name = item.find('div', class_='pick-number').text
        needs = item.find('div', class_='player-name').text
        team_id = teams_id[name]

        json_needs[team_id] = needs.replace(' ','').split(',')

    f.close()
    return json.loads(json.dumps(json_needs))

app.run()