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
            "question": " What is used to clean between your teeth?",
            "choices": [
                {"text": "floss", "image_path": r"./images/brush.jpeg", "is_correct": True},
                {"text": "safety pin", "image_path": r"./images/brush.jpeg", "is_correct": False},
                {"text": "toothpick", "image_path": r"./images/brush.jpeg", "is_correct": False},
                {"text": "keys", "image_path": r"./images/brush.jpeg", "is_correct": False}],
        },
        {
        "question": " What should you use to protect your teeth when playing sports?",
        "choices": [
               {"helmet","image_path": r"./images/Helmet.jpg", "is_correct": False},
               {"mouth gaurd","image_path": r"./images/brush.jpeg", "is_correct": True},
               {"bubble gum","image_path": r"./images/brush.jpeg", "is_correct": False}
               {"mask","image_path": r"./images/brush.jpeg", "is_correct": False}],
    },
    {
        "question": "Which picture represents a healthy snack for your teeth?",
        "choices": [
               {"apple","image_path": r"./images/brush.jpeg", "is_correct": False},
               {"sandwich","image_path": r"./images/brush.jpeg", "is_correct": True},
               {"candy","image_path": r"./images/brush.jpeg", "is_correct": False},
               {"gummy bear","image_path": r"./images/brush.jpeg", "is_correct": False}],
      
    },
    {
        "question": "Which picture represents a healthy drink for your teeth?",
        "choices": [
             {"water","image_path": r"./images/brush.jpeg", "is_correct": True}, 
             {"milk", "image_path": r"./images/brush.jpeg", "is_correct": False},
             {"soda", "image_path": r"./images/brush.jpeg", "is_correct": False},
             {"sugary juice","image_path": r"./images/brush.jpeg", "is_correct": False}],
        
    },
      
    {
        "question": "What should you avoid doing with your teeth?",
        "choices": [
            {"brushing","image_path": r"./images/brush.jpeg", "is_correct": False},
            {"flossing","image_path": r"./images/brush.jpeg", "is_correct": False},
            {"mouth rinse","image_path": r"./images/brush.jpeg", "is_correct": False}, 
            {"opening bottle","image_path": r"./images/brush.jpeg", "is_correct":True}],
       
    },
    {
        "question": "What should you do when you first arrive at the dental clinic?",
        "choices": [
            {"Run around and explore","image_path": r"./images/brush.jpeg", "is_correct": False},
            {"Sit quietly and wait for your turn", "image_path": r"./images/brush.jpeg", "is_correct": True},
            {"Yell and make noise","image_path": r"./images/brush.jpeg", "is_correct": False},
            {"None of the above,"image_path": r"./images/brush.jpeg", "is_correct": False"}],
        
    },
    {
        "question": "What might the dentist use to count your teeth during a check-up?",
        "choices": [
            {"Pencil","image_path": r"./images/brush.jpeg", "is_correct": False},
            {"Toothbrush","image_path": r"./images/brush.jpeg", "is_correct": False},
            {"Mirror and a small tool","image_path": r"./images/brush.jpeg", "is_correct": True},
            {"Toy","image_path": r"./images/brush.jpeg", "is_correct": False}],
       
    },
    {
        "question": "How should you behave while sitting in the dental chair?",
        "choices": [
             {"Wiggle and squirm","image_path": r"./images/brush.jpeg", "is_correct": False},
             {"Sit still and listen to the dentist", "image_path": r"./images/brush.jpeg", "is_correct": True},
             {"Jump up and down","image_path": r"./images/brush.jpeg", "is_correct": False},
             {"Shout and walk around","image_path": r"./images/brush.jpeg", "is_correct": False}],
      
    },
    {
        "question": "What can you do to be brave during a dental treatment?",
        "choices": [
            {"Cry loudly","image_path": r"./images/brush.jpeg", "is_correct": False},
            {"Hold the dentist's hand and take deep breaths", "image_path": r"./images/brush.jpeg", "is_correct": True},
            {"Refuse to cooperate","image_path": r"./images/brush.jpeg", "is_correct": False},
            {"Shout when dentist come", "image_path": r"./images/brush.jpeg", "is_correct": False}],
   
    },
    {
        "question": "What is the name of the machine that the dentist might use to take pictures of your teeth?",
        "choices": [
            {"Camera", "image_path": r"./images/brush.jpeg", "is_correct": False},
            {"Microscope","image_path": r"./images/brush.jpeg", "is_correct": False},
            {"X-ray machine","image_path": r"./images/brush.jpeg", "is_correct": True},
            {"Phone""image_path": r"./images/brush.jpeg", "is_correct": False}],
     
    },
    {
        "question": "What can you do if you feel scared at the dental clinic?",
        "choices": [
            {"Scream loudly", "image_path": r"./images/brush.jpeg", "is_correct": False},
            {"Talk to the dentist about your feelings", "image_path": r"./images/brush.jpeg", "is_correct": True},
            {"Hide under the chair","image_path": r"./images/brush.jpeg", "is_correct": False},
            {"None of the above","image_path": r"./images/brush.jpeg", "is_correct": False}],
    
    },
    {
        "question": "What might the dentist use to fix a small hole in your tooth?",
        "choices": [
            {"Glue", "image_path": r"./images/brush.jpeg", "is_correct": False},
            {"Toothpaste","image_path": r"./images/brush.jpeg", "is_correct": False},
            {"Filling","image_path": r"./images/brush.jpeg", "is_correct": True},
            {"Sauce","image_path": r"./images/brush.jpeg", "is_correct": False}],
        
    },
    {
        "question": "What should you do if you accidentally bite the dentist's fingers during a treatment?",
        "choices": [
            {"Laugh loudly","image_path": r"./images/brush.jpeg", "is_correct": False},
            {"Apologize and try not to bite again", "image_path": r"./images/brush.jpeg", "is_correct": True},
            {"Bite again on purpose","image_path": r"./images/brush.jpeg", "is_correct": False},
            {"Ignore it","image_path": r"./images/brush.jpeg", "is_correct": False}],
        
    },
    {
        "question": "Why is it important to be honest with the dentist?",
        "choices": [
             {"To tell funny stories", "image_path": r"./images/brush.jpeg", "is_correct": False},
             {"To keep secrets","image_path": r"./images/brush.jpeg", "is_correct": False},
             {"So the dentist can help you better", "image_path": r"./images/brush.jpeg", "is_correct": True},
             {"None of the above", "image_path": r"./images/brush.jpeg", "is_correct": False}],
     
    },
    {
        "question": "How should you behave in the dental clinic's restroom?",
        "choices": [
            {"Flush the toilet and wash your hands","image_path": r"./images/brush.jpeg", "is_correct": True}, 
            {"Skip washing hands","image_path": r"./images/brush.jpeg", "is_correct": False},
            {"Make a mess","image_path": r"./images/brush.jpeg", "is_correct": False},
            {"Argue with dentist","image_path": r"./images/brush.jpeg", "is_correct": False}],
    
    },
    {
        "question": "How should you brush your teeth before going to the dentist?",
        "choices": [
        { "Quickly and without toothpaste","image_path": r"./images/brush.jpeg", "is_correct": False},
        { " Thoroughly with toothpaste","image_path": r"./images/brush.jpeg", "is_correct": True},
        {"No need to brush your teeth before dental visit", "image_path": r"./images/brush.jpeg", "is_correct": False},
        {"None of the above", "image_path": r"./images/brush.jpeg", "is_correct": False}],
        
    },
    # Add more questions here
]

    root = tk.Tk()
    app = QuizApp(root, quiz_data)
    root.mainloop()
