#This program is used for initally entering all cards into the database.

file = open("database.json", "w")

#header stuff
file.write("{ \"cards\" : [ ")

while(True):
    #Write a card

    print "Press enter to continue..."

    if raw_input() != "":
        break

    print #a space

    #start a card
    file.write("{ ")

    #name
    print "Name? "
    text = raw_input()
    if text != "":
        file.write(" \"Name\": \"" + text + "\", ")

    #type
    print "Type? "
    cardType = raw_input()
    if cardType != "":
        file.write(" \"Type\": \"" + cardType + "\", ")

    if cardType == "Reaction":
        #reaction type
        print "Reaction Type? "
        text = raw_input()
        if text != "":
            file.write(" \"Reaction Type\": \"" + text + "\", ")

    if cardType == "Action":
        #Action type
        print "Action Type? "
        actionType = raw_input()
        if actionType != "":
            file.write(" \"Action Type\": \"" + actionType + "\", ")

        if actionType == "Attack":
            #Attack type
            print "Attack Type? "
            text = raw_input()
            if text != "":
                file.write(" \"Attack Type\": \"" + text + "\", ")

                #Damage
                print "Damage? "
                text = raw_input()
                if text != "":
                    file.write(" \"Damage\": " + text + ", ")

        if actionType == "Focus":
            #Focus type
            print "Focus Type? "
            text = raw_input()
            if text != "":
                file.write(" \"Focus Type\": \"" + text + "\", ")
        
        #Range type
        print "Range Type? "
        text = raw_input()
        if text != "":
            file.write(" \"Range\": { ")
            file.write(" \"Type\": \"" + text + "\" ")

            #Min Range
            print "Min? "
            text = raw_input()
            if text != "":
                file.write(", \"Min\": " + text + " ")

            #Max Range
            print "Max? "
            text = raw_input()
            if text != "":
                file.write(", \"Max\": " + text + " ")

            file.write("}, ")

        #AP cost
        print "AP cost? "
        text = raw_input()
        if text != "":
            file.write(" \"AP cost\": " + text + ", ")

        #Starting Class
        print "Starting Class? "
        text = raw_input()
        if text != "":
            file.write(" \"Starting Class\": \"" + text + "\", ")

    if cardType == "Equipment":
        #star level
        print "Star Level? "
        text = raw_input()
        if text != "":
            file.write(" \"Star Level\": " + text + ", ")


    #Rules Text
    print "Rules Text? "
    text = raw_input()
    if text != "":
        file.write(" \"Rules Text\": \"" + text + "\", ")

    #Empowered Classes
    print "Empowered Class? "
    text = raw_input()
    if text != "": #write a list of the classes
        file.write(" \"Empowered Classes\": [")

        file.write(" \"" + text + "\" ") #first class
        
        while True:
            print "Another Empowered Class?"
            text = raw_input()

            if text == "":
                break
                
            file.write(", \"" + text + "\" ")#other classes
            
        file.write(" ], ")

        #Empowered Text
        print "Empowered Text? "
        text = raw_input()
        if text != "":
            file.write(" \"Empowered Text\": \"" + text + "\", ")

    #Flavor Text
    print "Flavor Text? "
    text = raw_input()
    if text != "":
        file.write(" \"Flavor Text\": \"" + text + "\", ")

    if cardType == "Class":
        #health?
        print "Health? "
        text = raw_input()
        if text != "":
            file.write(" \"Health\": " + text + ", ")

        #Starting Actions
        print "Starting Action? "
        text = raw_input()
        if text != "": #write a list of the classes
            file.write(" \"Starting Actions\": [")

            file.write(" \"" + text + "\" ") #first class
            
            while True:
                print "Another starting action?"
                text = raw_input()

                if text == "":
                    break
                
                file.write(", \"" + text + "\" ")#other actions
                
            file.write(" ], ")

        #Class ability
        print "Class Ability? "
        text = raw_input()
        if text != "":
            file.write(" \"Class Ability\": { ")

            #name  
            file.write(" \"Name\": \"" + text + "\", ")

            #Starting Class
            print "Rules Text? "
            text = raw_input()
            if text != "":
                file.write(" \"Rules Text\": \"" + text + "\"")

            file.write(" },")

    print "Image Number? "
    text = raw_input()
    if text != "":
        file.write(" \"Image Number\": " + text + " ")

    #end the card
    file.write("}, ")

#footer stuff
file.write("] }")

file.close()
