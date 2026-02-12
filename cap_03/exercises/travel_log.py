'''
Crea una lista destinations che rappresenta luoghi che vuoi visitare (5 nomi di città/stati in inglese, ordine casuale, es. ["tokyo", "paris", "new york", "sydney", "cairo"]).
Esegui queste operazioni nell'ordine, stampando la lista dopo ogni modifica con un commento che spiega cosa hai fatto:

    Stampa la lista originale
    Usa sorted() per stampare la lista ordinata alfabeticamente senza modificarla (stampa anche la lista originale subito dopo per dimostrare che è intatta)
    Usa .sort() per ordinare la lista permanentemente, poi stampala
    Usa .reverse() per invertire l'ordine, poi stampala
    Rimossa la destinazione in posizione 2 con del (non pop, non serve il valore)
    Inserisci una nuova destinazione in posizione 1 con .insert()
    Stampa il numero totale di destinazioni rimaste usando len() in una f-string: "Still want to visit X places"

Requisiti:

Requisiti:

    Tutto in inglese
    Commenta ogni sezione (# Step 1: original list, # Step 2: temporary sort, etc.)
    Output chiaro che mostri l'evoluzione della lista
'''
#Step1 the original list
destinations = ["tokyo", "paris", "new york", "sydney", "cairo"]
print(f"The cities i'll wish to visit are: {destinations[0]}, {destinations[1]}, {destinations[2]}, {destinations[3]} and {destinations[4]}")

#Step2 print a sorted destinations without modifyng itself
alias = sorted(destinations)
print(f"some order in those metas {alias[0]}, {alias[1]}, {alias[2]}, {alias[3]} and {alias[4]} ")
print(f"much better than {destinations[0]}, {destinations[1]}, {destinations[2]}, {destinations[3]} and {destinations[4]} right?")

#Step3 use of method that modify the list destination 
destinations.sort()
print(f"yes that's' really better  {destinations[0]}, {destinations[1]}, {destinations[2]}, {destinations[3]} and {destinations[4]} !")
destinations.reverse()
print(f"or pherarps so {destinations[0]}, {destinations[1]}, {destinations[2]}, {destinations[3]} and {destinations[4]}?")
del(destinations[2]) #remove the second element 
destinations.insert(1, "new delhi") #insert the first element

#Step4 how to count the length of a list  
print(f"Still want to visit {len(destinations)} places")



