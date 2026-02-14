'''
Crea un programma che gestisca un catalogo di videogiochi. Il programma deve:

    Creare un dizionario chiamato game_library con almeno 3 giochi. Ogni gioco deve avere:
        'title': titolo del gioco (stringa)
        'genre': genere (stringa)
        'rating': valutazione da 1 a 10 (numero)
        'platforms': lista delle piattaforme disponibili (lista di stringhe)
    Aggiungere un nuovo gioco al catalogo usando una chiave nuova
    Stampare tutti i giochi nel formato:
    
    Game: [title] | Genre: [genre] | Rating: [rating]/10
    Available on: [platform1], [platform2], ...
    
    Cercare un gioco specifico usando il metodo get(). Se il gioco esiste, stampa i suoi dettagli. Se non esiste, stampa "Game not found in library."
    Bonus (opzionale): Calcola e stampa la valutazione media di tutti i giochi nel catalogo
    
'''

    #game_library.items()#.count(num_games)                      
#for (key,value) in game_library.items():
    #valutazione += value.get('rating', 0) 
    #num_games += 1;
#print(valutazione)                          #(key,value)
#print(num_games)
  
'''
for key in game_library: print(game_library[key])
print()
'''

game_library = {
                    "doom":{"title":"doom","genre":"shooter","rating":5,"platform":['msdos']},
                    "quake":{"title":"quake","genre":"shooter","rating":10,"platform":['win','linux']},
                    "wolfstein":{"title":"wolfstein3D","genre":"shooter","rating":8,"platform":['msdos']}
                 }

rating = 0
num_games = 0
game_library['doomII'] = {"title":"doomII","genre":"shooter","rating":6,"platform":['msdos']}
for (key,value) in game_library.items():
        str_platforms = ""
        platforms = value.get('platform')
        for platform in platforms: str_platforms +=  platform + ','
        str_platforms = str_platforms[:-1]    
        print(f"Game: {value.get('title')} | Genre: {value.get('genre')} | Rating: {value.get('rating')}/10")
        print(f"Available on: {str_platforms}") 
        rating += value.get('rating', 0) 
        num_games += 1;
        
print("-------------------------")
                       
game = game_library.get('doom','Game not found in library')

if game == 'Game not found in library': 
    print(game) 
else:
	print(f"Game: {game.get('title')} | Genre: {game.get('genre')} | Rating: {game.get('rating')}/10")
	print(f"Available on: {game.get('platform')}")


print(f"Average Rating: {rating/num_games}")                     