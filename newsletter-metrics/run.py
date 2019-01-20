import os
import json

postreqdata = json.loads(open(os.environ['req']).read())
response = open(os.environ['res'], 'w')

track_event = postreqdata['msys']["track_event"]

#http://localhost:3000/api/v1/admin/link/newsletter-sent
if track_event["type"] == "click":
    response.write(track_event["target_link_url"])
elif track_event["type"] == "click":
    response.write(track_event["target_link_url"])
elif track_event["type"] == "click":
    response.write(track_event["target_link_url"])
#{
#	"campaign_id":"",
#	"target_link_name": "",
#	"target_link_url": ""
#}

response.close()