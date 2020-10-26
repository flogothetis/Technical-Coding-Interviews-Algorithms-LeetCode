from  typing import  List
def isPalindrome (string:str, low:int, high:int)->bool:
    while(low < high):
        if string[low] != string[high]:
            return False
        low+=1
        high=-1
    return True


def dfs (string:str, low:int, high:int, curr_res:List[str], all_res: List[List[str]]):
    if (low >=high):
        all_res.append(curr_res.copy())
        return
    for i in range (low, high):
        if(isPalindrome(string, low, i)):
            curr_res.append(string[low:i+1])
            dfs(string, i+1, high, curr_res, all_res)
            curr_res.pop()

# Driver Code
input = "aab"
all_res= []

dfs(input, 0, len(input), [], all_res)
print(all_res)