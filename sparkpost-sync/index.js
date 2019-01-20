var request = require("axios");

module.exports = function(context, myTimer) {
  var users = context.bindings.dnwDocument;
  var newRecipients = [];

  for (var i = 0; i < users.length; i++) {
    if (users[i].$v.subscribed.$v && users[i].$v.isActive.$v) {
      newRecipients.push({
        address: {
          email: users[i].$v.email.$v,
          name: users[i].$v.firstName.$v
        },
        substitution_data: {
          username: users[i].$v.username.$v,
          usubscribe_key: users[i].$v.keyUnsubscribe.$v
        }
      });
    }
  }

  request
    .put(
      "https://api.sparkpost.com/api/v1/recipient-lists/dnw-subscribers",
      { recipients: newRecipients },
      {
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
          Authorization: ""
        }
      }
    )
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
