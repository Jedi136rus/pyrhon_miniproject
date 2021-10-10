from random import shuffle

class Card():
        suit = ["пики","черви","крести", "буби" ]                                                           #масти
        values = [None,None, "2", "3","4","5","6","7","8","9","10","валет","дама","король","туз",]          #карты
        def __init__ (self, v, s):
            self.values = v                                 
            self.suit = s

        def __it__ (self, c2):                                   #сравнение карт на большую     
            if self.values < c2.values:
                return True
            if self.value == c2.values:
                if self.suit < c2.suit:
                    return True
                else:
                    return False
            return False
        def __gt__(self, c2):                                   #сравнение карт на меньшую
            if self.values > c2.values:
                return True
            if self.values == c2.values:
                if self.suit > c2.suit:
                    return True
                else:
                    return False
            return False
        def __repr__(self):                                                     #вывести карту
            v = Card.values[self.values] + "  " + Card.suit[self.suit]
            return v

class Deck:             #создание колоды
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range (4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0 :
            return
        return self.cards.pop()         #берет верхнее значение списка (карту)

class Player:                           #игрок
    def __init__ (self, name):
        self.wins = 0
        self.card = None                #карта которую держит игрок
        self.name = name

class Game:                                         #сама игра
    def __init__(self):
        name1 = input ("имя первого игрока: ")
        name2 = input ("имя второго игрока: ")
        self.deck = Deck()                          #создание колоды
        self.p1 = Player(name1)                    #присвоение имен
        self.p2 = Player(name2)                    #присвоение имен

    def wins(self, winner):                         #вывод победителя
        w = "{} забирает карты"
        w = w.format(winner)
        print(w) 

    def draw (self, p1n, p1c, p2n, p2c):               #вывод хода
        d = "{} кладет {}, а {} кладет {}"
        d = d.format (p1n, p1c, p2n, p2c,)
        print(d)

    def play_game(self):
        cards = self.deck.cards                     #инициализация колоды карт
        print ("Игра началась!")
        while len(cards) >=2:                      #проверка количества карт
            m = "Нажмите X для выхода. Нажмите любую другую клавишу для начала игры."
            response = input (m)
            if response == "X":
                break
            p1c = self.deck.rm_card()               #1 игрок берет карту из колоды
            p2c = self.deck.rm_card()               #2 игрок берет карту из колоды
            p1n = self.p1.name                      
            p2n = self.p2.name                      
            self.draw (p1n, p1c, p2n, p2c)          #вывод имени взятой карты
            if p1c > p2c:                           #поиск победителя
                self.p1.wins += 1
                self.wins (self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print ("Игра окончена. {} выйграл!".format(win))

    def winner(self, p1,p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "Ничья!"

game = Game()
game.play_game()