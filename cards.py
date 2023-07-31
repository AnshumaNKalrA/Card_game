import random


string_of_cards="spade_A,spade_2,spade_3,spade_4,spade_5,spade_6,spade_7,spade_8,spade_9,spade_K,spade_J,spade_Q,diamond_A,diamond_2,diamond_3,diamond_4,diamond_5,diamond_6,diamond_7,diamond_8,diamond_9,diamond_K,diamond_J,diamond_Q,club_A,club_2,club_3,club_4,club_5,club_6,club_7,club_8,club_9,club_K,club_J,club_Q,hearts_A,hearts_2,hearts_3,hearts_4,hearts_5,hearts_6,hearts_7,hearts_8,hearts_9,hearts_K,hearts_Q,hearts_J"
list_of_cards=string_of_cards.split(",")

random.shuffle(list_of_cards)
print("The shuffled list of cards is as follows , pick a card from the list, and remember it , I will ask a few questions , answer the questions , and let us see , whether I can get to what the chosen card was ")
candidate_cards=list_of_cards[:21]
print(candidate_cards)
global deck1,deck2,deck3
global deck_number_1
for k in range(3):
    deck1=list()
    deck2=list()
    deck3=list()
    #important we cannot use two arguments while skipping some set of values , if we have to skip some set of values , then we have to use 3 arguments
    for i in range(0,19,3):
        deck1.append(candidate_cards[i])
        deck2.append(candidate_cards[i+1])
        deck3.append(candidate_cards[i+2])
    dec1_dupl=deck1[:]
    dec2_dupl=deck2[:]
    dec3_dupl=deck3[:]
    random.shuffle(dec1_dupl)
    random.shuffle(dec2_dupl)
    random.shuffle(dec3_dupl)
    print("In which of the following decks , is your card, Input the deck Number")
    print(f"Deck 1 is as ,{dec1_dupl}")
    print(f"Deck 2 is as , {dec2_dupl}")
    print(f"Deck 3 is as, {dec3_dupl}")
    decknumber_1=int(input())
    deck_to_be_kept_up="deck"+str(decknumber_1)
    candidate_cards=globals()[deck_to_be_kept_up]
    for i in range(3):
        if i+1==decknumber_1:
            continue
        candidate_cards=candidate_cards+globals()["deck"+str(i+1)]
#Remember to comment away this line while showing the trick
print(candidate_cards)
if(decknumber_1 ==1):
    print(deck1[0])
else:
    print(globals()["deck"+str(deck_number_1)][0])
