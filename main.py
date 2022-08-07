import requests
import json
from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
s = requests.Session()

@app.route('/')
def get_draft_picks():
    url = 'https://www.pff.com/api/mock_draft_simulator/draft_picks'

    result_draft_picks = s.get(url)
    json_draft_picks = json.loads(result_draft_picks.text)
    return json_draft_picks

app.run()