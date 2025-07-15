# Level Up: Python - Coding Challenges

This repository contains a collection of Python coding challenges that are part of the Level Up: Python course in [LinkedIn Learning][url].  
Each script is self-contained and demonstrates a specific concept or programming technique.

## Overview and Folder Structure

Each challenge has two files:  
    '*1.py' refers in general to my own code, with some small modifications after checking the solution from the course.  
    '*2.py' refers in general to the solution proposed by the instructor, sometimes slightly adapted for my own comprehension.

Below is the general structure with a small description:  

| Challenge | Description                                          | Brief summary of skills learned          |
|-----------|------------------------------------------------------|------------------------------------------|
| 1         | Get prime factors of a number                        | For loops, list methods                  |
| 2         | Check if a word is palindrome                        | String methods                           |
| 3         | Sort words in a phrase                               | Regular expressions, join() method       |
| 4         | Find all the positions of an element in a list       | Recursion                                |
| 5         | Game to guess how many seconds have passed           | Time module, input() function            |
| 6         | Save and load dictionaries to a file                 | Reading and writing files, JSON module   |
| 7         | Schedule another function                            | OS module, multiple arguments function   |
| 8         | Send an e-mail with subject and message              | smtplib module, MIMEText                 |
| 9         | Probabilities of each outcome of a set of dices      | Random module, get() method              |
|10         | Count the words of a text file and rank top 20 words | Expression patterns, list comprehensions |
|11         | Generate Diceware pass phrases                       | Secrets module                           |
|12         | Merge CSV files                                      | csv module, DictWriter() method          |
|13         | Solve a Sudoku                                       | Backtracking, itertools                  |
|14         | Build a ZIP archive                                  | zipfile module, pathlib module           |

```plaintext
levelup-python-challenges/
├── hello.py                        # Simple hello world script
├── get_prime_factors1.py           # Challenge 1
├── get_prime_factors2.py           # Challenge 1
├── is_palindrome1.py               # Challenge 2
├── is_palindrome2.py               # Challenge 2
├── sort_words1.py                  # Challenge 3
├── sort_words2.py                  # Challenge 3
├── index_all1.py                   # Challenge 4
├── index_all2.py                   # Challenge 4
├── waiting_game1.py                # Challenge 5
├── waiting_game2.py                # Challenge 5
├── save_a_dictionary1.py           # Challenge 6
├── save_a_dictionary2.py           # Challenge 6
├── dictionaries/
    ├── PythonDictionary.txt        # Saved from saveadictionary1.py
    └── PythonDictionary.pickle     # Saved from saveadictionary2.py
├── schedule_a_function1.py         # Challenge 7 
├── schedule_a_function2.py         # Challenge 7
├── sounds/
    └── Ring08.wav                  # Sound used in Challenge 7
├── send_an_email1.py               # Challenge 8
├── send_an_email2.py               # Challenge 8
├── simulate_dice1.py               # Challenge 9
├── simulate_dice2.py               # Challenge 9
├── count_unique_words1.py          # Challenge 10
├── count_unique_words2.py          # Challenge 10
├── texts/
    └── pg100.txt                   # Text used in Challenge 10
    └── diceware.wordlist.asc       # Ascii file used in Challenge 11
    └── el_diceware_numbered.txt    # Alternative txt file used in Challenge 11
├── generate_a_password1.py         # Challenge 11
├── generate_a_password2.py         # Challenge 11
├── merge_csv_files1.py             # Challenge 12
├── merge_csv_files2.py             # Challenge 12
├── csv/
    └── class1.csv                  # CSV file created for Challenge 12
    └── class2.csv                  # CSV file created for Challenge 12
    └── all_students.csv            # Output of Challenge 12
├── solve_a_sudoku1.py              # Challenge 13
├── solve_a_sudoku2.py              # Challenge 13
├── build_a_zip_archive1.py          # Challenge 14
├── build_a_zip_archive2.py          # Challenge 14
├── zip/
    └── pics
        └── 480-360-sample.jpg      # JPG file used in Challenge 14
        └── logo.png                # PNG file used in Challenge 14
        └── python-logo-only.svg    # SVG file used in Challenge 14
    └── texts
        └── APPNOTE.TXT             # TXT file used in Challenge 14
├── README.md                       # This file
└── .gitignore                      # Ignored files
```

[url]:https://www.linkedin.com/learning/level-up-python
