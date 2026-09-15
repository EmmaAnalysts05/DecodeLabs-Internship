import json

# State Initialization: Setting up the Score Vault
score = 0

# Load the externalized JSON data
with open('quiz_data.json', 'r') as file:
    quiz_data = json.load(file)

print(f"Welcome to {quiz_data['quiz_name']}!\n")

# Loop through each question in the JSON file dynamically
for q in quiz_data["questions"]:
    # Step 1: Ask & Capture
    raw_answer = input(f"Question {q['id']}: {q['prompt']} ")
    
    # Step 2 & 3: Sanitize and Evaluate
    if raw_answer.strip().lower() == q['answer']:
        print("Correct!\n")
        # Step 4: Execute side effects (Update State)
        score += 1
    else:
        # F-string used to inject the correct answer dynamically
        print(f"Incorrect! The correct answer is {q['answer'].capitalize()}.\n")

# --- Output ---
total_questions = len(quiz_data["questions"])
print(f"Quiz Complete! Your final score is: {score}/{total_questions}")