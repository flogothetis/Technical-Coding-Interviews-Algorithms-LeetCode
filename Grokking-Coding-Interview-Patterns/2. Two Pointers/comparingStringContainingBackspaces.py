

# O(N +M)
# N : Length of string 1
# M : Length of string 2

def compareStringsContainingBackSpaces (string1, string2):



	pointer1 = len(string1) - 1
	pointer2 = len(string2) - 1

	while (pointer1 >=0 and pointer2>=0):

		count1 = 0
		while (pointer1>=0 and string1[pointer1] == '#'):
			count1+=1
			pointer1-=1

		pointer1 -=count1

		count2 = 0
		while (pointer2>=0 and string2[pointer2] == '#'):
			count2 +=1
			pointer2-=1
		pointer2-=count2


		if (pointer1 >=0 and pointer2>=0):
			if(string1[pointer1] != string2[pointer2]):
				return False
		pointer2-=1
		pointer1-=1
	return True


def main():
  print(compareStringsContainingBackSpaces("xy#z", "xzz#"))
  print(compareStringsContainingBackSpaces("xy#z", "xyz#"))
  print(compareStringsContainingBackSpaces("xp#", "xyz##"))
  print(compareStringsContainingBackSpaces("xywrrmp", "xywrrmu#p"))


main()
