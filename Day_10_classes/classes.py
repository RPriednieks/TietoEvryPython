class Song:
    def __init__(self, title, author, lyrics):
        self.title = title
        self.author = author
        self.lyrics = lyrics

    def sing(self, max_lines=-1):
        self.max_lines = max_lines
        print(f"{self.title} - {self.author}")
        if max_lines != -1:
            for i in self.lyrics[:max_lines]:
                print(i)
        else:
            for i in self.lyrics:
                print(i)
        return self

    def yell(self, max_lines=-1):
        capital_lyrics = [i.upper() for i in self.lyrics]
        self.max_lines = max_lines
        print(f"{self.title} - {self.author}")
        if max_lines != -1:
            for i in capital_lyrics[:max_lines]:
                print(i)
        else:
            for i in capital_lyrics:
                print(i)
        return self

ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])
ziemelmeita.sing(1).yell()
