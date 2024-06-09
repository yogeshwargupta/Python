import time

waitTime = 1
maxRetries = int(input("Enter the maximum tries: "))
attempt = 0

while attempt<maxRetries:
    print("Attempt", attempt+1, "-wait time", waitTime, "sec")
    time.sleep(waitTime)
    waitTime *= 2
    attempt += 1