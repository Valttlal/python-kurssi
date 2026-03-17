luku = int(input("Anna kokonaisluku: "))

on_alkuluku = True

if luku < 2:
    on_alkuluku = False
else:
    for jakaja in range(2, luku):
        if luku % jakaja == 0:
            on_alkuluku = False

if on_alkuluku:
    print(str(luku) + " on alkuluku.")
else:
    print(str(luku) + " ei ole alkuluku.")