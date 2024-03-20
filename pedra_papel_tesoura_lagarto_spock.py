# Title: Pedra, papel, tesoura, lagarto, spock

''' 
O jogo é uma extensão do clássico pedra, papel e tesoura.
Cada jogador escolhe uma das cinco opções: pedra, papel, tesoura, lagarto ou spock.
As regras são as seguintes:
- Tesoura corta papel
- Papel cobre pedra
- Pedra esmaga lagarto
- Lagarto envenena Spock
- Spock derrete tesoura
- Tesoura decapita lagarto
- Lagarto come papel
- Papel refuta Spock
- Spock vaporiza pedra
- Pedra quebra tesoura

tabela de regras:
    Escolha |   Pedra   |   Papel   |   Tesoura     |   Lagarto |   Spock
    ------- |   ------  |   ------  |   ------      |   ------  |   ------
    Pedra   |   0       |   -1      |   1           |   1       |   -1
    Papel   |   1       |   0       |   -1          |   -1      |   1
    Tesoura |   -1      |   1       |   0           |   1       |   -1
    Lagarto |   -1      |   1       |   -1          |   0       |   1
    Spock   |   1       |   -1      |   1           |   -1      |   0
'''
class Participant:
    def __init__(self, name):
        self.name = name
        self.symbol = ''
        self.__score__ = 0

    def choose(self):
        self.symbol = input(f'{self.name}, escolha pedra, papel, tesoura, lagarto ou spock: ')
        print(f'{self.name} escolheu {self.symbol}')

    def toNumericalChoice(self):
        switcher = {
            'pedra': 0,
            'papel': 1,
            'tesoura': 2,
            'lagarto': 3,
            'spock': 4
        }
        return switcher[self.symbol]
    
    def incrementScore(self):
        self.__score__ += 1

class GameRound:
    def __init__(self, participant1, participant2):
        
        self.rules = [[0,-1,1,1,-1],
                      [1,0,-1,-1,1],
                      [-1,1,0,1,-1],
                      [-1,1,-1,0,1],
                      [1,-1,1,-1,0]]
        
        participant1.choose()
        participant2.choose()
        
        result = self.compareSymbols(participant1, participant2)
        if result == 0:
            print('Empate')
        elif result > 0:
            print(f'{participant1.name} venceu')
        else:
            print(f'{participant2.name} venceu')

        if result > 0:
            participant1.incrementScore()
        elif result < 0:
            participant2.incrementScore()
        
    def compareSymbols(self, participant1, participant2):
        return self.rules[participant1.toNumericalChoice()][participant2.toNumericalChoice()]
    
    def getResultAsString(self, result):
        results = {
            0: 'Empate',
            1: 'Vitória',
            -1: 'Derrota'
        }
        return results[result]
        
    def awardPoints():
        print('implementar')

class Game:
    def __init__(self):
        self.end_game = False
        self.participant1 = Participant(input('Nome do jogador 1: '))
        self.participant2 = Participant(input('Nome do jogador 2:'))

    def start(self):
        while not self.end_game:
            GameRound(self.participant1, self.participant2)
            self.checkEndCondition()

    def checkEndCondition(self):
        answer = input('Deseja jogar novamente? (s/n): ')
        if answer == 'n':
            print(f'Fim do jogo, {self.participant1.name} tem {self.participant1.__score__} pontos e {self.participant2.name} tem {self.participant2.__score__} pontos')
            self.determineWinner()
            self.end_game = True
        else:
            GameRound(self.participant1, self.participant2)
            self.checkEndCondition()

    def determineWinner(self):  
        resultString = 'É um empate'
        if self.participant1.__score__ > self.participant2.__score__:
            resultString = f'{self.participant1.name} venceu!'
        elif self.participant1.__score__ < self.participant2.__score__:
            resultString = f'{self.participant2.name} venceu!'
        print(resultString)

if __name__ == '__main__':
    
    game = Game()
    game.start()