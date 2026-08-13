import json


with open("users.json", "r") as file:
    DATA = json.load(file)


def NUMERROR():
    print("try again, you should enter number !")


def WRONG():
    print("there is something wrong !")


while True:
    try:
        QUEST = int(input("""1. sign up
        2. login
        3. delete account
        4. exit
        type the number: """))
    except ValueError:
        NUMERROR()
    else:
        if QUEST == 1:
            USERNAME = input("gave username: ")
            PASSWORD = input("gave password: ")
            if USERNAME not in DATA:
                DATA[USERNAME] = {"USERNAME": USERNAME,
                                  "PASSWORD": PASSWORD}
                with open("users.json", "w") as file:
                    json.dump(DATA, file, indent=4)
                print(f"welcome {USERNAME}")
            else:
                WRONG()

        elif QUEST == 2:
            USERNAME1 = input("your username: ")
            PASSWORD1 = input("your password: ")
            if USERNAME1 in DATA:
                if PASSWORD1 == DATA[USERNAME1]["PASSWORD"]:
                    print(f"welcome {USERNAME1}")
                else:
                    WRONG()
            else:
                WRONG()
        elif QUEST == 3:
            print("we ahould verify you first")
            USERNAME2 = input("gave your username: ")
            PASSWORD2 = input("gave your password: ")
            if USERNAME2 in DATA:
                if PASSWORD2 == DATA[USERNAME2]["PASSWORD"]:
                    del DATA[USERNAME2]
                    with open("users.json", "w") as file:
                        json.dump(DATA, file, indent=4)

                    print("deleting done !")
                else:
                    WRONG()
            else:
                WRONG()
        elif QUEST == 4:
            print("good luck !")
            break
