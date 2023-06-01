import string, math, random

from poker import Poker

def main ():
  numHands = eval (input ('Enter number of hands to play: '))
  while (numHands < 2 or numHands > 6):
    numHands = eval( input ('Enter number of hands to play: ') )
  game = Poker (numHands)
  game.play()  

  print('\n')
  for i in range(numHands):
    curHand=game.hands[i]
    print ("Hand "+ str(i+1) + ": " , end="")
    game.isRoyal(curHand)

  maxpoint=max(game.tlist)
  maxindex=game.tlist.index(maxpoint)

  print ('\nHand %d wins'% (maxindex+1))
  
main()


