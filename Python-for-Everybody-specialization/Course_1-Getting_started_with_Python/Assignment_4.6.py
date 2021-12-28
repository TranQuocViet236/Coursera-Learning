h = float(input("Enter Hours: "))
r = float(input("Enter Rate: "))


def computepay(hrs, rate):
    new_rate = rate*1.5
    if hrs > 40:
        return 40*rate + (hrs-40)*new_rate
    else:
        return hrs*rate

pay = computepay(h, r)
print(f"Pay: {pay}")