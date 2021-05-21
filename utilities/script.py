import csv
import json

movies = []
with open('recommender.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        movies.append(' '.join(row).strip())



movies = json.dumps(movies, indent=2)
with open("movies.txt", "w") as wfile:
	wfile.write(str(movies))
   
