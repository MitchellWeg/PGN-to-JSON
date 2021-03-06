import chess.pgn
import sys
import json

file_name = sys.argv[1]
json_out_filename = sys.argv[2]

def main():
    file = open(file_name)
    json_file = open(json_out_filename, "a")

    while True:
        game = chess.pgn.read_game(file)
        if game is None:
            break

        _game = Game(game.headers, game.mainline_moves().__str__)
        json_out = json.dumps(_game.__dict__())

        json_file.write(json_out)
        json_file.write('\r\n')
        print(json_out)

class Game:
    headers = []
    game = ""

    def __init__(self, _headers, _game):
        self.headers = _headers
        self.game = _game

    def __dict__(self):
        return {
            'Event': self.headers["Event"],
            'Site': self.headers["Site"],
            'Date': self.headers["Date"],
            'White': self.headers["White"],
            'Black': self.headers["Black"],
            'Result': self.headers["Result"],
            'Eco': self.headers["ECO"],
            'Game': self.game()
        }

if __name__ == '__main__':
    main()