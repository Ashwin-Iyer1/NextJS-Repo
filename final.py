from last_fm import get_top
from coverArt import get_image, get_spotify_bearer
from databaseMod import addtoDatabase, clear_entries
import datetime
from fetchGithub import get_repos

#only run if friday
def is_friday():
    return datetime.datetime.today().weekday() == 4


def main():
    get_repos()
    if(not is_friday()):
        return
    songs = get_top(10)
    bearer = get_spotify_bearer()
    for song in songs:
        song.append(get_image(song, bearer))
        print("\n")
    clear_entries("Songs")
    addtoDatabase(songs)

    print(songs)

main()