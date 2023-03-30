class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.rigth=None

class Arbol:
    def __init__(self):
        self.raiz=None
        self.length=0
    def insert(self,value):
        if self.raiz==None:
            new_node=Node(value)
            self.raiz=new_node
            self.length=1
        else:
            new_node=Node(value)
            tem = self.raiz
            while True:
                if tem.value<new_node.value:
                    if tem.rigth==None:
                        tem.rigth=new_node
                        self.length+=1
                        return True
                    else:
                        tem=tem.rigth
                        continue
                elif tem.value>new_node.value:
                    if tem.left==None:
                        tem.left=new_node
                        self.length += 1
                        return True
                    else:
                        tem=tem.left
                        continue
                elif tem.value==new_node.value:
                    print("El valor ingresado ya existe en la lista")
                    return False


    def print_nodovalor(self):
        tem=self.raiz
        while True:
            value = int(input("Ingresa hacia que lado te quieres dirigir:\n 1.-Izquierda 2.-Derecha 3.-Imprimir\n"))
            if value==1:
                tem=tem.left
            if value==2:
                tem=tem.rigth
            if value==3:
                print(tem.value)
                return True

    def contains(self,value):
        tem=self.raiz
        while True:
            if tem.value<value:
                if tem.rigth==None:
                    print(f"El valor {value} no se encuentra en el arbol")
                    return False
                else:
                    tem=tem.rigth
            elif tem.value>value:
                if tem.left == None:
                    print(f"El valor {value} no se encuentra en el arbol")
                    return False
                else:
                    tem=tem.left
            elif tem.value==value:
                print(f"El valor {value} ya existe en la lista")
                return True

    def minimumValue(self):
        tem=self.raiz
        while True:
            if tem.left !=None:
                tem=tem.left

            else:
                print(f"El valor mas pequeño dentro del arbol es: {tem.value} ")
                return tem
    def closeValue(self,value):
        tem = self.raiz
        dif=10000
        valor=0
        while True:
            if abs(tem.value - value) == dif:
                if tem.value > valor:
                    valor = valor

                if tem.value < valor:
                    valor = tem.value
            if abs(tem.value-value)<dif:
                dif=abs(tem.value-value)
                valor=tem.value

            if tem.value<value:
                if tem.rigth==None:
                    print(f"El valor mas cercano a {value} es {valor} con un diferencia de {dif}")
                    return False
                else:
                    tem=tem.rigth
            elif tem.value>value:
                if tem.left == None:
                    print(f"El valor mas cercano a {value} es {valor} con un diferencia de {dif}")
                    return False
                else:
                    tem=tem.left
            elif tem.value==value:
                print(f"El valor mas cercano a {value} es {valor} con un diferencia de {dif}")
                return valor


miArbol=Arbol()
miArbol.insert(32)
miArbol.insert(18)
miArbol.insert(54)
miArbol.insert(29)
miArbol.insert(14)
miArbol.insert(11)
miArbol.insert(13)
miArbol.closeValue(12)
