totalseconds = int(input("Enter a whole number of seconds: "))

minutes = totalseconds // 60
seconds = totalseconds % 60

print("{} seconds is equal to {} minutes and {} seconds.".format(totalseconds, minutes, seconds))
