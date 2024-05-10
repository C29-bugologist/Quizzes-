def quiz_game():
    questions = [
        "What is the capital of France? \n(1) London \n(2) Paris \n(3) Rome \n",
        "What is the largest planet in our solar system? \n(1) Earth \n(2) Jupiter \n(3) Mars \n",
        "Who wrote 'Romeo and Juliet'? \n(1) William Shakespeare \n(2) Charles Dickens \n(3) Jane Austen \n",
        "What is the chemical symbol for water? \n(1) W \n(2) Wa \n(3) H2O \n",
        "Which year did the Titanic sink? \n(1) 1912 \n(2) 1908 \n(3) 1915 \n",
        "What is the capital of Japan? \n(1) Tokyo \n(2) Beijing \n(3) Seoul \n",
        "Who painted the Mona Lisa? \n(1) Vincent van Gogh \n(2) Leonardo da Vinci \n(3) Pablo Picasso \n",
        "What is the powerhouse of the cell? \n(1) Nucleus \n(2) Mitochondria \n(3) Ribosome \n",
        "What is the tallest mountain in the world? \n(1) Mount Everest \n(2) K2 \n(3) Mount Kilimanjaro \n",
        "Which planet is known as the Red Planet? \n(2) Jupiter \n(2) Venus \n(3) Mars \n"
    ]

    answers = [2, 2, 1, 3, 1, 1, 2, 2, 1, 3]
    score = 0

    print("Welcome to the Quiz Game!")
    print("-------------------------")
    for i in range(len(questions)):
        print("Question", i + 1)
        print(questions[i])
        user_answer = int(input("Enter your answer (1, 2, or 3): "))
        
        if user_answer == answers[i]:
            print("Correct!\n")
            score += 5
        else:
            print("Incorrect!\n")

    print("Quiz Completed!")
    print("Your score is:", score, "out of", 50 )

quiz_game()
