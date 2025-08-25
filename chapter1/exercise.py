"""
1. Which of the following are operators, and which are values?
   * 'hello'  --> value
   * -88.8    --> value
   * -        --> Operator
   * /        --> Operator
   * +        --> Operator
   * 52       --> value

2. Which of the following is a variable, and which is a string?
   * spam  --> variable
   * 'spam' -- > string

3. Name three data types.
---> int
---> float
---> string

4. What is an expression made up of? What do all expressions do?
--> An expression is made up for variables, values and operators 
--> They all work together to sing a single value as an answer 

5. This chapter introduced assignment statements, like spam = 10.
   What is the difference between an expression and a statement?

6. What does the variable bacon contain after the following code runs?
   bacon = 20
   bacon + 1
--> The variable bacon contains or holds an integer 20 but will not be evaluated in the next expression because of a missing assignment operator = for it to be
--> bacon = bacon + 1

7. What should the following two expressions evaluate to?
   'spam' + 'spamspam'
   'spam' * 3
---> spamspamspam

8. Why is eggs a valid variable name while 100 is invalid?
--> By naming convention in python you can start a variable name with small letter to be a word but you can with number only, except it's combined with letters

9. What three functions can be used to get the integer, floating-point
   number, or string version of a value?
--> int()
--> float()
--> str()

10. Why does this expression cause an error? How can you fix it?
    'I have eaten ' + 99 + ' burritos.'
--> Because 99 is not properly type casted, if you want it to be an integer displayed it should be as str(99) with the concatenation to be evaluated as string
--> 'I have eaten ' + str(99) + ' burritos.'
"""
