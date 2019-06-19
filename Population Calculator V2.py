#change base values here
baseyear = 2017
basepopulation = 7550262101
annualprcntchange = 1.2



#Question, gathers the desired year from input, doesn't allow invalid inputs

def question():
    loop = "on"
    while loop == "on":
        year=input("\nPlease Enter Desired Year: ")
        if year.isdigit() == False:
            loop = "on"
            print("please enter valid year.")
        else:
            year = (int(year))
            if (year<(baseyear)) == True:
                print("please enter year past "+(str(baseyear))+".")
                loop = "on"
            elif (len((str(year)))==4)== False:
                print("please enter a year no greater than 4 digits long.")
                loop = "on"
            else:
                return year
                loop = "off"






def stats():


    #Generates Estimated Population

    yeardiff = ((year)-(baseyear))
    pop = (basepopulation)
    for i in range (yeardiff):
        pop+= ((pop)/100*(annualprcntchange))
    estpop=(int(pop))


    #Finds change in population since base year

    popchange = (str(((estpop-(basepopulation)))))
    
    
    #generates length of surrounding line for box when printed
    
    line = ""
    for i in range (30+(len(str((estpop))))):
        line+="-"   

    #prints all data
    
    print("")
    print(line)
    print("Year: "+(str(year)))
    print("Estimated Population: "+(str(estpop)))
    print("Population change since "+(str(baseyear))+": "+(popchange))
    print(line)
    print("")


#runs program

loop = "on"
while loop == "on":
    year = question()
    if year =="kill":
        print("End Of Program")
    else:
        stats()





