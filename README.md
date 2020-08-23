# Python PGN -> JSON
This script can convert a PGN file to a JSON file.


## Usage

`python3 main.py <PGN FILE NAME> <OUTPUT JSON FILE NAME>`

## Benchmark script
This repo also contains a benchmark script, which automatically downloads a lichess database file,
decompresses it, and feeds it to the converter script.

First make the script executable:
`sudo chmod +x script.sh`

then run it:

`time ./script.sh`