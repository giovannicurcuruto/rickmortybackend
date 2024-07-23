import psycopg2
import json
from operator import itemgetter

hostname = 'localhost'
database = 'rmorty'
username = 'postgres'
password = 'passpost'
port_id = 5432

conn = psycopg2.connect(
    host = hostname,
    dbname = database,
    user = username,
    password = password,
    port = port_id
)

cur = conn.cursor()

with open("import/allCharsUpdated.json", encoding='utf-8') as file:
    chars_data_unsorted = json.load(file)

with open("import/allEpisodesUpdated.json", encoding='utf-8') as file:
    episodes_data_unsorted = json.load(file)

with open("import/allLocations.json", encoding='utf-8') as file:
    locations_data_unsorted = json.load(file)

chars_data_sorted = sorted(chars_data_unsorted, key=itemgetter("id"))
episodes_data_sorted = sorted(episodes_data_unsorted, key=itemgetter("id"))
locations_data_sorted = sorted(locations_data_unsorted, key=itemgetter("id"))

for x in locations_data_sorted:
    cur.execute('''
                INSERT INTO location ("name","type","dimension")
                VALUES (%s,%s,%s)''', 
                (
                    x["name"], 
                    x["type"], 
                    x["dimension"]
                ))
    
conn.commit()   
for x in episodes_data_sorted:
    cur.execute('''
                INSERT INTO episode ("name","air_date","episode")
                VALUES (%s,%s,%s)''', 
                (
                    x["name"],
                    x["air_date"],
                    x["episode"]
                )) 
conn.commit()

def to_int_or_none(value):
    try:
        return int(value) if value and value.strip() else None
    except (ValueError, TypeError):
        return None

                 
for x in chars_data_sorted:
    #print(type(int(x["location"]["url"].split("/")[-1])))
    #print(x["origin"]["url"].split("/")[-1])
    location_id = to_int_or_none(x["location"]["url"].split("/")[-1])
    origin_id = to_int_or_none(x["origin"]["url"].split("/")[-1])

    cur.execute('''
                INSERT INTO character ("name","status","type","gender", "image", "present_location_id", "origin_id")
                VALUES (%s,%s,%s,%s,%s,%s,%s)''', 
                (                    
                    x["name"], 
                    x["status"], 
                    x["type"], 
                    x["gender"], 
                    x["image"], 
                    location_id, 
                    origin_id
                ))
    id = x["id"]
    for episodes_id in x["episode"]:
        episode = episodes_id.split("/")[-1]
        
        cur.execute('''
                 INSERT INTO character_episodes ("character_id","episode_id")
                 VALUES (%s,%s)''', 
                (                    
                    id, episode
                ))
    




conn.commit()


#for characters_id in chars_data_sorted:
    

#conn.commit()

print("######################Testando a criação e iteração sobre o banco")
cur.close()
conn.close()

