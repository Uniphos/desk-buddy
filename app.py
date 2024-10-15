from tkinter import *
import keyboard
from openAi import get_response, clear_messages
#from io import BytesIO

bgGray = "#ABB2B9"
bgColor = "#17202A"
textColor = "#EAECEE"

font = "Helvetica 14"
font_bold = "Helvetica 13 bold"

class chatApplication:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        self.window.protocol("WM_DELETE_WINDOW", self.onClosing)


        # Set up a global hotkey for Ctrl+Alt+P
        keyboard.add_hotkey('ctrl+alt+p', self.reOpen)

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg="lightgray")

        # Head label
        head_label = Label(self.window, bg="lightgray", fg="black",
                           text="Welcome", font=("Helvetica", 13, "bold"), pady=10)
        head_label.place(relwidth=1)

        # Divider
        line = Label(self.window, width=450, bg="gray")
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # Text widget with horizontal scrollbar
        self.text_widget = Text(self.window, width=20, height=2, bg="white", fg="black",
                                font=("Helvetica", 14), padx=15, pady=15, wrap="word")
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)

        # Vertical scrollbar
        v_scrollbar = Scrollbar(self.window, orient="vertical", command=self.text_widget.yview)
        v_scrollbar.place(relheight=0.74, relx=.97, rely=0.085, relwidth=0.025)
        self.text_widget.configure(yscrollcommand=v_scrollbar.set)

        # Bottom label
        bottom_label = Label(self.window, bg="gray", height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # Message box
        self.msgBox = Entry(bottom_label, bg="white", fg="black", font=("Helvetica", 14))
        self.msgBox.place(relwidth=0.74, relheight=0.06, relx=0.011, rely=0.008)
        self.msgBox.focus()
        self.msgBox.bind("<Return>", self.enterPressed)

        # Send button
        sendButton = Button(bottom_label, text="Send", font=("Helvetica", 13, "bold"), width=20, bg="gray",
                            command=lambda: self.enterPressed(None))
        sendButton.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def enterPressed(self, event):
        msg = self.msgBox.get()
        self.insertMesssage(msg, "You")

    def insertMesssage(self, msg, sender):
        if not msg:
            return
        
        self.msgBox.delete(0,END)
        msg1 = f"{sender} : {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg1 = f"OpenAI : \n{get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)

    def onClosing(self):
        clear_messages()
        #self.minimize_to_tray()
        self.window.withdraw()
        
    def reOpen(self, event):
        self.window.deiconify()

    
if __name__ == "__main__":
    app = chatApplication()
    app.run()