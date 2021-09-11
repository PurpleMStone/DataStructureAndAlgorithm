# ------------------- 1. 寻找回文子串 ---------------------------------
def longestPalindrome(s: str) -> str:
    longest_str = ""
    n = len(s)

    for i in range(n):
        # 针对回文串长度为奇数的情形
        str1 = palindrome(s, i, i)

        # 针对回文串长度为偶数的情形
        str2 = palindrome(s, i, i + 1)

        longest_str = str1 if len(str1) > len(longest_str) else longest_str
        longest_str = str2 if len(str2) > len(longest_str) else longest_str

    return longest_str


def palindrome(s: str, l: int, r: int) -> str:
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1: r]


def isPalindrome(s: str) -> bool:
    """
    判断是否为回文子串：如"A man, a plan, a canal: Panama", 输出 true
    因为"amanaplanacanalpanama" 是回文串
    """
    newstring = ''
    for i in s.lower():
        if (i <= '9' and i >= '0') or (i >= 'a' and i <= 'z'):
            newstring += i
    print(newstring)

    if len(newstring) % 2 == 0:
        l = len(newstring) // 2 - 1
        r = l + 1
    else:
        l = len(newstring) // 2
        r = l

    while l >= 0 and r < len(newstring):
        if newstring[l] != newstring[r]:
            return False
        l -= 1
        r += 1

    return True
