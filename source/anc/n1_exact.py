#!/usr/bin/env python3
"""Exact N1 audit. Usage: nice -n 10 python3 n1_exact.py > n1_exact.out
Requires Python 3 and SymPy 1.14.0. Runs over QQ(z), lex, all 42 coordinates.
The script never evaluates transcendental functions.
"""
import sympy as s
from itertools import combinations
z=s.Symbol('z'); K=s.QQ.frac_field(z)
e=s.Symbol('e')
def block(prefix): return s.symbols(prefix+'_I '+prefix+'_V '+prefix+'_S '+prefix+'_W')
b0=block('b0'); bi=block('bi'); bn=block('bn'); km=block('km'); k2=block('k2')
b1=block('b1'); kh=block('kh'); kp=block('kp'); kc=block('kc')
free=s.symbols('E1 E2 E3 Eminus2 FE')
# Eliminate graph coordinates first. For each representative W precedes I,V,S.
variables=(*b1,*kh,*kp,*kc,*(x for B in [b0,bi,bn,km,k2] for x in [B[3],B[0],B[1],B[2]]),e,*free)
assert len(variables)==42 and len(set(variables))==42
I,V,S,W=b0
b1_rhs=[V,I-V/z,W-I/z,S-W/z+V/z+I/z**2]
kh_rhs=[e*I,e*(I+V),e*S,e*(S+W)]
f,v,h,w=km
kp_rhs=[e*f,e*(f+v),e*h,e*(h+w)]
F,Vp,Sg,Wp=kp
kc_rhs_plus=[F+3*z*Vp,F+(3*z+1)*Vp,Sg+3*z*Wp+9*z*Vp,Sg+(3*z+1)*Wp+(9*z+6)*Vp]
kc_rhs=[s.expand(x.subs(dict(zip(kp,kp_rhs)),simultaneous=True)) for x in kc_rhs_plus]
graphs=[s.expand(x-y) for B,rhs in [(b1,b1_rhs),(kh,kh_rhs),(kp,kp_rhs),(kc,kc_rhs)] for x,y in zip(B,rhs)]
def q(B):
 f,v,h,w=B; return z*(f*w-v*h)-f**2
def detn(B,nu):
 f,v,h,w=B; return z*(f*w-v*h)-2*nu*f*h+2*nu
D=[q(b0)+1,q(bi)+1,detn(bn,s.Rational(1,3)),e*q(km)+1,q(k2)+e**2]
good=graphs+D
print('SYMPY',s.__version__)
print('FIELD QQ(z); all constants in N1 generators are rational; base change to C(z) is allowed')
print('ORDER lex; earlier variables are larger')
print('VARIABLES',','.join(map(str,variables)))
print('INPUT_GOOD count=',len(good))
for i,p in enumerate(good,1): print(f'g{i:02d} = {p}')
G=s.groebner(good,*variables,order='lex',domain=K)
print('REDUCED_GB_GOOD count=',len(G.polys))
for i,p in enumerate(G.polys,1): print(f'GB{i:02d} = {p.as_expr()} ; LM={p.LM(order="lex").as_expr()}')
print('INPUT_REDUCES_TO_ZERO',all(G.reduce(p)[1]==0 for p in good))
monic=[s.Poly(p,*variables,domain=K).monic() for p in good]
assert set(p.as_expr() for p in monic)==set(p.as_expr() for p in G.polys)
LM=[p.LM(order='lex').exponents for p in G.polys]
print('PAIRWISE_COPRIME_LEADING_MONOMIALS',all(not any(min(a,b) for a,b in zip(x,y)) for x,y in combinations(LM,2)))
# A Buchberger calculation is independently checked by reducing all 210 S-polynomials.
sp_ok=True
for p,r in combinations(G.polys,2):
 a=p.LM(order='lex').exponents; b=r.LM(order='lex').exponents
 l=tuple(max(x,y) for x,y in zip(a,b))
 def mon(exp): return s.prod(v**k for v,k in zip(variables,exp))
 Sp=mon(tuple(x-y for x,y in zip(l,a)))*p.as_expr()-mon(tuple(x-y for x,y in zip(l,b)))*r.as_expr()
 if G.reduce(s.expand(Sp))[1]!=0: sp_ok=False; break
