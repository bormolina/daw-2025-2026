nums = [5, 2, 1, 0, 7, 2, 11, 4, 2, 10]

sumatoria = 0

for n in nums:
    sumatoria += n

media = sumatoria / len(nums)

print(f"La media es {media:.2f}")