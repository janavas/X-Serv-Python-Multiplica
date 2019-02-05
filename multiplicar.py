#Tablas de multiplicar del 1 al 10
variable = range(1,11);

for num in variable:
    print("\nTabla del " + str(num))
    print("-----------------------")

    for value in variable:
        print(str(num) + " por " + str(value) + " es " + str(num * value))
