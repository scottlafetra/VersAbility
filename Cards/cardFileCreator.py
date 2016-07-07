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
    text = raw_input()
    if text != "":
        file.write(" \"Type\": \"" + text + "\", ")

    #reaction type
    print "Reaction Type? "
    text = raw_input()
    if text != "":
        file.write(" \"Reaction Type\": \"" + text + "\", ")

    #Action type
    print "Action Type? "
    text = raw_input()
    if text != "":
        file.write(" \"Action Type\": \"" + text + "\", ")

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

    #star level
    print "Star Level? "
    text = raw_input()
    if text != "":
        file.write(" \"Star Level\": " + text + ", ")

    #AP cost
    print "AP cost? "
    text = raw_input()
    if text != "":
        file.write(" \"AP cost\": " + text + ", ")

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

    #Starting Class
    print "Starting Class? "
    text = raw_input()
    if text != "":
        file.write(" \"Starting Class\": \"" + text + "\", ")

    #health? (is parent for all class stuff)
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

            #Rules Text
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
    file.write("} ")

#footer stuff
file.write("] }")

file.close()
