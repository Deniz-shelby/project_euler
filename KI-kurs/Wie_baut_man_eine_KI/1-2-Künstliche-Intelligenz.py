'''
In dieser Aufgabe programmieren wir ein Zahlenspiel

In dieser Aufgabe sollst du ein Programm schreiben, dass Zahlen von 1 bis 100 ausschreibt und für jede Zahl, die durch 3 teilbar ist, "Künstliche" schreibt, für jede Zahl, die durch 5 teilbar ist, "Intelligenz" schreibt und für Zahlen, die durch 3 und durch 5 teilbar sind, "BWKI" schreibt.
'''

for i in range(1,101):
    if ((i%5==0) and (i%3==0)):
        print(f'{i} BWKI')
    elif i%5==0:
        print(f'{i} Künstliche')
    elif i%3==0:
        print(f'{i} Intelligenz')