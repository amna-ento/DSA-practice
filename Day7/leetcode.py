class Solution(object):
    def sequence(self, s):
        seen = set()
        repeated = set()

        for i in range(len(s) - 9):
            seq = s[i:i + 10]

            if seq in seen:
                repeated.add(seq)
            else:
                seen.add(seq)

        return list(repeated)


solution = Solution()

s = input(str("enter the strng: "))


result = solution.sequence(s)


print("Input:", s)
print("Repeated 10-letter sequences:", result)