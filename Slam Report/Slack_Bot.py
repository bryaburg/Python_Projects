import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

try:
    # Call the files.upload method using the WebClient
    response = client.files_upload(
        channels="#general",
        file="/path/to/myfile.xlsm",
        initial_comment="Here is the .xlsm file you requested",
        title="myfile.xlsm"
    )
    print(response)
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    # (caused by an error returned by the Slack API)
    print("Error: {}".format(e))

# API token link https://api.slack.com/authentication/token-types#bot