from datetime import datetime

if __name__ == '__main__':
    my_string = 'Python Programming'
    print(len(my_string))   # length of the string object
    print(my_string[0])     # first character of the string
    print(my_string[-1])    # last character of the string
    print(my_string[-3])    # last 3rd character of the string
    print(my_string[0:6])   # first 6  'Python
    print(my_string[:6])    # first 6  'Python
    print(my_string[7:10])  # 7 to 10 'Pro'
    print(my_string[7:])    # 7 to end 'Programming
    print(my_string[:])     # All