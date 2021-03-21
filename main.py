from tkinter import *
 
root = Tk()


root.title("Sticker")
root.geometry("300x300")


text = Text(width=200, height=200)# текстовое поле
text.configure(bg='black', foreground="green")# черный фон, зеленый текст
text.pack()


root.lift()# закидывает на верх текущих приложений, дабы не 
# надо было кликать на панеле
root.call('wm', 'attributes', '.', '-topmost', True)# оставляет наверху


root.mainloop()