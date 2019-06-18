'''
Link: https://leetcode.com/discuss/interview-question/306859/Google-phone-screen-Split-strings-to-form-a-palindrome

Given 2 strings a and b with the same length. Strings are alligned one under the other. We can choose an index and split both strings into 4 subtrings: a1 + a2 and b1 + b2. Find out if it's possible to split a and b such that a1 + b2 or a2 + b1 forms a palindrome.

Example 1:

Input: a = "abcbbbb", b = "xxxbcba"
Output: true
Explanation: 

abc|bbbb
xxx|bcba

We can split the strings at index 3. We will get a1 = "abc", a2 = "bbbb" and b1 = "xxx", b2 = "bcba"
a1 + b2 forms a palidnrome "abcbcba" so return true.
Follow-up:
Now it's allowed to split the strings independently:

a|bcbbbb
xxxbcb|a
So in the exampe above a can be splitted into a1 = "a" a2 = "bcbbbb" and b can be splitted b1 = "xxxbcb" b2 = "a". As a result a1+ b2 forms a palindrome "aa". Find the longest palindrome.
'''

def split_to_form_palindrome(a, b):
    for i in range(len(a)):
        a_1, a_2 = a[0:i], a[i:]
        b_1, b_2 = b[0:i], b[i:]
        if (is_palindrome(a_1) and is_palindrome(b_2)) or (is_palindrome(a_2) and is_palindrome(b_1)):
            return i
    return False
    
def is_palindrome(s):
    return s == s[::-1]