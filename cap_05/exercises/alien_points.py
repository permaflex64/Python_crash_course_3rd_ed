'''
Requisiti:

    alien_color = 'green', 'yellow' o 'red'
    Punteggi: 5 (green), 10 (yellow), 15 (red)
    Messaggi bonus diversi per ogni colore
    Stampa finale 'Continue mission...' in ogni caso

 '''
alien_color = ['green','yellow','red']
bonus = 0

for color in alien_color:
    if  color == "green":
        bonus = 5
        print(f"Green bonus is:{bonus}")
    elif color == "yellow":
        bonus = 10
        print(f"Yellow bonus is:{bonus}") 
    elif color == "red":
        bonus = 15
        print(f"Red bonus is:{bonus}")          
 
print("Continue mission")