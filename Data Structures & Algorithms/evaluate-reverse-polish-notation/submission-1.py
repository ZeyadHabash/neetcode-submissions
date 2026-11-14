class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+","-","*","/"}
        stack = []

        for token in tokens:
            if token in operators:
                op2 = stack.pop()
                op1 = stack.pop()
                result = 0
                match token:
                    case "+":
                        result = op1 + op2
                    case "-":
                        result = op1 - op2
                    case "*":
                        result = op1 * op2
                    case "/":
                        result = op1 / op2
                stack.append(int(result))
            else:
                stack.append(int(token))

        return stack[0]