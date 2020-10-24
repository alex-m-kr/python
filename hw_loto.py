import random


class LotoCard:
    def __init__(self, name):
        self.name = name
        self._create_card()

    def _create_card(self):
        card = random.sample(range(1, 91), 27)
        card1 = card[:9]
        card2 = card[9:18]
        card3 = card[18:]
        card = [sorted(card1), sorted(card2), sorted(card3)]
        for line in card:
            whitespace_pos = random.sample(range(9), 4)
            for pos in whitespace_pos:
                line[pos] = ' '
        self.card = card

    def __str__(self):
        str1 = self.name
        str2 = '-' * 34
        str3 = '\n'.join(['\t'.join([str(elem) for elem in line]) for line in self.card])
        return str1 + '\n' + str2 + '\n' + str3


class LotoGame:
    def __init__(self, first, second):  # пока прописана такая логика, что компьютер всегда второй
        self.first = first
        self.second = second
        self.lst_barrel = [el for el in range(1, 91)]
        random.shuffle(self.lst_barrel)
        self.human_win = False
        self.end_game = False

    def computer_step(self, barrel):
        cnt = 0
        for line in self.second.card:
            if barrel in line:
                line[line.index(barrel)] = '-'
            cnt += line.count('-')
            if cnt >= 15:
                self.end_game = True

    def human_step(self, barrel):
        cnt = 0
        answer = input('Хотите зачеркнуть? y/n ')
        if answer.lower() == 'y':
            if barrel not in self.first.card[0] and barrel not in self.first.card[1] \
                    and barrel not in self.first.card[2]:
                self.end_game = True
            for line in self.first.card:
                if barrel in line:
                    line[line.index(barrel)] = '-'
                cnt += line.count('-')
            if cnt >= 15:
                self.human_win = True
                self.end_game = True
        else:
            if barrel in self.first.card[0] or barrel in self.first.card[1] \
                    or barrel in self.first.card[2]:
                self.end_game = True

    def start(self):
        while True:
            print(self.first)
            print()
            print(self.second)
            barrel = self.gen_barrel()
            print(f'\nНовый бочонок {barrel}, осталось {len(self.lst_barrel)}\n')
            self.human_step(barrel)
            self.computer_step(barrel)
            if self.end_game:
                break
        if self.human_win:
            print('Игрок победил!')
        else:
            print('Игрок проиграл!')

    def gen_barrel(self):
        return self.lst_barrel.pop()
        # проверка работы
        # for _ in range(90):
        #     print(self.lst_barrel.pop())
        #     print(f'Осталось {len(self.lst_barrel)}')


human_player = LotoCard('Игрок')
computer_player = LotoCard('Компьютер')
game = LotoGame(human_player, computer_player)
game.start()
