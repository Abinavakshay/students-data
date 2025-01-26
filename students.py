import pandas as pd
import json

# Current Quiz Data
current_quiz_data = [
    {
        "quiz_id": 101,
        "user_id": 1,
        "question_id": 1,
        "topic": "Mathematics",
        "difficulty_level": "Medium",
        "selected_option_id": 2,
        "correct_option_id": 2,
        "is_correct": True
    },
    {
        "quiz_id": 101,
        "user_id": 1,
        "question_id": 2,
        "topic": "Science",
        "difficulty_level": "Hard",
        "selected_option_id": 3,
        "correct_option_id": 1,
        "is_correct": False
    },
    {
        "quiz_id": 101,
        "user_id": 1,
        "question_id": 3,
        "topic": "History",
        "difficulty_level": "Easy",
        "selected_option_id": 4,
        "correct_option_id": 4,
        "is_correct": True
    }
]

# Historical Quiz Data
historical_quiz_data = [
    {
        "quiz_id": 95,
        "user_id": 1,
        "question_id": 1,
        "topic": "Mathematics",
        "difficulty_level": "Medium",
        "selected_option_id": 3,
        "correct_option_id": 2,
        "is_correct": False
    },
    {
        "quiz_id": 96,
        "user_id": 1,
        "question_id": 2,
        "topic": "Science",
        "difficulty_level": "Hard",
        "selected_option_id": 1,
        "correct_option_id": 1,
        "is_correct": True
    },
    {
        "quiz_id": 97,
        "user_id": 1,
        "question_id": 3,
        "topic": "History",
        "difficulty_level": "Easy",
        "selected_option_id": 4,
        "correct_option_id": 3,
        "is_correct": False
    },
    {
        "quiz_id": 98,
        "user_id": 1,
        "question_id": 4,
        "topic": "Geography",
        "difficulty_level": "Medium",
        "selected_option_id": 2,
        "correct_option_id": 2,
        "is_correct": True
    }
]

# Combine current and historical quiz data into a DataFrame
combined_data = current_quiz_data + historical_quiz_data
combined_df = pd.DataFrame(combined_data)

# Define the student_persona function
def student_persona(df):
    # Example implementation: Calculate the number of correct answers and topics
    total_questions = len(df)
    correct_answers = df['is_correct'].sum()
    topics = df['topic'].unique()
    
    return {
        "total_questions": total_questions,
        "correct_answers": correct_answers,
        "topics": topics.tolist()
    }

# Call the function and print the result
print(student_persona(combined_df))
