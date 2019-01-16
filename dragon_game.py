#!/usr/bin/env python
#
# Author: Maryam Jamali, 1397
# Description: Dongeon & Dragon
#
import os
import random

class Dragon:
    x = [0,0]
    d = [0,0]
    z = [0,0]
    n = 0
    moves = []
    table = []
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def __init__(self):
        print("Welcom to the 'Dangeon Dragon' game!")
        enter = input("Press Enter to start!")
        self.n = int(input('Enter N value for N*N Game (N > 2): '))

    def initialize(self):
        #enter = input("Press Enter to start!")
        #self.n = int(input('Enter N value for N*N Game (N > 2): '))
        self.tables = []
        self.moves = []
        i = 0
        j = 0
        for i in range(self.n):
            row = []
            for j in range(self.n):
                row.append('| _ ')
            row.append('|')
            self.table.append(row)


        self.x[0] = random.randint(0,self.n-1)
        self.x[1] = random.randint(0,self.n-1)
        self.d[0] = random.randint(0,self.n-1)
        self.d[1] = random.randint(0,self.n-1)
        self.z[0] = random.randint(0,self.n-1)
        self.z[1] = random.randint(0,self.n-1)
        while (self.x == self.d) or (self.x == self.z):
            self.x[0] = random.randint(0, self.n-1)
            self.x[1] = random.randint(0, self.n-1)

    def allowed_moves(self):
        self.moves = []
        if (self.x[0] < self.n-1):
            self.moves.append('RIGHT')
        if (self.x[0] > 0):
            self.moves.append('LEFT')
        if (self.x[1] > 0):
            self.moves.append('UP')
        if (self.x[1] < self.n-1):
            self.moves.append('DOWN')

    def display(self):
        #print("x = {}\nd = {}\nz = {}".format(self.x, self.d, self.z))
        row = list()
        for j in range(self.n):
            row.append('  _ ')
        print ("".join(row))
        self.table[self.x[1]][self.x[0]] = '| X '
        for i in range(self.n):
            print ("".join(self.table[i]))
        print ("You're currently in room ({},{})".format(self.x[0],self.x[1]))
        print ("You can move {}".format(', '.join(self.moves)))
        print ("Enter QUIT to quit.")

    def move(self, command):
        if command == 'quit':
            exit(0)
        elif command == 'right':
            if "RIGHT" in self.moves:
                self.x[0] += 1
                return True
            else:
                print('Your command is wrong!')
                enter = input("Press Enter to continue!")
                return False

        elif command == 'left':
            if "LEFT" in self.moves:
                self.x[0] -= 1
            else:
                print('Your command is wrong!')
                enter = input("Press Enter to continue!")
                return False

        elif command == 'up':
            if "UP" in self.moves:
                self.x[1] -= 1
            else:
                print('Your command is wrong!')
                enter = input("Press Enter to continue!")
                return False

        elif command == 'down':
            if "DOWN" in self.moves:
                self.x[1] += 1
            else:
                print('Your command is wrong!')
                enter = input("Press Enter to continue!")
                return False

        else:
            print ('Your command is wrong!')
            enter = input("Press Enter to continue!")
            return False

    def state(self):
        if self.x == self.d:
            print ("** You scaped ! congratulaation general **")
            return False
        elif self.x == self.z:
            print ("** You lost !")
            return False
        else:
            return True

    def play(self):
        while self.state():
            self.allowed_moves()
            self.clear_screen()
            self.display()
            command = input (">")
            command.lower()
            self.table[self.x[1]][self.x[0]] = '| _ '
            self.move(command)

        again = input("Play again? (Y/n)")
        return again.lower()

if __name__ == "__main__":
    dragon = Dragon()
    again = 'y'
    while again == 'y':
        dragon.initialize()
        again = dragon.play()
    exit(0)