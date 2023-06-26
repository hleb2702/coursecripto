from course import course, valute_list
from tkinter import Tk, ttk

root = Tk()
root.title('Course CriptoValute')
root.geometry('300x250')

def go():
    win = Tk()
    win.title('List')
    win.geometry('200x200')
    tree = ttk.Treeview(win, show="tree")
    tree.pack(expand=1, fill='both')

    tree.insert("", 'end', iid=1, text="List of criptovalute", open=True)

    for i in valute_list:
        a = tree.insert(1, index='end', text=i)
    win.mainloop()

def entry():
    try:
        l2['text'] = f'Price {ent.get()}: {course(ent.get())}$'
    except:
        l2['text'] = 'Error'
    ent.delete(0, 'end')


btn = ttk.Button(text='Get result', command=entry)
btn2 = ttk.Button(text='Checking list cripto', command=go)
l1 = ttk.Label(text='Write name\'s cripto:')
ent = ttk.Entry()
l2 = ttk.Label(text='')
l3 = ttk.Label(text='Gleb Hlebnikov was making this GUI :)')

ent.place(x=80, y=50)
l1.place(x=80, y=30)
btn.place(x=30, y=150)
btn2.place(x=150, y=150)
l2.place(x=80, y=100)
l3.place(x=50, y=220)

root.mainloop()

