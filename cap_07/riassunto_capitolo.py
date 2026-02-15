# Sintassi base
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# verificare se un numero è pari/dispari o divisibile per N.
number = int(input("Inserisci un numero: "))
if number % 2 == 0:
	print(f"{number} is even")
else:
	print(f"{number} is odd")  

# while loop  
  
current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1    
		
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
	print(current_number)
    
# 5 controllo del ciclo

# Flag, variabile booleana

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True  # Flag
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False  # Disattiva il ciclo
    else:
        print(message)
        
# break, esce subito dal ciclo

while True:
	message = input(prompt + "_2")
	
	if message == 'quit':
		break
	else:
		print(message)  
        
# 6. continue (Salta l'iterazione)
# Salta il resto del codice nel ciclo e torna all'inizio:

current_number = 0
while current_number < 10:
    current_number += 1
    
    if current_number % 2 == 0:
        continue  # Salta i numeri pari
    
    print(current_number)  # Stampa solo dispari: 1, 3, 5, 7, 9     
    
# 7. Cicli while con Liste e Dizionari

# Spostare elementi tra liste

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
	current_user = unconfirmed_users.pop()     
    
	print(f"Verifying user: {current_user}")
	confirmed_users.append(current_user)
	
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user)
                
#Rimuovere tutte le occorrenze di un valore da una lista

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')
	
print(pets)

# Riempire un dizionario con input utente

responses = {}

polling_active = True

while polling_active:
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb someday? ")
	
	responses[name] = response
	
	repeat = input("Would you like to let another person respond? (yes/no) ")
	if repeat == 'no':
		polling_active = False
		
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(f"{name} would like to climb {response}.")
    
# ripeti l'esempio sopra usando break e/o continue ed eliminando la variabile boolean polling_active

responses = {}

while True:
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb someday? ")
	
	responses[name] = response
	
	repeat = input("Would you like to let another person respond? (yes/no) ")
	if repeat == 'no':
		break
		
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(f"{name} would like to climb {response}.")


    
                
