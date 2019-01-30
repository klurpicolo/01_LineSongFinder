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
                   "quorum_factor": "1",
                   "apikey": "0d8df63a47cd46d09b04b9c30c8d023b",
                   "s_track_rating": "desc"}

    payload = ""
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "2e513763-e240-4faf-9098-7db6917904c8"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    response_json = json.loads(response.text)
    print(response.text)
    track_list = response_json["message"]["body"]["track_list"]

    result_track_list = []
    for track in track_list:
        # print(track["track"]["track_name"] + ", by " + track["track"]["artist_name"])
        result_track_list.append(track["track"]["track_name"])

    # Remove duplicate data by set function
    return set(result_track_list)


def get_search_list_musixmatch_web(lyric):
    url = "https://api.musixmatch.com/ws/1.1/track.search"

    querystring = {"format": "json", "callback": "callback",
                   "q_lyrics": lyric,
                   "quorum_factor": "1",
                   "apikey": "0d8df63a47cd46d09b04b9c30c8d023b",
                   "s_track_rating": "desc"}

    payload = ""
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "2e513763-e240-4faf-9098-7db6917904c8"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    response_json = json.loads(response.text)
    print(response.text)
    track_list = response_json["message"]["body"]["track_list"]

    result_track_list = []
    track_dict = {}
    for track in track_list:
        track_detail = track["track"]
        track_dict["track_name"] = track_detail["track_name"]
        track_dict["artist_name"] = track_detail["artist_name"]
        track_dict["track_id"] = track_detail["track_id"]
        track_dict["lyric"] = get_lyric(track_detail["track_id"])
        result_track_list.append(track_dict.copy())

    return result_track_list


def get_lyric(track_id):
    url = "https://api.musixmatch.com/ws/1.1/track.lyrics.get"

    querystring = {"track_id": track_id,
                   "format": "json",
                   "apikey": "0d8df63a47cd46d09b04b9c30c8d023b"}

    payload = ""
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "e3981505-e6b7-458e-b507-18fa5855f832"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    response_json = json.loads(response.text)
    lyrics = response_json["message"]["body"]["lyrics"]["lyrics_body"]

    # Remove warning from musixmatch
    lyrics = lyrics.split("*******", 1)[0]

    return lyrics


if __name__ == '__main__':
    search_tracks = get_search_list_musixmatch_web("I found a love for me Darling just dive right in")
    print(search_tracks)
    # for track in search_tracks:
    #     print(get_lyric(track["track_id"]))
    #     # track["track_id"]
    #     # break
