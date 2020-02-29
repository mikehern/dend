# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE songplays (
    songplay_id BIGINT,
    start_time BIGINT,
    user_id INTEGER,
    level TEXT,
    song_id VARCHAR(4),
    artist_id VARCHAR(18),
    session_id INTEGER NOT NULL,
    location TEXT,
    user_agent TEXT
)
""")

user_table_create = ("""CREATE TABLE users (
    user_id INTEGER,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    gender TEXT,
    level VARCHAR(4)
)
""")

song_table_create = ("""CREATE TABLE songs(
    song_id VARCHAR(18) NOT NULL,
    title TEXT NOT NULL,
    artist_id VARCHAR(18) NOT NULL,
    year SMALLINT,
    duration FLOAT NOT NULL
)
""")

artist_table_create = ("""CREATE TABLE artists(
    artist_id VARCHAR(18) NOT NULL,
    name TEXT NOT NULL,
    location TEXT,
    lat TEXT,
    lon TEXT
)
""")

time_table_create = ("""CREATE TABLE time(
    start_time timestamp NOT NULL,
    hour SMALLINT NOT NULL,
    day SMALLINT NOT NULL,
    week SMALLINT NOT NULL,
    month SMALLINT NOT NULL,
    year SMALLINT NOT NULL,
    weekday SMALLINT NOT NULL
)
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays(
    songplay_id,
    start_time,
    user_id,
    level,
    song_id,
    artist_id,
    session_id,
    location,
    user_agent
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""INSERT INTO users(
    user_id,
    first_name,
    last_name,
    gender,
    level
) VALUES (%s, %s, %s, %s, %s)
""")

song_table_insert = ("""INSERT INTO songs(
    song_id,
    title,
    artist_id,
    year,
    duration
) VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""INSERT INTO artists(
    artist_id,
    name,
    location,
    lat,
    lon
) VALUES (%s, %s, %s, %s, %s)
""")


time_table_insert = ("""INSERT INTO time(
    start_time,
    hour,
    day,
    week,
    month,
    year,
    weekday
) VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""SELECT songs.artist_id, songs.song_id
    FROM songs
    INNER JOIN artists
    ON songs.artist_id=artists.artist_id
    WHERE songs.title=%s
    AND artists.name=%s
    AND songs.duration=%s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]