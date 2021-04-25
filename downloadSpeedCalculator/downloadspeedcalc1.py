def get_download_speed():
    print ("What is your download speed in MB/s? (MegaBytes a second)")
    download_speed = float(input(">"))
    return download_speed


def get_file_size():
    print ("How big is the file you want to download in GB/s? (GigaBytes a second)")
    file_size = float(input(">"))
    return file_size


def calculate_download_time():
    download_speed = get_download_speed() 
    file_size = get_file_size()
    
    download_time = ((file_size * 1000) / download_speed) / 60
    print(f"It will take {download_time} minutes, to download {file_size}GB, at {download_speed}MB/s")


def playApp():

    calculate_download_time()


playApp()
