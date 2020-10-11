class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            current_string = ''
            if i % 3 == 0:
                current_string += 'Fizz'
            if i % 5 == 0:
                current_string += 'Buzz'
            if i % 3 and i % 5:
                current_string += str(i)
            result.append(current_string)
        return result 
        
