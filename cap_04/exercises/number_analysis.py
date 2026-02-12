''' 
Generi una lista di numeri da 1 a 10 usando range() e list() (es: numbers = list(range(1, 11)))
Calcoli (usando cicli o list comprehension):

    La lista dei quadrati (** 2) di questi numeri
    La somma di tutti i numeri originali (usando sum() o un accumulatore)
    La lista dei numeri pari solamente (indizio: if number % 2 == 0)

Stampi i risultati con f-strings formattate:
Originals: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Squares: [1, 4, 9, 16...]
Sum: 55
Even numbers: [2, 4, 6, 8, 10]
'''

numbers = list(range(1,11))
print(f"Originals: {numbers}")

squares = []   
tot = 0
even = []
for number in numbers: 
   squares.append(number**2)
   tot = tot + number
   if number % 2 == 0:
        even.append(number)
   
print(f"Squares: {squares}")   
print(f"Sum: {tot}")
print(f"Even numbers: {even}")


    
