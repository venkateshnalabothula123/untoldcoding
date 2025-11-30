import tkinter as tk
from tkinter import messagebox, simpledialog

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard Quiz App")
        self.root.geometry("400x300")
        self.root.config(bg="#f7f7f7")
        self.flashcards = [
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "What is 5 + 7?", "answer": "12"},
            {"question": "Who wrote 'Hamlet'?", "answer": "William Shakespeare"}
        ]
        self.current_index = 0
        self.showing_answer = False
        self.card_text = tk.Label(root, text="", wraplength=350, font=("Arial", 14), bg="#f7f7f7")
        self.card_text.pack(pady=40)

        self.show_button = tk.Button(root, text="Show Answer", command=self.toggle_answer)
        self.show_button.pack()

        nav_frame = tk.Frame(root, bg="#f7f7f7")
        nav_frame.pack(pady=10)
        tk.Button(nav_frame, text="Previous", command=self.previous_card).grid(row=0, column=0, padx=10)
        tk.Button(nav_frame, text="Next", command=self.next_card).grid(row=0, column=1, padx=10)

        manage_frame = tk.Frame(root, bg="#f7f7f7")
        manage_frame.pack(pady=10)
        tk.Button(manage_frame, text="Add", command=self.add_card).grid(row=0, column=0, padx=5)
        tk.Button(manage_frame, text="Edit", command=self.edit_card).grid(row=0, column=1, padx=5)
        tk.Button(manage_frame, text="Delete", command=self.delete_card).grid(row=0, column=2, padx=5)

        self.display_card()

    def display_card(self):
        card = self.flashcards[self.current_index]
        if self.showing_answer:
            self.card_text.config(text=card["answer"])
        else:
            self.card_text.config(text=card["question"])

    def toggle_answer(self):
        self.showing_answer = not self.showing_answer
        self.display_card()

    def next_card(self):
        self.current_index = (self.current_index + 1) % len(self.flashcards)
        self.showing_answer = False
        self.display_card()

    def previous_card(self):
        self.current_index = (self.current_index - 1) % len(self.flashcards)
        self.showing_answer = False
        self.display_card()

    def add_card(self):
        question = simpledialog.askstring("Add Card", "Enter question:")
        if question:
            answer = simpledialog.askstring("Add Card", "Enter answer:")
            if answer:
                self.flashcards.append({"question": question, "answer": answer})
                messagebox.showinfo("Success", "Flashcard added!")

    def edit_card(self):
        card = self.flashcards[self.current_index]
        question = simpledialog.askstring("Edit Card", "Edit question:", initialvalue=card["question"])
        if question:
            answer = simpledialog.askstring("Edit Card", "Edit answer:", initialvalue=card["answer"])
            if answer:
                self.flashcards[self.current_index] = {"question": question, "answer": answer}
                messagebox.showinfo("Success", "Flashcard updated!")
                self.display_card()

    def delete_card(self):
        if len(self.flashcards) == 0:
            messagebox.showwarning("Warning", "No flashcards to delete.")
            return
        del self.flashcards[self.current_index]
        if self.flashcards:
            self.current_index %= len(self.flashcards)
            self.display_card()
        else:
            self.card_text.config(text="")
        messagebox.showinfo("Deleted", "Flashcard deleted!")

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
