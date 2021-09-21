import dropbox

class TransferData:
    def__init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

    f=open(file_from,'rb')
    dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.A4-nUbUhgwcIL8nuPYgOXPwrwYYPNmA_tejGCGUQwwTlJQecU9LV-_sRzos8Bsod5JjkFTlSb8ggUjuJZGgCLJOBZR6YdYaPpcP0K2mjm44GbougrFV9hTjmlE6PvtvPRuYUQmM'
    TransferData=TransferData(access_token)

    file_from=input("Enter the File Path to Transfer.-")
    file_to=input("Enter the Full Path to Upload to Dropbox.-")

    TransferData.upload_file(file_from,file_to)
    print("File Has Been Moved!")

if __name__=='__main__':
    main()