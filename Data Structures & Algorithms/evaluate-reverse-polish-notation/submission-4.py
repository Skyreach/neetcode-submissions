import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # here I think a stack is required, we'd append
        # tokens until an operand is found, then apply the
        # operand against the last 2 tokens in the stack
        # then reduce the replaced tokens with the new value

        # Example 1:
        # We add 1
        # We add 2
        # We receive an operator
        # We pop the last 2 tokens and apply +
        # We add the result (3) to the container
        # We add the next token (3) to the container
        # We receive an operand and pop the last 2 values
        # and apply the operator (*) => 9 and add it to the stack
        # we add the next token (4)
        # we find the last operator and apply it, adding it to the stack

        # Assumes there is always only 1 output token

        stack = []

        for token in tokens:
            if (token not in ["+", "-", "*", "/"]):
                stack.append(token)
                continue
            elif len(stack) == 1:
                continue

            term2, term1 = int(stack.pop()), int(stack.pop())
            if token == "+":
                stack.append(term1 + term2)
            elif token == "-":
                stack.append(term1 - term2)
            elif token == "*":
                stack.append(term1 * term2)
            elif token == "/":
                # note the round toward 0 trap
                # by wrapping in int we get both // and round to 0
                stack.append(int(term1 / term2))

        return int(stack[0])
            
        