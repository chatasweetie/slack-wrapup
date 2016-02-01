import os
from slackclient import SlackClient

import time



SLACK_TOKEN=os.environ.get("SLACK_TOKEN", ['SLACK_TOKEN'])

sc = SlackClient(SLACK_TOKEN)
print sc.api_call("api.test")
print sc.api_call("channels.info", channel="test-channel-")

sc.rtm_connect()

while True:
	l = sc.rtm_read()
	if l == []:
		break
	else:
		print l

# if sc.rtm_connect():
#     while True:
#         print sc.rtm_read()
#         # time.sleep(1)
# else:
#     print "Connection Failed, invalid token?"