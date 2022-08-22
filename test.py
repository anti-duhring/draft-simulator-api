import json

txt = {'Forfeited': 0, 'ARI': 1, 'Cardinals': 1, 'ATL': 2, 'Falcons': 2, 'BAL': 3, 'Ravens': 3, 'BUF': 4, 'Bills': 4, 'CAR': 5, 'Panthers': 5, 'CHI': 6, 'Bears': 6, 'CIN': 7, 'Bengals': 7, 'CLE': 8, 'Browns': 8, 'DAL': 9, 'Cowboys': 9, 'DEN': 10, 'Broncos': 10, 'DET': 11, 'Lions': 11, 'GB': 12, 'Packers': 12, 'HOU': 13, 'Texans': 13, 'IND': 14, 'Colts': 14, 'JAC': 15, 'Jaguars': 15, 'KC': 16, 'Chiefs': 16, 'LAR': 26, 'Rams': 26, 'LAC': 27, 'Chargers': 27, 'LV': 23, 'Raiders': 23, 'MIA': 17, 'Dolphins': 17, 'MIN': 18, 'Vikings': 18, 'NE': 19, 'Patriots': 19, 'NO': 20, 'Saints': 20, 'NYG': 21, 'Giants': 21, 'NYJ': 22, 'Jets': 22, 'PHI': 24, 'Eagles': 24, 'PIT': 25, 'Steelers': 25, 'SEA': 29, 'Seahawks': 29, 'SF': 28, '49ers': 28, 'TB': 30, 'Buccaneers': 30, 'TEN': 31, 'Titans': 31, 'WAS': 32, 'Commanders': 32}

for team in txt.keys():
    if "Jets" in team: 
        print(team)