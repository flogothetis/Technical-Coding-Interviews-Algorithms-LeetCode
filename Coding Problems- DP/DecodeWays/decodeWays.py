from typing import Dict

def decodeWaysRec(s:str , pointer:int, cache :Dict[int,int])->int:
    if (pointer >= len(s)):
        return 1

    if pointer in cache:
        return cache[pointer]

    cache[pointer] = 0
    if 1<= int(s[pointer:pointer+1])<=26:
        cache [pointer] += decodeWaysRec(s, pointer+1, cache)

    if pointer+2<=len(s) and 1<= int(s[pointer:pointer+2])<=26:
        cache [pointer] += decodeWaysRec(s, pointer+2, cache)

    return cache[pointer]




if __name__=='__main__':
    s ='1'
    ans = decodeWaysRec(s, 0 , {})
    print (ans)