import random

characters = ["a clever fox", "a brave rabbit", "a sleepy bear", "a curious cat"]
places = ["in the forest", "on the mountain", "by the river", "under the stars"]
actions = ["found a treasure", "helped a friend", "solved a mystery", "learned something new"]

def generate_story():
    character = random.choice(characters)
    place = random.choice(places)
    action = random.choice(actions)
    return f"One day, {character} {action} {place}."

# Run it!
if __name__ == "__main__":
    print(generate_story())
