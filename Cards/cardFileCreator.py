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
        file.write(" \"Name\": \"" + text + "\" ")

    #star level
    print "Star Level? "
    text = raw_input()
    if text != "":
        file.write(" \"Star Level\": " + text + " ")

    #end the card
    file.write("} ")

#footer stuff
file.write("] }")

file.close()
