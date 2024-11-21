import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from gui.capture_gui import capture_settings_window
from gui.processing_gui import processing_settings_window
from gui.pdf_gui import pdf_settings_window
from main import start_workflow  # Import the workflow function from main.py

def main_gui():
    root = ttk.Window(themename="superhero")  # Create the main window
    root.title("DIY Book Scanner")
    root.geometry("600x400")

    ttk.Label(root, text="DIY Book Scanner", font=("Helvetica", 24), bootstyle="primary").pack(pady=20)
    ttk.Button(root, text="Capture Settings", command=lambda: capture_settings_window(root), bootstyle="info").pack(pady=10)
    ttk.Button(root, text="Processing Settings", command=lambda: processing_settings_window(root), bootstyle="warning").pack(pady=10)
    ttk.Button(root, text="PDF Settings", command=lambda: pdf_settings_window(root), bootstyle="secondary").pack(pady=10)
    ttk.Button(root, text="Start Workflow", command=lambda: run_workflow(root), bootstyle="success").pack(pady=20)
    ttk.Button(root, text="Exit", command=root.quit, bootstyle="danger").pack(pady=10)

    # Start the Tkinter event loop
    print("GUI initialized")
    root.mainloop()

def run_workflow(root):
    try:
        start_workflow()  # Call the workflow function from main.py
        messagebox.showinfo("Success", "Workflow completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Workflow failed: {e}")

if __name__ == "__main__":
    main_gui()
