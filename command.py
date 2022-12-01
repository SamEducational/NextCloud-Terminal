from nextcloud import NextCloud
from rich.table import Table
from rich.console import Console
from rich.theme import Theme


custom_theme = Theme({"success": "green"})

console = Console(theme=custom_theme)

class Command:
	def __init__(self, username, password):
		"""Initialization"""
		self.URL = "https://nextcloud.zthompson.me:443"
		self.USERNAME = username
		self.PASSWORD = password
		self.table = Table()

		#self.MENU = '''
	#Please select an option:\n
	#1. Create a Folder
	#2. Upload a File
	#3. Copy a File/Folder to Destination
	#4. Delete a File/Folder
	#5. Download a File/Folder
	#6. Set Favorite File/Folder
	#7. Move a File/Folder 
	#8. Edit your user
	#9. List Users
	#X. Exit Program
		#'''

		self.nxc = NextCloud(endpoint=self.URL, user=self.USERNAME, password=self.PASSWORD)

	def getConnectionIssues(self):
		return self.nxc.get_connection_issues()
		
	def getMenu(self):
		return self.table


	def createMenu(self):
		self.table = Table(title="Please select an option:")
		self.table.add_column("Key")
		self.table.add_column("Option")
		self.table.add_row("1.", "Create a Folder")
		self.table.add_row("2.", "Upload a File")
		self.table.add_row("3.", "Copy a File/Folder to Destination")
		self.table.add_row("4.", "Delete a File/Folder")
		self.table.add_row("5.", "Download a File/Folder")
		self.table.add_row("6.", "Set Favorite File/Folder")
		self.table.add_row("7.", "Move a File/Folder")
		self.table.add_row("8.", "Edit your user")
		self.table.add_row("9.", "List Users")
		self.table.add_row("X.", "Exit Program")


	def createFolder(self):
		print('\nYou entered "Create a Folder"\n')
		folder_name = input("Enter the name of the folder: ")
		self.nxc.create_folder(folder_name)
		console.print("You created a Folder\n",style="success")


	def uploadFile(self):
		print('\nYou entered "Upload a File"\n')
		local_file = input("Enter path of the file/folder on local storage: ")
		online_file = input("Enter path for the file in nextCloud: ")
		self.nxc.upload_file(local_file, online_file, timestamp=None)
		console.print("You uploaded a File/Folder\n",style="success")


	def copyFile(self):
		print('\nYou entered "Copy a File/Folder to Destination"\n')
		copied_file = input("Enter the file/folder to copy: ")
		destination = input("Enter the destination for the copy: ")
		self.nxc.copy_path(copied_file, destination, overwrite=False)
		console.print("You copied a File/Folder to destination\n",style="success")


	def deleteFile(self):
		print('\nYou entered "Delete a File/Folder"\n')
		deleted_file = input("Enter the file/folder you want to delete: ")
		self.nxc.delete_path(deleted_file)
		console.print("You deleted a File/Folder\n",style="success")


	def downloadFile(self):
		print('\nYou entered "Download a File/Folder"\n')
		downloaded_file = input("Enter path of the file/folder you want to download: ")
		self.nxc.download_file(downloaded_file)
		console.print("You dowloaded a File/Folder\n",style="success")


	def setFavorite(self):
		print('\nYou entered "Set Favorite File/Folder"\n')
		favorited_file = input("Enter path of the file you want to favorite: ")
		self.nxc.set_favorites(favorited_file)
		console.print("You set a favorite File/Folder\n",style="success")

		# TODO: Parse json
		#print("Your favorites:\n")
		#print(self.nxc.list_favorites(path="").data)


	def moveFile(self):
		print('\nYou entered "Move a File/Folder"\n')
		moved_file = input("Enter path for the file you wish to move: ")
		new_location = input("Enter new path for the file: ")
		self.nxc.move_path(moved_file, new_location, overwrite=False)
		console.print("You moved a File/Folder\n",style="success")


	def editUser(self):
		print('\nYou entered "Edit Your User"\n')
		print("What do you want to edit?\n")
		selection = input("Options: email, quota, phone, address, website, twitter, displayname, password\n").lower()
		newvalue = input(f"What is the new value for {selection}? ")
		self.nxc.edit_user(self.USERNAME, selection, newvalue)


	def listUsers(self):
		toStrip = ["{", "}", "'", "[", "]"]

		print('\nYou entered "List Users"\n')
		response = str(self.nxc.get_users(search=None, limit=None, offset=None).data)
		new_response = ""

		for x in response:
			if x in toStrip:
				continue
			else:
				new_response += x

		console.print(new_response + "\n")