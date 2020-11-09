'''
Rearrange String K Distance Apart (hard) #
Given a string and a number ‘K’, find if the string can be rearranged such that the same characters are at least ‘K’
distance apart from each other.
'''

from heapq import *
from collections import deque


from collections import  deque
from heapq import *

# Time Complexity: O(NlogN)
# Space Comp : O(N)
def reorganize_string(str, k):
    # Keep a frequency dictionary
    freq_dict = {}
    for ch in str:
        freq_dict[ch] = freq_dict.get(ch, 0) + 1

    k_window_q = deque()
    max_heap= []
    # Append (character, frequent) into deque
    for (ch, freq) in freq_dict.items():
        heappush(max_heap, (-freq, ch))

    # Pop from max_heap, keep it in a qeue for K timeSlots
    # and the push it again in the max_heep

    result = []
    while (max_heap) :
        freq, ch = heappop(max_heap)
        result.append(ch)
        #decrease freq
        freq = -freq - 1
        #Keep it in queue for K timeSlots
        k_window_q.append((-freq, ch))
        if (len(k_window_q) == k):
            (freq, ch) = k_window_q.popleft()
            if (-freq >0):
                heappush(max_heap, (-freq, ch))

    return "".join(result)  if (len(result) == len(str)) else ""

def main():
  print("Reorganized string: " + reorganize_string("Programming", 3))
  print("Reorganized string: " + reorganize_string("mmpp", 2))
  print("Reorganized string: " + reorganize_string("aab", 2))
  print("Reorganized string: " + reorganize_string("aapa", 3))


main()
