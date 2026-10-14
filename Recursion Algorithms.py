def sum_digits(num):
    if num < 10:
        return num
    return sum_digits(num // 10) + num % 10
def is_sorted(list):
    if len(list)==1:
        return True
    if is_sorted(list[1:]) and list[0] < list[1]:
        return True
    else :
        return False
def counter(list,target):
    if len(list)<=1:
        if list[0]==target:
            return 1
        else:
            return 0
    if list[0]==target:
        return counter(list[1:],target)+1
    else: return counter(list[1:],target)
def largest(list):
    if len(list)==1:
        return list[0]
    if list[0]>largest(list[1:]):
        return list[0]
    else:
        return largest(list[1:])
def binary_search(nums, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return binary_search(nums, target, low, mid - 1)
    else:
        return binary_search(nums, target, mid + 1, high)
def remove_char(string, char):
    if not string:
        return string
    if char==string[0]:
        return remove_char(string[1:], char)
    else:
        return string[0]+remove_char(string[1:], char)
def power(x, n):
    if n==0:
        return 1
    half=power(x, n//2)
    if n%2==0:
        return half*half
    else:
        return half*half*x
def binary_strings(n):
    values=[]
    if n==0:
        return []
    if n==1:
        return ['0','1']
    for string in binary_strings(n-1):
        values.append(string+'0')
        values.append(string+'1')
    return values
def binary_string(n):
    values=[]
    if n==0:
        return ['']

    def build(current):
        if len(current) == n:
            values.append(current)
            return
        else:
            build(current+'0')
            build(current+'1')
    build('')
    return values
def fibonacci(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
