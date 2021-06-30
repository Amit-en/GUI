from tkinter import *

root = Tk()
root.geometry("300x300")
root.title("Fetch Jokes")

submit = Button(root, text="Get other Joke", font="Helvetica 11 bold").grid(row=5, column=2)


root.mainloop()