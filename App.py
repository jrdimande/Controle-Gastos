class Gerenciamneto:
    def __init__(self, salario):
        self.salario = salario
        self.luz = 0.0
        self.internet = 0.0
        self.agua = 0.0

    def gerenciar_dispesa(self, tipo, valor):
        if tipo == "luz":
            self.luz = valor

        elif tipo == "internet":
            self.internet = valor
        elif tipo == "agua" :
            self.agua = valor


    def calcular_total_despesas(self):
        return self.luz + self.internet + self.agua

    def calcular_saldo_restante(self):
        total_despesas = self.calcular_total_despesas()
        return self.salario - total_despesas

    def mostrar_relatorio(self):
        print(f"Salário: {self.salario:.2f} MT")
        print(f"Despesa com Luz: {self.luz:.2f}MT")
        print(f"Despesa com Internet: {self.internet: .2f}")
        print(f"Despesa com Água: {self.agua: .2f} MT")
        print(f"Saldo Restante: {self.calcular_saldo_restante()} MT")

flag = True

while flag:
    print('Bem-vindo')
    salario = float(input("Introduzir Sálario: "))
    usuario = Gerenciamneto(salario)

    message = input("Adicionar dispesa [y/n]: ")
    if message == 'y':

        while flag:
            if message == 'y':
                tipo = input("Tipo: ")
                valor = float(input("Valor: "))

                usuario.gerenciar_dispesa(tipo, valor)
                usuario.calcular_total_despesas()
                usuario.calcular_saldo_restante()

                message = input("Pretende Adicionar Mais Despesas? [y/n]: ")
                if message == 'y':
                    flag = True
                else:
                    usuario.mostrar_relatorio()
                    flag = False
    else:
        flag = True






