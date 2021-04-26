def MB():
    while True:
        try:
            print ("What is your download speed in MB/s? (MegaBytes a second)")
            download_speed = float(input(">"))
            return download_speed
            break

        except ValueError:
            print("Please enter your download speed as a number!")


def mb():
    while True:
        try:
            print ("What is your download speed in mb/s? (megabits a second)")
            download_speed = float(input(">"))
            return download_speed
            break

        except ValueError:
            print("Please enter your download speed as a number!")


def get_file_size_GB():
    while True:
        try:
            print ("How big is the file you want to download in GB?")
            file_size = float(input(">"))
            return file_size

        except ValueError:
            print("Please enter your download speed as a number!")


def get_file_size_MB():
    while True:
        try:
            print ("How big is the file you want to download in MB?")
            file_size = float(input(">"))
            return file_size
        except ValueError:
            print("Please enter your download speed as a number!")


def auwbstw_input():
    #auwbstw = ask user which byte size they want
    while True:
        try:
            print("What are you measuring your download speed in? [mb][MB]/s")
            auwbstw = str(input(">"))
            
            if auwbstw == "mb" or auwbstw == "MB":
                return auwbstw
                break

            elif auwbstw != "mb" or auwbstw != "MB":
                print("Please type either of the following, [mb][MB]")
                

        except ValueError:
            print("Please type either of the following, [mb][MB]")
    return auwbstw


def wmiyfsi_input():
    #wmiyfsi = what measurement is your file size in?
    while True:
        try:
            print("What are you measuring your file size in? [MB][GB]")
            wmiyfsi = str(input(">"))
            wmiyfsi = wmiyfsi.lower()
            
            if wmiyfsi == "mb" or wmiyfsi == "gb":
                return wmiyfsi
                break

            elif wmiyfsi != "mb" or wmiyfsi != "gb":
                print("Please type either of the following, [MB][GB]")
                

        except ValueError:
            print("Please type either of the following, [MB][GB]")
    return wmiyfsi


def calculate_download_time():
    auwbstw = auwbstw_input()
    wmiyfsi = wmiyfsi_input()

    if wmiyfsi == "mb":
        file_size = get_file_size_MB()

    elif wmiyfsi == "gb":
        file_size = get_file_size_GB()

    
    if auwbstw == "mb" and wmiyfsi == "mb":
        download_speed = mb()

        download_time = ((file_size) / (download_speed/8))/60
        print(f"It will take {download_time} minutes, to download {file_size}MB, at {download_speed}mb/s")

    elif auwbstw == "MB" and wmiyfsi == "mb":
        download_speed = MB()

        download_time = ((file_size) / download_speed)/60
        print(f"It will take {download_time} minutes, to download {file_size}MB, at {download_speed}MB/s")
    
    elif auwbstw == "mb" and wmiyfsi == "gb":
        download_speed = mb()

        download_time = ((file_size * 1000) / (download_speed/8))/60
        print(f"It will take {download_time} minutes, to download {file_size}GB, at {download_speed}mb/s")

    elif auwbstw == "MB" and wmiyfsi == "gb":
        download_speed = MB()

        download_time = ((file_size * 1000) / download_speed)/60 
        print(f"It will take {download_time} minutes, to download {file_size}GB, at {download_speed}MB/s")


def playApp():

    calculate_download_time()


playApp()