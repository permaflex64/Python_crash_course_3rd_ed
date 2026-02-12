'''



 '''
 
#0 Accesso ai Valori
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])      # Output: green
print(alien_0['points'])     # Output: 5

#1 Aggiunge nuova chiave-valore
alien_0['x_position'] = 0    
alien_0['y_position'] = 25
print(alien_0)


#2 lista di due alieni
aliens = [{'color': 'green', 'points': 5},{'color': 'yellow', 'points': 10}]
print((aliens[0])["color"])
print((aliens[0])["points"])

#3 Sovrascrive il valore
alien_0 = {'color': 'green'}
alien_0['color'] = 'yellow'  
print(f"#3: {alien_0}")

#4 Eliminare coppia chiave valore
alien_0 = {'color': 'green', 'points': 5}
del alien_0['points']        # Rimuove la chiave 'points' permanentemente
print(f"#4: {alien_0}")

#5 Dizionario vuoto
alien_0 = {}                 # Inizializzazione vuota
alien_0['color'] = 'green'   # Poi si popola
print(f"#5: {alien_0}")

#6 Metodo get
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points')           # Restituisce None
print(f"#6: {point_value}")
point_value = alien_0.get('points', 0)        # Restituisce 0 se non esiste
print(f"#6: {point_value}")


#Iterazione sui Dizionari
#------------------------

#7 Iterare su tutte le coppie chiave-valore
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"#7")
    print(f"#7 Key: {key}") #print(f"#7 \nKey: {key}")
    print(f"#7 Value: {value}")
'''    
for pippo, pluto in user_0.items():
    print(f"#7_")
    print(f"#7_ Key: {pippo}") #print(f"#7 \nKey: {key}")
    print(f"#7_ Value: {pluto}")
'''

#8 Iterare solo sulle chiavi
for key in user_0.keys():      # Oppure semplicemente: for key in user_0:
    print(f"#8 {key})")
    
#9 Iterare solo sui valori
for value in user_0.values():
    print(f"#9 {value})")
    
#10 Iterare in ordine
for key in sorted(user_0.keys()):    # Ordinato alfabeticamente
   # print(key)
    print(f"#10 {key}")    
print(f"#10 user_0 e' inalterato{user_0}")   

#Nesting (Annidamento) - Strutture Complesse
#--------------------------------------------

#Lista di Dizionari 
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(f"#11{alien}")
    
#Lista all'interno di un dizionario
# Memorizzare più valori per una chiave
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],  # Lista come valore
}

print(f"#12 You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print(f"#12\t{topping}")
    
#Dizionario all'interno di un dizionario
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\nUsername: {username}")
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

    