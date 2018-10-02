def main():
    file = input("Enter a filename: ")
    f = open(file, "r")
    lines = f.readlines()

    userName = []
    userDate = []
    userAmount = []

    for line in lines:

        lineList = line.split("date=")

        # working for Name
        name = lineList[0].strip()

        nameList = name.split(",")

        newName = nameList[1] + " " + nameList[0]

        #print(newName)

        userName.append(newName)

        # working for date and amount

        dateAmtList = lineList[1]. split("$")

        # Working for date

        date = dateAmtList[0].strip()

        dateList = date.split("/")

        newDate = dateList[0] + "/" + dateList[1] + "/" + dateList[2][-2:]

        # print(newDate)
        userDate.append(newDate)

        # working for amount

        newAmount = dateAmtList[1].strip()

        userAmount.append(newAmount)

    total = 0

    for i in range(len(userDate)):
        date = userDate[i]
        name = userName[i]
        amount = userAmount[i]

        finalAmount = "$ " + amount.rjust(6)

        print("{: <20} {: <20} {: >20}".format(date, name, finalAmount))

        total = total + float(amount)

    print()
    print("Total: " + "$ " + str(total))

    f.close()


main()

