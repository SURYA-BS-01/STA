def check_sign(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"
    
nums = [5, -2, 0]

for num in nums:
    print(check_sign(num))