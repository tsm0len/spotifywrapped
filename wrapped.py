import json
from tkinter.filedialog import askopenfilename

def wrapped(criteria="minPlayed", byAuthors=False):

    fileName = "C:/Users/tomek/Desktop/python/StreamingHistory_music_0.json" #askopenfilename()

    f = open(fileName, encoding="utf8")
    text = f.read()
    data = json.loads(text)
    f.close()

    def getData():
        output = {}
        for entry in data:
            song = entry["trackName"]
            if song not in output:
                output[song] = {"minPlayed": 0, "timesPlayed": 0, "author": entry["artistName"]}
            output[song]["timesPlayed"] += 1
            output[song]["minPlayed"] += round(entry["msPlayed"] / 60000)
        return output

    stats = dict(sorted(getData().items(), key=lambda item: item[1][criteria], reverse=True))
    return stats

def outputStats(stats, byAuthors, places=5):
    print("===========================================")
    for i, (key, value) in enumerate(stats.items()):
        if i < places:
            if byAuthors:
                print(f"{i+1}.{value['author']}:")
            else:
                print(f"{i+1}. {key} - {value['author']}:")
            print(f"\tMinutes Played: {value['minPlayed']}")
            print(f"\tTimes Played: {value['timesPlayed']}")
            print("===========================================")
        else:
            break

def saveAsFile(stats):
    jsonStats = json.dumps(stats, indent=4)
    with open("wrapped.json", "w") as wrappedFile:
        wrappedFile.write(jsonStats)


criteria = "minPlayed" #minPlayed/timesPlayed (timesPlayed is not as accurate)
byAuthors = True
#53387
stats = wrapped(criteria, byAuthors)
outputStats(stats, byAuthors)
print("Done!")