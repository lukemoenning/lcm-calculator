def user_input():
    num_string = input("Enter any amount of numbers you wish to find the least common multiple of.")
    temp = num_string.split()
    num_list = list()

# sorts num_list in descending order to improve runtime by minimizing the number of times multiplier must be incremented
    try:
        for num in temp:
            num_list.append(int(num))
            num_list.sort(reverse=True)
    except ValueError:
        print("This calculator only works with integers.")

    return num_list
 

def lcm_calculator(nums):
    multiplier = 1
    found = False

    while not found:
        for i in range(1, len(nums)):
            if (multiplier * nums[0]) % nums[i] != 0:
                found = False
                break
            else:
                lcm = nums[0] * multiplier
                found = True
        multiplier += 1

    nums.sort()
    print("\nThe least common multiple of "+str(nums)+" is "+str(lcm))


lcm_calculator(user_input())
