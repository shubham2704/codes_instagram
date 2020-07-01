print("QUIZ GAME.")
print("Hello, Welcome to this game!")
ans = input("Are you ready to play this game (yes/no):")
print()
score = 0
total_Q = 5

if ans.lower() == "yes":
    print("Q1.which team is the winner of 2019 Cricket World Cup? ")
    print("""
option a. India
option b. Zew Zealand
option c. Sri Lanka
option d. England
    """)
    ans = input()
    if ans == 'd' or ans == 'England':
        score+=1
        print('Correct')
    else:
        print("Incorrect")

    print("Q2.what is the data type of alphabetic data? ")
    print("""
option a. Int
option b. Float
option c. String
option d. Double
    """)
    ans = input()
    if ans == 'c' or ans == 'Double':
        score+=1
        print('Correct')
    else:
        print("Incorrect")

    print("Q3.what is the full form of AI? ")
    print("""
option a. Artificial Intelligence
option b. Automatic Intelligence
option c. Artificial Integritiy
option d. Artificial India
    """)
    ans = input()
    if ans == 'a' or ans == 'Artificial Intelligence':
        score+=1
        print('Correct')
    else:
        print("Incorrect")

    print("Q4.Which one of the following is an application of Stack Data Structure?")
    print("""
option a. Managing function calls
option b. The stock span problem
option c. Arithmetic expression evaluation
option d. All of the Above
    """)
    ans = input()
    if ans == 'd' or ans == 'All of the Above':
        score+=1
        print('Correct')
    else:
        print("Incorrect")
    
    print("Q5.Which of these is not a core data type in Python? ")
    print("""
option a. List 
option b. Tuples
option c. Class
option d. Dictionary
    """)
    ans = input()
    if ans == 'c' or ans == 'Class':
        score+=1
        print('Correct')
    else:
        print("Incorrect")
print()
print(f"Thank you for playing this game. You got {score} question correct.")
mark = (score/total_Q) * 100
print("mark: ", str(mark))
print("Thank you for taking the Quiz")