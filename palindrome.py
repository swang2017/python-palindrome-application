inputWord = raw_input("Please enter a word\n")
listLetter = list(inputWord)
isPalindrome = False

print(listLetter)
print(len(listLetter))
for index in range (0,len(inputWord)):
        if inputWord[index] != inputWord[(len(inputWord)-1)-index]:
            isPalindrome = False
            break
        else:
            isPalindrome = True

if isPalindrome:
    print("Yes palindrome")
else:
    print("Not palindrome")
