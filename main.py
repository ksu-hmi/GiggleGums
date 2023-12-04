import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from PIL import Image, ImageTk


class QuizApp:
    def __init__(self, root, quiz_data):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("800x300")  # Adjust the window size as needed

        self.quiz_data = quiz_data
        self.current_question = 0
        self.score = 0

        self.create_widgets()

    def create_widgets(self):
        self.qs_label = ttk.Label(
            self.root,
            text="Welcome to the Quiz App!",
            font=("Helvetica", 20),
            wraplength=700,
            padding=10
        )
        self.qs_label.pack(pady=10)

        self.choice_btns = []
        for i in range(4):
            button = ttk.Button(
                self.root,
                command=lambda i=i: self.check_answer(i, self.choice_btns),
                text="",
                compound="top"  # To display image above the text
            )
            button.pack(side="left", padx=10)  # Adjust padx as needed
            self.choice_btns.append(button)

        self.feedback_label = ttk.Label(
            self.root,
            text="",
            font=("Helvetica", 16),
            padding=10
        )
        self.feedback_label.pack(pady=10)

        self.score_label = ttk.Label(
            self.root,
            text="Score: 0/{}".format(len(self.quiz_data)),
            font=("Helvetica", 16),
            padding=10
        )
        self.score_label.pack(pady=10)

        self.next_btn = ttk.Button(
            self.root,
            text="Next",
            command=self.next_question,
            state="disabled"
        )
        self.next_btn.pack(pady=10)

        self.show_question()

    def show_question(self):
        question_data = self.quiz_data[self.current_question]
        self.qs_label.config(text=question_data["question"])

        for i in range(4):
            choice_btn = self.choice_btns[i]
            choice_data = question_data["choices"][i]

            # Load and display the image
            image = Image.open(choice_data["image_path"])
            image.thumbnail((100, 100))  # Adjust the size as needed
            photo = ImageTk.PhotoImage(image)
            choice_btn.config(text=choice_data["text"], image=photo)
            choice_btn.photo = photo  # To prevent garbage collection

            # Enable the button
            choice_btn.config(state="normal")

        self.feedback_label.config(text="")
        self.next_btn.config(state="disabled")

    def check_answer(self, choice, buttons):
        question_data = self.quiz_data[self.current_question]
        selected_choice = question_data["choices"][choice]

        if selected_choice["is_correct"]:
            self.score += 1
            self.feedback_label.config(text="Correct!", foreground="green")
        else:
            self.feedback_label.config(text="Incorrect!", foreground="red")

        for btn in buttons:
            btn.config(state="disabled")
        self.next_btn.config(state="normal")
        self.score_label.config(text="Score: {}/{}".format(self.score, len(self.quiz_data)))

    def next_question(self):
        self.current_question += 1

        if self.current_question < len(self.quiz_data):
            self.show_question()
        else:
            messagebox.showinfo("Quiz Completed",
                                "Quiz Completed! Final score: {}/{}".format(self.score, len(self.quiz_data)))
            self.root.destroy()


