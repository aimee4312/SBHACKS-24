import random
choices = {"shield": 2, "shoot": 0} #make global in main

def computer_choice():
    possible_choices = ["reload"]
    if choices["shield"]:
        possible_choices.append("shield")
    if choices["shoot"]:
        possible_choices.append("shoot")
    
    selected_choice = random.choice(possible_choices)
    if selected_choice != "reload":
        choices[selected_choice] -= 1
        
    else:
        if choices["shoot"] < 2:
            choices["shoot"] += 1
    
    return selected_choice