songs = ["ROCKSTAR", "Do It", "For The Night"]
print(songs[0], songs[-1])
print(songs[1:3])
songs[-1] = "Wow"
songs.extend(["Mood", "Circle", "Right Here"])
del songs[1]
print(songs)

animals = ["dog", "cat", "bunny"]
animals.append("bird")
print(animals[2])
del animals[0]
for animal in animals:
    print(animal)