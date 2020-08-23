# this will download a 39mb lichess database PGN file.
curl https://database.lichess.org/standard/lichess_db_standard_rated_2013-07.pgn.bz2

# decompress it with bz2, and keep the old file
bz2 -dk lichess_db_standard_rated_2013-07.pgn.bz2

python main.py lichess_db_standard_rated_2013-07.pgn

 
