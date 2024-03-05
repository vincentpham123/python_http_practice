import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/')

counts = {}
for line in fhand:
    words = line.decode().split()

    

