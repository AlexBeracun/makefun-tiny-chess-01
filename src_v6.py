import json,os,random
from urllib.request import Request,urlopen
E=os.environ["MAKEFUN_ENV_URL"]
L=110000
X=10000
O=6400
V=(0,100,320,330,500,900,20000)
A=(0,100,320,330,500,900,0)
p=(0,0,0,0,50,50,50,50,10,10,20,30,5,5,10,25,0,0,0,20,5,-5,-10,0,5,10,10,-20,0,0,0,0)
n=(-50,-40,-30,-30,-40,-20,0,0,-30,0,10,15,-30,5,15,20,-30,0,15,20,-30,5,10,15,-40,-20,0,5,-50,-40,-30,-30)
f=(-20,-10,-10,-10,-10,0,0,0,-10,0,5,10,-10,5,5,10,-10,0,10,10,-10,10,10,10,-10,5,0,0,-20,-10,-10,-10)
r=(0,0,0,0,5,10,10,10,-5,0,0,0,-5,0,0,0,-5,0,0,0,-5,0,0,0,-5,0,0,0,0,0,0,5)
q=(-20,-10,-10,-5,-10,0,0,0,-10,0,5,5,-5,0,5,5,0,0,5,5,-10,5,5,5,-10,0,5,0,-20,-10,-10,-5)
g=(-30,-40,-40,-50,-30,-40,-40,-50,-30,-40,-40,-50,-30,-40,-40,-50,-20,-30,-30,-40,-10,-20,-20,-20,20,20,0,0,20,30,10,0)
d=(-50,-40,-30,-20,-30,-20,-10,0,-30,-10,20,30,-30,-10,30,40,-30,-10,30,40,-30,-10,20,30,-30,-30,0,0,-50,-30,-30,-30)
Pb=(0,0,0,0,25,60,120,0)
def t(h,w):
 o=[0]*128
 for s in range(128):
  if s&0x88:continue
  a=s>>4;e=s&7;m=e if e<4 else 7-e
  o[s]=h[(a if w else 7-a)*4+m]
 return o
W=[None]+[t(x,0)for x in(p,n,f,r,q)]
J=[None]+[t(x,1)for x in(p,n,f,r,q)]
g0=t(g,0);g1=t(g,1);d0=t(d,0);d1=t(d,1)
C=[[0]*128 for _ in range(13)]
for pc in range(1,6):
 for s in range(128):
  C[pc+6][s]=A[pc]+W[pc][s]
  C[6-pc][s]=-(A[pc]+J[pc][s])
Rr=random.Random(7)
Z=[Rr.getrandbits(64)for _ in range(1689)]
s0=Z[1664];s1=Z[1665:1681];s2=Z[1681:1689]
Kn=(-33,-31,-18,-14,14,18,31,33)
Kd=(-17,-16,-15,-1,1,15,16,17)
Bd=(-17,-15,15,17)
Rd=(-16,-1,1,16)
Cm=[15]*128
Cm[4]=12;Cm[7]=14;Cm[0]=13;Cm[116]=3;Cm[119]=11;Cm[112]=7
Sq=[chr(97+(s&7))+str((s>>4)+1)if not s&0x88 else "?"for s in range(128)]
b=[0]*128;s=1;c=0;e=-1;hm=0;k=[4,116];v=0;ph=0;nb=[0,0];z=0;hs=[];u=[]
Tz=1<<18;Tm=Tz-1
Tk=[0]*Tz;Td=[0]*Tz;Ts=[0]*Tz;Tf=[0]*Tz;Tt=[0]*Tz
Kl=[0]*512;Hy=[0]*896;Nd=0
class Ab(Exception):pass
def at(q,w):
 if w:
  t=q-15
  if not t&0x88 and b[t]==1:return 1
  t=q-17
  if not t&0x88 and b[t]==1:return 1
 else:
  t=q+15
  if not t&0x88 and b[t]==-1:return 1
  t=q+17
  if not t&0x88 and b[t]==-1:return 1
 j=2 if w else -2;g=6 if w else -6
 for d in Kn:
  t=q+d
  if not t&0x88 and b[t]==j:return 1
 for d in Kd:
  t=q+d
  if not t&0x88 and b[t]==g:return 1
 for d in Bd:
  t=q+d
  while not t&0x88:
   y=b[t]
   if y:
    if(y>0)==w and abs(y)in(3,5):return 1
    break
   t+=d
 for d in Rd:
  t=q+d
  while not t&0x88:
   y=b[t]
   if y:
    if(y>0)==w and abs(y)in(4,5):return 1
    break
   t+=d
 return 0
