import streamlit as st

# Initialize session state variables
if 'current_screen' not in st.session_state:
    st.session_state.current_screen = 'welcome'
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_question_index' not in st.session_state:
    st.session_state.current_question_index = 0
if 'total_score' not in st.session_state:
    st.session_state.total_score = 0
if 'selected_category' not in st.session_state:
    st.session_state.selected_category = None
if 'questions' not in st.session_state:
    st.session_state.questions = []

# Quiz questions data
def load_questions():
    general_knowledge = [
        {
            "question": "What is the capital of France?",
            "options": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
            "answer": "C. Paris"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
            "answer": "B. Mars"
        },
        {
            "question": "How many sides does a hexagon have?",
            "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
            "answer": "B. 6"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
            "answer": "D. Pacific Ocean"
        },
        {
            "question": "Which of these is not a primary color?",
            "options": ["A. Red", "B. Blue", "C. Green", "D. Yellow"],
            "answer": "C. Green"
        }
    ]

    movies_tv = [
        {
            "question": "Who played Iron Man in the Marvel Cinematic Universe?",
            "options": ["A. Chris Evans", "B. Robert Downey Jr.", "C. Chris Hemsworth", "D. Mark Ruffalo"],
            "answer": "B. Robert Downey Jr."
        },
        {
            "question": "Which TV show features a high school chemistry teacher who becomes a drug dealer?",
            "options": ["A. Breaking Bad", "B. The Walking Dead", "C. Game of Thrones", "D. Stranger Things"],
            "answer": "A. Breaking Bad"
        },
        {
            "question": "What was the first film in the Star Wars original trilogy?",
            "options": ["A. The Empire Strikes Back", "B. Return of the Jedi", "C. A New Hope", "D. The Phantom Menace"],
            "answer": "C. A New Hope"
        },
        {
            "question": "Which actress played Katniss Everdeen in The Hunger Games?",
            "options": ["A. Emma Watson", "B. Jennifer Lawrence", "C. Scarlett Johansson", "D. Emma Stone"],
            "answer": "B. Jennifer Lawrence"
        },
        {
            "question": "Which animated movie features a snowman named Olaf?",
            "options": ["A. Toy Story", "B. Shrek", "C. Frozen", "D. Finding Nemo"],
            "answer": "C. Frozen"
        }
    ]

    science_nature = [
        {
            "question": "What is the chemical symbol for gold?",
            "options": ["A. Go", "B. Au", "C. Ag", "D. Gd"],
            "answer": "B. Au"
        },
        {
            "question": "Which animal can change its color to match its surroundings?",
            "options": ["A. Chameleon", "B. Elephant", "C. Giraffe", "D. Penguin"],
            "answer": "A. Chameleon"
        },
        {
            "question": "How many elements are in the periodic table?",
            "options": ["A. 92", "B. 100", "C. 118", "D. 120"],
            "answer": "C. 118"
        },
        {
            "question": "What is the largest organ in the human body?",
            "options": ["A. Brain", "B. Liver", "C. Heart", "D. Skin"],
            "answer": "D. Skin"
        },
        {
            "question": "Which of these is not a type of cloud?",
            "options": ["A. Cumulus", "B. Stratus", "C. Cirrus", "D. Nucleus"],
            "answer": "D. Nucleus"
        }
    ]

    video_games = [
        {
            "question": "Which video game features a character named Mario?",
            "options": ["A. Call of Duty", "B. Super Mario Bros", "C. Minecraft", "D. Fortnite"],
            "answer": "B. Super Mario Bros"
        },
        {
            "question": "What color is the ghost Inky in Pac-Man?",
            "options": ["A. Red", "B. Pink", "C. Blue", "D. Orange"],
            "answer": "C. Blue"
        },
        {
            "question": "Which game features a character named Master Chief?",
            "options": ["A. Halo", "B. God of War", "C. The Last of Us", "D. Uncharted"],
            "answer": "A. Halo"
        },
        {
            "question": "In Minecraft, what material is needed to create a torch?",
            "options": ["A. Wood and Iron", "B. Coal and Stick", "C. Stone and Flint", "D. Gold and Wood"],
            "answer": "B. Coal and Stick"
        },
        {
            "question": "Which of these is not a Pokémon type?",
            "options": ["A. Fire", "B. Water", "C. Earth", "D. Electric"],
            "answer": "C. Earth"
        }
    ]

    return {
        "General Knowledge": general_knowledge,
        "Movies and TV Shows": movies_tv,
        "Science and Nature": science_nature,
        "Video Games": video_games,
        "Random Mix": general_knowledge + movies_tv + science_nature + video_games
    }

