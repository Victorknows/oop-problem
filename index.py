def sort_scoreboard(entry):
    return (entry['score'], entry['name'])

def calculate_score(participants):
    scoreboard = []
    
    for participant in participants:
        name = participant['name']
        score = participant['chickenwings'] * 5 + participant['hamburgers'] * 3 + participant['hotdogs'] * 2
        scoreboard.append({'name': name, 'score': score})
    
    scoreboard.sort(key=sort_scoreboard)
    
    return scoreboard

participants = [
    {'name': "Habanero Hillary", 'chickenwings': 5, 'hamburgers': 17, 'hotdogs': 11},
    {'name': "Big Bob", 'chickenwings': 20, 'hamburgers': 4, 'hotdogs': 11}
]

scoreboard = calculate_score(participants)
print(scoreboard)
