file=open("Table_de_multiplication.txt","w+")
for i in range(1,11):
    n = 1
    file.write("Table de multiplication de " + str(i) + "\n")
    for j in range (1,11):
        n = i*j
        file.write(str(i) + " x " + str(j) + " = " + str(n) + "\n")
file.close ()
