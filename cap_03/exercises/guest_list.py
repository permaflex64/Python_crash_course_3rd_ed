''' 
    Crea lista guests con 3 nomi in inglese (es. "alice", "bob", "charlie")
    Stampa: "I'm inviting X people to dinner" dove X è calcolato con len()
    Rimuovi l'ultimo ospite con .pop() e salvalo in cannot_come
    Stampa: "Sorry, {cannot_come}, you can't make it" (usa f-string)
    Aggiungi un nuovo ospite (es. "david") in fondo con .append()
    Stampa lista finale: "Final guest list: {guests}"
    
    I'm inviting 3 people to dinner
    Sorry, charlie, you can't make it
    Final guest list: ['alice', 'bob', 'david']
'''
guests = ["alice", "bob", "charlie"]
print(f"I'm inviting {len(guests)} people to dinner")

cannot_come = guests.pop() #print(cannot_come)  #print(cannot_come)
print(f"Sorry, {cannot_come}, you can't make it")

guests.append("alex")
print(f"Final guest list: {guests}")