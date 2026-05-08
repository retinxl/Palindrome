def is_valid_int(user_input):
    try:
        int(user_input)
        return True
    except ValueError:
        return False
    
def is_palindrome(user_input):
    # Reverse the number mathematically and compare it to original
    if user_input < 0:
        return False
    
    temp = user_input
    reversed_num = 0

    while temp > 0:
        reversed_num = reversed_num * 10 + temp % 10
        temp //= 10

    return reversed_num == user_input
    
def main():
    num = input("Enter a number: ")
    print("You entered:",num)

    if not is_valid_int(num):
        print("Invalid Input")
    else:
        if is_palindrome(int(num)):
            print(num,"is a palindrome!")
        else:
            print(num,"is not a palindrome.")

if __name__ == "__main__":
    main()
    