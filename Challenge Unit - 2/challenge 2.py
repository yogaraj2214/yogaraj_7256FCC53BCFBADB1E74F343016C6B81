class Player:
    def play(self):
        print("The player is play cricket.")
class Batsman(Player):
    def play(self):
        print("The batsman is bating.")
class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")
batsman = Batsman()
bowler = Bowler()
batsman.play()
bowler.play()