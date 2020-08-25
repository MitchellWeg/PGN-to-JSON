# the lichess databases consist of multiple big files

DownloadList=(https://database.lichess.org/standard/lichess_db_standard_rated_2016-04.pgn.bz2  https://database.lichess.org/standard/lichess_db_standard_rated_2016-02.pgn.bz2 https://database.lichess.org/standard/lichess_db_standard_rated_2016-01.pgn.bz2)


for url in ${!DownloadList[@]}  
do
    curl ${DownloadList[$url]} --output lichess-db-$url.pgn.bz2;
    bzip2 -dk lichess-db-$url.pgn.bz2 
    python3 main.py lichess-db-$url.pgn lichess-db-$url.json 
done