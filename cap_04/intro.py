magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    
print()
    
for value in range(1, 5):  # Mi aspetto 1,2,3,4 (il 5 è escluso!)
    print(value)

print()
    
squares = [value**2 for value in range(1, 11)]
# Crea: [1, 4, 9, 16... 100]
for square in squares:
    print(square)
    
print()

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])   # Primi tre: indici 0,1,2
print(players[:4])    # Dall'inizio a indice 3
print(players[-2:])   # Ultimi due

dimensions = (200, 50)  # Lista immutabile Non puoi fare dimensions[0] = 250