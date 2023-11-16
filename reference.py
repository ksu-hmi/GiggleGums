import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from PIL import Image


quiz_data = [
    {
        "question": "Which Of these is a toothbrush?",
        "choices": ["cloth", "pencil", "toothbrush", "stick"],
        "answer": "toothbrush"
    },
    {
        "question": " What is used to clean between your teeth?",
        "choices": ["floss", "safety pin", "toothpick", "keys"],
        "answer": "floss"
    },
    {
        "question": " What should you use to protect your teeth when playing sports?",
        "choices": ["helmet", "mouth gaurd", "bubble gum", "mask"],
        "answer": "mouth gaurd"
    },
    {
        "question": "Which picture represents a healthy snack for your teeth?",
        "choices": ["apple", "sandwich", "candy", "gummy bear"],
        "answer": "apple"
    },
    {
        "question": "Which picture represents a healthy drink for your teeth?",
        "choices": ["water", "milk", "soda", "sugary juice"],
        "answer": "water"
    },
    {
        "question": " Which picture shows a tooth with a cavity?",
        "choices": ["yellow tooth", "white tooth", "brown tooth", "golden tooth"],
        "answer": "brown tooth"
    },
    {
        "question": "Which picture shows a toothbrushing technique?",
        "choices": ["up and down", "round and round", "back and forth", "zigzag"],
        "answer": "round and round"
    },
    {
        "question": "Which picture represents a dental check-up?",
        "choices": ["pic1", "pic2", "pic3"],
        "answer": "pic3"
    },
    {
        "question": "What should you avoid doing with your teeth?",
        "choices": ["brushing", "flossing", "mouth rinse", "opening bottle"],
        "answer": "opening bottle"
    },
    {
        "question": "What should you do when you first arrive at the dental clinic?",
        "choices": ["Run around and explore","Sit quietly and wait for your turn","Yell and make noise"],
        "answer": "Sit quietly and wait for your turn"
    },
    {
        "question": "What might the dentist use to count your teeth during a check-up?",
        "choices": ["Pencil", "Toothbrush", "Mirror and a small tool"],
        "answer": "Mirror and a small tool"
    },
    {
        "question": "How should you behave while sitting in the dental chair?",
        "choices": ["Wiggle and squirm", "Sit still and listen to the dentist", "Jump up and down"],
        "answer": "Sit still and listen to the dentist"
    },
    {
        "question": "What can you do to be brave during a dental treatment?",
        "choices": ["Cry loudly", "Hold the dentist's hand and take deep breaths", "Refuse to cooperate"],
        "answer": "Hold the dentist's hand and take deep breaths"
    },
    {
        "question": "What is the name of the machine that the dentist might use to take pictures of your teeth?",
        "choices": ["Camera", "Microscope","X-ray machine"],
        "answer": "X-ray machine"
    },
    {
        "question": "What can you do if you feel scared at the dental clinic?",
        "choices": ["Scream loudly", "Talk to the dentist about your feelings","Hide under the chair"],
        "answer": "Talk to the dentist about your feelings"
    },
    {
        "question": "What might the dentist use to fix a small hole in your tooth?",
        "choices": ["Glue", "Toothpaste","Filling"],
        "answer": "Filling"
    },
    {
        "question": "What should you do if you accidentally bite the dentist's fingers during a treatment?",
        "choices": ["Laugh loudly", "Apologize and try not to bite again"," Bite again on purpose"],
        "answer": "Apologize and try not to bite again"
    },
    {
        "question": "Why is it important to be honest with the dentist?",
        "choices": ["To tell funny stories", "To keep secrets","So the dentist can help you better"],
        "answer": "So the dentist can help you better"
    },
    {
        "question": "How should you behave in the dental clinic's restroom?",
        "choices": ["Flush the toilet and wash your hands", "Skip washing hands","Make a mess"],
        "answer": "Flush the toilet and wash your hands"
    },
    {
        "question": "How should you brush your teeth before going to the dentist?",
        "choices": ["Quickly and without toothpaste", " Thoroughly with toothpaste","No need to brush your teeth before dental visit"],
        "answer": " Thoroughly with toothpaste"
    },
    # Add more questions here
]


# Function to display the current question and choices
def show_question():
    # Get the current question from the quiz_data list
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])

    # Display the choices on the buttons
    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal") # Reset button state

    # Clear the feedback label and disable the next button
    feedback_label.config(text="")
    next_btn.config(state="disabled")

# Function to check the selected answer and provide feedback
def check_answer(choice):
    # Get the current question from the quiz_data list
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    # Check if the selected choice matches the correct answer
    if selected_choice == question["answer"]:
        # Update the score and display it
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text="Correct!", foreground="green")
    else:
        feedback_label.config(text="Incorrect!", foreground="red")
    
    # Disable all choice buttons and enable the next button
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

# Function to move to the next question
def next_question():
    global current_question
    current_question +=1

    if current_question < len(quiz_data):
        # If there are more questions, show the next question
        show_question()
    else:
        # If all questions have been answered, display the final score and end the quiz
        messagebox.showinfo("Quiz Completed",
                            "Quiz Completed! Final score: {}/{}".format(score, len(quiz_data)))
        root.destroy()

# Create the main window
root = tk.Tk()
root.title("Quiz App")
root.geometry("600x500")
style = Style(theme="flatly")

# Configure the font size for the question and choice buttons
style.configure("TLabel", font=("Helvetica", 20))
style.configure("TButton", font=("Helvetica", 16))

# Create the question label
qs_label = ttk.Label(
    root,
    anchor="center",
    wraplength=500,
    padding=10
)
qs_label.pack(pady=10)

# Create the choice buttons
choice_btns = []
for i in range(4):
    button = ttk.Button(
        root,
        command=lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    choice_btns.append(button)

# Create the feedback label
feedback_label = ttk.Label(
    root,
    anchor="center",
    padding=10
)
feedback_label.pack(pady=10)

# Initialize the score
score = 0

# Create the score label
score_label = ttk.Label(
    root,
    text="Score: 0/{}".format(len(quiz_data)),
    anchor="center",
    padding=10
)
score_label.pack(pady=10)

# Create the next button
next_btn = ttk.Button(
    root,
    text="Next",
    command=next_question,
    state="disabled"
)
next_btn.pack(pady=10)

# Initialize the current question index
current_question = 0

# Show the first question
show_question()

# Start the main event loop
root.mainloop()
