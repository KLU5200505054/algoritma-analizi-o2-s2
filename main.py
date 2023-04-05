import re

ASIZE = 256

def RAITA(x, m, y, n):
   j, bmBc = 0, [m] * ASIZE

   for i in range(m - 1):
      bmBc[ord(x[i])] = m - i - 1
   
   while j <= n - m:
      if x[m - 1] == y[j + m - 1] and x[0] == y[j]:
         if x[1:m - 1] == y[j + 1:j + m - 1]:
            return True
         j += 1
      else:
         j += bmBc[ord(y[j + m - 1])]
   return False


sigh_count = 0
dormouse_count = 0
jury_box_count = 0
swim_count = 0

with open("alice_in_wonderland.txt", "r", encoding="utf-8") as f:
   text = f.read()
   words = re.findall(r'\b\w+\b', text) # metindeki tüm kelimeleri bulan regular expresison

   # Kelimeleri kontrol ediyorum
   for word in words:
      if RAITA('sigh', len('sigh'), word, len(word)):
         sigh_count += 1
      if RAITA('Dormouse', len('Dormouse'), word, len(word)):
         dormouse_count += 1
      if RAITA('jury-box', len('jury-box'), word, len(word)):
         jury_box_count += 1
      if RAITA('swim', len('swim'), word, len(word)):
         swim_count += 1

print("sigh kelimesi sayısı:", sigh_count)
print("Dormouse kelimesi sayısı:", dormouse_count)
print("jury-box kelimesi sayısı:", jury_box_count)
print("swim kelimesi sayısı:", swim_count)
