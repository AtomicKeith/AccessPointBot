from prod import main as prodbot
from dev import main as devbot

if __name__ == "__main__":
    whichBot = ""
    while whichBot == "":
        whichBot = input("Which bot would you like to run? ('Prod' or 'Dev'): ")
        if whichBot != "Prod" and whichBot != "Dev":
            print("Invalid Response! Please use 'Prod' or 'Dev'")
            whichBot = ""
    if whichBot == "Prod":
        prodbot.run_bot()
    else:
        devbot.run()