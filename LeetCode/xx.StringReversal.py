import sys

class Solution:
  def reverseString(self, s: str) -> str:
    l = len(s)
    last = l-1
    m = l // 2

    a = list(s)
    for i in range(m):
      c = a[i]
      a[i] = a[last-i] 
      a[last-i] = c

    return "".join(a)

def main():
  args = sys.argv[1:]
  input = 'Ooops !'

  if len(args) > 0: input = args[0]

  s = Solution()
  print('--->', s.reverseString(input))

if __name__ == '__main__':
  main()