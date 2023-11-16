import tkinter as tk
from PIL import Image, ImageTk

class QuizApp:
    def __init__(self, root, quiz_data):
        self.root = root
        self.quiz_data = quiz_data
        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(root, text="")
        self.question_label.pack()

        self.choices_frame = tk.Frame(root)
        self.choices_frame.pack()

        self.feedback_label = tk.Label(root, text="")
        self.feedback_label.pack()

        self.load_question()

    def load_question(self):
        if self.current_question < len(self.quiz_data):
            question_data = self.quiz_data[self.current_question]
            question_text = question_data["question"]
            choices = question_data["choices"]

            self.question_label.config(text=question_text)

            self.choice_buttons = []
            for i, choice in enumerate(choices):
                image_path = f"{choice}.png"  # Assuming you have images named after choices
                image = Image.open(image_path)
                image = image.resize((50, 50), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(image)

                button = tk.Button(self.choices_frame, text=choice, image=photo, compound=tk.LEFT,
                                   command=lambda c=choice: self.check_answer(c))
                button.image = photo
                button.grid(row=i, column=0, padx=10, pady=5, sticky="w")
                self.choice_buttons.append(button)
        else:
            self.show_result()

    def check_answer(self, selected_choice):
        correct_answer = self.quiz_data[self.current_question]["answer"]
        if selected_choice == correct_answer:
            self.score += 1
            feedback = "Correct!"
        else:
            feedback = "Incorrect. The correct answer is: {}".format(correct_answer)

        self.feedback_label.config(text=feedback)
        self.current_question += 1

        for button in self.choice_buttons:
            button.destroy()

        self.load_question()

    def show_result(self):
        result_text = "Quiz completed!\nYour score: {}/{}".format(self.score, len(self.quiz_data))
        result_label = tk.Label(self.root, text=result_text, font=("Helvetica", 16))
        result_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quiz App")

    app = QuizApp(root, quiz_data)

    root.mainloop()
