# You are given an array of strings words and a string chars.

# A string is good if it can be formed by characters from chars (each character can only be used once).
# Return the sum of lengths of all good strings in words.

# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: 
# The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

def word_length(word_list,char_str):
    if (not word_list) or (not char_str):
        return
    
    char_dict = {}
    result_list=[]
    count = 0
    for char in char_str:
        if char in char_dict:
            char_dict[char] = char_dict[char] + 1
        else:
            char_dict[char] = 1
    
    for word in word_list:
        word_dict = {}
        for ch in word:
            if ch in word_dict:
                word_dict[ch] = word_dict[ch] + 1
            else:
                word_dict[ch] = 1

        flag = False
        for key,val in word_dict.items():
            if key not in char_dict or  val > char_dict[key]:
                flag = True
                break
        if not flag:
            result_list.append(word)
            count = count + len(word)

    print(result_list)
    print(count)