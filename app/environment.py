class Environment:
    def __init__(self):
        self.quartos = ["L", "R"]

        self.estado = {
            "L": "sujo",
            "R": "sujo"
        }
        self.posicaoAgente = 0

    def ver_quarto_atual(self):
        quarto = self.quartos[self.posicaoAgente]
        estado = self.estado[quarto]
        return f"Você está no quarto {quarto} e ele está {estado}"

    def limpar_quarto(self):
        quarto = self.quartos[self.posicaoAgente]
        if self.estado[quarto] == "sujo":
            self.estado[quarto] = "limpo"
            return f"Você limpou o quarto: {quarto}"
        return f"O quarto {quarto} já está limpo"

    def mover(self, direcao):
        direcao = direcao.upper()

        if direcao == "MOVERIGHT":
            if self.posicaoAgente < len(self.quartos) - 1:
                self.posicaoAgente += 1
                return f"Você se moveu para a sala: {self.quartos[self.posicaoAgente]}"
            else:
                return "Esse quarto não existe"

        elif direcao == "MOVELEFT":
            if self.posicaoAgente > 0:
                self.posicaoAgente -= 1
                return f"Você se moveu para a sala: {self.quartos[self.posicaoAgente]}"
            else:
                return "Ação bloqueada: Você já está na sala mais à esquerda"

        return "Direção inválida"
    def terminou(self):
     return all(
        estado == "limpo"
        for estado in self.estado.values()
    )


environment = Environment()