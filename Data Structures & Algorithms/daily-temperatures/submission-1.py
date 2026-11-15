class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        
        # naive solution first as always
        # nested loop that checks the next highest value for each number in the array
        # for i in range(len(temperatures)-1):
        #     next_warm = 0
        #     for j in range(i,len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             result[i] = next_warm
        #             break
        #         else: 
        #             next_warm += 1

        # so for a better solution we can prob get to O(n)
        # for that we can use a stack to push each element
        # before pushing we check against top element
        # if the element we wanna push is larger than top of stack
        # pop top of stack and store new_elem_index - popped_elem_index in result[idx]

        stack = []
        
        for i in range(len(temperatures)):
            t = temperatures[i]
            if stack:
                top = stack[-1]
                while t > top[0]:
                    result[top[1]] = i - top[1]
                    stack.pop()
                    if not stack:
                        break
                    top = stack[-1]

            stack.append((t,i))

        for elem in stack:
            result[elem[1]] = 0
            

        return result