def gn(x):
 ms=[];a=ms.append;w=s
 for q in range(128):
  if q&0x88:continue
  pc=b[q]
  if not pc or(pc>0)!=(w>0):continue
  y=pc if pc>0 else -pc
  if y==1:
   d=16 if w>0 else -16;pr=7 if w>0 else 0;to=q+d
   if not to&0x88 and b[to]==0:
    if(to>>4)==pr:
     for pp in(5,2,4,3):a(q|(to<<7)|(pp<<14))
    elif not x:
     a(q|(to<<7))
     if(q>>4)==(1 if w>0 else 6):
      o=q+2*d
      if b[o]==0:a(q|(o<<7))
   for to in(q+d-1,q+d+1):
    if to&0x88:continue
    cp=b[to]
    if(cp and(cp>0)!=(w>0))or to==e:
     if(to>>4)==pr:
      for pp in(5,2,4,3):a(q|(to<<7)|(pp<<14))
     else:a(q|(to<<7))
  elif y==2 or y==6:
   for d in Kn if y==2 else Kd:
    to=q+d
    if to&0x88:continue
    cp=b[to]
    if not cp:
     if not x:a(q|(to<<7))
    elif(cp>0)!=(w>0):a(q|(to<<7))
  else:
   ds=Bd if y==3 else Rd if y==4 else Bd+Rd
   for d in ds:
    to=q+d
    while not to&0x88:
     cp=b[to]
     if not cp:
      if not x:a(q|(to<<7))
     else:
      if(cp>0)!=(w>0):a(q|(to<<7))
      break
     to+=d
 if not x:
  if w>0:
   if c&1 and b[5]==0 and b[6]==0 and b[7]==4 and not at(4,0)and not at(5,0)and not at(6,0):a(4|(6<<7))
   if c&2 and b[3]==0 and b[2]==0 and b[1]==0 and b[0]==4 and not at(4,0)and not at(3,0)and not at(2,0):a(4|(2<<7))
  else:
   if c&4 and b[117]==0 and b[118]==0 and b[119]==-4 and not at(116,1)and not at(117,1)and not at(118,1):a(116|(118<<7))
   if c&8 and b[115]==0 and b[114]==0 and b[113]==0 and b[112]==-4 and not at(116,1)and not at(115,1)and not at(114,1):a(116|(114<<7))
 return ms
def mk(m):
 global s,c,e,hm,v,ph,z
 f=m&127;to=(m>>7)&127;pr=(m>>14)&7;pc=b[f];g=1 if pc>0 else -1;cp=b[to];q=to
 if(pc==1 or pc==-1)and to==e and not cp:q=to-16*g;cp=b[q]
 u.append((m,cp,q,c,e,hm,z,v,ph,nb[0],nb[1]))
 h=z
 if c:h^=s1[c]
 if e>=0:h^=s2[e&7]
 b[f]=0;o=g*pr if pr else pc;b[to]=o
 if q!=to:b[q]=0
 h^=Z[(pc+6)*128+f]^Z[(o+6)*128+to]
 v+=C[o+6][to]-C[pc+6][f]
 if cp:
  v-=C[cp+6][q];h^=Z[(cp+6)*128+q]
  if abs(cp)!=1:ph-=A[abs(cp)]
  if abs(cp)==3:nb[0 if cp>0 else 1]-=1
 if pr:
  ph+=A[pr]
  if pr==3:nb[0 if g>0 else 1]+=1
 if abs(pc)==6:
  k[0 if g>0 else 1]=to
  if to-f==2 or f-to==2:
   rf,rt=((7,5)if to==6 else(0,3)if to==2 else(119,117)if to==118 else(112,115));rk=b[rf];b[rf]=0;b[rt]=rk;h^=Z[(rk+6)*128+rf]^Z[(rk+6)*128+rt];v+=C[rk+6][rt]-C[rk+6][rf]
 c=c&Cm[f]&Cm[to]
 if c:h^=s1[c]
 e=f+16*g if abs(pc)==1 and to-f==32*g else -1
 if e>=0:h^=s2[e&7]
 h^=s0;z=h;hm=0 if abs(pc)==1 or cp else hm+1;s=-s;hs.append(z)
 if at(k[0 if g>0 else 1],s>0):um();return 0
 return 1
def um():
 global s,c,e,hm,v,ph,z
 m,cp,q,oc,oe,oh,oz,ov,op,n0,n1=u.pop()
 f=m&127;to=(m>>7)&127;pr=(m>>14)&7;s=-s;g=s;o=b[to];pc=g if pr else o
 b[f]=pc;b[to]=0
 if q!=to:b[q]=cp
 elif cp:b[to]=cp
 if abs(pc)==6:
  k[0 if g>0 else 1]=f
  if to-f==2 or f-to==2:
   rf,rt=((7,5)if to==6 else(0,3)if to==2 else(119,117)if to==118 else(112,115));b[rf]=b[rt];b[rt]=0
 c,e,hm,z,v,ph=oc,oe,oh,oz,ov,op;nb[0]=n0;nb[1]=n1;hs.pop()
