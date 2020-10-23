'''
Zengping Xu
CS 5001 Fall 2020

This program get input from test object about the answer of three questions and decide which Marvel Heroes you are.

'''


def main():
    valid_answer1 = {"A", "B", "C", "D"}
    valid_answer2 = {"A", "B", "C"}
    valid_answer3 = {"A", "B"}

    answer1 = str(input("which place do you prefer to stay at weekend? \
A-Home, B-Outside Park, C-Business Mall, D-Company: ")).upper()
    answer2 = str(input("When you wake up in the morning, the first thing \
you do is? A-Pick up your phone, B-Drink a glass of water, \
C-Go to toilet: ")).upper()
    answer3 = str(input("Do you live with your parent? A-Yes, B-No: ")).upper()

    if answer1 not in valid_answer1:
        answer1 = "A"
    
    if answer2 not in valid_answer2:
        answer2 = "A"
    
    if answer3 not in valid_answer3:
        answer3 = "A"
    
    if answer1 == "A" or answer1 == "B":
        if answer2 == "A" and answer3 == "A":
            superhero =  "Doctor Strange"
        elif answer2 == "A" and answer3 == "B":
            superhero = "Jean Grey"
        elif answer2 == "B" and answer3 == "A":
            superhero = "Silver Surfer"
        elif answer2 == "B" and answer3 == "B":
            superhero = "Thor"
        elif answer2 == "C" and answer3 == "A":
            superhero = "Captain Marvel"
        else:
            superhero = "Star-Lord "
    elif answer1 == "C" or answer1 == "D":
        if answer2 == "A" and answer3 == "A":
            superhero =  "Ghost Rider"
        elif answer2 == "A" and answer3 == "B":
            superhero = "Iron Man"
        elif answer2 == "B" and answer3 == "A":
            superhero = "Mr.Fantastic"
        elif answer2 == "B" and answer3 == "B":
            superhero = "Professor X"
        elif answer2 == "C" and answer3 == "A":
            superhero = "The Incredible Hulk"
        else:
            superhero = "The Human Torch"
    
    print("Bravo~ You are %s in Marvel movie" % superhero)


if __name__ == "__main__":
    main()
