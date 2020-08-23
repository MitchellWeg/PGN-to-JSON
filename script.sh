# this will download a 39mb lichess database PGN file.
curl https://database.lichess.org/standard/lichess_db_standard_rated_2013-07.pgn.bz2 --output lichess-database.pgn.bz2

# decompress it with bz2, and keep the old file
bzip2 -dk lichess-database.pgn.bz2

# call the main parser script.
python main.py lichess-database.pgn lichessdb.json

 
