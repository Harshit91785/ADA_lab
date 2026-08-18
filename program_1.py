
# Linear Search
def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


nums = list(map(int, input("Enter elements: ").split()))
target = int(input("Enter target: "))

result = search(nums, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")


# Power Function
def myPow(x, n):
    result = 1.0

    if n < 0:
        x = 1 / x
        n = -n

    for i in range(n):
        result = result * x

    return result


x = float(input("Enter x: "))
n = int(input("Enter n: "))

answer = myPow(x, n)

print("Power:", answer)
