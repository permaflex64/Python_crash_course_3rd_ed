'''
Crea un programma per gestire un sistema di ordini per una pizzeria. Il programma deve:

    Inizializzare una lista vuota chiamata orders e un dizionario menu con almeno 3 pizze (chiave = nome pizza, valore = prezzo)
    Chiedere all'utente di inserire ordini ripetutamente con questo formato:
        Nome della pizza
        Se l'utente scrive 'done', smetti di accettare ordini
    Per ogni ordine valido:
        Verifica che la pizza esista nel menu
        Se esiste, aggiungi il prezzo a un totale e memorizza l'ordine
        Se non esiste, stampa "Sorry, we don't have [pizza_name] on the menu."
    Alla fine, stampa:
        Tutte le pizze ordinate (con i prezzi)
        Il totale da pagare
        Un messaggio di ringraziamento
    Bonus (opzionale): Permetti all'utente di rimuovere un ordine prima di confermare (chiedi "Remove any item? (yes/no)" e poi quale pizza rimuovere)

Requisiti tecnici da usare:

    input() per l'interazione
    while per il ciclo principale
    break o flag per terminare
    Dizionario per il menu
    Lista per memorizzare gli ordini


'''

    
    

#Step1 the menu
menu = {
	"Margherita": 10,
	"Pepperoni": 12,
	"Hawaiian": 15,
	"Vegetarian": 12,
	}

#Step2 the orders
orders = []
total = 0   
while True:
	order = input("What pizza would you like to order? done to finish: ")
	if order == "done":
		break
	elif order in menu:
		orders.append(order)
		total += menu[order]
	else:
		print(f"Sorry, we don't have {order} on the menu.")
        
#Step3 remove an order if yes show all the orders from wich to remove





remove_order = input("Remove any item? (yes/no): ")
if remove_order == "yes":
	for order in orders:
		print(f"{order}: ${menu[order]}")
	order_to_remove = input("What item would you like to remove? ")
	if order_to_remove in orders:
		orders.remove(order_to_remove)
		total -= menu[order_to_remove]
		print(f"{order_to_remove} has been removed from your order.")
	else:
		print(f"{order_to_remove} is not in your order.")
        
        
#Step3 print the orders
print("--- Your Order ---")

for order in orders:
	print(f"{order}: ${menu[order]}")
		
print("---")
print(f"Total: ${total}")
print("Thank you for your order!")
 
            





