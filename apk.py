from course import course, valute_list
from tkinter import Tk, ttk

root = Tk()
root.title('Course CriptoValute')
root.geometry('500x500')

tree = ttk.Treeview(show="tree")
tree.pack(expand=1, fill='both')

tree.insert("", 'end', iid=1, text="List of criptovalute", open=True)

for i in valute_list():
    tree.insert(1, index='end', text=i)

root.mainloop()

