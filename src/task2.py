import turtle

def draw_pythagoras_tree(branch_length, level, pointer):
    if level == 0:
        return
    pointer.forward(branch_length)
    pointer.left(45)
    draw_pythagoras_tree(branch_length * 0.7, level - 1, pointer)
    pointer.right(90)
    draw_pythagoras_tree(branch_length * 0.7, level - 1, pointer)
    pointer.left(45)
    pointer.backward(branch_length)

def main():
    recursion_level = int(input("Enter the recursion level: "))
    screen = turtle.Screen()
    pointer = turtle.Turtle()
    pointer.left(90)
    pointer.speed(0)
    screen.tracer(0, 0)
    draw_pythagoras_tree(100, recursion_level, pointer)
    screen.update()
    screen.mainloop()

if __name__ == "__main__":
    main()