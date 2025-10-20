import requests 
import random
import json

url = "https://opentdb.com/api.php?amount=14"
respone = requests.get(url)
data = respone.json()

questions = data["results"]
letters = ['A', 'B', 'C', 'D']
prizes = [1000, 2000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]

print("🎉 Welcome to Who Wants to Be a Millionaire 🎉\n")
for i, question in enumerate(questions): 
     print(f"Q.{i}: {question['question']}")

     options = question['incorrect_answers'] + [question['correct_answer']]
     random.shuffle(options)
     option_dict = {}
     for j in range(len(options)):
       option_dict[letters[j]] = options[j]

     for ch, opt in option_dict.items():
       print(ch, "-", opt)
     while True:
        answer = input("Enter your option (A/B/C/D): ").upper()
        if answer in letters:
            break
        else:
            print("Invalid input. Please choose A, B, C, or D.")
     if option_dict[answer]==question['correct_answer']:
        print(f"Correct! You won ₹{prizes[i]}")
        print("----------------------------------------")
     else:
        print(f" Wrong! The correct answer was: {question['correct_answer']}")
        print(f"You leave with ₹{prizes[i-1] if i>0 else 0}")
        break
else:
    print(f"🎉 Congratulations! You answered all questions correctly and won ₹{prizes[len(questions)-1]}!")


    