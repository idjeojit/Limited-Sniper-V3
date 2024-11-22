import tkinter as tk
from tkinter import messagebox

def show_popup():
    # Create the main application window (hidden)
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Show the popup message
    messagebox.showinfo("Information", "Thank you for your information! deleted loves you")

    # Close the tkinter application after the popup is dismissed
    root.quit()

if __name__ == "__main__":
    show_popup()
