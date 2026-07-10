import re


class RegolaPassword:

    def verifica(self, password):
        pass


class RegolaLunghezza(RegolaPassword):

    def verifica(self, password):
        return len(password) >= 8


class RegolaMaiuscola(RegolaPassword):

    def verifica(self, password):
        return bool(re.search(r"[A-Z]", password))


class RegolaNumero(RegolaPassword):

    def verifica(self, password):
        return bool(re.search(r"\d", password))