def cp():
 global v,ph,z
 v=0;ph=0;nb[0]=0;nb[1]=0;z=0
 for q in range(128):
  if q&0x88:continue
  pc=b[q]
  if not pc:continue
  y=pc if pc>0 else -pc
  if y==6:k[0 if pc>0 else 1]=q;z^=Z[(pc+6)*128+q];continue
  v+=C[pc+6][q]
  if y!=1:ph+=A[y]
  if y==3:nb[0 if pc>0 else 1]+=1
  z^=Z[(pc+6)*128+q]
 if s<0:z^=s0
 if c:z^=s1[c]
 if e>=0:z^=s2[e&7]
def st():
 global b,s,c,e,hm
 b=[0]*128
 b[0:8]=[4,2,3,5,6,3,2,4];b[16:24]=[1]*8;b[96:104]=[-1]*8;b[112:120]=[-4,-2,-3,-5,-6,-3,-2,-4]
 s=1;c=15;e=-1;hm=0;u.clear();cp();hs.clear();hs.append(z)
def ev():
 r=v;w=ph
 r+=(g0[k[0]]*w+d0[k[0]]*(O-w))//O
 r-=(g1[k[1]]*w+d1[k[1]]*(O-w))//O
 if nb[0]>=2:r+=30
 if nb[1]>=2:r-=30
 for q in range(128):
  y=b[q]
  if y==1 and q>63:
   p=1
   for o in(15,16,17):
    t=q+o
    while t<128 and b[t]!=-1:t+=16
    if t<128:p=0;break
   if p:r+=Pb[q>>4]
  elif y==-1 and q<64:
   p=1
   for o in(-15,-16,-17):
    t=q+o
    while t>=0 and b[t]!=1:t-=16
    if t>=0:p=0;break
   if p:r-=Pb[7-(q>>4)]
 return r if s>0 else -r
def rp():
 n=len(hs);t=n-1-hm
 if t<0:t=0
 h=hs[-1];i=n-3
 while i>=t:
  if hs[i]==h:return 1
  i-=2
 return 0
def od(ms,t,pl):
 a=Kl[pl*2];d=Kl[pl*2+1];o=[]
 for m in ms:
  if m==t:r=1000000
  else:
   f=m&127;to=(m>>7)&127;pr=(m>>14)&7
   if pr:r=900000+V[pr]
   else:
    cp=b[to]
    if cp:r=100000+10*V[abs(cp)]-V[abs(b[f])]
    elif to==e and(b[f]==1 or b[f]==-1):r=100000+10*V[1]-V[1]
    elif m==a:r=50000
    elif m==d:r=40000
    else:r=Hy[abs(b[f])*128+to]
  o.append(m|(r<<20))
 o.sort(reverse=True)
 return o
def qs(a,be,pl):
 global Nd
 Nd+=1
 if Nd>=L:raise Ab
 if pl>0 and(hm>=100 or rp()):return 0
 if pl>=120:return ev()
 j=at(k[0 if s>0 else 1],s<0)
 if j:y=-X-1;ms=od(gn(0),0,pl)
 else:
  y=ev()
  if y>=be:return y
  if y>a:a=y
  ms=od(gn(1),0,pl)
 n=0
 for m in ms:
  w=m&131071
  if not mk(w):continue
  n+=1
  try:r=-qs(-be,-a,pl+1)
  except Ab:um();raise
  um()
  if r>y:y=r
  if r>a:a=r
  if a>=be:break
 if j and n==0:return -X+pl
 return y
