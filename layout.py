'''
This is just going to be for working on the layout of my cat adoption program
By Daisy Chamberlain

started 18/07/2025
'''

from tkinter import *
from tkinter import ttk

class CatAdoption:
    '''
    Main applications
    '''
    def __init__(self):
        self.root = Tk()
        self.root.title("Adopt A Cat!! :-)")
        self.root.geometry("450x350")

        # Container for all frames
        self.container = Frame(self.root)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Dictionary to hold the frames
        self.frames = {}

        # Add each frame to the dictionary
        for F in (MainFrame,): # Only MainFrame for now
            frame = F(self.container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show initial frame
        self.show_frame("MainFrame")

    def show_frame(self, frame_name):
        # shows requested frame
        frame = self.frames[frame_name]
        frame.tkraise()

    def run(self):
        # tkinter loop
        self.root.mainloop()

class MainFrame(Frame):
    # main menu with navigation
    def __init__(self, parent, controller):
        # Set the background color for the MainFrame
        Frame.__init__(self, parent, bg="#D6CCC2")

        # Configure a style for the ttk.Label to set its background and font
        style = ttk.Style()
        # The background of a ttk.Label needs to be set via a style configuration
        style.configure("My.TLabel", background="#D6CCC2", font=("PMingLiU", 16, "bold"))

        # Create the label and apply the custom style
        label = ttk.Label(self, text="Find your purrfect match", style="My.TLabel")
        label.pack(pady=20, padx=10)

        # Uncomment and modify these buttons as you progress with your layout
        # # Button to switch to the Fahrenheit to Celsius converter
        # to_c_button = Button(self, text="Convert Fahrenheit to Celsius", bg="pink",
        #                      command=lambda: controller.show_frame("CelsiusFrame"))
        # to_c_button.pack(pady=5, fill='x', padx=20)

        # # Button to switch to the Celsius to Fahrenheit converter
        # to_f_button = Button(self, text="Convert Celsius to Fahrenheit", bg="lightyellow",
        #                      command=lambda: controller.show_frame("FahrenheitFrame"))
        # to_f_button.pack(pady=5, fill='x', padx=20)

        # # Button to show a picture
        # to_cat_button = Button(self, text="Show a Picture", bg="#C4A484",
        #                      command=lambda: controller.show_frame("CatFrame"))
        # to_cat_button.pack(pady=5, fill='x', padx=20)

# run the application
if __name__ == "__main__":
    app = CatAdoption()
    app.run()
