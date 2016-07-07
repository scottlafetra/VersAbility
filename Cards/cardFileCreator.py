#This program is used for initally entering all cards into the database.

file = open("database.json", "w")

#header stuff
file.write("{ \"cards\" : [ ")

while(True):
    #Write a card

    print "Stop?"

    if raw_input() == ""
        break

    print #a space

    #start a card
    file.write("{ ")

    #name
    print "Name? "
    name = input()
    if input != "":
        file.write(" \"name\": ")

    #end the card
    file.write("} ")

#footer stuff
file.write("] }")
