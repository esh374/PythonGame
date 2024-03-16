#Write a Python program to simulate a single round of a fictional game Pyjack (a variation of Blackjack). You can find the rules of Blackjack explained here. For Pyjack, the rules are as follows:
#The program should be able to deal the cards for the Player and the Dealer in random order.
#The deck will contain only the number cards and not the “face” cards. I.e. there is no Ace, King, Queen or Jack. Therefore, there will be a total of 36 cards in the deck.
#First, the Dealer and the player will be dealt 1 card each.
#Subsequently, the Player should get the option to “stand” or “hit” an additional card.
#The Dealer will take additional cards till their total reaches 17 or higher.
#If the Player total exceeds 21, the Player loses the round. If the Dealer total exceeds 21, the Player wins the round.
#If the Player total is exactly 21, the Player wins the round

import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10]*4

random.shuffle(deck)

player = str(input("Enter your name: "))
dealer = "Dealer"

d = []
p = []

d.append(deck.pop())
print("The dealer got", d)
p.append(deck.pop())
print(player, "got", p)

while sum(d) < 17:
  d.append(deck.pop())

print("Now the dealer will take cards till they hit 17 or higher.")

if sum(d) > 21:
  print("Oh wait-", player, "won! XD")
elif sum(d) <= 21:
  while sum(p) <  21:
    q = input("Would you like to 'stand' or 'hit'?  ")
    if q == 'hit':
      c = deck.pop()
      p.append(c)
      print (player, "got", c)
    elif q == 'stand':
      break
  if sum(p) > sum(d) and sum(p) < 21:
    print("Yay!", player, "won!")
  elif sum(p) == 21:
    print("Yay!", player, "won!")
  elif sum(p) < sum(d) and sum(p) < 21:
    print("Awww, the Dealer won this one :(")
  elif sum(p) > 21:
    print("Awww, the Dealer won this one :(")
  elif sum(d) == 21: 
    print("Awww, the Dealer won this one :(")
  elif sum(p) == sum(d):
    print("It's a tie!")
    

print(player, "had the cards", p, "which amounts up to", sum(p))
print("The Dealer had the cards", d, "which amounts up to", sum(d))

