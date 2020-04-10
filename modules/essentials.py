#--------------------------------------------------------------------------------------------------------------------------------------------
# date important
def convertDates():
    # import
    from datetime import date
    date = date.today()
    # data converted to str and chopped
    date=str(date);month=date[5]+date[6]# month == '03' something like that
    toDate=date[8]+date[9]
    index=["01","02","03","04","05","06","07","08","09","10","11","12"]
    replacement = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    realDate=""
    for i in range(12):
        # checking if the month maches then replaces with the letter month
        if month==index[i]:
            realDate+=replacement[i]      # replaces the number month with the letter month
            realDate+=" " + toDate + ", " # adds space, today, coma, and space respectively
            for i in range(4):            # adds the year
                realDate += date[i]
            return realDate
# date?
def inputDate():
    # of course ask first
    asdf=str(input("Mannually input Date? ----Y/N-----")); asdf=asdf.capitalize()
    if asdf[0]=="Y":
        delta = str(alfred("Date ---- Jan 24, 2020"))
        return delta
    else:
        delta=convertDates()
        return delta
# this is for balance sheet and for annual only
def alfred(query):
    quest = input("what is the " + str(query)+ "? ")
    return quest
# 21
def askLoop(list):
    listLength = len(list)
    # this is just numbers; all numbers according to the list
    emptyList = [0]*(listLength)
    for i in range(listLength):
        # asking according to the list
        if list[i] == "Date" or list[i]=="Category" or list[i]=="Reason" or list[i]=="Due":
            if list[i] == "Date":
                emptyList[i]=inputDate()
            else:
                delta = str(alfred(list[i]))
                emptyList[i] = delta
        else:
            # asking according to the list non STR
            if list[i] == "ConfirmationNumber":
                delta = round(float(alfred(list[i])), 2)
                emptyList[i] = delta
            else:
                if delta>=1.0:
                    list[i]=0.0
                else:
                    delta = round(float(alfred(list[i])), 2)
                    emptyList[i] = delta
    modifiedList = emptyList
    return modifiedList

