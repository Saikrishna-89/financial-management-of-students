print("Welcome To Saving Simple Bank")
Monthly_allowance = int(input("Enter Your Monthly allowance in Rupees: "))
Savings_goal = int(input("Savings Goal For Month In Percentage: "))
amount_after_ded_savings = Monthly_allowance - (Monthly_allowance*(Savings_goal/100))
Manupulative_amount = amount_after_ded_savings
Savings_amount = (Monthly_allowance*(Savings_goal/100))

print("Amount In Spending Account: {} Rs.".format(amount_after_ded_savings))
print("Amount In Savings Account: {}Rs.".format(Savings_amount))
count = 0
for i in range(1,32):

    day_input = int(input("day {} expense:".format(i)))
    if day_input > Manupulative_amount :
        print("Insuffecent Balance in Account!!")
        y = 2
        x = 1
        break
    Manupulative_amount = Manupulative_amount - day_input
    print("Amount Left In The Bank: {} Rs.".format(Manupulative_amount))
    if Manupulative_amount <= (0.25 * amount_after_ded_savings):
        print("75% of the Amount used.")

    count = count + 1
    x = 2
    y = 2

Amount2 = Manupulative_amount + (Monthly_allowance * (Savings_goal / 100))
count2 = count
if x == 1:
    print("Use amount from savings?")
    Validate = str(input("YES/NO: "))
    if Validate == "YES":
        for j in range(count+1,32):
            day_input = int(input("day {} expense:".format(j)))
            if day_input > Amount2:
                print("You have exhausted your bank account")

                y = 1
                break


            Amount2 = Amount2 - day_input
            print("Amount left in Bank: {} Rs.".format(Amount2))
    elif Validate == "NO":
        Left_amount = Amount2 + (Monthly_allowance * (Savings_goal/100))
        print("Amount left With Your Savings: {}".format(Amount2))
        y = 4
    else:
        print("Use Valid Input:")
        Validate1 = str(input("YES/NO: "))
        y = 4
    count2 = count2 + 1
if y == 1:
    print("Bad perfomance due to Exhaustion of bank limit")
    Left_amount2 = Amount2 + (Monthly_allowance * (Savings_goal/100))
    print("Amount left including Savings: {} Rs.".format(Amount2))
if count2 == 31:
    print("Amount left at the end of the month is {} Rs.".format(Amount2))
if count == 31:
    print("Amount left at the end of the month is {} Rs.".format(Amount2))
    print("Congratulations You've Managed to Save {} Rs.".format(Savings_amount))