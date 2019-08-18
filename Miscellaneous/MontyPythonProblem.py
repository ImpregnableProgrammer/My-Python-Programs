import random
def MontyPython(NumTrials):
    NumWonSwitch = 0
    NumWonStay = 0
    for i in range(NumTrials):
        car = random.randint(1,3)
        choice = random.randint(1,3)
        if choice == car:
            NumWonStay += 1
        reveal = random.choice([*{1,2,3}-{choice, car}])
        switch = [*{1,2,3} - {reveal, choice}][0]
        if switch == car:
            NumWonSwitch += 1
    return {"Switch Won": NumWonSwitch, "Stay Won": NumWonStay,
            "Switch Win Ratio": NumWonSwitch / NumTrials, "Stay Win Ratio": NumWonStay / NumTrials,
            "Trials": NumTrials}

print(MontyPython(100000))
