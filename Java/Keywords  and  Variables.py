What are Keywords?
Keywords in java are reserved words which have a predefined meaning;
         you write java code by using a combination of these keywords with other elements such as variable ,data types ,&operators
    Unused Keywords:
            goto: Reserved but not used.
            const: Reserved but not used (use final instead).

what are variables?
 Variables are containers used to store data values. They have a name, a data type, and a value.
    Examples:
           int age = 25;
               Stores an integer value.

           double price = 19.99;
               Stores a decimal value.

           String name = "Alice";
               Stores a sequence of characters (text).

           boolean isJavaFun = true;
                Stores a true or false value.
  Program:

class Variables
{
    public static void main(String[] args)
    {
        byte myByteMaxValue = Byte.MAX_VALUE;
        byte myByteMinValue = Byte.MIN_VALUE;
        System.out.println("The byte Maximum value is ="+myByteMaxValue);
        System.out.println("The byte Minimum value is ="+myByteMinValue);

        short myShortMaxValue = Short.MAX_VALUE;
        short myShortMinValue = Short.MIN_VALUE;
        System.out.println("The short Maximum value is ="+myShortMaxValue);
        System.out.println("The short Minimum value is ="+myShortMinValue);

        int myIntMaxValue = Integer.MAX_VALUE;
        int myIntMinValue = Integer.MIN_VALUE;
        System.out.println("The integer Maximum value is ="+myIntMaxValue);
        System.out.println("The integer Minimum value is ="+myIntMinValue);

        long myLongMaxValue = Long.MAX_VALUE;
        long myLongMinValue = Long.MIN_VALUE;
        System.out.println("The long maximum value is ="+myLongMaxValue);
        System.out.println("The long minimum value is ="+myLongMinValue);

        float myFloatMaxValue = Float.MAX_VALUE;
        float myFloatMinValue = Float.MIN_VALUE;
        System.out.println("The float maximum value is ="+myFloatMaxValue);
        System.out.println("The float minimum value is ="+myFloatMinValue);

        double myDoubleMaxValue = Double.MAX_VALUE;
        double myDoubleMinValue = Double.MIN_VALUE;
        System.out.println("The double maximum value is ="+myDoubleMaxValue);
        System.out.println("The double minimum value is ="+myDoubleMinValue);

        char myCharMaxValue = Character.MAX_VALUE;
        char myCharMinValue = Character.MIN_VALUE;
        System.out.println("The character maximum value is ="+myCharMaxValue);
        System.out.println("The character minimum value is ="+myCharMinValue);

        char letter = 'A';
        System.out.println(letter);

        boolean inActive = false;
        System.out.println(inActive);
  }
}

Output:

The byte Maximum value is =127
The byte Minimum value is =-128
The short Maximum value is =32767
The short Minimum value is =-32768
The integer Maximum value is =2147483647
The integer Minimum value is =-2147483648
The long maximum value is =9223372036854775807
The long minimum value is =-9223372036854775808
The float maximum value is =3.4028235E38
The float minimum value is =1.4E-45
The double maximum value is =1.7976931348623157E308
The double minimum value is =4.9E-324
The character maximum value is =￿
The character minimum value is = 
A
false