if __name__ == "__main__":
    quiz_data = [
        {
            "question": "Which of these is used to clean the teeth?",
            "choices": [
                {"text": "Cloth", "image_path": r"./images/Q1 Cloth.jpeg", "is_correct": False},
                {"text": "Finger", "image_path": r"./images/Q1 Finger.jpeg", "is_correct": False},
                {"text": "Pencil", "image_path": r"./images/Q1 Pencil.jpeg", "is_correct": False},
                {"text": "Toothbrush", "image_path": r"./images/Q1 Toothbrush.jpeg", "is_correct": True},
            ],
        },
        {     
            "question": "What is used to clean the area between your teeth?",
            "choices": [
                {"text": "Floss", "image_path": r"./images/Q2 Floss.jpeg", "is_correct": True},
                {"text": "Safety Pin", "image_path": r"./images/Q2 Safety Pin.jpeg", "is_correct": False},
                {"text": "Toothpick", "image_path": r"./images/Q2 Toothpick.jpeg", "is_correct": False},
                {"text": "Keys", "image_path": r"./images/Q2 Keys.jpeg", "is_correct": False},
            ],
        },
        {
            "question": "What should you use to protect your teeth when playing sports?",
            "choices": [
                {"text": "Helmet", "image_path": r"./images/Q3 Helmet.jpeg", "is_correct": False},
                {"text": "Mouth guard", "image_path": r"./Q3 Mouth guard.jpeg", "is_correct": True},
                {"text": "Bubble gum", "image_path": r"./Q3 images/Bubble gum.jpeg", "is_correct": False},
                {"text": "Mask", "image_path": r"./images/Q3 Mask.jpeg", "is_correct": False},
            ],
        },
        {
            "question": "Which picture represents a healthy snack for your teeth?",
            "choices": [
                {"text": "Apple", "image_path": r"./images/Q4 Apple.jpeg", "is_correct": False},
                {"text": "Sandwich", "image_path": r"./images/Q4 Sandwich.jpeg", "is_correct": True},
                {"text": "Candies", "image_path": r"./images/Q4 Candies.jpeg", "is_correct": False},
                {"text": "Gummy bears", "image_path": r"./images/Q4 Gummy bears.jpeg", "is_correct": False},
            ],
        },
        {
            "question": "Which picture represents a healthy drink for your teeth?",
            "choices": [
                {"text": "Water", "image_path": r"./images/Q5 Water.jpeg", "is_correct": True},
                {"text": "Milk", "image_path": r"./images/Q5 Milk.jpeg", "is_correct": False},
                {"text": "Soda", "image_path": r"./images/Q5 Soda.jpeg", "is_correct": False},
                {"text": "Sugary Juice", "image_path": r"./Q5 images/Sugary Juice.jpeg", "is_correct": False},
            ],
        },
        {
            "question": "Which picture shows a tooth with a cavity?",
            "choices": [
                {"text": "Yellow Tooth", "image_path": r"./images/Q6 Yellow Tooth.jpeg", "is_correct": False},
                {"text": "White Tooth", "image_path": r"./images/Q6 White Tooth.jpeg", "is_correct": False},
                {"text": "Brown Tooth", "image_path": r"./images/Q6 Brown Tooth.jpeg", "is_correct": True},
                {"text": "Broken Tooth", "image_path": r"./images/Q6 Broken Tooth.jpeg", "is_correct": False},
            ],
        },
        {
            "question": "Which picture shows a toothbrushing technique?",
            "choices": [
                {"text": "Up and Down", "image_path": r"./images/Q7 up and down.jpeg", "is_correct": False},
                {"text": "Round and Round", "image_path": r"./images/Q7 round and round.jpeg", "is_correct": False},
                {"text": "Back and Forth", "image_path": r"./images/Q7 back and forth.jpeg", "is_correct": False},
                {"text": "Combination of all", "image_path": r"./images/Q7 Combination of all.jpeg", "is_correct": True},
            ],
        },
        {
            "question": "Which picture represents a dental check-up?",
            "choices": [
                {"text": "Pic1", "image_path": r"./images/Q8 Pic1.jpeg", "is_correct": False},
                {"text": "Pic2", "image_path": r"./images/Q8 Pic2.jpeg", "is_correct": False},
                {"text": "Pic3", "image_path": r"./images/Q8 Pic3.jpeg", "is_correct": True},
                {"text": "Pic4", "image_path": r"./images/Q8 Pic4.jpeg", "is_correct": False},
            ],
        },
        {
            "question": "What should you avoid doing with your teeth?",
            "choices": [
                {"text": "Brushing", "image_path": r"./images/Q9 brushing.jpeg", "is_correct": False},
                {"text": "Flossing", "image_path": r"./images/Q9 flossing.jpeg", "is_correct": False},
                {"text": "Mouth rinse", "image_path": r"./images/Q9 mouth rinse.jpeg", "is_correct": False},
                {"text": "Opening Bottle", "image_path": r"./images/Q9 opening bottle.jpeg", "is_correct": True},
            ],
        },
        {
            "question": "What should you do when you first arrive at the dental clinic?",
            "choices": [
                {"text": "Run around and explore", "image_path": r"./images/Q10 run around and explore.jpeg", "is_correct": False},
                {"text": "Sit quietly and wait for your turn", "image_path": r"./images/Q10 sit quietly and wait for your turn.jpeg", "is_correct": True},
                {"text": "Yell and make noise", "image_path": r"./images/Q10 yell and make noise.jpeg", "is_correct": False},
                {"text": "Cry", "image_path": r"./images/Q10 cry.jpeg", "is_correct": False},
            ],
        },
        {
            "question": "What might a Dentist use to count your teeth during a Check-up?",
            "choices": [
                {"text": "Pencil", "image_path": r"./images/Q11-Pencil.jpeg", "is_correct": False},
                {"text": "Toothbrush", "image_path": r"./Q11-Toothbrush.jpeg", "is_correct": False},
                {"text": "Mirror and a small tool", "image_path": r"./images/Q11-Dental-mirror-and-tool.jpeg", "is_correct": True},
                {"text": "Toothbrush", "image_path": r"./Q11-Toothbrush.jpeg", "is_correct": False},
            ],
        },
        {
            "question": "How should you behave while sitting in the dental chair?",
            "choices": [
                {"text": "Wiggle and squirm", "image_path": r"./images/Q12 wiggle and squirm.jpeg", "is_correct": False},
                {"text": "Sit still and listen to the dentist", "image_path": r"./images/Q12 sit still.jpeg", "is_correct": True},
                {"text": "Jump up and down", "image_path": r"./images/Q12 Jump up and down.jpeg", "is_correct": False},
                {"text": "Cry loudly", "image_path": r"./images/Q12 cry loudly.jpeg", "is_correct": False},
            ],
        },
        {
            "question": "What can you do to be brave during a dental treatment?",
            "choices": [
                {"text": "Cry loudly", "image_path": r"./images/Q13 Cry loudly.jpeg", "is_correct": False},
                {"text": "Hold the dentist's hand and take deep breaths", "image_path": r"./images/Q13 Hold dentist hand.jpeg", "is_correct": True},
                {"text": "Refuse to cooperate", "image_path": r"./images/Q13 Refuse to cooperate.jpeg", "is_correct": False},
                {"text": "Hide under the table", "image_path": r"./images/Q13 Hide under table.jpeg", "is_correct": False},
            ],
        },
        {
            "question": "What is the name of the machine that the dentist might use to take pictures of your teeth?",
            "choices": [
                {"text": "Camera", "image_path": r"./images/Q14 camera.jpeg", "is_correct": False},
                {"text": "Microscope", "image_path": r"./images/Q14 Microscope.jpeg", "is_correct": False},
                {"text": "X-ray machine", "image_path": r"./images/Q14 Xray machine.jpeg", "is_correct": True},
                {"text": "Phone", "image_path": r"./images/Q14 phone.jpeg", "is_correct": False},
            ],
        },
        {
            "question": "What can you do if you feel scared at the dental clinic?",
            "choices": [
                {"text": "Scream loudly", "image_path": r"./images/Q15 Scream loudly.jpeg", "is_correct": False},
                {"text": "Talk to the dentist about your feelings", "image_path": r"./images/Q15 Talk to dentist.jpeg", "is_correct": True},
                {"text": "Hide under the chair", "image_path": r"./images/Q15 Hiding under chair.jpeg", "is_correct": False},
                {"text": "Bite dentist hand", "image_path": r"./images/Q15 Bite dentist hand.jpeg", "is_correct": False},
            ],
        },
        {
            "question": "What might the dentist use to fix a small hole in your tooth?",
            "choices": [
                {"text": "Glue", "image_path": r"./images/Q16 Glue.jpeg", "is_correct": False},
                {"text": "Toothpaste", "image_path": r"./images/Q16 Toothpaste.jpeg", "is_correct": False},
                {"text": "Filling", "image_path": r"./images/Q16 Filling.jpeg", "is_correct": True},
                {"text": "Bubble gum", "image_path": r"./images/Q16 Bubble gum.jpeg", "is_correct": False},
            ],
        },
        {
            "question": "What should you do if you accidentally bite the dentist's fingers during a treatment?",
            "choices": [
                {"text": "Laugh loudly", "image_path": r"./images/Q17 Laugh loudly.jpeg", "is_correct": False},
                {"text": "Apologize and try not to bite again", "image_path": r"./images/Q17 Apologize.jpeg", "is_correct": True},
                {"text": "Bite again on purpose", "image_path": r"./images/Q17 Bite on purpose.jpeg", "is_correct": False},
                {"text": "Cry loudly", "image_path": r"./images/Q17 Cry loudly .jpeg", "is_correct": False},
            ],
        },
        {
            "question": "Why is it important to be honest with the dentist?",
            "choices": [
                {"text":"To tell funny stories","image_path": r"./images/Q18-Funny-stories.jpeg", "is_correct": False},
                {"text":"To keep secrets","image_path": r"./Q18-Keep-secret.jpeg", "is_correct": False},
                {"text":"So the dentist can help you better","image_path": r"./images/Q18 Dentist helping.jpeg", "is_correct": True},
                {"text":"Avoid Punishment","image_path": r"./images/Q18-Avoid punishment.jpeg", "is_correct": False}
            ],
      
       },
       {
            "question": "How should you behave in the dental clinic's restroom?",
            "choices": [
                {"text":"Flush the toilet and wash your hands", "image_path": r"./Q19-Flush-and-wash-hands.jpeg", "is_correct": True},
                {"text":"Skip washing hands","image_path": r"./Q19-Skip-washing-hands.jpeg", "is_correct": False},
                {"text":"Make a mess","image_path": r"./Q19-Make-mess.jpeg", "is_correct": False},
                {"text":"Spill soap","image_path": r"./Q19-Spill saop.jpeg", "is_correct": False}
            ],
       
       },
       {
            "question": "How should you brush your teeth before going to the dentist?",
            "choices": [
                {"text":"Quickly and without toothpaste","image_path": r"./images/Q20-Without-toothpaste.jpeg", "is_correct": False},
                {"text":" Thoroughly with toothpaste","image_path": r"./images/Q20-Thoroughly-with-toothpaste.jpeg", "is_correct": True},
                {"text":"No need to brush your teeth before dental visit","image_path": r"./images/Q20-No-brushing-teeth.jpeg", "is_correct": False},
                {"text":"Just use Mouthwash","image_path": r"./Q20-Mouthwash.jpeg", "is_correct": False}
            ],
        
       },
    # Add more questions here
]

    root = tk.Tk()
    app = QuizApp(root, quiz_data)
    root.mainloop()
