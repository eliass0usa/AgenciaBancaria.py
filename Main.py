class Main:
    pass

from Cliente import Cliente
from Conta import Conta

c1 = Cliente("Elias", "99999-9999")
conta = Conta(0, c1.get_nome(), 11)

conta.deposita(120)
conta.saque(15)
conta.extrato()