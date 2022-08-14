import random
def get_guess():
    '''
    Asks for the number guess and transforms the string to a list.
    '''
    return list(input ("What is your guess: "))

def generate_code():
    '''
    generates a 3 digit list for the code
    '''
    digits= [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]

def generate_clues(code,user_guess):
    '''
    Takes in a user guess and code then compares the numbers in a loop and
    creates a list of clues according to the matching parameters.
    '''
    if user_guess==code:
        return "CODE CRACKED!"

    clues=[]

    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("Match")
        elif num in code:
            clues.append("Close")
    if clues ==[]:
        return ["nope"]
    else:
        return clues

print("Welcome code breaker!")
secret_code=generate_code()
clue_report=[]
while clue_report != "CODE BREAKER!":
    guess=get_guess()
    clue_report= generate_clues(guess,secret_code)
    print("Here is the result of your guess: ")
    for clue in clue_report:
        print(clue)
