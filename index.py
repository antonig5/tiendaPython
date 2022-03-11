
product1 = "leche"
product2 = "arroz"
precio1 = 200000 * 1.19
precio2 = 400000 * 1.19
precio3 = 200000
precio4 = 400000
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
        cta1 = cantidad1*precio1
        cta2 = cantidad2*precio2

        if cta1 + cta2 > 1000000:
            total2 = cta1+cta2-30000
            print(total2)
        else:
            print("no paso el millon")
        opc2 = input("desea seguir comprando \r\n")
        while opc2 in "si":
            print("Cuales productos desea comprar",
                  "productos disponibles:", product1, "precio:", "200000", product2, "precio", "400000")

            def cantid1():
                global cantidad3
            cantidad3 = int(input("arroz\r\n"))

            cantidad4 = int(input("leche\r\n"))
            opc2 = input("desea seguir comprando \r\n")
            if cantidad3 == None:
                print("siii")
            else:
                cant = cantidad1 + cantidad3
                cant2 = cantidad2 + cantidad4
                ct1 = cant*precio1
                ct2 = cant2*precio2
                total1 = ct1+ct2-30000
                if total1 > 1000000:
                    print(total1)
            print(cantidad3)
        break
    print("bienvenid@ a Economax")
    print("desea vender o comprar, por favor digitar")
    opc = input()

if opc in "vender":
    print("usted a ingresado a venta")
    abono2 = int(input("dijite un abono inicial mayor a 1.000.000\r\n"))
    while abono2 >= 1000000:
        name2 = input("por favor dijite su nombre\r\n")
        lastname2 = input("por favor digite su apellido\r\n")

        if cant < 1:
            print("cuales productos desea vender",
                  "arroz", cantidad1, "leche", cantidad2)
            cantv5 = int(input("arroz"))
            cantv6 = int(input("leche"))
            ven3 = cantidad1 - cantv5
            ven4 = cantidad2 - cantv6
            descontar = total1 * 0.3
            fin2 = total2-descontar
            print(fin2, ven3, ven4)

        else:

            print("cuales productos desea vender",
                  "azucar", precio1, "panela", precio2, "arroz", cant, "leche", cant2)
            cantv1 = int(input("azucar"))
            cantv2 = int(input("panela"))
            cantv3 = int(input("arroz"))
            cantv4 = int(input("leche"))
            ven1 = cant - cantv3
            ven2 = cant2 - cantv4
            descontar = total1 * 0.3
            fin = total1-descontar
            print(fin, ven1, ven2)

        break
