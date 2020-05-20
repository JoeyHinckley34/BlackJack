import random

###########################
#Interactive Python BlackJack game
#Only can hit stand and double down
#Still working on split
#Dealer hits on soft 17
#Done using the terminal window
#I have only tested this on Mac
#Let me know what you think
##########################

#function which takes in a list of ints
#returns the sum of all the values of that list and a boolen on whether or not the sum is greater than 21
def total(hand):
    count = 0
    bust = False
    for x in hand:
        if x == '2':
            count += 2
        elif x == '3':
            count += 3
        elif x == '4':
            count += 4
        elif x == '5':
            count += 5
        elif x == '6':
            count += 6
        elif x == '7':
            count += 7
        elif x == '8':
            count += 8
        elif x == '9':
            count += 9
        elif x == '10':
            count += 10
        elif x == 'J':
            count += 10
        elif x == 'Q':
            count += 10
        elif x == 'K':
            count += 10
        elif x == 'X':
            count += 0
        else:
            if count + 11 > 21:
                count += 1
            else:
                count += 11
    if count > 21:
        bust = True
    return count,bust

#function which adds a random card to the hand
def hit(hand):
    hand.append(random.choice(cards))

#function which shows the outcome of the game is after player stands
def stand(hand,dealer):
    printd(dealer)
    #loop to play dealers hand
    #continues until dealers gets to 17
    #hits on soft 17
    while True:
        if total(dealer)[0] <= 16:
            print('Dealer must hit less than 17',end='')
            hit(dealer)
            printd(dealer)
        elif total(dealer)[0] == 17 and 'A' in dealer == True:
            print('Dealer must hit a soft 17',end='')
            hit(dealer)
            printd(dealer)
        else:
            break
    
#function which prints users hand
def printh(hand):
    print("You have ",end = '')
    for x in hand:
        print(x,'',end = '')
    print('which is a',total(hand)[0],end='')

#function which prints dealers hand
def printd(dealer):
    print("\nDealer has ",end = '')
    for x in dealer:
        print(x,'',end = '')
    print('which is a',total(dealer)[0])
    
cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
bankroll = 100

#Game Loop contines until bankroll is 0
while True:
    #sets bust to false for each hand
    bust = False
    #prints bankroll
    print("bankroll = ",bankroll)
    #asks for bet
    bet = int(input('what is your bet\n'))
    if bet > bankroll:
        print('Can not bet more than what you have\n')
    else:
        #assigns random values to each of the hands
        h1 = random.choice(cards)
        h2 = random.choice(cards)
        d1 = random.choice(cards)
        d2 = random.choice(cards)
        hand = [h1,h2]
        dealer = [d1,d2]
        #prints the dealers hand and your hand
        print('Dealer has',dealer[0])
        printh(hand)
        #sets the turn to 0
        t = 0
        #loop for your turn
        while True:
            #Gives the option to split but I have not coded for split yet
            if t == 0 and hand[0] == hand[1]:
                x = input('\nDo you want to hit(h) stand(s) split(p) or double(h)\n')
            #Gives the option to double down on the first turn
            elif t == 0:
                x = input('\nDo you want to hit(h) stand(s) or double(d)\n')
            #else just asks to hit or stand
            else:
                x = input('\nDo you want to hit(h) or stand(s)\n')
            #hits hand and prints hand
            if x == 'h':
                hit(hand)
                printh(hand)
                #if you bust prints that out and deducts from your bank roll
                if total(hand)[1] == True:
                    print("\nYou busted!")
                    bankroll -= bet
                    bust = True
                    #ends your turn
                    break
            #stands and calls the stand function ending the players turn
            elif x == 's':
                stand(hand,dealer)
                break
            #doubles bet and hits hand once ending players hand
            elif x == 'd':
                bet *= 2
                hit(hand)
                printh(hand)
                #if you bust prints that out and deducts from your bank roll
                if total(hand)[1] == True:
                    print("\nYou busted!")
                    bankroll -= bet
                    bust = True
                    #ends your turn
                    break
                stand(hand,dealer)
                break
            #this is what I have started for split, but I am still working on the logic
            '''elif x == 'p':
                bet *= 2
                ha1 = [hand[0],random.choice(cards)]
                ha2 = [hand[1],random.choice(cards)]
                printh(ha1)'''
            #increments turn number
            t += 1
        #if the user has not already busted evaluates the hand
        if(bust == False):
            #if user hand is greater than dealers or dealer busts user wins
            if (total(hand)[0]>total(dealer)[0] or total(dealer)[1]):
                print("You Win")
                bankroll+= bet
            #if user and dealer have equal values for their hand pushes
            elif total(hand)[0] == total(dealer)[0]:
                print("Push")
            #otherwise the user loses
            else:
                bankroll -= bet
                print("You Lose")
        #ends game if user is our of money
        if bankroll == 0:
            print("You are out of money!")
            break
            
