import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate(cards):
    return sum(cards)


playing = True
while playing:

    want_play = input("Would you like to play Blackjack. Type 'y' or 'n'.\n")
    if want_play == "n":
        playing = False
        print("Thanks for stopping by.")
    elif want_play == "y":
        hand_over = False
        while not hand_over:

            computer_cards = (random.choices(deck, k=2))
            player_cards = (random.choices(deck, k=2))

            sum_player = sum(player_cards)
            sum_computer = sum(computer_cards)

            if sum_computer == 21 and sum_player == 21:
                print("Player and computer have blackjack. Player pushes.")
                hand_over = True
            elif sum_computer == 21:
                print(f"Computer has blackjack. You have {sum_player}. You lose")
                hand_over = True
            elif sum_player == 21:
                print(f"You have blackjack. Computer has {sum_computer}. You win.")
                hand_over = True
            else:
                dealer_turn = True
                while dealer_turn:
                    sum_computer = calculate(computer_cards)
                    if sum_computer > 21 and 11 in computer_cards:
                        for i in range(len(computer_cards)):
                            if computer_cards[i] == 11:
                                computer_cards[i] = 1
                    elif sum_computer < 17:
                        computer_cards.append(random.choice(deck))
                    elif sum_computer > 16:
                        dealer_turn = False

                player_turn = True
                while player_turn:
                    sum_player = calculate(player_cards)
                    if sum_player > 21 and 11 in player_cards:
                        for i in range(len(player_cards)):
                            if player_cards[i] == 11:
                                player_cards[i] = 1
                    elif sum_player > 21:
                        player_turn = False
                    else:
                        print(f"Your cards: {player_cards}, your current score: {sum_player}")
                        print(f"Dealer's first card: {computer_cards[0]}")
                        more = input("Do you want another card? Type 'y' or 'n':\n")
                        if more == "y":
                            player_cards.append(random.choice(deck))
                        elif more == "n":
                            player_turn = False
                print(f"Player has {sum_player}. Computer has {sum_computer}.")
                if sum_player > 21:
                    print("Player loses.")
                    hand_over = True
                elif sum_computer == sum_player:
                    print("Player pushes.")
                    hand_over = True
                elif 22 > sum_computer > sum_player:
                    print("Computer wins.")
                    hand_over = True
                elif 22 > sum_player > sum_computer:
                    print("Player wins.")
                    hand_over = True
    else:
        print("You did not enter a valid decision. Please try again.")




