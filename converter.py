# Importing Tkinter **********
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# Classes **********


class MainFrame(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = parent
        self.main_frame = ttk.LabelFrame(self.parent, text='Dollar To Rupee Converter')
        self.main_frame.grid(row=0, column=0, padx=15, pady=10)
        self.value_entry1 = tk.StringVar()
        self.value_entry2 = tk.StringVar()
        self.value_entry3 = tk.StringVar()
        self.labels()
        self.entries()
        self.btn()

    def labels(self):
        label1 = ttk.Label(self.main_frame, text='Dollar ', font=('Arial', 12, 'bold'))
        label1.grid(row=0, column=0, sticky=tk.W, pady=5)
        label2 = ttk.Label(self.main_frame, text='Dollar Rate ', font=('Arial', 12, 'bold'))
        label2.grid(row=1, column=0, sticky=tk.W, pady=5)
        label3 = ttk.Label(self.main_frame, text='Pakistani Rupee ', font=('Arial', 12, 'bold'))
        label3.grid(row=2, column=0, sticky=tk.W, pady=5)

    def entries(self):
        entry1 = ttk.Entry(self.main_frame, width=20, textvariable=self.value_entry1)
        entry1.grid(row=0, column=1, padx=5, pady=5)
        entry1.focus()
        entry2 = ttk.Entry(self.main_frame, width=20, textvariable=self.value_entry2)
        entry2.grid(row=1, column=1, padx=5, pady=5)
        entry3 = ttk.Entry(self.main_frame, width=20, state='readonly', textvariable=self.value_entry3)
        entry3.grid(row=2, column=1, padx=5, pady=5)

    def convert_to(self):
        value1 = self.value_entry1.get()
        value2 = self.value_entry2.get()
        try:
            value1 = int(value1)
            value2 = int(value2)
            if value2 > 170:
                messagebox.showwarning('High Rate', 'Dollar Rate You Entered Is Too High')
                self.value_entry2.set('170')
                value2 = self.value_entry2.get()
            ans = int(value1) * int(value2)
            self.value_entry3.set(ans)

        except ValueError:
            messagebox.showerror('Only Integers', 'Value Must Be Integer, Not Alphabetic')
            self.value_entry1.set('')
            self.value_entry2.set('')

    def btn(self):
        convert = ttk.Button(self.main_frame, text='Convert', command=self.convert_to)
        convert.grid(row=0, column=2, pady=5)


class MyConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resizable(width=False, height=False)
        self.title('Money Converter')
        self.geometry_settings()

    def geometry_settings(self):
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        my_w = 450
        my_h = 180
        win_x = int(screen_w/2 - my_w/2)
        win_y = int(screen_h/2 - my_h/2)
        screen_geo = str(my_w)+"x"+str(my_h)+"+"+str(win_x)+"+"+str(win_y)
        self.geometry(screen_geo)


if __name__ == '__main__':
    app = MyConverter()
    MainFrame(app)
    app.mainloop()
