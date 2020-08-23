import chess.pgn
import sys
import json

def main():
    file = open(sys.argv[1])
    while True:
        game = chess.pgn.read_game(file)
        if game is None:
            break

        _game = Game(game.headers, game.mainline_moves().__str__)
        json_out = json.dumps(_game.__dict__(), indent=4)

        json_file = open("lichessdb.json", "a")
        json_file.write(json_out)
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