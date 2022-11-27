ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Plugboard:
    def __init__(self, pairs):
        self.board = dict(zip(ALPHABET, ALPHABET))
        if self.check_pairs(pairs):
            self.set_plugboard(pairs)

    def check_pairs(self, pairs):
        singles = []
        broken = False
        for combo in pairs:
            if combo[0] not in singles:
                singles.append(combo[0])
            else:
                broken = True
                break
            if combo[1] not in singles:
                singles.append(combo[1])
            else:
                broken = True
                break
        if broken:
            raise Exception("Must input pairs with no duplicates.")
        else:
            return True

    def set_plugboard(self, pairs):
        for pair in pairs:
            self.board[pair[0]] = pair[1]
            self.board[pair[1]] = pair[0]

    def output(self, letter):
        return self.board[letter]

