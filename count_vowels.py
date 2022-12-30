vowels = 'aeiou'

strr = 'Hello this is a test'

strr = strr.casefold()

count = {}.fromkeys(vowels,0)
for char in strr:
   if char in count:
       count[char] += 1

print(count)
