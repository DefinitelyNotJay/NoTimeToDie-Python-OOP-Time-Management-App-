from tkinter import *
from tkinter import ttk
class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('TO DO LIST')
        self.root.geometry('650x410+300+150')
        self.root.configure(bg="#f3d9fa")
        # "To Do List" Title
        self.label = Label(self.root, text='To Do List',
            font=("Acme", 30), width=10,bd=0.5,bg='#BE9FE1', fg='#F1F1F6')
        self.label.pack(side='top', fill=BOTH)
        # All tasks
        self.main_text = Listbox(self.root, height=4, bd=0.5, width=31, font=("Friendly", 25, "bold"), justify="center")
        self.main_text.place(x=14, y=180)

        # Adding task label
        self.text = Text(self.root, bd=0.5, height=1, width=30, font=("Friendly", 25, "bold"))
        self.text.place(x=23, y=60)

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
        #ปุ่มadd
        self.button = Button(self.root, text="Add", font=("Acme", 19),
                    width=8,bd=0.5, bg='#8ce99a',fg='#FBFACD', command=add)
        self.button.place(x=90, y=122)
        #ปุ่มลบ
        self.button2 = Button(self.root, text='Delete', font=("Acme", 19),
                    width=8,bd=0.5, bg='#ffa8a8', fg='#FBFACD', command=delete)
        self.button2.place(x=420, y=122)
def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()
if __name__ == "__main__":#เรียกหาหน้าต่าง
    main()
