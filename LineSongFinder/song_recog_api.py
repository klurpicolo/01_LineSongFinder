import requests
import json


def get_search_list_audd(lyric):
    # API param
    url = "https://api.audd.io/findLyrics/"

    querystring = {"q": "when I was your man"}

    payload = ""
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "57ae0a7c-82f0-4bcb-a866-dc8d68a7fddc"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    print(response.text)
    reponse_json = json.loads(response.text)
    print(reponse_json)

    # request_str = json.dumps(response.json, indent=4)
    # print(response.json)


def get_search_list_musixmatch(lyric):
    # API param
    url = "https://api.musixmatch.com/ws/1.1/track.search"

    querystring = {"format": "json", "callback": "callback",
                   "q_lyrics": lyric,
                   "quorum_factor": "1", "apikey": "0d8df63a47cd46d09b04b9c30c8d023b"}

    payload = ""
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "2e513763-e240-4faf-9098-7db6917904c8"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    print(response.text)
    response_json = json.loads(response.text)
    print(response_json)

    track_list = response_json["message"]["body"]["track_list"]

    result_track_list = []
    for track in track_list:
        # print(track["track"]["track_name"] + ", by " + track["track"]["artist_name"])
        result_track_list.append(track["track"]["track_name"])

    return result_track_list


if __name__ == '__main__':
    print(get_search_list_musixmatch("one twenty one guns, throw up your arms"))
