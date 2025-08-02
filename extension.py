cat = input("File name: ")

new_cat = cat.lower()

if '.gif' in new_cat:
    print("image/gif")
elif '.jpg' in new_cat:
    print("image/jpg")
elif '.jpeg' in new_cat:
    print("image/jpeg")
elif '.png' in new_cat:
    print("image/png")
elif '.pdf' in new_cat:
    print("application/pdf")
elif '.txt' in new_cat:
    print("text/plain")
elif '.zip' in new_cat:
    print("application/zip")
else:
    print("application/octet-stream")
