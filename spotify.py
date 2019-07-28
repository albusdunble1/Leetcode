playlist = {
    "title" : "patagonia bus",
    "author" : "Colt Steele",
    "songs" : [
                {
                    "name" : "Turn It Off",
                    "artist" : ["Culture Abuse"],
                    "album" : "Peach",
                    "duration" : 2.1
                },
                {
                    "name" : "Nights Off",
                    "artist" : ["Moderet", "Siruamo", "Solomun"],
                    "album" : "Mosaik",
                    "duration" : 3.5
                }
             ]
}

total_duration = 0
for song in playlist["songs"]:
    total_duration += song["duration"]

print(total_duration)
