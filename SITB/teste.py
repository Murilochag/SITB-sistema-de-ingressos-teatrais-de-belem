
import streamlit as st;

import Controllers.IngressoController as IngressoController;
import Controllers.SessaoController as SessaoController;


assentos = [
        ['a1','a2','a3','a4','a5','a6','a7','a8','a9','a10'],
        ['b1','b2','b3','b4','b5','b6','b7','b8','b9','b10'],
        ['d1','d2','d3','d4','d5','d6','d7','d8','d9','d10'],
        ['c1','c2','c3','c4','c5','c6','c7','c8','c9','c10'],
        ['e1','e2','e3','e4','e5','e6','e7','e8','e9','e10'],
        ['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10'],
        ['g1','g2','g3','g4','g5','g6','g7','g8','g9','g10'],
        ['h1','h2','h3','h4','h5','h6','h7','h8','h9','h10'],
        ['i1','i2','i3','i4','i5','i6','i7','i8','i9','i10'],
        ['j1','j2','j3','j4','j5','j6','j7','j8','j9','j10'],
        ['k1','k2','k3','k4','k5','k6','k7','k8','k9','k10'],
        ['l1','l2','l3','l4','l5','l6','l7','l8','l9','l10'],
        ['m1','m2','m3','m4','m5','m6','m7','m8','m9','m10'],
        ['n1','n2','n3','n4','n5','n6','n7','n8','n9','n10'],
        ['o1','o2','o3','o4','o5','o6','o7','o8','o9','o10'],
        ['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10']]

    

def ass():
    st.write(str(assentos))

def ass2():
     
    colms = st.columns((1,1,1,1))
    campos = ['1', '2', '3','']
    for col, campo_nome in zip(colms, campos):
        col.write(campo_nome)
    
    for item in assentos:
        a,b,c = st.columns((1,1,1))
        a.write(st.selectbox('a'))
        b.write(item[1])
        c.write(item[2])

def teste():
    st.write(
        SessaoController.getSessao()
    )