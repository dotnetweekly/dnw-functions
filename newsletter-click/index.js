const request = require("axios");
const url =
  "https://dnw-api.azurewebsite.net/api/v1/admin/link/newsletter-click";

module.exports = function(context, req) {
  const token = `Bearer ${os.environ["DNW_TOKEN"]}`;
  if (!(req.body || !req.body.msys || !req.body.msys.track_event)) {
    context.res = {
      body: "No msys or track_event found"
    };
  }

  const track_event = req.body["msys"]["track_event"];
  const post_fields = {
    target_link_url: track_event["target_link_url"],
    target_link_name: track_event["target_link_name"],
    campaign_id: track_event["campaign_id"]
  };

  request
    .post(url, post_fields, {
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
        Authorization: token
      }
    })
    .then(function(response) {
      if (response.status === 200) {
        context.log("done");
        context.done();
      } else {
        context.log(response.status);
        context.done();
      }
    })
    .catch(function(err) {
      context.log(err.response.data);
      context.done();
    });
};
