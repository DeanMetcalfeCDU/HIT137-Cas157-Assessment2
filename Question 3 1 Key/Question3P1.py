# https://github.com/DeanMetcalfeCDU/HIT137-Cas157-Assessment2
# Created by Group 157 (Adrian Voljak & Dean Metcalfe)

def find_key():
    # First code segment
    total = 0
    for i in range(5):
        for j in range(3):
            if i + j == 5:
                total += i + j
            else:
                total -= i - j

    # Second code segment
    counter = 0
    while counter < 5:
        if total < 13:
            total += 1
        elif total > 13:
            total -= 1
        else:
            counter += 2

    return total


key = find_key()
print(f"The encryption key is: {key}")