# Navigation functions
def go_to_welcome():
    st.session_state.current_screen = 'welcome'

def go_to_category_selection():
    st.session_state.current_screen = 'category_selection'

def go_to_quiz():
    st.session_state.current_screen = 'quiz'
    st.session_state.current_question_index = 0
    st.session_state.score = 0

def select_category(category_name):
    categories = load_questions()
    st.session_state.selected_category = category_name
    st.session_state.questions = categories[category_name]
    go_to_quiz()

def next_question():
    if st.session_state.current_question_index < len(st.session_state.questions) - 1:
        st.session_state.current_question_index += 1
    else:
        st.session_state.current_screen = 'results'
        st.session_state.total_score += st.session_state.score

def check_answer(selected_answer, correct_answer):
    if selected_answer == correct_answer:
        st.session_state.score += 10
        return True
    return False

# Welcome screen
def show_welcome():
    st.title("🎮 Ultimate Quiz Challenge 🎮")
    st.write("Welcome to the Ultimate Quiz Challenge! Test your knowledge in various categories.")
    
    if st.button("Start Quiz", key="start_button"):
        go_to_category_selection()

# Category selection screen
def show_category_selection():
    st.title("Select Quiz Category")
    st.write("Choose a category for your quiz challenge:")
    
    categories = load_questions().keys()
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("General Knowledge", key="cat_gen_knowledge"):
            select_category("General Knowledge")
        
        if st.button("Movies and TV Shows", key="cat_movies"):
            select_category("Movies and TV Shows")
            
        if st.button("Random Mix", key="cat_random"):
            select_category("Random Mix")
            
    with col2:
        if st.button("Science and Nature", key="cat_science"):
            select_category("Science and Nature")
            
        if st.button("Video Games", key="cat_games"):
            select_category("Video Games")

# Quiz screen
def show_quiz():
    q = st.session_state.questions[st.session_state.current_question_index]
    
    st.title(f"Question {st.session_state.current_question_index + 1} of {len(st.session_state.questions)}")
    st.write(f"### {q['question']}")
    
    selected_answer = None
    for option in q['options']:
        if st.button(option, key=f"option_{option}_{st.session_state.current_question_index}"):
            selected_answer = option
            if check_answer(selected_answer, q['answer']):
                st.success("✅ Correct! +10 points")
            else:
                st.error(f"❌ Wrong! The correct answer is {q['answer']}")
            next_question()
            st.experimental_rerun()
    
    st.write(f"Current Score: {st.session_state.score}")

# Results screen
def show_results():
    st.title("Quiz Completed! 🎉")
    st.write(f"### Your score: {st.session_state.score}/{len(st.session_state.questions) * 10}")
    
    if st.button("Play Again", key="play_again"):
        go_to_category_selection()
        
    if st.button("Exit", key="exit"):
        go_to_welcome()
        st.session_state.total_score = 0

# Main app logic
def main():
    if st.session_state.current_screen == 'welcome':
        show_welcome()
    elif st.session_state.current_screen == 'category_selection':
        show_category_selection()
    elif st.session_state.current_screen == 'quiz':
        show_quiz()
    elif st.session_state.current_screen == 'results':
        show_results()

if __name__ == "__main__":
    st.set_page_config(page_title="Quiz Game", page_icon="🎮")
    main()