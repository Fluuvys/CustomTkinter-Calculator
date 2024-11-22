from customtkinter import *

class App(CTk):
    def __init__(self, fg_color=None, **kwargs):
        super().__init__(fg_color, **kwargs)
        
        self.geometry("640x500")
        self.title("CTk calculator")
        self.grid_rowconfigure((0), weight=1)
        self.grid_columnconfigure((0), weight=1)
        
        # Top screen (Display Area)
        self.frame_top = CTkFrame(self, corner_radius=0, height=100)
        self.frame_top.grid(row=0, column=0, padx=20, pady=20, sticky="nswe")
        
        self.screen = CTkEntry(self.frame_top, width=640, height=300)
        self.screen.grid(row=0, column=0)
        
        # Bottom buttons
        self.frame_bottom = CTkFrame(self, corner_radius=0)
        self.frame_bottom.grid(row=1, column=0, padx=20, pady=0, sticky="nswe")  
        
        # Calculator Buttons
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ]
        for text, row, col in buttons:
            btn = CTkButton(self.frame_bottom, text=text, font=CTkFont(size=30), command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nswe")      
            
    def on_button_click(self, text):
        print(f'Button clicked:',text)
        if text == "C":
            self.screen.delete(0, END)
        elif text == "=":
            try:
                expression = self.screen.get()
                result = eval(expression)
                self.screen.delete(0, END)
                self.screen.insert(0, str(result))
            except Exception as e:
                self.screen.delete(0,END)
                self.screen.insert(0, 'Error')
        else:
            self.screen.insert(END, text)

app = App()
app.mainloop()
