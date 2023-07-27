limit = int(input("Enter total number of seats: "))
seatNumber = int(input("Enter seat number: "))

windowSeat = [j for j in range(1, limit+1, 6)]
for k in range(6, limit+1, 6):
    windowSeat.append(k)

midSeat = [j for j in range(2, limit+1, 6)]
for k in range(5, limit+1, 6):
    midSeat.append(k)

sideSeat = [j for j in range(3, limit+1, 6)]
for k in range(4, limit+1, 6):
    sideSeat.append(k)

grpLastSeat = [k for k in range(1, limit+1, 12)]
grpLastSeat.append(seatNumber)
grpLastSeat.sort()

grpNo = grpLastSeat.index(seatNumber)
oppoSeat = 0
if seatNumber - 6 >= grpLastSeat[grpNo - 1]:
    oppoSeat = seatNumber - 6
else:
    oppoSeat = seatNumber + 6

if seatNumber in windowSeat:
    print("Window Seat")
elif seatNumber in midSeat:
    print("Middle Seat")
elif seatNumber in sideSeat:
    print("Inside Corner Seat")

if oppoSeat <= limit:
    print("Opposite Seat = ", oppoSeat)
else:
    print("No Opposite Seat.")
