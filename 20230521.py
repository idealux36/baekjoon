# 1032: 성공
# n = int(input())
# searches = []
# for i in range(n):
#     searches.append(input())
# txt_len = len(searches[0])
# pattern = []
# for i in range(txt_len):
#     letter = searches[0][i]
#     for j in range(1, n):
#         if letter != searches[j][i]:
#             letter = '?'
#             break
#     pattern.append(letter)
# print(''.join(pattern))

# 1052: 포기
# 1 1 1 -> 2 1 -> 2 1 +1 -> 2 2 -> 4 = 4*1
# 1 1 1 1 1 1 1 1 1 1 1 1 1
# 2 2 2 2 2 2 1
# 4 4 4 1 -> 4 4 4 1 +3 -> 8 8 = 8*2

# 1 1 1 1 1 1 1 1
# 2 2 2 2 +2 = 2*5

# 1*1000000 -> 2*500000 -> 4*250000

# 1015808 -> 507904 -> 253,952 -> 126,976 -> 63,488

# 1310720

# n, k = map(int, input().split())
# op = 1
# while n > op*k:
#     op *= 2
# print(op*k-n)

# 1010
def fact(n):
    if n==1: return 1
    else: return n*fact(n-1)

def combi(n, r):
    if n==r: return 1
    return int(fact(n)/(fact(r)*fact(n-r)))

n = int(input())
for i in range(n):
    n, m = map(int, input().split())
    print(combi(m, n))
