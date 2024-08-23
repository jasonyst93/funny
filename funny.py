import pyjokes
import tkinter as tk


# Create the main window
root = tk.Tk()
root.title("Jokes_world")
joke= pyjokes.get_joke()

# Add a label to the window
label = tk.Label(root, text=joke)
label.pack()
# Start the Tkinter event loop
root.mainloop()
break