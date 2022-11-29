import sys
from os.path import dirname
from os.path import join
from command import Command
from getpass import getpass
from rich.console import Console


sys.path.insert(0, join(dirname(__file__), 'src'))


def main():

    console = Console()
    print("Please log in to your NextCloud account: ")
    NEXTCLOUD_USERNAME = input("Username: ")
    NEXTCLOUD_PASSWORD = getpass("Password: ")

    INSTANCE = Command(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD)
    INSTANCE.createMenu()


    loggedIn = True


    # TODO: Parse json
    # print(nxc.list_folders(path=None, depth=1, all_properties=False, fields=None).data)


    while loggedIn:
        console.print(INSTANCE.getMenu())
        currInput = input("Enter your command: ")

        match currInput.upper():
            case "1":
                INSTANCE.createFolder()
            case "2":
                INSTANCE.uploadFile()
            case "3":
                INSTANCE.copyFile()
            case "4":
                INSTANCE.deleteFile()
            case "5":
                INSTANCE.downloadFile()
            case "6":
                INSTANCE.setFavorite()
            case "7":
                INSTANCE.moveFile()
            case "8":
                INSTANCE.editUser()
            case "9":
                print(INSTANCE.listUsers())
            case "X":
                loggedIn = False
                break
            case _:
                print("No such input, try again")

    print("Goodbye...")

    return None    


if __name__ == "__main__":
    main()