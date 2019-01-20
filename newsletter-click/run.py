import os
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

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
        post_fields = {"target_link_url": track_event["target_link_url"],
                       "target_link_name": track_event["target_link_name"], "campaign_id": track_event["campaign_id"]}
        headers = {'Authorization': token, 'Content-Type': 'application/json'}
        # Set destination URL here
        url = 'https://dnw-api.azurewebsite.net/api/v1/admin/link/newsletter-click'

        request = Request(url, urlencode(
            post_fields).encode(), headers=headers)
        json = urlopen(request).read().decode()
        #r = requests.get(url, data=post_fields, headers=headers)
    # {
    #	"campaign_id":"",
    #	"target_link_name": "",
    #	"target_link_url": ""
    # }

response.close()
