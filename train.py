seat = int(input("Enter seat number: "))

import time
start_time = time.time()

if seat < 1 or seat > 108:
    print("Invalid seat number.")
else:
    position = seat % 12

    if position == 1:
        pair = seat + 11
        seat_type = "Window seat"
    elif position == 2:
        pair = seat + 9
        seat_type = "Middle seat"
    elif position == 3:
        pair = seat + 7
        seat_type = "Aisle seat"
    elif position == 4:
        pair = seat + 5
        seat_type = "Aisle seat"
    elif position == 5:
        pair = seat + 3
        seat_type = "Middle seat"
    elif position == 6:
        pair = seat + 1
        seat_type = "Window seat"
    elif position == 7:
        pair = seat - 1
        seat_type = "Window seat"
    elif position == 8:
        pair = seat - 3
        seat_type = "Middle seat"
    elif position == 9:
        pair = seat - 5
        seat_type = "Aisle seat"
    elif position == 10:
        pair = seat - 7
        seat_type = "Aisle seat"
    elif position == 11:
        pair = seat - 9
        seat_type = "Middle seat"
    elif position == 0:  # seat number divisible by 12, so it's position 12
        pair = seat - 11
        seat_type = "Window seat"

end_time= time.time()
print("Exectution time: {:.6f} seconds".format(end_time-start_time))

print("Output:", pair)
print("Type:", seat_type)