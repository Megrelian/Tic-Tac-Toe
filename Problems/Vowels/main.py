vowels = 'aeiou'
# create your list here
vowels_list = list(vowels)

word = input()
word_list = list(word)

new_list = [x for x in word_list if x in vowels_list]
print(new_list)