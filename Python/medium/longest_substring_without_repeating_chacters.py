#=========================================================================================================================#
# Name:                                                  Harold Sy                                                        #
# Title: ............................................... longest_substring_without_repeating_chacters.py                  #
# 1st Method used: ..................................... Brute Force                                                      #
# Submitted program runtime: ........................... 15 ms                                                            #
# Time complexity ...................................... O(n^2)                                                           #
# Beats: ............................................... 90.58%                                                           #
# 2nd Method used: ..................................... Sliding window technique                                         #
# Submitted program runtime: ........................... 12 ms                                                            #
# Beats: ............................................... 94.91%                                                           #
# Time complexity: ..................................... O(n)                                                             #
# Difficulty: .......................................... Medium                                                           #
# Time for completion .................................. 15 minutes                                                       #
#                                                                                                                         #
# Mission: ............................................. Given a string 's', find the length of the longest substring     #
#                                                        without duplicate characters.                                    #
#                                                                                                                         #
# Definitions: ......................................... Substring - a substring is simply a portion or slice of a        #
#                                                                    string. This means that we can take a slice of the   #
#                                                                    string and if put back into the string it will fit   #
#                                                                    back in like a puzzle piece.                         #
#                                                        Subsequence - a subsequence is simply a sequence of a string     #
#                                                                    that retains its order but cannot be put back like   #
#                                                                    a puzzle piece.                                      # 
#                                                                                                                         #
# Assumptions: ......................................... ** None given                                                    #
#                                                                                                                         #
# Constraints: ......................................... ** 0 <= s.length <= 5 * 10^4                                     #
#                                                           length of s is greater than 0 and less than 10 to the 4th     #
#                                                           power of characters                                           #
#                                                        ** s consists of English letters, digits, symbols and spaces     #
#                                                                                                                         #
# Example 1: ........................................... Input: s = "abcabcdd"                                            #
#                                                        Output: =====================================================> 3 #
#                                                        Explanation: The answer is "abc", with the length of 3.          #
#                                                                                                                         #
# Example 2: ........................................... Input: s = "bbbbb"                                               #
#                                                        output: =====================================================> 1 #
#                                                        Explaniation: The answer is "b", with the length of 1.           #
#                                                                                                                         #
# Example 3: ........................................... Input: s = "pwwkew"                                              #
#                                                        Output: =====================================================> 3 #
#                                                        Explanation: The answer is "wke", with length of 3.              #
#                                                        Notice that the answer must be a substring, "pwke" is a sub-     #
#                                                        sequence and not a substring.                                    #
#                                                                                                                         #
# Provided by leetcode ................................. class Solution(object):                                          #
#                                                            def lengthOfLongestSubstring(self, s):                       #
#                                                                """                                                      #
#                                                                :type s: str                                             #
#                                                                :rtype: int                                              #
#                                                                """                                                      #
#                                                                                                                         #
#=========================================================================================================================#
#                                                                                                                         #  
# Original code submitted:                                                                                                #
#                                                                                                                         #
# class Solution(object):                                                                                                 #
#    def lengthOfLongestSubstring(self, s):                                                                               #
#        """                                                                                                              #
#        :type s: str                                                                                                     #
#        :rtype: int                                                                                                      #
#        """                                                                                                              #
#                                                                                                                         #
#        string_holder = ''                                                                                               #
#        longest_substring = ''                                                                                           #
#        for character in s:                                                                                              #
#            if character not in string_holder:                                                                           #
#                string_holder += character                                                                               #
#            else:                                                                                                        #
#                if len(longest_substring) < len(string_holder):                                                          #
#                    longest_substring = string_holder                                                                    #
#                if character == string_holder[-1]:                                                                       #
#                    string_holder = ''                                                                                   #
#                    string_holder += character                                                                           #
#                else:                                                                                                    #
#                    character_index = string_holder.find(character)                                                      #
#                    string_holder = string_holder[character_index+1:]                                                    #
#                    string_holder += character                                                                           #
#        if len(longest_substring) < len(string_holder):                                                                  #
#                    longest_substring = string_holder                                                                    #
#        print(longest_substring)                                                                                         #
#        return len(longest_substring)                                                                                    #
#                                                                                                                         #
# string1 = "abcabcbb"                                                                                                    #
# string2 = "bbbb"                                                                                                        #
# string3 = "pwwkew"                                                                                                      #
# string4 = "jbpnbwwd"                                                                                                    #
#                                                                                                                         #
# my_solution = Solution()                                                                                                #
# print(my_solution.lengthOfLongestSubstring(string1))                                                                    #
# print(my_solution.lengthOfLongestSubstring(string2))                                                                    #
# print(my_solution.lengthOfLongestSubstring(string3))                                                                    #
# print(my_solution.lengthOfLongestSubstring(string4))                                                                    #
#                                                                                                                         #
#=========================================================================================================================#
#                                                                                                                         #
# Things learned from this problem: .................. *** Getting the longest substring of a string means getting the    #
#                                                           longest possible thus getting rid of the duplicate if it is   #
#                                                           at the beginning of the string or getting rid of characters   #
#                                                           up to and including the duplicate character before getting    #
#                                                           the next letter and concatenating it to the old string!       # 
#=========================================================================================================================#

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        char_index = {}
        start = 0
        max_length = 0

        for i, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1  # move start to one past the duplicate

            char_index[char] = i  # update the last seen index
            max_length = max(max_length, i - start + 1)

        return max_length
    
string1 = "abcabcbb"
string2 = "bbbb"
string3 = "pwwkew"
string4 = "jbpnbwwd"

my_solution = Solution()
print(my_solution.lengthOfLongestSubstring(string1))
print(my_solution.lengthOfLongestSubstring(string2))
print(my_solution.lengthOfLongestSubstring(string3))
print(my_solution.lengthOfLongestSubstring(string4))
