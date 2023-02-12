from tkinter import *

import math
import random

class Data_for_neurons:
    A = [0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1]
    B = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0]
    C = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1]
    D = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0]
    E = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1]
    F = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    G = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1]
    H = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
    I = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    J = [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0]
    K = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1]
    L = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]
    M = [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
    N = [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1]
    O = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    P = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0]
    Q = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    R = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1]
    S = [1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1]
    T = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    U = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    V = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0]
    W = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0]
    X = [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1]
    Y = [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    Z = [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1]

    tab_letters = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z]

class Neurons(object):
    def __init__(self, name : int) -> None:
        self.psize = 35
        self.name = name
        self.weight = list()
        self.alpha = 1
        self.factor = 0.4

        for x in range(self.psize):
            self.weight.append(round(random.uniform(0.01, self.factor), 2))

    def adder(self, data : list) -> float:
        sums = 0
        for i in range(self.psize):
            sums = sums + self.weight[i] * data[i]
        return sums

    def sigmoid_function(self, x : float) -> float:
        return (1 / (1 + math.exp(-1 * self.alpha * x)))

    def output(self, data : list) -> float:
        sums : float = 0
        sums = self.sigmoid_function(self.adder(data))
        return sums
    
    def error_value(self, correct : float, result : float) -> float:
        return correct - result
        
    def update(self, data : list, error : float):
        for i in range(self.psize):
            self.weight[i] = self.weight[i] + self.factor * error * data[i]
        
    def learning(self, data : list , correct : int):
        result = self.output(data)
        error = self.error_value(correct, result)
        self.update(data, error)

w = 5
h = 7
grid_size = 60
result = 0
canvas = 0
neurons = []
neurons_nr = 26
repetitions_nr = 200
states = [[0]*h for j in range(w)]

def value_in(piece):
    return piece['prawdopodobienstwo']

def compatibility_check(value : float) -> float:
    return round(value, 2) * 100

def print_grid(canvas):
    for i in range(w):
        for j in range(h):
            color = 'black' if states[i][j] > 0 else 'white'
            canvas.create_rectangle(i * grid_size, j * grid_size, (i + 1) * grid_size, (j + 1) * grid_size, outline="black", fill=color)

def mouseClick(event, canvas):
    x = math.floor(event.x / grid_size)
    y = math.floor(event.y / grid_size)
    if x < w and y < h: states[x][y] = 0 if states[x][y] > 0 else 1
    print_grid(canvas)      

def test():
    global neurons
    input = sum(states.copy(), [])
    values = list()
    
    for i in range(neurons_nr):
        values.append({'Litera' : chr(neurons[i].name), 'prawdopodobienstwo' : neurons[i].output(input)*100})

    values.sort(key=value_in, reverse=True)
    if(value_in(values[0])<=60):
        return

    print("1: ", values[0])

    if(value_in(values[1])>=30):
        print("2: ", values[1])
    print("\n")

def clear():
    global canvas
    for i in range(len(states)):
        for j in range(len(states[i])):
            states[i][j] = 0
    print_grid(canvas)

def teaching():
    for i in range(repetitions_nr):
        for j in range(neurons_nr):
            for k in range(neurons_nr):
                if(k == j):
                    correct = 1
                else:
                    correct = 0
                neurons[j].learning(Data_for_neurons.tab_letters[k], correct)

def begin():
    global neurons
    neurons = [Neurons(i + 65) for i in range(neurons_nr)]
    teaching()

def init_interface():
    global neurons
    begin()
    root = Tk()
    root.title('WDSI - LABORATORIUM 4')

    frame = Frame()

    # The padx and the pady parameters put some space between the widgets. 
    frame.pack(padx=10, pady=10)

    toolbar = Frame(frame)
    toolbar.pack(fill=X)     
     
    global canvas
    canvas = Canvas(frame, width=grid_size*w, height=grid_size*h)
    canvas.bind("<Button>", lambda event: mouseClick(event, canvas))
    canvas.pack(fill=X)

    print_grid(canvas)

    bottom_bar = Frame(frame, height=50)
    bottom_bar.pack(fill=X)
        
    Button(bottom_bar, text="Test", command = test).pack(side=LEFT)

    Label(bottom_bar, text='Wynik').pack(side=LEFT, padx = 10)
    result = Entry(bottom_bar, width=20, textvariable=StringVar())
    result.pack(side=LEFT, padx = 10)
    Button(bottom_bar, text='Clear', command=clear).pack(side=RIGHT)

    root.mainloop()

if __name__ == "__main__":
    init_interface()