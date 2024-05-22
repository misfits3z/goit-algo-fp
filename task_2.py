import turtle
import math

def draw_pythagoras_tree(t, length, level):
    if level == 0:
        t.forward(length)
        t.backward(length)
    else:
        t.forward(length)
        t.left(45)
        draw_pythagoras_tree(t, length * math.sqrt(2) / 2, level - 1)
        t.right(90)
        draw_pythagoras_tree(t, length * math.sqrt(2) / 2, level - 1)
        t.left(45)
        t.backward(length)

def main():
    level = int(input("Введіть рівень рекурсії: "))
    length = 100  # Довжина початкової гілки

    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.left(90)

    draw_pythagoras_tree(t, length, level)

    screen.mainloop()

if __name__ == "__main__":
    main()
