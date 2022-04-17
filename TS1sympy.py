# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 17:48:22 2022

@author: fcfra
"""

import sympy as sp
from sympy.abc import s
from IPython.display import display, Math

V1, V2, Va = sp.symbols("V1, V2, Va")
R1, R2, C, R3 = sp.symbols("R1, R2, C, R3")

aa = sp.solve([ 
                Va*(C+1/R3)-V1*C, 
                Va*(1/R1+1/R2) -V1/R1 -V2/R2
                ], 
                [V1, V2])

transf_func = aa[V2]/aa[V1]

tf = transf_func.subs(C, s*C)

num, den = sp.fraction(sp.simplify(sp.expand(tf)))

num = sp.Poly(num,s)
den = sp.Poly(den,s)

k = num.LC() / den.LC()

num = num.monic()
den = den.monic()

den_coeffs = den.all_coeffs()
wo = den_coeffs[-1]

tf_final = sp.Mul(k,num/den, evaluate=False)

display(tf_final)