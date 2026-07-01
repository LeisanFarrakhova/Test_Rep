import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb



def check():
    colors = ('зеленый', 'красный', 'жёлтый')
    computer = random.choice(colors)

    user = e.get(),lower()
    if computer == user:
        mb.showinfo('Результат', 'Вы угадали')
    else:
        mb.showinfo('Результат',f'Вы не угадали \n компьютер выбрал {computer}')



root = tk.Tk()
root.geometry(500x300+200+100)
root.title('Угадай цвет светофора!')

l = tk.Label(root, text='Ввведите цвет светофора!')
l.pack(pady=10)

b = tk.Button(root, text='Проверить', command=)