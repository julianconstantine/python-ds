__author__ = 'Julian'

# EXERCISE 3: Implement a direct infix evaluator that combines the functionality of infix-to-postfix conversion and
# the postfix evaluation algorithm. Your evaluator should process infix tokens from left to right and use two stacks,
# one for operators and one for operands, to perform the evaluation.


class Stack:
    def __init__(self):  # Initialize Stack
        self.items = []

    def isEmpty(self):  # Returns True if Stack is empty
         return self.items == []

    def push(self, item):  # Adds item to top of Stack
        self.items.append(item)

    def pop(self):  # Removes item at top of Stack
        return self.items.pop()

    def peek(self):  # Returns item at top of Stack without removing it
        return self.items[len(self.items)-1]

    def size(self):  # Returns number of items in the Stack
        return len(self.items)


def evalInfix(infix):
    # Step 1: Define the infix-to-postfix converter within the function.
    def infixToPostfix(infix):
        # Creates dictionary to hold order of operators ("precedence values") for infix expressions
        prec = {}
        prec["^"] = 4
        prec["*"] = 3
        prec["/"] = 3
        prec["+"] = 2
        prec["-"] = 2
        prec["("] = 1

        opstack = Stack()  # Stack for storing operators
        postfix = []  # Empty list for storing postfix expression

        for token in infix.split():
            # If token is a letter or number, append to postfix list
            if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
                postfix.append(token)
            # If token is a left parenthesis, append to operator Stack
            elif token == "(":
                opstack.push(token)
            # If token is a right parenthesis, pop operator Stack and add to postfix list until
            # you hit a left parenthesis
            elif token == ")":
                top = opstack.pop()

                while top != "(":
                    postfix.append(top)
                    top = opstack.pop()
            # Otherwise, pop the operator Stack and append to the postfix list until either the
            # operator Stack is empty or you run into an operator over which the token has precedence
            else:
                while (not opstack.isEmpty()) and (prec[opstack.peek()] >= prec[token]):
                      postfix.append(opstack.pop())

                opstack.push(token)

        # Pop the operator Stack and add to postfix list until the Stack is empty
        while not opstack.isEmpty():
            postfix.append(opstack.pop())

        # Convert postfix list to string with list elements separated by blank spaces
        postfix = " ".join(postfix)

        return postfix

    # Step 2: Convert the infix expression to a postfix expression
    postfix = infixToPostfix(infix)

    # Step 3: Define the postfix evaluator within the function
    def evalPostfix(postfix):

        # Define the operandMath() function
        def operandMath(operator, A, B):

            if operator == "*":
                return A*B
            elif operator == "/":
                return A/B
            elif operator == "+":
                return A+B
            elif operator == "-":
                return A-B
            elif operator == "^":
                return A**B

        operand = Stack()  # Creates operand Stack

        for token in postfix.split():
            # If token is a number, convert it to an integer and push to operand Stack
            if token in "0123456789":
                operand.push(int(token))
            # Otherwise, token must be an operator, so pop the operand Stack twice and
            # evaluate the expression A OPERATOR B using the operandMath() function then
            # push result to operand Stack
            else:
                A = operand.pop()
                B = operand.pop()
                evalAB = operandMath(token, A, B)
                operand.push(evalAB)

        # Pop final result of operand Stack
        out = operand.pop()

        return out

    # Step 4: Evaluate the postfix expression and return
    return evalPostfix(postfix)

evalInfix("3 + 4")

# THIS ONE DOESN'T WORK :(
evalInfix("(20 * ( 9 / 7)) + ((87.5 + 22.222) * 0.98)")


# EXERCISE 4: Turn your direct infix evaluator from the previous problem into a calculator.

