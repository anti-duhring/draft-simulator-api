from bs4 import BeautifulSoup
import requests
import json
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config["DEBUG"] = True
s = requests.Session()
nfl_season = '2023'


@app.route('/draft-picks', methods=['GET'])
def get_draft_picks():
    url = 'https://www.pff.com/api/mock_draft_simulator/draft_picks'

    result_draft_picks = s.get(url)
    json_draft_picks = json.loads(result_draft_picks.text)
    response = jsonify(json_draft_picks)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/needs')
def get_needs():
    url = 'https://www.nflmockdraftdatabase.com/team-needs-' + nfl_season

    result_needs = s.get(url)
    doc_needs = BeautifulSoup(result_needs.text, "lxml")
    list_needs = doc_needs.find_all('li', class_='mock-list-item')

    json_needs = {}
    teams_id = {}
    f = open('NFL_teams.json')
    data_teams = json.load(f)

    for i in data_teams:
        teams_id[i['team_abbr']] = i['team_id']

    for item in list_needs:
        name = item.find('div', class_='pick-number').text
        needs = item.find('div', class_='player-name').text
        team_id = teams_id[name]

        json_needs[team_id] = needs.replace(' ', '').split(',')

    f.close()
    data = json.loads(json.dumps(json_needs))
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/picks', methods=['GET'])
def get_picks():
    url = 'https://tankathon.com/nfl/full_draft'

    result_picks = s.get(url)
    data_picks = BeautifulSoup(result_picks.text, 'lxml')

    # Json object to return at endpoint
    obj_picks = {}
    # All 7 tables containing all picks from each round
    tables_picks = data_picks.find_all('div', class_='full-draft-round')

    # Get all teams id
    teams_id = {'Forfeited': 0}
    f = open('NFL_teams.json')
    data_teams = json.load(f)

    for i in data_teams:
        teams_id[i['team_abbr']] = i['team_id']
        teams_id[i['team_name']] = i['team_id']
    f.close()

    # loop to get each round table containing picks
    for table in tables_picks:
        obj_round = []
        round = table.find('div', class_='round-title').text
        value = obj_round
        

        # All picks from this round
        picks_from_round = table.find_all('tr')

        # Loop to get each pick item from this round
        for pick_item in picks_from_round:
            pick_obj = {}

            pick_number = pick_item.find('td', class_='pick-number').text
            pick_team = pick_item.find('div', class_='desktop').text
            pick_prev_team = pick_item.find('div', class_='trade')

            # Get the team id
            for team in teams_id.keys():
                if pick_team in team:
                    pick_team_id = teams_id[team]
                    pick_obj['current_team_id'] = pick_team_id
            
            # Add pick property
            pick_obj['pick'] = int(pick_number)

            # Get prev team id
            if pick_prev_team is not None:
                pick_obj['prev_team_id'] = teams_id[pick_prev_team.text.replace(" ", "").replace("WSH", "WAS")]
            else: 
                pick_obj['prev_team_id'] = pick_team_id
            

            # Add this pick to round object
            obj_round.append(pick_obj)

        # Add this round in response object
        obj_picks[round[0]] = value

    response = jsonify(obj_picks)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

app.run()
