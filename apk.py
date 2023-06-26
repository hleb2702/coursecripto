from course import course, valute_list 
from tkinter import Tk, ttk, font

root = Tk()
root.title('Course CriptoValute')
root.geometry('400x300')
root.resizable(False, False)
root.configure(bg='white')

myFont = font.Font(family='Arial', size=12)

def go():
    win = Tk()
    win.title('List of cryptocurrencies')
    win.geometry('300x300')
    win.resizable(False, False)
    win.configure(bg='white')
    
    tree = ttk.Treeview(win, show="tree")
    tree.pack(expand=1, fill='both')

    tree.insert("", 'end', iid=1, text="List of cryptocurrencies", open=True)

    for i in valute_list:
        a = tree.insert(1, index='end', text=i)
    win.mainloop()

def entry():
    try:
        l2['text'] = f'Price of {ent.get()}: {course(ent.get())}$'
    except:
        l2['text'] = 'Error'
    ent.delete(0, 'end')


btn = ttk.Button(text='Get result', command=entry)
btn2 = ttk.Button(text='Crypto list', command=go)
l1 = ttk.Label(text='Enter a cryptocurrency name:', font=myFont)
ent = ttk.Entry(font=myFont)
l2 = ttk.Label(text='', font=myFont)
l3 = ttk.Label(text='Made by Gleb Hlebnikov', font=myFont)

ent.place(x=120, y=70, width=160, height=30)
l1.place(x=100, y=40)
btn.place(x=70, y=150, width=100, height=30)
btn2.place(x=240, y=150, width=100, height=30)
l2.place(x=120, y=110)
l3.place(x=115, y=250)

root.mainloop()

