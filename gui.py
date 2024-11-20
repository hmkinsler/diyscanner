import tkinter as tk
from tkinter import filedialog, messagebox
import threading
from main import main  # Import your main workflow function

class BookScannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DIY Book Scanner")

        # Directories
        self.capture_dir = tk.StringVar()
        self.process_dir = tk.StringVar()
        self.output_dir = tk.StringVar()

        # Buttons and inputs
        self.create_widgets()

    def create_widgets(self):
        # Directory selection
        tk.Label(self.root, text="Capture Directory").grid(row=0, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.capture_dir, width=40).grid(row=0, column=1)
        tk.Button(self.root, text="Browse", command=self.browse_capture).grid(row=0, column=2)

        tk.Label(self.root, text="Process Directory").grid(row=1, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.process_dir, width=40).grid(row=1, column=1)
        tk.Button(self.root, text="Browse", command=self.browse_process).grid(row=1, column=2)

        tk.Label(self.root, text="Output Directory").grid(row=2, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.output_dir, width=40).grid(row=2, column=1)
        tk.Button(self.root, text="Browse", command=self.browse_output).grid(row=2, column=2)

        # Start/Stop Buttons
        self.start_button = tk.Button(self.root, text="Start Workflow", command=self.start_workflow)
        self.start_button.grid(row=3, column=1, pady=10)

        self.log_text = tk.Text(self.root, height=10, width=50, state="disabled")
        self.log_text.grid(row=4, column=0, columnspan=3, pady=10)

    def browse_capture(self):
        folder = filedialog.askdirectory()
        if folder:
            self.capture_dir.set(folder)

    def browse_process(self):
        folder = filedialog.askdirectory()
        if folder:
            self.process_dir.set(folder)

    def browse_output(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_dir.set(folder)

    def log_message(self, message):
        self.log_text.config(state="normal")
        self.log_text.insert("end", message + "\n")
        self.log_text.config(state="disabled")
        self.log_text.see("end")

    def start_workflow(self):
        # Run workflow in a separate thread to keep GUI responsive
        self.log_message("Starting workflow...")
        workflow_thread = threading.Thread(target=self.run_workflow)
        workflow_thread.start()

    def run_workflow(self):
        try:
            main()  # Call your workflow function
            self.log_message("Workflow completed successfully!")
        except Exception as e:
            self.log_message(f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BookScannerApp(root)
    root.mainloop()
