'''
> While statement is used to repeatedly execute a block of code
     as long as a specified condition is true. 
> Condition is an expression that evaluates to True or False. 
    As long as the condition remains True, the code block under the while loop will continue to execute repeatedly.
       Once the condition becomes False, the loop terminates, and the program continues executing the code that follows the loop.     
Syntax:

while condition:
    # code block to be executed as long as condition is true

Program:

count = 1
while count <= 5:
    print(count)
    count += 1
