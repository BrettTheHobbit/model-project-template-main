CONJECTUREPANEL Quiz
PROOF "∃y.(B(1)∧RxCxC(x)) ⊢ ¬∀y.(B(y)∧¬B(1))∧RxCxC(x)"
INFER ∃y.(B(1)∧RxCxC(x))
     ⊢ ¬∀y.(B(y)∧¬B(1))∧RxCxC(x)
FORMULAE
0 RxCxC(x),
1 ¬∀y.(B(y)∧¬B(1)),
2 ¬∀y.(B(y)∧¬B(1))∧RxCxC(x),
3 ⊥,
4 ¬B(1),
5 B(1),
6 B(i)∧¬B(1),
7 B(i),
8 actual i,
9 ∀y.(B(y)∧¬B(1)),
10 B(y)∧¬B(1),
11 i,
12 y,
13 ∀y.(B(y)∧¬B(1)),
14 B(1)∧RxCxC(x),
15 ∃y.(B(1)∧RxCxC(x)),
16 ∃y.(B(1)∧RxCxC(x))
IS
SEQ ("∃ elim"[i,C,P,x\11,2,14,12]) (hyp[A\15]) (cut[B,C\5,2]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\5,0]) (hyp[A\14])) (cut[B,C\0,2]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\5,0]) (hyp[A\14])) (cut[B,C\1,2]) ("¬ intro"[A\13]) (cut[B,C\6,3]) ("∀ elim"[P,i,x\10,11,12]) (hyp[A\9]) (hyp[A\8]) (cut[B,C\4,3]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\7,4]) (hyp[A\6])) (cut[B,C\3,3]) ("¬ elim"[B\5]) (hyp[A\5]) (hyp[A\4]) (hyp[A\3]) (cut[B,C\0,2]) (hyp[A\0]) ("∧ intro"[A,B\1,0]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Quiz
PROOF "∀x.(A(x)∧¬B(x)) ⊢ ∀x.(A(x))∧¬∃x.(C(x)∧B(x))"
INFER ∀x.(A(x)∧¬B(x))
     ⊢ ∀x.(A(x))∧¬∃x.(C(x)∧B(x))
FORMULAE
0 ¬∃x.(C(x)∧B(x)),
1 ∀x.(A(x)),
2 ⊥,
3 ¬B(i),
4 B(i),
5 A(i)∧¬B(i),
6 A(i),
7 actual i,
8 ∀x.(A(x)∧¬B(x)),
9 A(x)∧¬B(x),
10 i,
11 x,
12 C(i)∧B(i),
13 C(i),
14 ∃x.(C(x)∧B(x)),
15 C(x)∧B(x),
16 ∃x.(C(x)∧B(x)),
17 ∀x.(A(x))∧¬∃x.(C(x)∧B(x)),
18 A(i1),
19 A(i1)∧¬B(i1),
20 ¬B(i1),
21 actual i1,
22 i1,
23 A(x),
24 ∀x.(A(x)∧¬B(x))
IS
SEQ (cut[B,C\1,17]) ("∀ intro"[i,P,x\22,23,11]) (cut[B,C\19,18]) ("∀ elim"[P,i,x\9,22,11]) (hyp[A\8]) (hyp[A\21]) (cut[B,C\18,18]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\18,20]) (hyp[A\19])) (hyp[A\18]) (cut[B,C\0,17]) ("¬ intro"[A\16]) ("∃ elim"[i,C,P,x\10,2,15,11]) (hyp[A\14]) (cut[B,C\4,2]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\13,4]) (hyp[A\12])) (cut[B,C\5,2]) ("∀ elim"[P,i,x\9,10,11]) (hyp[A\8]) (hyp[A\7]) (cut[B,C\3,2]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\6,3]) (hyp[A\5])) (cut[B,C\2,2]) ("¬ elim"[B\4]) (hyp[A\4]) (hyp[A\3]) (hyp[A\2]) ("∧ intro"[A,B\1,0]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Quiz
PROOF "RxC1P→¬RxC1C, RxC2P→¬RxC2C, RxC3P→¬RxC3C, RxC4P→¬RxC4C, RxC1C∨RxC2C∨RxC3C∨RxC4C∨RxC5C, RxC1P∧RxC2P∧RxC3P∧RxC4P ⊢ RxC5C"
INFER RxC1P→¬RxC1C,
     RxC2P→¬RxC2C,
     RxC3P→¬RxC3C,
     RxC4P→¬RxC4C,
     RxC1C∨RxC2C∨RxC3C∨RxC4C∨RxC5C,
     RxC1P∧RxC2P∧RxC3P∧RxC4P 
     ⊢ RxC5C 
FORMULAE
0 RxC5C,
1 ⊥,
2 ¬RxC4C,
3 RxC4C,
4 ¬RxC3C,
5 RxC3C,
6 ¬RxC2C,
7 RxC2C,
8 ¬RxC1C,
9 RxC1C,
10 RxC1C∨RxC2C,
11 RxC1C∨RxC2C∨RxC3C,
12 RxC1C∨RxC2C∨RxC3C∨RxC4C,
13 RxC1C∨RxC2C∨RxC3C∨RxC4C∨RxC5C,
14 RxC4P,
15 RxC4P→¬RxC4C,
16 RxC1P∧RxC2P∧RxC3P∧RxC4P,
17 RxC1P∧RxC2P∧RxC3P,
18 RxC3P,
19 RxC3P→¬RxC3C,
20 RxC1P∧RxC2P,
21 RxC2P,
22 RxC2P→¬RxC2C,
23 RxC1P,
24 RxC1P→¬RxC1C 
IS
SEQ (cut[B,C\17,0]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\17,14]) (hyp[A\16])) (cut[B,C\20,0]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\20,18]) (hyp[A\17])) (cut[B,C\23,0]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\23,21]) (hyp[A\20])) (cut[B,C\8,0]) ("→ elim"[A,B\23,8]) (hyp[A\24]) (hyp[A\23]) (cut[B,C\21,0]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\23,21]) (hyp[A\20])) (cut[B,C\6,0]) ("→ elim"[A,B\21,6]) (hyp[A\22]) (hyp[A\21]) (cut[B,C\18,0]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\20,18]) (hyp[A\17])) (cut[B,C\4,0]) ("→ elim"[A,B\18,4]) (hyp[A\19]) (hyp[A\18]) (cut[B,C\14,0]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\17,14]) (hyp[A\16])) (cut[B,C\2,0]) ("→ elim"[A,B\14,2]) (hyp[A\15]) (hyp[A\14]) ("∨ elim"[A,B,C\12,0,0]) (hyp[A\13]) ("∨ elim"[A,B,C\11,3,0]) (hyp[A\12]) ("∨ elim"[A,B,C\10,5,0]) (hyp[A\11]) ("∨ elim"[A,B,C\9,7,0]) (hyp[A\10]) (cut[B,C\1,0]) ("¬ elim"[B\9]) (hyp[A\9]) (hyp[A\8]) ("contra (constructive)"[B\0]) (hyp[A\1]) (cut[B,C\1,0]) ("¬ elim"[B\7]) (hyp[A\7]) (hyp[A\6]) ("contra (constructive)"[B\0]) (hyp[A\1]) (cut[B,C\1,0]) ("¬ elim"[B\5]) (hyp[A\5]) (hyp[A\4]) ("contra (constructive)"[B\0]) (hyp[A\1]) (cut[B,C\1,0]) ("¬ elim"[B\3]) (hyp[A\3]) (hyp[A\2]) ("contra (constructive)"[B\0]) (hyp[A\1]) (hyp[A\0])
END
