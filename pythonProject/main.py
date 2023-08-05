# this app calculates the perimeter/ area of a circle
user_ans= input("seconds: ")
n=int(user_ans)
if n < 60:
    seconds=n +0
    minutes=n//60
    hours=n//3600
    days=n//86400
    print(days, "days", hours, "hours", minutes, "minutes", seconds, "seconds")

elif n<3600:
    seconds=n%60
    minutes=n//60
    hours=n//3600
    days=n//86400
    print(days, "days", hours, "hours", minutes, "minutes", seconds, "seconds")
elif n <86400:
    seconds = n % 60
    minutes = (n % 3600)//60
    hours=n//3600
    days=n//86400
    print(days,"days", hours, "hours", minutes, "minutes", seconds, "seconds")
else:
    seconds = n % 60
    minutes = n % 3600
    hours = n % (3600 * 24)
    days = n // (3600 * 24)
    print(days,"days",hours,"hours",minutes,"minutes",seconds,"seconds")


