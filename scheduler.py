import schedule
import requests
import json

def injest_positions():
    r = requests.get('https://opensky-network.org/api/states/all')
    headers = {'content-type': 'application/json'}
    data = json.dumps(r.text)
    data = json.loads(data)
    requests.post('http://localhost:5000/api/positions', data=data, headers=headers)
    print("Added " + str(len(r.json()['states'])) + " positions")

schedule.every(1).minute.do(injest_positions)

while True:
    schedule.run_pending()