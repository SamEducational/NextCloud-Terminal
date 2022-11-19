from nextcloud import NextCloud

class Command:
	def __init__(self, username, password):
		"""Initialization"""
		self.URL = "https://nextcloud.zthompson.me:443"
		self.USERNAME = username
		self.PASSWORD = password

		self.MENU = '''
	Please select an option:\n
	1. Create a Folder
	2. Upload a File
	3. Copy a File/Folder to Destination
	4. Delete a File/Folder
	5. Download a File/Folder
	6. Set Favorite File/Folder
	7. Move a File/Folder 
	8. Edit your user
	9. List Users
	X. Exit Program
		'''

		self.nxc = NextCloud(endpoint=self.URL, user=self.USERNAME, password=self.PASSWORD)


	def getMenu(self):
		"""Return the menu"""
		return self.MENU


	def createFolder(self):
		print('\nYou entered "Create a Folder"\n')
		folder_name = input("Enter the name of the folder: ")
		self.nxc.create_folder(folder_name)


	def uploadFile(self):
		print('\nYou entered "Upload a File"\n')
		local_file = input("Enter path of the file/folder on local storage: ")
		online_file = input("Enter path for the file in nextCloud: ")
		self.nxc.upload_file(local_file, online_file, timestamp=None)


	def copyFile(self):
		print('\nYou entered "Copy a File/Folder to Destination"\n')
		copied_file = input("Enter the file/folder to copy: ")
		destination = input("Enter the destination for the copy: ")
		self.nxc.copy_path(copied_file, destination, overwrite=False)


	def deleteFile(self):
		print('\nYou entered "Delete a File/Folder"\n')
		deleted_file = input("Enter the file/folder you want to delete: ")
		self.nxc.delete_path(deleted_file)


	def downloadFile(self):
		print('\nYou entered "Download a File/Folder"\n')
		downloaded_file = input("Enter path of the file/folder you want to download: ")
		self.nxc.download_file(downloaded_file)


	def setFavorite(self):
		print('\nYou entered "Set Favorite File/Folder"\n')
		favorited_file = input("Enter path of the file you want to favorite: ")
		self.nxc.set_favorites(favorited_file)
		print("Your favorites:\n")

		# TODO: Parse json
		print(self.nxc.list_favorites(path="").data)


	def moveFile(self):
		print('\nYou entered "Move a File/Folder"\n')
		moved_file = input("Enter path for the file you wish to move: ")
		new_location = input("Enter new path for the file: ")
		self.nxc.move_path(moved_file, new_location, overwrite=False)


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

		return new_response