def sc(d,a,be,pl):
 global Nd,s,e,z
 Nd+=1
 if Nd>=L:raise Ab
 if pl>0 and(hm>=100 or rp()):return 0
 if d<=0 or pl>=120:return qs(a,be,pl)
 i=z&Tm;t=0
 if Tk[i]==z:
  t=Tt[i]
  if Td[i]>=d:
   r=Ts[i]
   if r>9000:r-=pl
   elif r<-9000:r+=pl
   f=Tf[i]
   if f==1:return r
   if f==2 and r>=be:return r
   if f==3 and r<=a:return r
 a0=a;ck=at(k[0 if s>0 else 1],s<0)
 if d>=3 and pl>0 and ph>=500 and not ck:
  oe,oz=e,z;h=z
  if e>=0:h^=s2[e&7]
  h^=s0;z=h;e=-1;s=-s
  try:r=sc(d-3,-be,-be+1,pl+1)
  except Ab:s=-s;e,z=oe,oz;raise
  s=-s;e,z=oe,oz
  if r<=-be:return be
 ms=od(gn(0),t,pl);y=-X-1;w=0;n=0
 for m in ms:
  mm=m&131071
  if not mk(mm):continue
  n+=1
  try:
   if n<2:r=-sc(d-1,-be,-a,pl+1)
   else:
    r=-sc(d-1,-a-1,-a,pl+1)
    if a<r<be:r=-sc(d-1,-be,-a,pl+1)
  except Ab:um();raise
  um()
  if r>y:y=r;w=mm
  if r>a:a=r
  if a>=be:
   f=mm&127;to=(mm>>7)&127;pr=(mm>>14)&7
   if pr==0 and b[to]==0 and not(to==e and abs(b[f])==1):
    if Kl[pl*2]!=mm:Kl[pl*2+1]=Kl[pl*2];Kl[pl*2]=mm
    j=abs(b[f])*128+to;g=Hy[j]+d*d;Hy[j]=g if g<30000 else 30000
   break
 if n==0:return -X+pl if at(k[0 if s>0 else 1],s<0) else 0
 f=1 if y>a0 and y<be else 2 if y>=be else 3
 r=y
 if r>9000:r+=pl
 elif r<-9000:r-=pl
 Tk[i]=z;Td[i]=d;Ts[i]=r;Tf[i]=f;Tt[i]=w
 return y
def rt(d,ms):
 a=-X-1;o=[]
 for j,mm in enumerate(ms):
  if not mk(mm):continue
  try:
   if j==0:r=-sc(d-1,-X-1,X+1,1)
   else:
    r=-sc(d-1,-a-1,-a,1)
    if r>a:r=-sc(d-1,-X-1,X+1,1)
    elif r==a:r=a-1
  except Ab:um();raise
  um();o.append((r,mm))
  if r>a:a=r
 o.sort(reverse=True)
 return o
def th(ms):
 if len(ms)==1:return ms[0],0
 global Nd
 ms=[m&131071 for m in od(ms,0,0)];y=ms[0];r=-X-1
 for d in range(1,33):
  Nd=0
  try:o=rt(d,ms)
  except Ab:break
  if not o:break
  r,y=o[0];ms=[m for _,m in o]
  if abs(r)>X-200:break
 return y,r
def lg():
 o=[]
 for m in gn(0):
  if mk(m):o.append(m);um()
 return o
def uc(m):
 r=Sq[m&127]+Sq[(m>>7)&127];pr=(m>>14)&7
 if pr:r+="nbrq"[pr-2]
 return r
def pu(u):
 f=(ord(u[1])-49)*16+(ord(u[0])-97);t=(ord(u[3])-49)*16+(ord(u[2])-97);pr="nbrq".find(u[4])+2 if len(u)>4 else 0
 return f|(t<<7)|(pr<<14)
D={"b1c3g8f6":("2v","15g1qqzsq9kzgy"),"d2d4c5d4":("p7","2561yte2uetl4j5k3"),"f1c4f8c5":("2t","2zjt8jvx4w6"),"f1b5g8f6":("3h","26wmlwfnfszprufra"),"g1f3g8f6":("1z3","q2ei1f81e8b1esde7f508cijpra"),"d2d4g8f6":("e7","2x9hxrfvj9y8seify2fgrkehe")}
def bk(mv):
 v=D.get(mv[4]+mv[5])
 if not v:return ''
 a,c=v;n=int(c,36);m=int(a,36);k=(len(mv)-8-(0 if s>0 else 1))//2
 if k<0 or not m>>k&1:return ''
 j=0
 for i in range(k):j+=m>>i&1
 x=(n>>(14*j))&16383
 return Sq[x>>7]+Sq[x&127]
def ch(o,mv,l2):
 st()
 for w in mv:
  if not mk(pu(w)):return l2[0]
 m=bk(mv)
 if m and m in l2:return m
 ms=lg()
 if not ms:return l2[0]
 return uc(th(ms)[0])
def po(q,o):
 r=Request(E+q,data=json.dumps(o).encode(),headers={"content-type":"application/json"})
 with urlopen(r)as w:return json.load(w)
def main():
 while 1:
  g=po("/game",{})
  if g["status"]=="done":break
  while g["status"]=="your_move":
   try:
    mv=ch(g["fen"],g["moves"],g["legal_moves"])
    if mv not in g["legal_moves"]:raise ValueError("illegal "+mv)
   except Exception:mv=g["legal_moves"][0]
   g=po("/move",{"game":g["game"],"move":mv})
if __name__=="__main__":main()
