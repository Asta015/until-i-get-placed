arr = [1,2,3,4,5]

small = sec_small = float("inf")

for num in arr:
    if num < small:
        sec_small = small
        small = num
    elif num < sec_small and num != small:
        sec_small = num

print("second smallest :", sec_small)
