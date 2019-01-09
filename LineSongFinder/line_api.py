import requests
import json
from . import song_recog_api

# Setup parameter for Line API
url = "https://api.line.me/v2/bot/message/reply"

querystring = {"Content-Type": "application/json",
               "Authorization": "%20Bearer%201hFvFhSffFNku6B/E0Yt+7a7yNF2xLU0/yMz5SfoEUBsnLX1JddQHXg2q0lWCXYnsjjFTi85oqD0DRsVre3UgombcFA+8ZfpSDbWQRjZ6Qx3wNwLt8uPP5uwFwpjP6X2uE9Mav01WQcxDAT9gx7+2AdB04t89/1O/w1cDnyilFU="}

reply_payload = {
    "replyToken": "xxxxxxxx",
    "messages": [
        {
            "type": "text",
            "text": "This is reply_echo_msh: "
        }
    ]
}

reply_msg = {
    "type": "text",
    "text": "This is reply_echo_msh: "
}

headers = {
    'Content-Type': "application/json",
    'Authorization': "Bearer 1hFvFhSffFNku6B/E0Yt+7a7yNF2xLU0/yMz5SfoEUBsnLX1JddQHXg2q0lWCXYnsjjFTi85oqD0DRsVre3UgombcFA+8ZfpSDbWQRjZ6Qx3wNwLt8uPP5uwFwpjP6X2uE9Mav01WQcxDAT9gx7+2AdB04t89/1O/w1cDnyilFU=",
    'cache-control': "no-cache",
    'Postman-Token': "33629a0d-e4e1-4e75-bd2d-db1a37cf2377"
}


#######################################################


def echo_msg(request):
    events = request.json["events"]

    for event in events:
        print(event["type"])
        print(event["replyToken"])


def reply_echo_msg(request):
    events = request.json["events"]

    for event in events:
        reply_token = event["replyToken"]
        if event["message"]["type"] == "text":
            msg_text = event["message"]["text"]
        else:
            msg_text = "This isn't text!"

    # reply_payload
    reply_msg["text"] = "This is reply_echo_msh: " + msg_text
    reply_msgs = [reply_msg]
    # Set reply message
    reply_payload["replyToken"] = reply_token
    reply_payload["messages"] = reply_msgs

    print(reply_payload)

    response = requests.request("POST", url, data=json.dumps(reply_payload), headers=headers, params=querystring)
    print(response.text)
    print(response.status_code)


def reply_guess_song(request):
    events = request.json["events"]

    for event in events:
        reply_token = event["replyToken"]
        if event["message"]["type"] == "text":
            lyric = event["message"]["text"]
            msg_text_list = song_recog_api.get_search_list_musixmatch(lyric)
            msg_text = ""
            for msg in msg_text_list:
                if msg_text == "":
                    msg_text = msg
                else:
                    msg_text = msg_text + ', ' + msg
                    if len(msg_text) > 20:
                        break
        else:
            msg_text = "This isn't text!"

    # reply_payload
    reply_msg["text"] = msg_text
    reply_msgs = [reply_msg]
    # Set reply message
    reply_payload["replyToken"] = reply_token
    reply_payload["messages"] = reply_msgs

    print(reply_payload)

    response = requests.request("POST", url, data=json.dumps(reply_payload), headers=headers, params=querystring)
    print(response.text)
    print(response.status_code)
