class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        i = j = 0
        new_list = list(S)
        new_arr = []
        for k in range(0,len(S)):
            if  new_list[k] == '(':
                i = i + 1
                new_arr.append(i)
            else:
                i -= 1
                new_arr.append(i)

        #print(new_arr)
        #print(new_list)
        for k in range(0,len(S)):
            if new_arr[k] == 1 and new_list[k] == '(':
                new_list[k] = ''
            if new_arr[k] == 0 and new_list[k] == ')':
                new_list[k] = ''
        return ''.join(new_list)
        