arr= [1,2,3,4,5]

largest = sec_largest = float('-inf')

for num in arr:
    if num > largest:
        sec_largest = largest

        largest = num
    elif num > sec_largest and num != largest:
        sec_largest = num

print("sec largest:",sec_largest)

