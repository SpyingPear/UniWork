class Album:
    def __init__(self, album_name, album_artist, number_of_songs):
        self.album_name = album_name
        self.album_artist = album_artist
        self.number_of_songs = number_of_songs

    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"

albums1 = [
    Album("Thriller", "Michael Jackson", 9),
    Album("Back in Black", "AC/DC", 10),
    Album("The Bodyguard", "Whitney Houston", 12),
    Album("Rumours", "Fleetwood Mac", 11),
    Album("Hotel California", "Eagles", 9)
]

print("Original albums1:")
for album in albums1:
    print(album)

albums1.sort(key=lambda a: a.number_of_songs)

print("\nSorted albums1 by number_of_songs:")
for album in albums1:
    print(album)

albums1[0], albums1[1] = albums1[1], albums1[0]

print("\nAfter swapping first two albums in albums1:")
for album in albums1:
    print(album)

albums2 = []

albums2.extend([
    Album("21", "Adele", 11),
    Album("Abbey Road", "The Beatles", 17),
    Album("Good Kid, M.A.A.D City", "Kendrick Lamar", 12),
    Album("Lemonade", "Beyoncé", 12),
    Album("1989", "Taylor Swift", 13)
])

print("\nInitial albums2:")
for album in albums2:
    print(album)

albums2.extend(albums1)

albums2.append(Album("Dark Side of the Moon", "Pink Floyd", 9))
albums2.append(Album("Oops!... I Did It Again", "Britney Spears", 16))

albums2.sort(key=lambda a: a.album_name)

print("\nSorted albums2 by album_name:")
for album in albums2:
    print(album)

for index, album in enumerate(albums2):
    if album.album_name == "Dark Side of the Moon":
        print(f"\nIndex of 'Dark Side of the Moon' in albums2: {index}")
        break