print('ALL_210_S_POLYNOMIALS_REDUCE_TO_ZERO',sp_ok)
print('E_UNIT_CERTIFICATE e*(-q(km)) = 1 mod I; remainder=',G.reduce(s.expand(-e*q(km)-1))[1])
# Saturation directly by Rabinowitsch elimination.
u=s.Symbol('u')
Gs=s.groebner([*good,u*e-1],u,*variables,order='lex',domain=K)
sat=[p.as_expr() for p in Gs.polys if not p.as_expr().has(u)]
print('GOOD_SATURATION_GB_EQUALS_GOOD_GB',set(sat)==set(p.as_expr() for p in G.polys))
# Alternative representative: keep PLUS determinant; use four cleared minus links.
alt_graphs=[s.expand(x-y) for B,rhs in [(b1,b1_rhs),(kh,kh_rhs),(kc,kc_rhs_plus)] for x,y in zip(B,rhs)]
alt_graphs += [e*km[0]-kp[0],e*km[1]-kp[1]+kp[0],e*km[2]-kp[2],e*km[3]-kp[3]+kp[2]]
alt=[*alt_graphs,q(b0)+1,q(bi)+1,detn(bn,s.Rational(1,3)),q(kp)+e,q(k2)+e**2]
print('INPUT_ALTERNATIVE count=',len(alt))
for i,p in enumerate(alt,1): print(f'a{i:02d} = {p}')
Ga=s.groebner(alt,*variables,order='lex',domain=K)
print('ALTERNATIVE_GB count=',len(Ga.polys))
print('ALTERNATIVE_GB_DIFF_FROM_GOOD')
for p in Ga.polys:
 if p.as_expr() not in set(x.as_expr() for x in G.polys): print(p.as_expr())
Gsa=s.groebner([*alt,u*e-1],u,*variables,order='lex',domain=K)
sata=[p.as_expr() for p in Gsa.polys if not p.as_expr().has(u)]
print('ALTERNATIVE_SATURATION_EQUALS_GOOD',set(sata)==set(p.as_expr() for p in G.polys))
print('ALTERNATIVE_GOOD_CERTIFICATE_REMAINDER',Ga.reduce(e*q(km)+1)[1])
# Exact zero-divisor: alt modulo its graph relations has e*(e*q(km)+1)=0.
print('ALT_ZERO_DIVISOR_PRODUCT_REMAINDER',Ga.reduce(s.expand(e*(e*q(km)+1)))[1])
print('ALT_E_REMAINDER',Ga.reduce(e)[1])
# Extra component, as its Groebner basis, and exact ideal intersection.
G0=s.groebner([*alt,e],*variables,order='lex',domain=K)
print('EXTRA_COMPONENT_GB count=',len(G0.polys))
for p in G0.polys: print('Z0',p.as_expr())
v=s.Symbol('v')
Gint=s.groebner([*(v*p.as_expr() for p in G.polys),*((1-v)*p.as_expr() for p in G0.polys)],v,*variables,order='lex',domain=K)
inter=[p.as_expr() for p in Gint.polys if not p.as_expr().has(v)]
print('ALTERNATIVE_EQUALS_INTERSECTION_OF_GOOD_AND_ZERO_COMPONENT',set(inter)==set(p.as_expr() for p in Ga.polys))
# N3: actual closure with inverse theta, W and derivative of Sigma.
U,V,P,A,B,C,WW,CC,t,ti=s.symbols('U V P A B C WW CC t ti')
N3=[z*(U*WW-V*P)-U**2+1,A-t*U,B-t*(U+V),C-t*P,CC-t*(P+WW),t*ti-1]
GN3=s.groebner(N3,WW,CC,t,ti,U,V,P,A,B,C,order='lex',domain=K)
N3elim=[p.as_expr() for p in GN3.polys if not p.as_expr().has(WW,CC,t,ti)]
minors=[U*B-(U+V)*A,U*C-P*A,(U+V)*C-P*B]
GM=s.groebner(minors,U,V,P,A,B,C,order='lex',domain=K)
print('N3_ELIMINATION_EQUALS_MINOR_IDEAL',set(N3elim)==set(p.as_expr() for p in GM.polys))
print('N3_REDUCED_GB',N3elim)
print('ALL_ASSERTIONS_PASSED')
