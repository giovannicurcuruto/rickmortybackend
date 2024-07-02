import psycopg2

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

#criando as tabelas no banco
cur.execute("""
        CREATE TABLE IF NOT EXISTS "character" (
        "id" bigint,
        "name" text,
        "status" text,
        "species" text,
        "type" text,
        "gender" text,
        "origin.name" text,
        "origin.url" text,
        "location.name" text,
        "location.url" text,
        "image" text,
        "url" text,
        "created" text
        );

        CREATE TABLE IF NOT EXISTS "episodes" (
        "id" bigint,
        "name" text,
        "air_date" text,
        "episode" text,
        "url" text,
        "created" text
        );

        CREATE TABLE IF NOT EXISTS "locations" (
        "id" bigint,
        "name" text,
        "type" text,
        "dimension" text,
        "url" text,
        "created" text
        );
""")
conn.commit()

cur.execute("""
            INSERT INTO "character" ("id","name","status","species","type","gender","origin.name","origin.url","location.name","location.url","image","url","created")
            VALUES
            (2,
            'Morty Smith',
            'Alive',
            'Human',
            '',
            'Male',
            'unknown',
            '',
            'Citadel of Ricks',
            'https://rickandmortyapi.com/api/location/3',
            'https://rickandmortyapi.com/api/character/avatar/2.jpeg',
            'https://rickandmortyapi.com/api/character/2',
            '2017-11-04T18:50:21.651Z');

            INSERT INTO "episodes" ("id","name","air_date","episode","url","created")
            VALUES
            (1,'Pilot','December 2, 2013','S01E01','https://rickandmortyapi.com/api/episode/1','2017-11-10T12:56:33.798Z');

            INSERT INTO "locations" ("id","name","type","dimension","url","created")
            VALUES
            (1,'Earth (C-137)','Planet','Dimension C-137','https://rickandmortyapi.com/api/location/1','2017-11-10T12:42:04.162Z');
            
            
            
            """)


#script.py só deve importar os dados
#SQLALCAMY deve ser responsável por criar as tabelas

print("Testando a criação e iteração sobre o banco")

