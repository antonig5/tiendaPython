product1 = "leche"
product2 = "arroz"
precio1 = 200000
precio2 = 400000

print("bienvenid@ a Economax")
print("desea vender o comprar, por favor digitar")
opc = input()
if opc in r"comprar":
    print("usted a ingresado a compra")
    abono1 = int(input("dijite un abono inicial mayor a 300.000\r\n"))
    while abono1 >= 300000:

        name1 = input("por favor dijite su nombre\r\n")
        lastname1 = input("por favor digite su apellido\r\n")
        print("Cuales productos desea comprar",
              "productos disponibles:", product1, "precio:", "200000", product2, "precio", "400000")
        cantidad1 = int(input("arroz \r\n"))
        cantidad2 = int(input("leche\r\n"))
        opc2 = input("desea seguir comprando \r\n")
        while opc2 in "si":
            print("Cuales productos desea comprar",
                  "productos disponibles:", product1, "precio:", "200000", product2, "precio", "400000")
            cantidad3 = int(input("arroz\r\n"))
            cantidad4 = int(input("leche\r\n"))
            opc2 = input("desea seguir comprando \r\n")

        break
    cant = cantidad1 + cantidad3
    cant2 = cantidad2 + cantidad4
    ct1 = cant*precio1
    ct2 = cant2*precio2
    if ct1 + ct2 > 1000000:
        total1 = ct1+ct2-30000
        print(total1)
    if cant + cant2 > 1000000:
        total2 = cant+cant2-30000
        print(total2)

    print("bienvenid@ a Economax")
    print("desea vender o comprar, por favor digitar")
    opc = input()

if opc in "vender":
    print("usted a ingresado a venta")
    abono2 = int(input("dijite un abono inicial mayor a 1.000.000\r\n"))
    while abono2 >= 1000000:
        name2 = input("por favor dijite su nombre\r\n")
        lastname2 = input("por favor digite su apellido\r\n")
        print("que productos desea vender", product1, product2,
              cantidad1+cantidad3, cantidad2+cantidad4)


else:
    while opc != "vender":
        print("valor invalido ingrese nuevamente")
        print("desea vender o comprar, por favor digitar")
        opc = input()
        while opc != "comprar":
            print("valor invalido ingrese nuevamente")
            print("desea vender o comprar, por favor digitar")
            opc = input()

        continue
