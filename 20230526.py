# 1181
# n = int(input())
# words = []
# for i in range(n):
#     words.append(input())
# words = list(set(words))
# n = len(words)
# len_words = sorted(set([len(w) for w in words]))
# for l in len_words:
#     temp_words = []
#     for i in range(n):
#         if len(words[i]) == l:
#             temp_words.append(words[i])
#     print(*sorted(temp_words), sep='\n')

# 1193
# x = int(input())
# cnt = 1
# while cnt < x:
#     x -= cnt
#     cnt += 1
# if cnt%2 == 1:
#     print(f"{cnt-x+1}/{x}")
# else:
#     print(f"{x}/{cnt-x+1}")

# 1251
# a rre sted -> aerrdets
# a rreste d -> aetserrd
# mob ite l -> bometil
# 실패
# word = input()
# chars = word.split()
# idx1 = 0
# idx2 = 0
# is_solved = 0
# for i in range(26):
#     letter = chr(97+i)
#     if letter in chars:
#         if chars.count(letter) >= 2:
#             is_solved = 1
#             for j in range(len(chars)):
#                 if chars[j] == letter:
#                     idx1 = j
#         else:
#             for j in range(len(chars)):
#                 if chars[j] == letter:
#                     idx1 = j
#                     break

# word = input()
# res = []
# for i in range(1, len(word)-1):
#     for j in range(i+1, len(word)):
#         first = word[:i]
#         second = word[i:j]
#         third = word[j:]
#         res.append("".join(
#             [*reversed(first), 
#              *reversed(second),
#              *reversed(third)]
#         ))
# print(min(res))

# 4673
def d(n):
    return n + sum(map(int, list(str(n))))
i = 1
not_self_numbers = set()
self_numbers = set()
while i<=10000:
    # if i is a self number -> add to self_numbers
    if i not in not_self_numbers:
        j = i
        while j<=10000:
            not_self_numbers.add(j)
            j = d(j)
        self_numbers.add(i)
    i += 1
print(*sorted(self_numbers), sep='\n')
