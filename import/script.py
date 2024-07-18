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

#print(episodes_data_sorted[3])

print(locations_data_sorted[2]["name"])

for x in locations_data_sorted:
    cur.execute('''
                INSERT INTO location ("name","type","dimension")
                VALUES (%s,%s,%s)''', 
                (
                    x["name"], x["type"], x["dimension"]
                ))
    
for x in episodes_data_sorted:
    cur.execute('''
                INSERT INTO episode ("name","air_date","episode")
                VALUES (%s,%s,%s)''', 
                (
                    x["name"], x["air_date"], x["episode"]
                )) 


                 
for x in chars_data_sorted:
    cur.execute('''
                INSERT INTO character ("name","status","type","gender", "image")
                VALUES (%s,%s,%s,%s,%s)''', 
                (
                    x["name"], x["status"], x["type"], x["gender"], x["image"]
                ))




episode_character_dicionary = {character['id']: character['episode'] for character in chars_data_sorted}

episode_character_dicionary_onlynumbers = {
    character_id: [int(episode.split('/')[-1]) for episode in episodes]
    for character_id, episodes in episode_character_dicionary.items()
}

print(episode_character_dicionary[100])

for character_id, episode_ids in episode_character_dicionary.items():
    for episode_id in episode_ids:
        cur.execute('''
                    INSERT INTO character_episodes ("character_id", "episode_id")
                    VALUES (%s, %s)''', 
                    (character_id, episode_id))


print("######################Testando a criação e iteração sobre o banco")

# created, url - descartar em todas as tabelas
# db.create_all() -> gerar a tabela novamente
# origin e location, apontar na tabela location

