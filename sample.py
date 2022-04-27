import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BGfK1-kmV_TSlLcN-KgS3iOEGb-8rDJJU9V0XJXyYTjdNQHIOi9uU47Apch8fwY9Hb2n2SzGhJmeWZgXHrty6fSgbmDYePuen8eWq2m44g5N8xO--XQNVxangVZfi-l3LxldGVCsk4OF'
    transferData = TransferData(access_token)

    file_from = "text.txt"
    file_to = "/testfolder/text.txt"

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()