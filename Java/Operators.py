what are operators?
 Operators are symbols that perform operations on one or more operands(operands means operands are the values or 
variables on which operators act to perform a specific operation.In simple terms, when you have an expression 
like x + y, x and y are the operands, and + is the operator performing the addition operation on them.) to produce a result.

Examples:

Arithmetic Operators: 
      Perform mathematical operations like addition, subtraction, multiplication, division, and modulus.
             Example: int result = 10 + 5;

Assignment Operators:
      Assign values to variables.
          Example: int x = 10;

Comparison Operators: 
            Compare two values and return a boolean result.
                    Example: boolean isEqual = (x == y);

Logical Operators: 
        Perform logical operations like AND, OR, and NOT.
              Example: boolean isTrue = (x > 5 && y < 10);

Bitwise Operators: 
         Perform bit-level operations on operands.
             Example: int result = num1 & num2;

Program:
class Variables
{
    public static void main(String[] args)
    {
       // Arithmetic Operator
        int n1 = 5;
        int n2 = 5;
        System.out.println(n1 + n2);
        System.out.println(n1 - n2);
        System.out.println(n1 * n2);
        System.out.println(n1 / n2);
        System.out.println(n1 % n2);

        //Assignment Operator
        int myNumber = 0;
        myNumber += 1;
        System.out.println(myNumber);

        myNumber -= 1;
        System.out.println(myNumber);

        myNumber *= 1;
        System.out.println(myNumber);

        myNumber %= 1;
        System.out.println(myNumber);


        myNumber =0;
       System.out.println("prifix increment ="+ ++myNumber);
        System.out.println("postfix increment ="+ myNumber++);

        System.out.println("prifix decrement ="+ --myNumber);
        System.out.println("postfix decrement ="+ myNumber--);

    }
}

Output:

10
0
25
1
0
1
0
0
0
prifix increment =1
postfix increment =1
prifix decrement =1
postfix decrement =1

 
