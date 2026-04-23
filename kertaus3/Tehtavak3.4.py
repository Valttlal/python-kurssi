def create_point(x, y):
    return (x, y)

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return d

x1 = float(input("Anna ensimmäisen pisteen x: "))
y1 = float(input("Anna ensimmäisen pisteen y: "))
x2 = float(input("Anna toisen pisteen x: "))
y2 = float(input("Anna toisen pisteen y: "))

p1 = create_point(x1, y1)
p2 = create_point(x2, y2)

etaisyys = distance(p1, p2)

print("Piste 1:", p1)
print("Piste 2:", p2)
print(f"Etäisyys on {etaisyys:.2f}")