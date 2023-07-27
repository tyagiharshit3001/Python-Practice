class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o

    def do_wrk(self):
        if self.occupation == "tennis":
            print(self.name, "plays tennis")
        elif self.occupation == "actor":
            print(self.name, "shoots a film")

    def speaks(self):
        print(self.name, "says Hello How r u?")


tome = Human("tom cruise", "actor")
tome.do_wrk()
tome.speaks()

sania = Human("Sania Mirza", "tennis")
sania.do_wrk()
sania.speaks()
