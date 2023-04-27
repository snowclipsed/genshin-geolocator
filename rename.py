import os

folders = ["images/starsnatch_cliff","images/stormbearer_mountains", "images/stormbearer_point", "images/thousand_winds_temple", "images/whispering_woods", "images/windrise"]

def folderlist(folderlist):

    for folder in folderlist:
        for count, filename in enumerate(os.listdir(folder)):
            count = count+1
            filepath = os.path.split(folder)
            dst = f"{str(filepath[1])}_{str(count)}.png"
            src = f"{folder}/{filename}"
            dst = f"{folder}/{dst}"
            os.rename(src,dst)

folderlist(folders)