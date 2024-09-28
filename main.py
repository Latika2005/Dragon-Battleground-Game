
import random
import dice

#display details funciton
def roll_die():
    for roli in range(0,6):
        roll=random.randint(1,6) #generates a random number from 1-6 (inclusive)
    return roll

def roll_damage(size):
      list = []
      for die_roll in range(0,size):#runs the loop till the size
            list+=(roll_die) #appends list with the function roll_die
      return list
      

#functions which adds all the values
def calculate_dammage(roll):
      damage = 0
      for die_value in roll:
            damage = damage+die_value
      return damage       
      
#variable for showing end results and continuing loops
play = "y"
player_won = 0
dragon_won = 0
draw = 0
game = 0
dragon_died =0
#play loopp
while play == "y":  
      play = input("Would you like to play Dragon Battleground [y|n]? ")
      if play == "y":
            number_rounds = 0
            player_health = 100
            dragon_health = 100
            print()#line spacing as default end is \n
            ask=int(input("Please enter number of battle rounds:" )) #askinf number of rounds to start the round
            #loop to run 5 rounds until the player or dragon dies
            while (ask!=number_rounds):
                  if ask>0 and ask <6:#checking number of rounds is between 1 and 5
                        print()
                        print("-- Battle -- Player versus Dragon:", ask ,"rounds --")      
                        number_rounds +=1 #incrimenting number of rounds
                        print()
                        print("Round: ",number_rounds)
                        print()
                        player_roll = roll_damage(5) # list that stores the values of players's rolls

                        #Display player's roll to screen
                        print("Player rolled :")
                        dice.display_dice(player_roll)


                        die_count = [0,0,0,0,0,0,0] #list to count die values

                        #loop to count the die values
                        for die_value in player_roll:
                              die_count[die_value] = die_count[die_value] + 1

                        

                        player_dammage=0   #value to sstore damage by player

                        #conditional statements to check how much damage delt
                        if die_count[1] == 3 and die_count[3] == 3 and die_count[5] == 3:
                              player_dammage == 0
                              print("-- Swing and miss - no damage inflicted!")

                        elif 2 in die_count:
                              player_dammage=calculate_dammage(player_roll)*2
                              print("-- Hit - double the damage!")

                        elif 3 in die_count:
                              player_dammage=calculate_dammage(player_roll)*3
                              print("-- Critical hit - triple the damage!")

                        else:
                              player_dammage=calculate_dammage(player_roll)

                        #total damage done to dragon
                        print("-- Player has dealt",player_dammage,"Damage")
                        print()

                        #dragon roll
                        dragon_roll = roll_damage(5) # list that stores the values of dragon's rolls

                        #Display dragon's roll to screen
                        print("dragon rolled :")
                        dice.display_dice(dragon_roll)


                        die_count = [0,0,0,0,0,0,0] #list to count die values

                        #loop to count the die values
                        for die_value in dragon_roll:
                              die_count[die_value] = die_count[die_value] + 1
            

                        dragon_dammage=0   #value to sstore damage by dragon

                        #conditional statements to check how much damage delt
                        if die_count[1] == 3 and die_count[3] == 3 and die_count[5] == 3:
                              dragon_dammage == 0
                              print("-- Swing and miss - no damage inflicted!")
                        
                        elif 2 in die_count:
                              dragon_dammage=calculate_dammage(dragon_roll)*2
                              print("-- Hit - double the damage!")

                        elif 3 in die_count:
                              dragon_dammage=calculate_dammage(dragon_roll)*3
                              print("-- Critical hit - triple the damage!")

                        else:
                              dragon_dammage=calculate_dammage(dragon_roll)


                        #total damage done to player
                        print("--Dragon has dealt",dragon_dammage,"Damage")
                        print()

                        player_health -= dragon_dammage
                        dragon_health -= player_dammage

                        current_p_health = player_health
                        current_d_health = dragon_health

                        #if player health goes less than 0 changing it to 0 again to display
                        if player_health<0 :
                              current_p_health =0
                        if current_d_health<0:
                              current_d_health=0
                              print("> Player - Damage taken:",dragon_dammage," - Current health:",current_p_health)
                              print("> Dragon - Damage taken:",player_dammage," - Current health:",current_d_health)
                              break #breaking the loop if someone dies

                        print(" Player - Damage taken:",dragon_dammage," - Current health:",current_p_health)
                        print(" Dragon - Damage taken:",player_dammage," - Current health:",current_d_health)
                  
                  else:
                        print("Must be between 1-5 inclusive.")
                        print()
                        ask=int(input("Please enter number of battle rounds:"))
                        
            #ending battle
            game +=1 #adding nummber of games 
            print()
            print("-- End of battle --")
            #conditional statemets too see who won
            if current_d_health > current_p_health:
                   print("** Dragon wins! **")
                   dragon_won +=1 #adding dragon won
            elif current_p_health>current_d_health:
                  print("** Player wins! **")
                  player_won +=1 #adding player won
                  if current_d_health == 0:
                        dragon_died +=1
            else:
                  print("** Draw! **")
                  draw +=1
            play = input("Play again [y|n]?  ")
            #if player enters n display game summary     
            if play == "n":
                   print()
                   print("Game Summary")
                   print("============")
                   print("You played ",game, "games")
                   print(" |--> Games won: ",player_won)
                   print(" |--> Games lost: ",dragon_won)
                   print(" |--> Games drawn: ",draw)
                   print(" |--> Dragons killed: ",player_won)
                   print()
                   print("Thanks for playing!")
            
            elif play != "y" and play !="n":
                  print("Please enter either 'y' or 'n'.")
                  play = "y"

      #if player enter no in the first round
      elif play == "n":
            print()
            print("No worries... you live to battle another day... :)") 
      
      #if player enters anything else other than y or n
      else:
            print("Please enter either 'y' or 'n'.")
            play = "y"
      
      