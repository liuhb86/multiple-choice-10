A=0
B=1
C=2
D=3

def check2(a, c):
  return a[5] == c
def check3(a):
  c = a[3]
  tmp = [3,6,2,4]
  d = tmp[c]
  tmp[c] = 4
  if a[tmp[0]] != a[tmp[1]] or a[tmp[0]] != a[tmp[2]]: return False
  return a[d] != a[tmp[0]]
def check4(a, c):
  return a[c[0]] == a[c[1]]
def check5(a,c):
  return a[5] == a[c]
def check6(a,c):
  return a[8]==a[c[0]] and a[8]==a[c[1]]
def check7(count, min_count, c):
  return min_count == count[c]
def check8(a,c):
  return a[c]-a[1] != 1 and a[c]-a[1] != -1
def check9(a,c):
  return (a[1]==a[6]) != (a[c] ==a[5])
def check10(diff, c):
  return diff==c

def check(a):
  if not check2(a, [C,D,A,B][a[2]]): return False
  if not check4(a, [[1,5],[2,7],[1,9],[6,10]][a[4]]): return False
  if not check5(a, [8,4,9,7][a[5]]): return False
  if not check6(a, [[2,4],[1,6],[3,10],[5,9]][a[6]]): return False
  if not check8(a, [7,5,2,10][a[8]]): return False
  if not check9(a, [6,10,2,9][a[9]]): return False
  if not check3(a): return False
  # 7
  count = [0,0,0,0]
  for i in range(1,11):
    count[a[i]] += 1
  min_count = min(count)
  if not check7(count, min_count, [C,B,A,D][a[7]]): return False
  # 10
  max_count = max(count)
  if not check10(max_count-min_count, [3,2,4,1][a[10]]): return False
  return True

answer = []
for i in range(12):
  answer.append(A)

while answer[11] == A:
  if check(answer):
    print [chr(65+x) for x in answer[1:11]]
  for i in range(1, 12):
    c = answer[i]
    if c == D:
      answer[i] = A
    else:
      answer[i] = c + 1
      break
  
