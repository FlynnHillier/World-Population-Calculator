#change base year and base population here
baseyear = 2017
basepopulation = 7550262101
annualprcntchnge = 1.2

def question():
    loop = "on"
    while loop == "on":
        year=input("Please Enter Desired Year: ")
        if year.isdigit() == False:
            loop = "on"
            print("please enter valid year")
        else:
            year = (int(year))
            if (year<(baseyear)) == True:
                print("please enter year past "+(str(baseyear))+".")
                loop = "on"
            else:
                return year
                loop = "off"


def popcalc(percentincrease):
    yeardiff = ((year)-(baseyear))
    pop = (basepopulation)
    for i in range (yeardiff):
        pop+= ((pop)/100*(percentincrease))
    pop=(int(pop))
    return pop


def stats():

    popchange = (str(((estpop-(basepopulation)))))
    
    
    line = ""
    for i in range (22+(len(str((estpop))))):
        line+="-"   


    print("")
    print(line)
    print("Year: "+(str(year)))
    print("Estimated Population: "+(str(estpop)))
    print("Population change since "+(str(baseyear))+": "+(popchange))
    print(line)
    print("")


loop = "on"
while loop == "on":
    year = question()
    estpop = popcalc((annualprcntchnge))
    stats()





