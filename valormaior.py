
n=int(input("n:"))

d=1
maior=0
segundo=0

while d<=n:
    value=int(input(f"value {d}:"))
    if value>maior:
        segundo=maior
        maior=value
    elif value>segundo:
        segundo=value
    d+=1


print(f"Highest value = {maior} 2nd. Highest value = {segundo}")
    

    