print("Hello")
response = raw_input("\nWhat is your name ?\n ")
print("\nHello " + response + ". How are you feeling?\n  ")

import random
moods1 = ["bad", "not great", "horrible", "not too bad"]
responses1 = ["\nOh cheer up, I'm sure you'll be just fine\n "]
moods2 = ["ok", "good", "great", "amazing", "fantastic"]
responses2 = ["\nGlad to hear!\n", "\nI'm happy to hear that\n"]
question = ["how are you?","how are you doing?"]
responses3 = ["\nOkay\n","\nNot too bad\n", "\nI'm fine\n"]

while True:
        userInput = raw_input()
        if userInput in moods1:
                random_response = random.choice(responses1)
                print(random_response)
        
        elif userInput in moods2:
                random_response = random.choice(responses2)
                print(random_response)
        
        elif userInput in question:
                random_response = random.choice(responses3)
                print(random_response)
        
        else:
             print("\nWould you like to know some random facts?\n")
             break
    
                
                
        
                
answer = ["yes", "go on", "why not"]
facts = ["\nBanging your head against a wall burns 150 calories an hour\n", 
         "\nPteronophobia is the fear of being tickled by feathers\n",
         "\nA flock of crows is known as a murder\n",
         "\nThe first man to urinate on the moon was Buzz Aldrin, shortly after stepping onto the lunar surface\n",
         "\nThe top of the Eiffel Tower leans away from the sun, as the metal facing the sun heats up and expands. It can move as much as 7 inches\n",
         "\nYou are 1% shorter in the evening than in the morning\n",
         "\nMost dust particles in your house are made from dead skin\n",
         "\nA man from Britain changed his name to Tim Pppppppppprice to make it harder for telemarketers to pronounce\n",
         "\nThe word gorilla is derived from a Greek word meaning, A tribe of hairy women\n",
         "\nThe average person spends 6 months of their lifetime waiting on a red light to turn green\n",
         "\nBy law a pregnant woman can pee anywhere she wants to in Britain even if she chooses in a police officers helmets\n",
         "\nHuman saliva has a boiling point three times that of regular water\n",
         "\nIf you consistently fart for 6 years & 9 months, enough gas is produced to  create the energy of an atomic bomb\n",
         "\nFacebook, Skype and Twitter are all banned in China\n",
         "\nArtist Salvador Dali would often get out of paying for drinks and meals by drawing on the cheques, making them priceless works of art and therefore un-cashable.\n"]

while True:
        userInput = raw_input()
        if userInput in answer:
                random_response = random.choice(facts)
                print(random_response + "\nAnother one?\n")
                
        else:
             print("\nNice talking to you, goodbyeeeeeeeeeee\n")
                
       
                
        
        
        

    
    






 
 
    



    
    

 