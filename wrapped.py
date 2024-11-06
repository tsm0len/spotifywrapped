import json
from tkinter.filedialog import askopenfilename

def wrapped(criteria="minPlayed", byAuthors=False):

    fileName = askopenfilename()

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

    for i, (key, value) in enumerate(stats.items()):
        if i < 5:
            print(f"{i+1}. {key} - {value['author']}:")
            print(f"\tMinutes Played: {value['minPlayed']}")
            print(f"\tTimes Played: {value['timesPlayed']}")
            print("===========================================")
        else:
            break

    jsonStats = json.dumps(stats, indent=4)
    with open("wrapped.json", "w") as wrappedFile:
        wrappedFile.write(jsonStats)
        
    return stats

criteria = "minPlayed" #minPlayed/timesPlayed
byAuthors = False
wrapped(criteria, byAuthors)
print("Done!")