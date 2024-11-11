import json
from tkinter.filedialog import askopenfilename

def getFile() -> dict:

    fileName = askopenfilename()

    f = open(fileName, encoding="utf8")
    text = f.read()
    data = json.loads(text)
    f.close()
    return data

def sortStats(data) -> dict:
    stats = sorted(data, key=lambda item: item["minPlayed"], reverse=True)
    return stats

def getData(data):
    output = []
    for i in data:
        obj = {"author":i["artistName"], "song":i["trackName"], "minPlayed":0}
        if obj not in output:
            output.append(obj)
            
    for i in output:
        for song in data:
            if song["artistName"]==i["author"] and song["trackName"]==i["song"]:
                i["minPlayed"]+=song["msPlayed"]
        i["minPlayed"]=round(i["minPlayed"]/1000/60, 2)
        
    return output

def outputStats(stats, places=5):
    print("===========================================")
    for i in range(5):
        print(f"{i+1}. {stats[i]['song']} - {stats[i]['author']}:")
        print(f"\tMinutes Played: {stats[i]['minPlayed']}")
        print("===========================================")

def saveAsFile(stats):
    jsonStats = json.dumps(stats, indent=4)
    with open("output.json", "w") as wrappedFile:
        wrappedFile.write(jsonStats)

file = getFile()
data = getData(file)
stats = sortStats(data)
outputStats(stats, False)
saveAsFile(stats)