class SqlQueries:
    songplay_table_insert = ("""
       insert into songplays ( start_time, userId, level,song_id, artist_id,sessionId,location, userAgent)
        SELECT DISTINCT 
        TIMESTAMP 'epoch' + ts/1000 *INTERVAL '1 second' as start_time, 
        E.userId,
        E.level,
        S.song_id,
        S.artist_id,
        E.sessionId,
        E.location,
        E.userAgent
    from staging_events E
    INNER JOIN  staging_songs S 
    on(E.artist = S.artist_name)
    AND E.page = 'NextSong';
    """)

    user_table_insert = ("""
       insert into users (  userId , firstName , lastName ,gender, level)
        SELECT distinct userId, firstName, lastName, gender, level
        FROM staging_events
        WHERE userId IS NOT NULL 
         AND  page = 'NextSong';
        
    """
        )

    song_table_insert = ("""
       insert into songs ( song_id , title , 
                          artist_id , year , duration )
        SELECT distinct song_id, title, artist_id, year, duration
        FROM staging_songs
        WHERE song_id IS NOT NULL;
    """)

    artist_table_insert = ("""
                INSERT into artists (artist_id , artist_name , 
                    artist_location ,artist_latitude, 
                    artist_longitude)
                SELECT DISTINCT artist_id,
                    artist_name,
                    artist_location,
                        artist_latitude,
                artist_longitude
                    FROM staging_songs;
    """ 
       )

    time_table_insert = ("""
    insert into time (  start_time, hour, day, week, month, year, weekday) 
        SELECT start_time, extract(hour from start_time), extract(day from start_time), extract(week from start_time), 
               extract(month from start_time), extract(year from start_time), extract(weekday from start_time)
        FROM songplays
    """)