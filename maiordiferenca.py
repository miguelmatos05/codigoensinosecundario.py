n=int(input("n:"))

d=1
maior_dif=0


while d<=n:
    value=int(input(f"value {d}:"))
    if d>1:
        dif=abs(value-anterior)

        if dif>maior_dif:
            maior_dif=dif

    anterior=value
    d+=1

    
print(f"Maximum difference = {maior_dif:.2f}")