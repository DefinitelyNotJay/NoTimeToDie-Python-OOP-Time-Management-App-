from tkinter import *
from tkinter import ttk
class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('TO DO LIST')
        self.root.geometry('650x410+300+150')
        # "To Do List" Title
        self.label = Label(self.root, text='To Do List',
            font=("MN Kunghaeng Bold", 28), width=10,bd=0.5,bg='#f3d9fa', fg='#862e9c')
        self.label.pack(side='top', fill=BOTH)

        # "Add text" label
        self.label2 = Label(self.root, text='Add text',
            font='ariel, 18 bold', width=10,bd=5,bg='#a9f5b4', fg='black')
        self.label2.place(x=40, y=54)

        # "Text" label
        self.label3 = Label(self.root, text='Text',
            font='ariel, 18 bold', width=10,bd=5,bg='#a9f5b4', fg='black')
        self.label3.place(x=380, y=54)

        # All tasks
        self.main_text = Listbox(self.root, height=5, bd=5, width=50, font=("MN Kunghaeng", 25, "bold"), justify="center")
        self.main_text.place(x=270, y=100)

        # Adding task label
        self.text = Text(self.root, bd=5, height=1, width=18, font=("MN Kunghaeng", 25, "bold"))
        self.text.place(x=20, y=120)

        def add():
            """ Add contents by append text from Add Text label """
            content = self.text.get(1.0, END)
            print(content)
            self.main_text.insert(END, content)
            with open('data.txt', 'a') as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0, END)

        def delete():
            delete_ = self.main_text.curselection()
            look = self.main_text.get(delete_)
            with open('data.txt', 'r+') as f:
                new_f = f.readlines()
                print('-----------------------')
                print(delete_)
                print(look)
                print(new_f)
                print('-----------------------')
                f.seek(0)
                for line in new_f:
                    item = str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_)
        with open('data.txt', 'r') as file:
            # readlines -> Taking all text that is separated by line and containing them in a list
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(-1, ready)
                file.close()
        self.button = Button(self.root, text="Add", font=("MN Kunghaeng Bold", 24),
                    width=14,bd=2, bg='#a9e34b', command=add)
        self.button.place(x=30, y=180)
        self.button2 = Button(self.root, text='Delete', font='sarif, 20 bold italic',
                    width=10,bd=5, bg='#ff8787', fg='black', command=delete)
        self.button2.place(x=30, y=280)

def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()
if __name__ == "__main__":#เรียกหาหน้าต่าง
    main()
