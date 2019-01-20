import os
import json
import requests

token = "Bearer " % os.environ['DNW_TOKEN']

response = open(os.environ['res'], 'w')
postreqdata = json.loads(response.read())

if (not("msys" in postreqdata)):
    response.write("")
    response.close()
else:
    track_event = postreqdata["msys"]["track_event"]
    response.write(json.dumps(postreqdata))
    response.close()

    if track_event["type"] == "click":
        payload = {"target_link_url": track_event["target_link_url"],
                   "target_link_name": track_event["target_link_name"], "campaign_id": track_event["campaign_id"]}
        headers = {'Authorization': token, 'Content-Type': 'application/json'}
        r = requests.get(
            'https://dnw-api.azurewebsite.net/api/v1/admin/link/newsletter-click', data=payload, headers=headers)
        response.write(r.status_code)
    # {
    #	"campaign_id":"",
    #	"target_link_name": "",
    #	"target_link_url": ""
    # }

response.close()
