import json,os,urllib.request
T='kkkk|||}lrpshnknfklmglkielidkkkk]`^cij{hlxnzoptrklrohmnoggkk]geg`_XahmrcirgtonoqmlnonopmoomlijhhntmgotylktuxkhooggjjeiihdgihcedgeyvWhmvvbphiapmiafaccdc]kmh`orkj'
W=0,1,2,2,3,4
V=(100,280,320,479,929,60000)
A=(-10,1,10,-1);B=(-9,11,9,-11);K=A+B
D={'P':(-10,-20,-11,-9),'N':(-19,-8,12,21,19,8,-12,-21),'B':B,'R':A}
P={p:tuple(V[k]+(ord(T[W[k]*32+((i//10-2)%8)*4+min(i%10-1,8-i%10)%4])-107)*5 for i in range(120))for k,p in enumerate('PNBRQK')}
Y='         \n'
I=Y*2+' rnbqkbnr\n pppppppp\n'+' ........\n'*4+' PPPPPPPP\n RNBQKBNR\n'+Y*2
R0=(I,0,(1,1),(1,1),0,0)
ML=47923;MU=69290
BG=30000;ND=0;TS={};TM={};H=set()
class X(Exception):pass
def u(b,i,p):return b[:i]+p+b[i+1:]
def r(o,n=0):
 b,s,w,c,e,k=o
 return(b[::-1].swapcase(),-s,c,w,(119-e)*(e and not n),(119-k)*(k and not n))
def v(o,m):
 b,s,w,c,e,k=o
 i,j,q=m
 p,t=b[i],b[j]
 d=P[p][j]-P[p][i]
 if t in'pnbrqk':d+=P[t.upper()][119-j]
 if abs(j-k)<2:d+=P['K'][119-j]
 if p=='K'and abs(i-j)==2:d+=P['R'][(i+j)//2]-P['R'][91 if j<i else 98]
 if p=='P':
  if 21<=j<=28:d+=P[q][j]-P['P'][j]
  if j==e:d+=P['P'][119-(j+10)]
 return d
def g(o):
 b,s,w,c,e,k=o
 for i,p in enumerate(b):
  if p not in'PNBRQK':continue
  for d in D.get(p,K):
   j=i+d
   while 1:
    q=b[j]
    if q in' \nPNBRQK':break
    if p=='P':
     if d in(-10,-20)and(q!='.'or d==-20 and(i<81 or b[i-10]!='.')):break
     if d in(-11,-9)and q=='.'and j!=e and abs(j-k)>1:break
     if 21<=j<=28:
      for t in'NBRQ':yield(i,j,t)
      break
    yield(i,j,'')
    if p in'PNK'or q in'pnbrqk':break
    if i in(91,98)and b[j+d]=='K'and w[d<0]:yield(j+d,j-d,'')
    j+=d
def f(o,m):
 b,s,w,c,e,k=o
 i,j,q=m
 p=b[i]
 s+=v(o,m)
 b=u(u(b,j,p),i,'.')
 w=(w[0]*(i!=91),w[1]*(i!=98))
 c=(c[0]*(j!=28),c[1]*(j!=21))
 e2=k2=0
 if p=='K':
  w=(0,0)
  if abs(j-i)==2:
   k2=(i+j)//2;b=u(b,91 if j<i else 98,'.');b=u(b,k2,'R')
 if p=='P':
  if 21<=j<=28:b=u(b,j,q)
  if j-i==-20:e2=i-10
  if j==e:b=u(b,j+10,'.')
 return r((b,s,w,c,e2,k2))
def a(o):
 b,k=o[0],o[5]
 for m in g(o):
  j=m[1]
  if b[j]=='k'or abs(j-k)<2:return m
 return None
def s(o,y,d,t=0):
 global ND
 ND+=1
 if ND>BG:raise X
 q=o[1]
 if q<=-ML:return-MU
 d=max(d,0)
 l,h=-MU,MU
 if not t:
  z=TS.get((o,d))
  if z:l,h=z
  if l>=y:return l
  if h<y:return h
  if d and o in H:return 0
 if not t and d>=3 and any(x in o[0]for x in'RBNQ'):
  n=-s(r(o,1),1-y,d-3)
  if n>q+15:n=q+15
  if n>=y:
   TS[(o,d)]=(n,h)
   return n
 ms=[(x,m)for m in g(o)for x in[v(o,m)]if d or x>=36]
 km=TM.get(o)
 ms.sort(key=lambda z:(z[1]==km,z[0]),reverse=True)
 b=q if d==0 else-MU
 L=0;F=0
 for z,m in ms:
  if z>=ML:c=MU;L=1
  else:
   cp=MU if d>4 else q+z+max(d-1,0)*180
   if cp<y:b=max(b,cp);F=1;break
   c=min(cp,-s(f(o,m),1-y,d-1))
   L|=c>-MU
  if c>b:b=c
  if b>=y:
   if d:TM[o]=m
   break
 if d and not L and not F:
  b=max(1-MU,-ML-d*15)if a(r(o,1))else 0
 if not t:TS[(o,d)]=(b,h)if b>=y else(l,b)
 return b
def n(c):return ord(c[0])+4-10*int(c[1])
def w(m,o):
 i,j,q=m
 if o:i,j=119-i,119-j
 return''.join(chr(x%10+96)+str(10-x//10)for x in(i,j))+q.lower()
def b(u):
 h=[R0]
 for k,x in enumerate(u):
  i,j=n(x[:2]),n(x[2:4])
  if k%2:i,j=119-i,119-j
  h.append(f(h[-1],(i,j,x[4:].upper())))
 return h
def t(u):
 global ND,H
 Y=b(u)
 z=Y[-1];H=set(Y);TS.clear();TM.clear()
 ND=0
 L=[m for m in g(z)if not a(f(z,m))]
 if not L:return[]
 e=L[0]
 try:
  for d in range(1,100):
   l,h=1-MU,MU;y=0
   while l<h-15:
    c=s(z,y,d,1)
    if c>=y:l=c
    else:h=c
    y=(l+h+1)//2
   m2=TM.get(z)
   if m2:e=m2
 except X:pass
 o=(len(Y)-1)%2==1
 L.sort(key=lambda m:v(z,m),reverse=True)
 return[w(m,o)for m in[e]+[m for m in L if m!=e]]
def p(a,c):
 try:return json.load(urllib.request.urlopen(os.environ['MAKEFUN_ENV_URL']+a,json.dumps(c).encode(),30))
 except Exception:return{'_e':1}
def main():
 while 1:
  q=p('/game',{})
  if'_e'in q or q.get('status')=='done':break
  n=q['game']
  while q.get('status')=='your_move':
   c=t(q['moves'])
   for m in c:
    z=p('/move',{'game':n,'move':m})
    if'_e'not in z:q=z;break
   else:q=p('/resign',{'game':n})
__name__=='__main__'and main()