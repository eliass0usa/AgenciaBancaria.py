class Conta:
    def __init__(self, saldo, numero, titular):
        self.saldo = 0
        self.numero = numero
        self.titular = titular

        def get_saldo(self):
            return self.saldo

        def set_saldo(self, saldo):
            if (saldo >= 0):
                self._saldo = saldo
            else:
                print("O saldo da conta não pode ser negativo")
