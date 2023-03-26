# Algorithms


[Trybe](https://www.betrybe.com/) is a technology school focused on training Web Developers. This project was proposed as an activity to improve studies on Computer Science.

### Description

This project was developed to optimize the complexity of algorithms and solve daily problems using python.

### Technologies and Tools

The project was developed using:
- [Python](https://www.python.org/)
- [pytest](https://docs.pytest.org/en/7.2.x/)

### How to use

To run the project on your machine, start by making a clone of this repository with the following command.

      git clone git@github.com:larissaperinoto/python-algorithms.git
  
Create a virtual environment

      python3 -m venv .venv
    
Activate the virtual environment

      source .venv/bin/activate
    
Install the dependencies in the virtual environment

      python3 -m pip install -r dev-requirements.txt
      
Run the tests using the following command

      python3 -m pytest
      

### Content

This project has some functions to solve daily problems:

<details>

  <summary><strong>challenge_study_schedule</strong></summary>
  
  <br>
  
  `challenges/challenge_study_schedule.py`

You work in a education company and need to know what time there are more students accessing the course. Your system has information about students login and logout times. This function finds how many students are online in a given time when you pass as parameter the `target_time` and a tuples array with the login and logout time.

    
    permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)] # tuples array
    target_time = 3
    # Answer 3

</details>


<details>

  <summary><strong>challenge_palindromes_recursive</strong></summary>
  
  <br>
  
  `challenges/challenge_palindromes_recursive.py`


This function will receive a string as parameter and determine if it is a palindrome

    
    word = "ABCBA"
    # Answer True
    
    word = "ABCD"
    # Answer False

</details>

<details>

  <summary><strong>challenge_anagrams</strong></summary>
  
  <br>
  
  `challenges/challenge_anagrams.py`


An anagram is a play on words where two words have the same characters but different meanings. This function finds anagrams from input of two strings.

    
    first_string = "Amor"
    second_string = "Roma"
    # Answer True
    
    first_string = "Casa"
    second_string = "Mesa"
    # Answer False

</details>

<details>

  <summary><strong>challenge_find_the_duplicate</strong></summary>
  
  <br>
  
  `challenges/challenge_find_the_duplicate.py`


This function finds the duplicate number when receive a numbers array.
    
    nums = [1, 2, 2, 3]
    # Answer 2
    

</details>


---

Developed by [Larissa Perinoto](https://larissaperinoto.com.br/), © 2023.
