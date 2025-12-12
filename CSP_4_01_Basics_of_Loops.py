#All questions must use a loop for full points.
import random


def oddNumbers(n:int) ->str:
    """
    Print out all odd numbers from 1 to n(inclusive) in a single string seperated by spaces.
    example oddNumbers(5) -> "1 3 5"
    example oddNumbers(8) -> "1 3 5 7"
    example oddNumbers(-8) -> ""
    """
    answer = ""
    for odd in range(1,n+1,1):
        if odd == n:
            answer += ""
        elif odd%2 ==0:
            answer += " "
        if odd%2 == 1:
            answer += str(odd)
    print(answer)
    return answer
# oddNumbers(46)
def backwards(n)-> int:
    """
    modify the below function such that it prints out all the numbers from n to 1
    inclusive starting at n and counting down to 1
    example backwards(5) -> "5 4 3 2 1"
    example backwards(8) -> "8 7 6 5 4 3 2 1"
    example backwards(-2) -> ""
    """
    answer = ""
    for back in range(n,0,-1):
        if back > 1:
            answer += str(back) + " "
        else:
            answer += str(back)
    print(answer)
    return(answer)
# backwards(6)

def randomRepeating():
    """
    Print out a random number from 1-10 until you get a 10. Then print out how many
    times it took to roll a 10
    NOTE: Given randomness no test for this question
    :return:
    """
    tries = 0
    repeat = 0
    while repeat < 10:
        repeat = random.randint(1,10)
        print(repeat, end = " ")
        tries +=1
    print(f"it took {tries} tries to get a 10")
# randomRepeating()
def randomRange(n):
    """
    Generate a random number from 1 to 100 n number of times. Then after that is
    done print out what the highest number and the lowers number was from the rolled numbers.
    NOTE: Given randomness no test for this question
    :param n:
    :return:
    """
    firstRoll = random.randint(1,100)
    minNum = firstRoll
    maxNum = firstRoll
    print(firstRoll)
    for high in range(2,n+1):
        roll = random.randint(1,100)
        print(roll, end = " ")
        if roll < minNum:
            minNum = roll
        if roll > maxNum:
            maxNum = roll
    print("max", maxNum)
    print("min", minNum)
#randomRange(5)
def reverse(word:str)->str:
    """
    Takes in a string as an argument and return the given string in reverse.
    example reverse("cat") -> "tac"
    example reverse("Hello") -> "olleH"
    """
    answer = ""
    for back in range(len(word)-1, -1, -1):
        answer += word[back]
    print(answer)
    return answer
#
def fizzBuzzContinuous(n):
    """
    Modify the function such that it does the fizzbuzz operation on all numbers
    from 1 to n(inclusive).
    Fizz buzz is defined as
    if the number is divisble by 3 print fizz
    if the number is divisible by 5 print buzz
    if the number is divisible by both 3 and 5 print fizzbuzz
    if none of the above apply print the number.

    As with above questions add each anseer to a string and return the final string.
    :param n:
    :return:
    """
    ans = ""
    for i in range(1, n +1, 1):
        if i % 3==0 and i % 5 == 0:
            ans += "fizzbuzz" + " "
        elif i%3 == 0:
            ans += "fizz" + " "
        elif i%5 == 0:
            ans += "buzz" + " "
        else:
            ans += str(i) + " "

    return ans[0:-1]
print(fizzBuzzContinuous(2))

def collatz(n):
    """
    Modify this function such that it mimics the collatz conjecture starting at n
    and prints out each number.
    The collatz conjecture is that if n is an even number divide it by 2. if n is
    an odd number multiply it by 3 and add 1.
    Repeat this process until n == 1.
    :param n:
    :return:
    """
    answer = str(n)+" "
    while n!=1:
        if n%2 ==0:
            n//=2
        elif n%2 ==1:
            n= n* 3+1
        answer+= str(n)+" "
    return answer[0:-1]
print(collatz(9))
def fibonacci(n):
    """
    for the given argument n print out the first n numbers of the fibonacci
    sequence in a single string sperated by spaces.
    The fibonacci sequence is defined as a sequence that starts with 0 then 1 as
    the first two numbers. Every subsequent number is the prior two numbers added together.
    Example fibonacci(6) -> "0 1 1 2 3 5"
    Example fibonacci(10) -> "0 1 1 2 3 5 8 13 21 34"
    Example fibonacci(1) -> "0"
    :param n:
    :return:
    """
    answer = ""
    first = 0
    second = 1
    for prior in range(n):
        if prior <= 1:
            answer += str(prior)+" "
        else:
            add = first + second
            answer += str(add) + " "
            first = second
            second = add
    print(answer)
    return answer[0:-1]
# print(fibonacci(5))