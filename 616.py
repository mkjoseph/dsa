def addBoldTag(s, words):
    n = len(s)
    bold = [False] * n

    for word in words:
        start = s.find(word)
        while start != -1:
            end = start + len(word)
            for i in range(start, end):
                bold[i] = True
            start = s.find(word, start + 1)

    result = ""
    i = 0
    while i < n:
        if bold[i]:
            result += "<b>"
            while i < n and bold[i]:
                result += s[i]
                i += 1
            result += "</b>"
        else:
            result += s[i]
            i += 1

    return result

# Pass 2 

class Solution:
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        status = [False]*len(s)
        final = ""
        for word in dict:
            start = s.find(word)
            last = len(word)
            while start != -1:
                for i in range(start, last+start):
                    status[i] = True
                start = s.find(word,start+1)
        i = 0
        i = 0
        while i < len(s):
            if status[i]:
                final += "<b>"
                while i < len(s) and status[i]:
                    final += s[i]
                    i += 1
                final += "</b>"
            else:
                final += s[i]
                i += 1
        return final