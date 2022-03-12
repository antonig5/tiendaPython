# Declarar variables
product1 = "leche"
product2 = "arroz"
precio1 = 200000 / 1.19 * 0.19
precio2 = 400000 / 1.19 * 0.19
precio3 = 200000
precio4 = 400000
# Menu de la tienda Economax
print("bienvenid@ a Economax")
opc = input(
    "desea vender o comprar, por favor digitaro o si desea salir oprima 0\r\n")
# Ciclo while con la condicion de que si el usuario dijita "comprar" en opc le muestre lo que hay dentro
while opc in "comprar":
    print("usted a ingresado a compra")
    abono1 = int(input("dijite un abono inicial mayor a 300.000\r\n"))
    # Abono para que pueda acceder
    if abono1 >= 300000:
        # Recoleccion de datos personales del usuario
        name1 = input("por favor digite su nombre\r\n")
        lastname1 = input("por favor digite su apellido\r\n")
        phone = int(input("dijite su numero de celular\r\n"))
        # compra de productos
        print("Cuales productos desea comprar",
              "productos disponibles:", product1, "precio:", "200000", product2, "precio", "400000")
        cantidad1 = int(input("arroz \r\n"))
        cantidad2 = int(input("leche\r\n"))
        # operaciones de la cantidad de productos por el precio
        cta1 = cantidad1*precio1
        cta2 = cantidad2*precio2
        # condicion para hacer un descuento
        if cta1 + cta2 > 1000000:
            cta1+cta2-30000
            print("se le hizo un descuento por 30.000")
        else:
            print("no paso el millon no se genero el descuento")
        opc2 = input("desea seguir comprando \r\n")
        # si el cliente decide añadir mas productos
        if opc2 in "no":
            print("Factura\r\n", "comprador", "\r\n", name1, lastname1, "\r\n", "Celular", phone, "\r\n", "productos", "\r\n", product1, product2, "\r\n", "cantidad", "\r\n",
                  cantidad1, product2, "\r\n",  cantidad2, product1, "\r\n", "IVA: 19%)", "\r\n""total de la compra", "\r\n", round(cta1+cta2))
        while opc2 in "si":
            print("Cuales productos desea comprar",
                  "productos disponibles:", product1, "precio:", "200000", product2, "precio", "400000")
            # variable global de una funcion para almacenar datos en este cas una cantidad para hacer una condion

            def cantid1():
                global cantidad3
            cantidad3 = int(input("arroz\r\n"))

            cantidad4 = int(input("leche\r\n"))
            opc2 = input("desea seguir comprando \r\n")
            # condicion para verificar si un dato viene null
            if cantidad3 == None:
                print("vacio")
            else:
                cant = cantidad1 + cantidad3
                cant2 = cantidad2 + cantidad4
                ct1 = cant*precio1
                ct2 = cant2*precio2
                if ct1 + ct2 > 1000000:
                    ct1+ct2-30000
                print("Factura\r\n", "comprador", "\r\n", name1, lastname1, "\r\n", "Celular", phone, "\r\n", "productos", "\r\n", product1, product2, "\r\n",
                      "cantidad", "\r\n", cant, product2, "\r\n", cant2, product1, "\r\n", "IVA: 19%)", "\r\n", "total de la compra", "\r\n", round(ct1+ct2))

            break
    print("bienvenid@ a Economax")
    print("desea vender o comprar, por favor digitar o si desea salir oprima 0")
    opc = input()
    # para que el usuario decida comprar mas
    if opc in "comprar":
        continue
if opc in "vender":
    # condicion por si el usuario dijita "vender" en opc
    print("usted a ingresado a venta")
    abono2 = int(input("digite un abono inicial mayor a 1.000.000\r\n"))
    # si no abona 1millon no podra entrar al modulo "vender"
    while abono2 >= 1000000:
        name2 = input("por favor digite su nombre\r\n")
        lastname2 = input("por favor digite su apellido\r\n")
        phone1 = int(input("dijite su numero de celular\r\n"))
        print("azucar", precio3, "panela", precio4)
        cantv1 = int(input("azucar\r\n"))
        cantv2 = int(input("panela\r\n"))
        t1 = precio3 * cantv1
        t2 = precio4 * cantv2
        t3 = t1+t2
        descontar1 = t3 * 0.3
        fin3 = t3 - descontar1 / 1.19 * 0.19
        print("factura" "\r\n", "Vendedor", name2, lastname2, "\r\n", "Celular", phone1, "\r\n", "Productos vendidos",
              "\r\n", "panela", cantv2, "\r\n", "azucar", cantv1, "\r\n", "IVA: 19%)", "\r\n", "total", round(fin3))
        break
# por si el usuario decide salir del sistema
else:
    print("usted a salido del sistema")

# Created by Antonio Giraldo ^v^
