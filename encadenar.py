class Usuario:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.monto = 0
        

    def hacer_deposito(self, monto):
        self.monto += monto
        return self

    def hacer_giro(self,monto):
        self.monto -= monto
        return self

    def mostrar_balance(self):
        print(f"usuario: {self.nombre}, Balance: {self.monto}")
        return self

    def transferir_dinero(self,monto,usuario):
        self.monto -= monto
        usuario.monto += monto
        self.mostrar_balance()
        usuario.mostrar_balance()
        return self


mateo = Usuario("teo")
abel = Usuario("abelito")
masito = Usuario("masito23")

mateo.hacer_deposito(100).hacer_deposito(200).hacer_deposito(50).hacer_giro(45).mostrar_balance()

abel.hacer_deposito(1000).hacer_deposito(1000).hacer_giro(500).hacer_giro(300).mostrar_balance()

masito.hacer_deposito(1500).hacer_giro(1000).hacer_giro(5000).hacer_giro(3000).mostrar_balance()


abel.transferir_dinero(400, mateo)