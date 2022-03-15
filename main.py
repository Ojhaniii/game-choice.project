print("Welcome to Game-Choice!")


name = input("What is your name?")
age = int(input("How old are you?"))

health = 10

if age >= 18:
    print("Welcome", name, ", You are of age to play!")

    wants_to_play = input("Do you wish to continue to play (yes/no)?").lower()
    if wants_to_play == "yes":
       print("You're starting with", health, "health.")
       print("Let's get LIT!") 

       left_or_right = input("Left or Right (left/right)?")
       if left_or_right == "left":
           ans = input("Nice, you followed the path. You have reached a lake. Do you swim across or go around (across/around)?")

           if ans == "around":
               print("YAY! You've reached the other side of the lake safely.")

           elif ans == "across":
               print("You've made it across the lake, but was bit by a lake creature and lost 5 health.")
               health -= 5

           ans = input("Now you notice a house and a cave. Which do you wish to go to? (house/cave)?")
           if ans == "house":
               print("You are at the house and are greted by owner... He doesn't like you and you lose 5 health.")
               health -= 5

               if health <= 0:
                   print("You ran out of health! Game Over!")
               else:
                   print("You've Survived! You Win!")

           else:
               print("You got lost in the cave and lost..")

    
       else:
        print("YOU FELL!... game over.")

    else:
        print("BYE!")


else: 
    print("You are not approved to play...")







