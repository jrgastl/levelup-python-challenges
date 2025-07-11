# Level Up: Python - Coding Exercises

This repository contains a collection of Python coding exercises that are part of the Level Up: Python course in [LinkedIn Learning][url].  
Each script is self-contained and demonstrates a specific concept or programming technique.

## Overview and Folder Structure

Each exercise has two files:  
    '*1.py' refers in general to my own code, with some small modifications after checking the solution from the course.  
    '*2.py' refers in general to the solution proposed by the instructor, sometime slightly adapted for my own comprehension.

Below is the general structure with a small description:  

| Exercise | Description                                          | Brief summary of skills learned          |
|----------|------------------------------------------------------|------------------------------------------|
| 1        | Get prime factors of a number                        | For loops, list methods                  |
| 2        | Check if a word is palindrome                        | String methods                           |
| 3        | Sort words in a phrase                               | Regular expressions, join() method       |
| 4        | Find all the positions of an element in a list       | Recursion                                |
| 5        | Game to guess how many seconds have passed           | Time module, input() function            |
| 6        | Save and load dictionaries to a file                 | Reading and writing files, JSON module   |
| 7        | Schedule another function                            | OS module, multiple arguments function   |
| 8        | Send an e-mail with subject and message              | smtplib module, MIMEText                 |
| 9        | Probabilities of each outcome of a set of dices      | Random module, get() method              |
|10        | Count the words of a text file and rank top 20 words | Expression patterns, list comprehensions |
|11        | Generate Diceware pass phrases                       | Secrets module                           |
|12        | Merge CSV files                                      | csv module, DictWriter() method          |
|13        | Solve a Sudoku                                       | Backtracking, itertools                  |

```plaintext
levelup-python-exercises/
├── hello.py                        # Simple hello world script
├── get_prime_factors1.py           # Exercise 1
├── get_prime_factors2.py           # Exercise 1
├── is_palindrome1.py               # Exercise 2
├── is_palindrome2.py               # Exercise 2
├── sort_words1.py                  # Exercise 3
├── sort_words2.py                  # Exercise 3
├── index_all1.py                   # Exercise 4
├── index_all2.py                   # Exercise 4
├── waiting_game1.py                # Exercise 5
├── waiting_game2.py                # Exercise 5
├── save_a_dictionary1.py           # Exercise 6
├── save_a_dictionary2.py           # Exercise 6
├── dictionaries/
    ├── PythonDictionary.txt        # Saved from saveadictionary1.py
    └── PythonDictionary.pickle     # Saved from saveadictionary2.py
├── schedule_a_function1.py         # Exercise 7 
├── schedule_a_function2.py         # Exercise 7
├── sounds/
    └── Ring08.wav                  # Sound used in Exercise 7
├── send_an_email1.py               # Exercise 8
├── send_an_email2.py               # Exercise 8
├── simulate_dice1.py               # Exercise 9
├── simulate_dice2.py               # Exercise 9
├── count_unique_words1.py          # Exercise 10
├── count_unique_words2.py          # Exercise 10
├── texts/
    └── pg100.txt                   # Text used in exercise 10
    └── diceware.wordlist.asc       # Ascii file used in exercise 11
    └── el_diceware_numbered.txt    # Alternative txt file used in exercise 11
├── generate_a_password1.py         # Exercise 11
├── generate_a_password2.py         # Exercise 11
├── merge_csv_files1.py             # Exercise 12
├── merge_csv_files2.py             # Exercise 12
├── csv/
    └── class1.csv                  # CSV file created for exercise 12
    └── class2.csv                  # CSV file created for exercise 12
    └── all_students.csv            # Output of exercise 121
├── solve_a_sudoku1.py              # Exercise 13
├── solve_a_sudoku2.py              # Exercise 13
├── README.md                       # This file
└── .gitignore                      # Ignored files
```

[url]:https://www.linkedin.com/learning/level-up-python
