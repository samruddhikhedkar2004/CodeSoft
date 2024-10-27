import tkinter as tk
import random
import string

class PasswordGenerator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Password Generator")
        self.geometry("400x400")
        self.config(bg="#f0f0f0")

        self.create_widgets()

    def create_widgets(self):
        # Label for instructions
        instruction_label = tk.Label(self, text="Enter the desired password length:", bg="#f0f0f0")
        instruction_label.pack(pady=10)

        # Entry for password length
        self.length_entry = tk.Entry(self, width=5, font=("Arial", 18))
        self.length_entry.pack(pady=10)

        # Generate password button
        generate_button = tk.Button(self, text="Generate Password", command=self.generate_password, bg="#4CAF50", fg="white")
        generate_button.pack(pady=10)

        # Copy to clipboard button
        copy_button = tk.Button(self, text="Copy to Clipboard", command=self.copy_to_clipboard, bg="#008CBA", fg="white")
        copy_button.pack(pady=10)

        # Label to display generated password
        self.result_label = tk.Label(self, text="", font=("Arial", 18), bg="#f0f0f0")
        self.result_label.pack(pady=10)

    def generate_password(self):
        length = self.length_entry.get()

        try:
            length = int(length)
            if length <= 0:
                raise ValueError("Length must be a positive integer.")

            # Define the character set without special symbols
            characters = string.ascii_letters + string.digits
            
            # Generate a random password
            password = ''.join(random.choice(characters) for _ in range(length))
            self.result_label.config(text=f"Generated Password: {password}")
            self.password = password  # Store the generated password for copying
        except ValueError:
            self.result_label.config(text="Please enter a valid length.")

    def copy_to_clipboard(self):
        if hasattr(self, 'password'):
            self.clipboard_clear()  # Clear the clipboard
            self.clipboard_append(self.password)  # Append the password to clipboard
            self.update()  # Update the clipboard contents
            tk.messagebox.showinfo("Success", "Password copied to clipboard!")
        else:
            tk.messagebox.showwarning("Warning", "Generate a password first.")

# Run the password generator application
if __name__ == "__main__":
    app = PasswordGenerator()
    app.mainloop()

