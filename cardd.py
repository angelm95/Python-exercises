
import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
"7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
        card_choice = input("Pick a card [P] or Quit [Q] ")
        if card_choice == "Q":
            break
        if card_choice == "P":
            card = random.choice(diamonds)
            hand.append(card)
            diamonds.remove(card)
            print(f"You have selected {card}")
            print(f" Which means the cards left to choose are: {diamonds}")
        else:
            print("you must select either Q or P")
            continue
        if not diamonds:
            print("you've run out of cards")
            
        