# students-data
# Quiz Data Analysis

This project analyzes quiz data, combining current and historical quiz results to provide insights into a student's performance. The analysis includes calculating the total number of questions answered, the number of correct answers, and the unique topics covered.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Data Structure](#data-structure)
- [Functionality](#functionality)
- [License](#license)

## Installation

To run this project, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Required Libraries

This project uses the following Python libraries:

- `pandas`

You can install the required libraries using pip:

```bash
pip install pandas
Usage:
python quiz_analysis.py
Data Structure:
current data:
[
    {
        "quiz_id": 101,
        "user_id": 1,
        "question_id": 1,
        "topic": "Mathematics",
        "difficulty_level": "Medium",
        "selected_option_id": 2,
        "correct_option_id": 2,
        "is_correct": true
    },
    ...
]
Historic Data:
[
    {
        "quiz_id": 95,
        "user_id": 1,
        "question_id": 1,
        "topic": "Mathematics",
        "difficulty_level": "Medium",
        "selected_option_id": 3,
        "correct_option_id": 2,
        "is_correct": false
    },
    ...
]
Example output:

{'total_questions': 7, 'correct_answers': np.int64(4), 'topics': ['Mathematics', 'Science', 'History', 'Geography']}

Liscence:

### Instructions for Use:
1. **Save the README:** Create a file named `README.md` in your project directory and copy the above content into it.
2. **Customize as Needed:** Feel free to modify any sections to better fit your project, such as adding more details about the analysis or changing the example output.
3. **Add a License:** If you plan to share your project publicly, consider adding a license file to clarify how others can use your code.
