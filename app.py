import random
import streamlit as st
import time

# Simulated puzzle database with 15 puzzles for Game 1
puzzles = [
    {"question": "What has keys but can't open locks?", "answer": "Piano"},
    {"question": "What comes once in a minute, twice in a moment, but never in a thousand years?", "answer": "The letter 'M'"},
    {"question": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?", "answer": "An echo"},
    {"question": "What can travel around the world while staying in the corner?", "answer": "A stamp"},
    {"question": "What gets wetter as it dries?", "answer": "A towel"},
    {"question": "What has a heart that doesn’t beat?", "answer": "An artichoke"},
    {"question": "I’m tall when I’m young, and I’m short when I’m old. What am I?", "answer": "A candle"},
    {"question": "What has one head, one foot, and four legs?", "answer": "A bed"},
    {"question": "What can be broken but never held?", "answer": "A promise"},
    {"question": "The more of this there is, the less you see. What is it?", "answer": "Darkness"},
    {"question": "What is full of holes but still holds a lot of weight?", "answer": "A net"},
    {"question": "What comes down but never goes up?", "answer": "Rain"},
    {"question": "What is always in front of you but can’t be seen?", "answer": "The future"},
    {"question": "What has many keys but can’t open a single lock?", "answer": "A piano"},
    {"question": "What is light as a feather, yet the strongest man can’t hold it for much longer?", "answer": "Breath"}
]

# Initialize session state to store the current puzzle index for Game 1
if 'puzzle_index' not in st.session_state:
    st.session_state.puzzle_index = random.randint(0, len(puzzles) - 1)  # Start with a random puzzle

# Select a puzzle based on the current index for Game 1
selected_puzzle = puzzles[st.session_state.puzzle_index]

# Display a fun "FUN FRIDAY" header with emojis for Game 1
st.write("## 🎉 FUN FRIDAY Virtual Party! 🎉")
st.write("### Let's have some fun! 👏🎈")

# Display Puzzle Game Section (Game 1)
st.write("### Puzzle Challenge 👇:")

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

# Add a button for the next puzzle with a fun emoji (for Game 1)
if st.button("Next Puzzle ➡️"):
    # Update session state to point to the next puzzle
    st.session_state.puzzle_index = random.randint(0, len(puzzles) - 1)  # pick a new random puzzle index
    st.rerun()  # Trigger a rerun to load the new puzzle


# Updated Bollywood Dialogues and Movie Mapping for the second game (Game 2)
dialogues = [
    {"dialogue": "Tumse na ho payega", "movie": "Gully Boy"},
    {"dialogue": "Babu Moshai Zindagi Badi Haseen Hai, jeene ke liye khush rehna zaroori hai", "movie": "Anand"},
    {"dialogue": "Rishtey mein toh hum tumhare baap lagte hain", "movie": "Sultan"},
    {"dialogue": "Kabhi kabhi lagta hai apun hi bhagwan hai", "movie": "Sholay"},
    {"dialogue": "Agar tum sach kehte ho, toh sach ke saath raho", "movie": "Tumbbad"},
    {"dialogue": "Jab tak hai jaan, tab tak hai jaan", "movie": "Jab Tak Hai Jaan"},
    {"dialogue": "Aaj khush toh bahut honge tum", "movie": "Dilwale Dulhania Le Jayenge"},
    {"dialogue": "Main apni favourite hoon", "movie": "Jab We Met"},
    {"dialogue": "I don't believe in love. I believe in something better", "movie": "Love Aaj Kal"},
    {"dialogue": "Aap purush nahi, mahapurush hain", "movie": "Andheri Raat Mein Diya Tera Hi Jala"},
    {"dialogue": "Humein tumse kuch aur nahin chahiye, bas tumhara saath", "movie": "Dil Se"},
    {"dialogue": "Itni shiddat se maine tumhe chaha hai, ki har zarrre ne mujhe tumse milane ki saazish ki hai", "movie": "Om Shanti Om"},
    {"dialogue": "Kahani me twist hai", "movie": "Tanu Weds Manu"},
    {"dialogue": "Dil chahta hai kuch alag karna", "movie": "Dil Chahta Hai"},
    {"dialogue": "Zindagi badi ajib hai, ek baar fursat mil jaaye toh apne aapko dhundhne chalo", "movie": "Zindagi Na Milegi Dobara"}
]

# Initialize session state for player scores in Bollywood guessing game (Game 2)
# Replace the player names with your list of players
if 'player_scores' not in st.session_state:
    st.session_state.player_scores = {
        "Alima": 0,
        "Haroon": 0,
        "Manvi": 0,
        "Nikesh": 0,
        "Harron": 0,
        "Rajshree": 0,
        "Ratima": 0,
        "Ritika": 0,
        "Saptha Shree": 0,
        "Sweta": 0,
        "Vandana": 0,
        "Lavanya S": 0
    }  # Updated players list

# Function to display the Bollywood guessing game (Game 2)
def display_bollywood_guess_game():
    # Add a dropdown to select the player
    player_name = st.selectbox("Select your player name:", list(st.session_state.player_scores.keys()))

    # Select a random Bollywood dialogue
    puzzle = random.choice(dialogues)

    # Start the timer
    start_time = time.time()

    # Display the dialogue clue
    st.write("**Clue:** 🎬")
    st.write(f"**{puzzle['dialogue']}**")

    # Input for the player to guess the movie
    guess = st.text_input(f"Which movie is this dialogue from? Enter the movie name:", key=f"guess_bollywood")

    # Check if the guess is correct and calculate time taken
    if guess:
        time_taken = time.time() - start_time
        if guess.lower() == puzzle['movie'].lower():
            st.success(f"🎊 Correct! The movie is **{puzzle['movie']}**. You took {int(time_taken)} seconds! 🎉")
            # Add points based on time taken
            score = max(10 - int(time_taken), 1)  # Higher points for faster answers
            st.session_state.player_scores[player_name] += score
        else:
            st.error(f"😢 Incorrect. The correct answer was **{puzzle['movie']}**.")

    # Show leaderboard
    if st.button("Show Leaderboard 🏅"):
        sorted_scores = sorted(st.session_state.player_scores.items(), key=lambda x: x[1], reverse=True)
        st.write("## 🏆 Leaderboard 🏆")
        for rank, (player, score) in enumerate(sorted_scores, 1):
            st.write(f"{rank}. {player} - {score} points")

# Display the Bollywood guessing game with fun emoji (Game 2)
st.write("### Bollywood Movie Guessing Game 🎬🍿")
display_bollywood_guess_game()

# Option to restart the game (Game 2)
if st.button("Play Again ➡️"):
    st.session_state.player_scores = {
        "Alima": 0,
        "Haroon": 0,
        "Manvi": 0,
        "Nikesh": 0,
        "Harron": 0,
        "Rajshree": 0,
        "Ratima": 0,
        "Ritika": 0,
        "Saptha Shree": 0,
        "Sweta": 0,
        "Vandana": 0,
        "Lavanya S": 0
    }  # Reset all scores with updated player list
    st.experimental_rerun()  # Reset the app for a new game


# Game 3: Zoom Masked Singer 🎤🎶

# Initialize session state for Zoom Masked Singer votes and guesses (Game 3)
if 'votes' not in st.session_state:
    st.session_state.votes = {}
    st.session_state.singer_guess = {}

# Players (masked aliases)
masked_singers = [f"Masked Singer {i+1}" for i in range(5)]

# Function to simulate Zoom Masked Singer Game (Game 3)
def zoom_masked_singer_game():
    st.write("### Zoom Masked Singer 🎤🎶")

    # Select player alias
    player_name = st.selectbox("Select your alias (masked name):", masked_singers)

    # Step 1: Singing performance (simulated)
    st.write(f"🎤 **{player_name}** is now singing! 🎶")
    st.write("Since this is a virtual game, let's pretend the singing happened. ✨")

    # Step 2: Voting for favorite singer
    st.write("### Voting Time! 🗳️")
    if player_name not in st.session_state.votes:
        st.session_state.votes[player_name] = None

    # Let players vote for their favorite singer
    vote = st.selectbox("Vote for your favorite singer:", masked_singers)
    if vote != player_name and st.session_state.votes[player_name] is None:
        st.session_state.votes[player_name] = vote
        st.write(f"🎉 You voted for **{vote}**!")
    
    # Step 3: Guessing who is behind the masks
    if len(st.session_state.votes) == len(masked_singers):
        st.write("### Time to Guess! 🤔")
        
        guessed_singer = st.selectbox("Who do you think is behind the mask of each player?", masked_singers)
        if guessed_singer != player_name and player_name not in st.session_state.singer_guess:
            st.session_state.singer_guess[player_name] = guessed_singer
            st.write(f"🔮 You guessed that **{guessed_singer}** is behind the mask of {player_name}.")

        # Show results after all players have voted and guessed
        if len(st.session_state.singer_guess) == len(masked_singers):
            st.write("### Results! 🎉")
            for name, guessed in st.session_state.singer_guess.items():
                st.write(f"{name} guessed that **{guessed}** was behind their mask!")

# Trigger the Zoom Masked Singer Game (Game 3)
zoom_masked_singer_game()

# Option to restart the Zoom Masked Singer Game (Game 3)
if st.button("Play Again ➡️ Zoom Masked Singer"):
    st.session_state.votes = {}
    st.session_state.singer_guess = {}
    st
