print("-------------------------------")
print("----- REBOTES PELOTA ----------")
print("-------------------------------")

# input

H=int(input("Ingrese la altura inicial: "))
a=0
b= H/5

# processing

while(H>=b):
    H=H-(H*0.1)
    a=a+1
    print("H="+str(H))
    print("a="+str(a))

# output