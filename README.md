# DecodeLabs Project 4: Dynamic General Knowledge Quiz 🚀

This repository contains the final Optional Mastery Phase project for the DecodeLabs Python Programming Industrial Training Kit. 

Unlike a standard linear script, this project is built as a dynamic **Decision Engine** using the **IPOS (Input, Process, Output, Storage)** architecture. It demonstrates the ability to separate business logic from data storage, a critical concept for enterprise-scale applications.

## 🧠 System Architecture

The application is split into two core components:
1. **`Quiz_data.json` (The Data Layer):** Stores the quiz questions, prompts, and answers. This allows the quiz to scale infinitely without altering the core Python logic.
2. **`Quiz.py` (The Logic Layer):** The Python engine that dynamically loads the data, processes user input, and maintains the application state.

### The IPOS Framework in Action:
* **Input (Raw Data):** Captures user keystrokes via the CLI and pulls external data from the JSON file.
* **Process (Business Logic & Sanitization):** 
  * Defends data integrity by applying a sanitization pipeline (`.strip().lower()`) to eliminate whitespace and case-sensitivity bugs.
  * Evaluates sanitized input against the correct answer using precise `if-else` control flow gates.
* **Storage (State Management):** Initializes and maintains a persistent `score` variable to track session memory and evaluate user performance.
* **Output (Feedback):** Utilizes dynamic Python `f-strings` to deliver clean, right-aligned terminal feedback and final grading.

## 🛠️ How to Run

1. Ensure you have Python installed on your machine.
2. Clone this repository.
3. Keep both `Quiz.py` and `Quiz_data.json` in the same directory.
4. Run the script in your terminal:
   ```bash
   python Quiz.py