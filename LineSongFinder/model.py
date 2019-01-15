import pyrebase
import os


class db_util:

    def __init__(self):
        self.config = {
            "apiKey": "AIzaSyCauB8eEHYowXTimRWVWzHakCLf71H_ios",
            "authDomain": "linesongfinder.firebaseapp.com",
            "databaseURL": "https://linesongfinder.firebaseio.com",
            "storageBucket": "linesongfinder.appspot.com",
            # "serviceAccount": "D:\\03_Temp\\01_LineSongFinder\\resource\\ServiceAccountKey.json"
            # "serviceAccount": os.path.dirname(os.path.realpath(__file__)) + "\\resource\\ServiceAccountKey.json"
        }
        self.firebase = pyrebase.initialize_app(self.config)
        self.db = self.firebase.database()

    def record_to_firebase(self, q_lyric, a_track_list, a_tracks):
        # users = db.child("name1").get()
        # print(users.val())
        # users = db.child("testname2").get()
        # print(users.val())

        # data = {"q_lyric": "When she was just a girl she expected the world but it flew away from her reach",
        #         "a_track_list": "Paradise Lost ,Conquest to Paradise ,Paradaise ,Paradise"}

        data = {"q_lyric": q_lyric, "a_track_list": a_track_list, "a_tracks": a_tracks}
        self.db.child("querys").push(data)

    def retrieve_data(self):
        all_querys = self.db.child("querys").get()
        result = {}
        for user in all_querys.each():
            # print(user.key())  # Morty
            # print(user.val())  # {name": "Mortimer 'Morty' Smith"}
            result[user.key()] = user.val()

        return result


if __name__ == '__main__':
    # q_lyric = "Mark my words This love will make you levitate Like a bird, like a bird without a cage"
    # a_track_list = "Dark Horse (In the Style of Katy Perry) (Karaoke Version), Dark Horse (Originally Performed by Katy Perry"
    # a_tracks = ["Dark Horse (In the Style of Katy Perry) (Karaoke Version)", "Dark Horse (Originally Performed by Katy Perry"]
    # record_to_firebase(q_lyric, a_track_list, a_tracks)

    line_db_util = db_util()
    dict_results = line_db_util.retrieve_data()
    print(line_db_util.retrieve_data())
    for query_key, song_dict in dict_results.items():
        print(query_key)
        print("   " + song_dict["a_track_list"])
