
# l = [9,9]
#
# def func(l):
#     m = int(''.join(map(str, l))) +1
#     n = []
#     for i in str(m):
#         n.append(i)
#     return list(n)
#
#
# print(func(l))


# def f1(l):
#     str_l = ''.join(map(str, l))
#
#     int_l = int(str_l) + 1
#     str2_l = str(int_l)
#     return [int(i) for i in str2_l]
#
# print(f1([1,9,9]))

# l = (1, 2, 2, 3, 3)
# def unique_in_order(sequence):
#     result = []
#     for i, item in enumerate(sequence):    #  har bir obektni va uni indeksini oladi
#         if i == 0 or sequence[i] != sequence[i - 1]:
#             result.append(item)
#     return result
#
# print(unique_in_order(l))


# input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
# output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]
# def open_or_senior(data):
#     l = []
#     for x in data:
#         if x[0]>=55 and x[1]>7:
#             l.append("Senior")
#         else:
#             l.append('Open')
#     return l
# print(open_or_senior(input))



# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]

# def comp(a,b):
#     if a is None or b is None:
#         return False
#     a_squard = sorted([i**2 for i in a])
#     b_squard = sorted(b)
#     return a_squard==b_squard
# print(comp(a,b))


# def descending_order(num):
#     num_str = str(num)
#     filter_num = sorted([i for i in num_str], reverse=True)
#     return int(''.join(filter_num))
#
# print(descending_order(125432))


# def main(a,b):
#     x1 = a//b
#     x2 = a/b
#     return x1,x2
# if __name__=='__main__':
#     print(main(15,9))


# if __name__ == '__main__':
#     n = int(input(5))
#     for i in range(n-1):
#         print(i**2)


# l = [1,2,3,5]
# def list_kv(list):
#     l =[]
#     for i in list:
#         l.append(i**2)
#     return l
# print(list_kv(l))


# from itertools import permutations
# def func(str1, str2):
#     komb = [''.join(p) for p in permutations(str1)]
#     print(komb)
#     if str2 in komb:
#         return True
#     else:
#         return False
#
# print(func('ask', 'gerwfewgwreg'))

"""
s = 'salom'
d = 'msalo' True
j = 'molsa' True
k = 'saolm' False
"""



# def func(str1, str2):
#     if len(str1)!=len(str2):
#         return False
#
#     for i in range(len(str1)):
#         shifted = str1[i:]+str1[:i]
#         print(shifted)
#         if shifted==str2:
#             return True
#     return False
#
# print(func('assalom', 'alomass'))

# def func(s, goal):
#     if len(s)!=len(goal):
#         return False
#
#     elif goal in s+s:
#         print(s+s)
#         return True
#
#     return False
#
# print(func('Ozodbek', 'bekOzod'))



# if __name__ == '__main__':
#     n = int(input().strip())
#     if n%2==1:
#         print("Weird")
#     elif n in [2,4]:
#         print('Not Weird')
#     elif n%2==0 and (n>6, n<21):
#         print('Weird')
#     elif n%2==0 and n>20:
#         print('Not Weird')


# def func(n):
#     for i in range(1, n+1):
#         print(i, end='')
#
# func(32)

"""
n = p*q     p, q - tub son
"""


# def ikkita_tub_son(n):
#     def tub_mi(son):
#         if son < 2:
#             return False
#         for i in range(2, int(son ** 0.5) + 1):
#             if son % i == 0:
#                 return False
#         return True
#
#     for a in range(2, n):
#         for b in range(a + 1, n):
#             if tub_mi(a) and tub_mi(b):
#                 return a, b
#
#     return None

# print(ikkita_tub_son(9379))


# def tub_sonlar(n):
#     """
#     Belgilangan oraliqda tub sonlarni qaytaradi
#
#     Args:
#     boshlangich (int): Qidiruvni boshlash nuqtasi
#     oxirgi (int): Qidiruvni tugash nuqtasi
#
#     Returns:
#     list: Tub sonlar ro'yxati
#     """
#     tub_sonlar_royxati = []
#
#     for son in range(2, n + 1):
#         tub_bo_lmi = False
#
#         for bo_luvchi in range(2, int(son ** 0.5) + 1):
#             if son % bo_luvchi == 0:
#                 tub_bo_lmi = True
#                 break
#
#         if not tub_bo_lmi:
#             tub_sonlar_royxati.append(son)
#
#     return tub_sonlar_royxati
#
#
# # Misol
# print(tub_sonlar(50))


# def is_leap(year):
#     leap = False
#     if year%400==0:
#         leap=True
#     elif year%100==0:
#         leap=False
#
#     return leap
#
#
# year = int(input('yil='))
# print(is_leap(year))

allowed = "ab"
words = ["ad", "bd", "aaab", "baa", "badab"]

# def func(allowed:str, words:list[str]):
#     l = set(allowed)
#     count = 0
#     for word in words:
#         for char in word:
#             if char not in l:
#                 count+=1
#                 break
#     return len(words)-count
#
# print(func('ad',['ab', 'add', 'abc', 'adda', 'daa']))


# class Solution:
#     def countConsistentStrings(self, allowed:str, words:list[str]):
#         allowed_set = set(allowed)
#         count = 0
#
#         for word in words:
#             if set(word).issubset(allowed_set):
#                 count+=1
#
#         return count
#
# misol = Solution()
# n = misol.countConsistentStrings(allowed, words)
# print(n)




