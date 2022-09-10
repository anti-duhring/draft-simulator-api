from bs4 import BeautifulSoup
import requests
import json
from flask import  jsonify

class BigBoardCrawler:

    def initialize(self, nfl_season):
        self.url = 'https://www.nflmockdraftdatabase.com/big-boards/2023/consensus-big-board-{}'.format(nfl_season)
        self.result = {"players": []}

        self.request()

        return jsonify(self.result)
    
    def request(self):
        result_text = requests.get(self.url)
        result_soup = BeautifulSoup(result_text.text, 'lxml')
        mock_list_item = result_soup.find_all('li', class_='mock-list-item')

        self.result['amount'] = len(mock_list_item)

        self.loop_list_item(mock_list_item=mock_list_item)

    def loop_list_item(self, mock_list_item):
        
        for player in mock_list_item:
            name = player.find('div', class_='player-name').text
            rank = int(player.find('div', class_='pick-number').text)
            details = player.find('div', class_='college-details').text
            position = details.split('|')[0].replace(' ','')
            try:
                college = player.find('div', class_='college-details').select_one('a').text
            except:
                college = details.split('| ')[1]

            player_data = {
                "name": name,
                "ranking": rank,
                "position": position,
                "college": college
            }

            self.result['players'].append(player_data)

