def calc_x(V, M, a, t):
  x=[1]*(V+1)
  for n in range(1, V+1):
    sum=0
    for i in range(0, M):
      if n>=t[i]:
        sum += a[i] * t[i] * x[n - t[i]]
    x[n] = sum / n
  return x

def calc_po(x):
  sum = 0
  for item in x:
    sum += item
  return 1 / sum

def calc_pn(x, V, M, a, t):
  p = [1] * (V+1)
  p[0] = calc_po(x)
  for n in range(1,V+1):
    sum = 0
    for i in range(0,M):
      if n>=t[i]:
        sum += a[i] * t[i] * p[n-t[i]]
    p[n] = sum/n
  return p
  
def calc_bn(V, P, t, i=1):
  sum = 0
  for n in range(V - t[i - 1] + 1, V + 1):
    sum += P[n]
  return sum

M = 2 # strumienie ruchu
V = 3 # pojemnosc jednostki w kanalach
t = [[1, 2]] # liczba zadawanych jednostek przetwarzania
a = [[0.4, 1], [0.4, 2], [0.4, 3]]# ruch oferowany

print(f'M={M}\nV={V}\n')

for aI in a:
  for tI in t:
    print("\n")
    print("-"*30, "\n")
    print(f"ai = {aI}\nti = {tI}")
    x = calc_x(V, M, aI, tI)
    P = calc_pn(x, V, M, aI, tI)
    b = [1] * M
    for i in range(M):
      b[i] = calc_bn(V, P, tI, i + 1)
      i += 1
    
    print(f"x: {x}")
    print(f"P: {P}")
    print(f"b: {b}")
