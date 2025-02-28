import random
import streamlit as st

# Simulated puzzle database
puzzles = [
    {"question": "What has keys but can't open locks?", "answer": "Piano"},
    {"question": "What comes once in a minute, twice in a moment, but never in a thousand years?", "answer": "The letter 'M'"},
    {"question": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?", "answer": "An echo"},
    {"question": "What can travel around the world while staying in the corner?", "answer": "A stamp"},
    {"question": "What gets wetter as it dries?", "answer": "A towel"}
]

# Initialize session state to store the current puzzle index
if 'puzzle_index' not in st.session_state:
    st.session_state.puzzle_index = random.randint(0, len(puzzles) - 1)  # Start with a random puzzle

# Select a puzzle based on the current index
selected_puzzle = puzzles[st.session_state.puzzle_index]

# Display a fun "FUN FRIDAY" header with emojis
st.write("## 🎉 FUN FRIDAY Puzzle Challenge! 🎉")
st.write("### Let's have some fun! 👏🎈")
st.write("Here's your puzzle for today 👇:")

# Display the puzzle question
st.write(f"**{selected_puzzle['question']}**")

# Input for players to guess
guess = st.text_input("Your guess: 🧐")

# Check if the guess is correct
if guess:
    if guess.lower() == selected_puzzle['answer'].lower():
        st.success(f"🎊 Correct! 🎉 The answer is **{selected_puzzle['answer']}**. Great job! 💪")
    else:
        st.error(f"😢 Incorrect. The correct answer was **{selected_puzzle['answer']}**. Better luck next time! 🍀")

# Add a button for the next puzzle with a fun emoji
if st.button("Next Puzzle ➡️"):
    # Update session state to point to the next puzzle
    st.session_state.puzzle_index = random.randint(0, len(puzzles) - 1)  # pick a new random puzzle index
    st.rerun()  # Trigger a rerun to load the new puzzle
