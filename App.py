class Gerenciamneto:
    def __init__(self, salario):
        self.salario = salario
        self.dispesas = {}

    def gerenciar_dispesa(self, tipo, valor):
        self.dispesas[tipo] = valor




    def calcular_total_despesas(self):
        return sum(self.dispesas.values())

    def calcular_saldo_restante(self):
        total_despesas = self.calcular_total_despesas()
        return self.salario - total_despesas

    def mostrar_relatorio(self):
        print(f"Salário: {self.salario: .2f} MT")

        for tipo, valor in self.dispesas.items():
            print(f"Dispesa com {tipo.capitalize()}: {valor: .2f} Mt")

        # Verificar Dívida
        if self.calcular_saldo_restante() > 0:
            print(f"Saldo Restante: {self.calcular_saldo_restante()} MT")
        else:
            print(f"Tem uma dívida : {self.calcular_saldo_restante() * -1} MT")


# Loop Principal
def App_run():
    flag = True

    while flag:
        print('Bem-vindo')
        salario = float(input("Introduzir Sálario: "))

        # Verificar se o salário é válido
        while salario < 0:
            salario = int(input("Salário Invalid, Introduz Um Salário Válido: "))

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

App_run()






