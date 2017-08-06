
def reverse(arg):
 length = len(arg)
 reverse = ''
 while length != 0:
  reverse += s[length-1]
  length -= 1
 return reverse

def lreverse(arg):
 larg = list(arg)
 larg.reverse()
 reverse = ''
 for e in larg:
  reverse += e
 return reverse

s = "stressed"
print(reverse(s))
print(lreverse(s))

