class Conta:
    def __init__(self, numero, titular, saldo, limite): #função construtora
        self.__numero = numero #privei os atributos com __
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato(self):
        print("Saldo de R${} do titular {}".format(self.__saldo, self.__titular))

    def __pode_sacar(self, valor_do_saque): #metodo para encutar of if
        dinheiro_disponivel_saque = self.__saldo + self.__limite
        return valor_do_saque <= dinheiro_disponivel_saque

    def saque(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor #função que retirará um valor da minha conta
        else:
            print(f"O valor {valor} passou o limite")

    def deposito(self, valor):
        self.__saldo += valor #função que depositará um valor na minha conta

    def transferir(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)

    @property
    def saldo(self):
        return self.__saldo #função que retornará um unico dado da conta

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite  #set altera o valor do atributo

    @staticmethod
    def cod_banco():
        return "001"

    @staticmethod
    def cods_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

conta1 = Conta(123, "Ana", 50.0, 1000.0)
conta2 = Conta(321, "Renan", 100.0, 1000.0)
