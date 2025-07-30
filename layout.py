from tkinter import *
from tkinter import ttk

class CatAdoption:
    '''
    Main applications
    '''
    def __init__(self):
        self.root = Tk()
        self.root.title("Adopt A Cat!! :-)")
        self.root.geometry("700x720")

        self.root.resizable(False, False)

        # Container for all frames
        self.container = Frame(self.root)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Dictionary to hold the frames
        self.frames = {}

        for F in (MainFrame,):
            frame = F(self.container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show initial frame
        self.show_frame("MainFrame")

        self.bottom_frame = Frame(self.root, bg="#D6CCC2")
        self.bottom_frame.pack(side="bottom", fill="x")

    def show_frame(self, frame_name):
        # shows requested frame
        frame = self.frames[frame_name]
        frame.tkraise()

    def quit_app(self):
        # Method to quit the program
        self.root.destroy()

    def run(self):
        # tkinter loop
        self.root.mainloop()

class MainFrame(Frame):
    # main menu with navigation
    def __init__(self, parent, controller):
        # Set the background color for the MainFrame
        Frame.__init__(self, parent,
                       bg="#D6CCC2")

        style = ttk.Style()
        style.configure("My.TLabel",
                        background="#D6CCC2",
                        font=("PMingLiU", 16, "bold"))

        label = Label(self,
                      text="Find your purrfect match! \n Adopt a cat today!",
                      font=("PMingLiU", 16, "bold"),
                      fg="#827268",
                      background="#E3D5CA",
                      width=30,
                      height=5)
        label.pack(pady=20, fill='x', padx=10)

        # Button to go to Adoption page
        to_adopt_button = Button(self, text="Go", bg="#EDEDE9",
                                 font=("PMingLiU", 16, "bold"),
                                 fg="#827268",
                                 width=15,
                                 height=2,
                                 command=lambda: controller.show_frame("AdoptionFrame"))
        to_adopt_button.pack(pady=(85, 10), fill='x', padx=40)

        # moved quit button to MainFrame as it's part of the homepage layout
        button_quit = Button(self, text="Exit",
                                 font=("PMingLiU", 14, "bold"),
                                 fg="#827268",
                                 width=15,
                                 height=1,
                                 command=controller.quit_app)
        button_quit.pack(padx=40, fill='x', pady=(0, 10))

# run the application
if __name__ == "__main__":
    app = CatAdoption()
    app.run()
