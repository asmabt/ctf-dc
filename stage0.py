from utils.auth import IntersightAuth
import requests
import json
from env import config

auth = IntersightAuth(secret_key_filename=config['INTERSIGHT_CERT'],
                      api_key_id=config['INTERSIGHT_API_KEY'])

BASE_URL = 'https://www.intersight.com/api/v1'

# retreive ntp policies
ntp_url = f"{BASE_URL}/ntp/Policies"
headers = {
    "Accept": "application/json"
}
ntp_resp = requests.get(ntp_url, auth=auth, headers=headers)
print(json.dumps(ntp_resp.json(), indent=4))
