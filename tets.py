import tkinter as tk
import random

# Создаем главное окно
root = tk.Tk()
root.title("Рисование кругов")
root.geometry("400x400")

# Создаем холст для рисования
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Функция, рисующая круг в точке клика мыши
def draw_circle(event):
    x, y = event.x, event.y
    radius = random.randint(10, 50)  # Случайный радиус
    color = random.choice(["red", "blue", "green", "yellow", "purple", "orange"])  # Случайный цвет
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, outline="")

# Привязываем функцию к событию клика мыши
canvas.bind("<Button-1>", draw_circle)

# Запускаем главный цикл программы
root.mainloop()
