#this tool is made to Genrate a direct link

def GetDirLink(link):
    GDpart = 33
    dtr = "https://drive.google.com/uc?export=download&id="
    Id = link[33:]
    directlink = dtr + Id
    print(directlink)
