class Main:
    pass

print("Testando o projeto")

from Cliente import Cliente
from Conta import Conta

c1 = Cliente("Elias", "99999-9999")
conta = Conta(0, 555555, c1.nome)

print(conta.titular, " Numero: ",conta.numero, "Seu saldo: ", conta.saldo)
