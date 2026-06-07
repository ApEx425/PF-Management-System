import json
import random
import string
from pathlib import Path


class Staff:

    database = "data.json"
    data = []

    try:
        with open(database) as fs:
            data = json.loads(fs.read())
    except Exception as err:
        print(f"An Exception Occured as {err}")

    @staticmethod
    def update():
        with open(Staff.database, "w") as fs:
            json.dump(Staff.data, fs, indent=4)

    @classmethod
    def __accountGenretor(cls):

        while True:

            alpha = random.choices(string.ascii_letters, k=3)
            num = random.choices(string.digits, k=3)
            spchar = random.choices("!@#$%^&*", k=1)

            acc_id = alpha + num + spchar

            random.shuffle(acc_id)

            acc_id = "".join(acc_id)

            exists = any(user["accountNo"] == acc_id for user in Staff.data)

            if not exists:
                return acc_id

    def creatAccount(self):
        info = {
            "name": input("Tell Your Name - > "),
            "age": int(input("Enter Your Age - > ")),
            "email": input("Tell Your Email - > "),
            "pin": int(input("Tell Your pin - > ")),
            "accountNo": Staff.__accountGenretor(),
            "balance": 0,
        }

        if info["age"] < 18 or len(str(info["pin"])) != 4:
            print("sorry you cannot create your account")
        else:
            print(" - A/C Has Been Created Succesfully - ")

            for i in info:
                print(f"{i} : {info[i]}")
            print(" - Please Note Down Your Account Number - ")

            Staff.data.append(info)
            Staff.update()

    def depositpf(self):
        accNum = input("Enter The A/C No. : - ")
        pin = int(input("Enter The Pin - > "))

        user.data = [
            i for i in Staff.data if i["accountNo"] == accNum and i["pin"] == pin
        ]

        if not user.data:
            print("- No Data Found -")

        else:
            amount = int(input("How Much You Want To Add -- >"))

            if amount > 10000:
                print("Sorry Amount Value Is Exceed")
            else:
                user.data[0]["balance"] += amount
                Staff.update()

                print(f"Deposited Ammount Is -- > {amount}")
                print("\n-Your Ammount Deposited Succesfully-")

    def withdrawpf(self):
        accNum = input("Enter The A/C No. : - ")
        pin = int(input("Enter The Pin - > "))

        user.data = [
            i for i in Staff.data if i["accountNo"] == accNum and i["pin"] == pin
        ]

        if not user.data:
            print("- No Data Found -")

        amount = int(input("How Much You Want To Withdraw -- >"))

        if amount > user.data[0]["balance"]:
            print("Insufficient Balance")
            return

        else:

            if amount >= 10000:
                print("Sorry Amount Value Is Exceed")
            else:
                user.data[0]["balance"] -= amount
                Staff.update()

                print(f"Withdraw Ammount Is -- > {amount}")
                print("\n-Your Ammount Withdraw Succesfully-")

    def showpf(self):
        accNum = input("Enter The A/C No. : - ")
        pin = int(input("Enter The Pin - > "))

        user.data = [
            i for i in Staff.data if i["accountNo"] == accNum and i["pin"] == pin
        ]

        if not user.data:
            print("No Data Found")
            return

        print("\nYour Information Are \n\n")
        for i in user.data[0]:
            print(f"{i} : {user.data[0][i]}")

    def updatedetails(self):
        accNum = input("Enter The A/C No. : - ")
        pin = int(input("Enter The Pin - > "))

        user.data = [
            i for i in Staff.data if i["accountNo"] == accNum and i["pin"] == pin
        ]

        if not user.data:
            print(" - No Such Data Found - ")

        else:
            print(" You Cannot Change Age,Account No. and balance ")
            print("Fill The Details for Change Or Leave it Empty if no Change")

            newdata = {
                "name": input("Please Tell New Name or Press Enter : "),
                "email": input("Please Tell Your New Email or Press Enter to Skip : "),
                "pin": input("Enter New pin or press enter to skip "),
            }

            if newdata["name"] == "":
                newdata["name"] = user.data[0]["name"]
            if newdata["email"] == "":
                newdata["email"] = user.data[0]["email"]
            if newdata["pin"] == "":
                newdata["pin"] = user.data[0]["pin"]

            newdata["age"] = user.data[0]["age"]

            newdata["accountNo"] = user.data[0]["accountNo"]
            newdata["balance"] = user.data[0]["balance"]

            if type(newdata["pin"]) == str:
                newdata["pin"] = int(newdata["pin"])

            for i in newdata:
                if newdata[i] == user.data[0][i]:
                    continue
                else:
                    user.data[0][i] = newdata[i]

            Staff.update()

            print("Your Data Is Updated ")

    def deleteAc(self):
        accNum = input("Enter The A/C No. : - ")
        pin = int(input("Enter The Pin - > "))

        user.data = [
            i for i in Staff.data if i["accountNo"] == accNum and i["pin"] == pin
        ]

        if not user.data:
            print("No Data Found")
        else:
            check = input(
                "Press X If You To Delete The Account Permanently or  Press Y If You Want To frezz Account : - - > "
            )

            if check == "y" or check == "Y":
                print("You Account Is Frezz For Uncertain Period")

            if check == "x" or check == "X":
                index = Staff.data.index(user.data[0])
                Staff.data.pop(index)

                Staff.update()

                print("You Data Deleted Succesfully")


user = Staff()


print("Press -> 1 , For Adding New Staff")
print("Press -> 2 , For Deposting The Money in The PF Fund")
print("Press -> 3 , For Withdrawing The Money From PF Fund")
print("Press -> 4 , For Showing Details Of PF A/C")
print("Press -> 5 , For Updaing Details Of PF A/C")
print("Press -> 6 , For Closing Your PF A/C")

check = int(input(f"\nTell Your Respones - - > "))


if check == 1:
    user.creatAccount()

elif check == 2:
    user.depositpf()

elif check == 3:
    user.withdrawpf()

elif check == 4:
    user.showpf()

elif check == 5:
    user.updatedetails()

elif check == 6:
    user.deleteAc()

else:
    print("Invalid Choice")
