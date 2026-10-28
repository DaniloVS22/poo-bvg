
class Cliente:
    

    def __init__(self, nome, idade, saldo, status):
        self.__nome = nome
        self.__idade = idade
        self.__saldo = saldo
        if saldo < 0:
            raise ValueError("O saldo inicial não pode ser negativo.")
        self.__status = status

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def saldo(self):
        return self.__saldo

    @property
    def status(self):
        return self.__status

    def depositar(self, valor):
        
        if not self.__status:
            print("Erro: Conta inativa.")
        elif valor <= 0:
            print("Erro: Valor inválido.")
        else:
            self.__saldo += valor
            print("Depósito realizado com sucesso!")

    def sacar(self, valor):

        if not self.__status:
            print("Erro: Conta inativa.")
        elif valor <= 0:
            print("Erro: Valor inválido.")
        elif valor > self.__saldo:
            print("Erro: Saldo insuficiente!")
        else:
            self.__saldo -= valor
            print("Saque realizado com sucesso!")











