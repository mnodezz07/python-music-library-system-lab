

from lib.song import Song

# Create song objects
song1 = Song("Halo", "Beyonce", "Pop")
song2 = Song("Crazy in Love", "Beyonce", "R&B")
song3 = Song("Numb", "Linkin Park", "Rock")
song4 = Song("In Da Club", "50 Cent", "Rap")
song5 = Song("Rap God", "Eminem", "Rap")

# Display information about all songs
print("ALL SONGS")
for song in [song1, song2, song3, song4, song5]:
    print(song)

# Display library statistics
print("\nMUSIC LIBRARY STATISTICS")
print("Total songs:", Song.count)
print("Artists:", Song.artists)
print("Genres:", Song.genres)
print("Songs per genre:", Song.genre_count)
print("Songs per artist:", Song.artists_count)



