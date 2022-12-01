import sys
from os.path import dirname
from os.path import join
from command import Command
from getpass import getpass
from rich.console import Console
from os import system, name


sys.path.insert(0, join(dirname(__file__), 'src'))


def clear():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')


def main():

    clear()

    console = Console()
    print("Please log in to your NextCloud account: ")
    NEXTCLOUD_USERNAME = input("Username: ")
    NEXTCLOUD_PASSWORD = getpass("Password: ")

    INSTANCE = Command(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD)
    if INSTANCE.getConnectionIssues():
        print("ERROR: There was an issue when logging in.")
        exit()

    INSTANCE.createMenu()


    loggedIn = True


    # TODO: Parse json
    # print(nxc.list_folders(path=None, depth=1, all_properties=False, fields=None).data)


    while loggedIn:
        #clear()
        console.print(INSTANCE.getMenu())
        currInput = input("Enter your command: ")

        match currInput.upper():
            case "1":
                clear()
                INSTANCE.createFolder()
            case "2":
                clear()
                INSTANCE.uploadFile()
            case "3":
                clear()
                INSTANCE.copyFile()
            case "4":
                clear()
                INSTANCE.deleteFile()
            case "5":
                clear()
                INSTANCE.downloadFile()
            case "6":
                clear()
                INSTANCE.setFavorite()
            case "7":
                clear()
                INSTANCE.moveFile()
            case "8":
                clear()
                INSTANCE.editUser()
            case "9":
                clear()
                INSTANCE.listUsers()
            case "X":
                clear()
                loggedIn = False
                break
            case _:
                clear()
                print("No such input, try again")

    print("Goodbye...")

    return None    


if __name__ == "__main__":
    main()