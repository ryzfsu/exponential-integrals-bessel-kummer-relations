# Exact ancillary calculation for the mixed example

The script `n1_exact.py` checks the mixed example of Supplementary Section S1. It also performs an elimination check for a half-Kummer/Bessel closure. The file `n1_exact.out` contains the complete standard output. These finite exact calculations do not provide an independent proof, verify transcendental evaluations, or establish a general theorem about Gröbner-basis length.

## Command and environment

Run a local copy in its own scratch directory:

```bash
python3 n1_exact.py > check.out
cmp check.out n1_exact.out
```

The calculation requires Python 3 and SymPy. The reference output was produced with Python 3.12.3 and SymPy 1.14.0 and ends with `ALL_ASSERTIONS_PASSED`.

## File integrity

The SHA256 of `n1_exact.py` is
`cf7668372065818cfbd13958da21d218d99df47bc3400387b3af6070ce627ee8`.
The supplied complete output `n1_exact.out` has SHA256
`98cba5b53f6f5fe5d37316d4a61a4bc68a24291a27e417abeb534b1bcf3fc929`.

## Field, coordinates and monomial order

The calculation is in the polynomial ring over `QQ(z)`. Every coefficient of the specified example is rational in `z`; base change to `C(z)` is allowed. The symbol `e` is the indeterminate standing for the exponential coordinate `exp(z)`, not a floating-point value.

Each block prefix has four coordinate symbols `(prefix_I, prefix_V, prefix_S, prefix_W)`. The representatives are:

| Prefix | Block | Coordinate meaning |
|---|---|---|
| `b0` | Bess(1,0) | `(I,V,S,W)` |
| `bi` | Bess(i,0) | `(I,V,S,W)`; the determinant is scale-independent; the squared scale enters the differential operator |
| `bn` | Bess(1,1/3) | `(f_(1/3),f'_(1/3),f_(-1/3),f'_(-1/3))` |
| `km` | Kum(-1,2/3) | `(F,F',Sigma,Sigma')` |
| `k2` | Kum(2,1/3) | `(F,F',Sigma,Sigma')` |

The graph blocks `b1`, `kh`, `kp`, `kc` stand respectively for Bess(1,1), Kum(2,1/2), Kum(1,1/3), Kum(1,4/3). In `b1`, the last two slots are the integer-order entire-part coordinates `(P,P')` defined in the paper; they occupy separate slots. The five remaining free symbols `E1,E2,E3,Eminus2,FE` stand for `Ein_1(z),Ein_2(z),Ein_3(z),Ein(-2z),F^E`.

The order is lexicographic, with earlier variables larger. First come the graph blocks `b1,kh,kp,kc`, each in `(I,V,S,W)` order. Then come the representative blocks `b0,bi,bn,km,k2`, each in `(W,I,V,S)` order. Last come `e,E1,E2,E3,Eminus2,FE`. The full 42-variable list is printed in the supplied output. The auxiliary elimination variables `u` and `v`, when used, precede this list.

## Exact checks performed

For the good representative choice the script builds 16 linkage graphs and five determinants, computes the reduced lexicographic Gröbner basis, checks equality with the monic input set, checks pairwise coprime leading monomials, and reduces all 210 S-polynomials to zero. It checks the exponential coordinate's unit certificate and verifies that saturation by `e` changes no basis element.

For the alternative Kummer representative it computes the cleared presentation, its reduced basis, the nonzero remainder of the good unit certificate, and a zero-divisor product. Rabinowitsch elimination verifies that saturation recovers the good ideal. It also computes the component at `e=0` and verifies the exact ideal-intersection identity. Both presentations have 21 reduced basis elements for this specified order; the script does not claim basis length is invariant under a change of order.

The final check adjoins inverse-exponential and derivative variables to a half-Kummer/Bessel closure, eliminates them, and compares the result with the three-minor ideal in the six remaining variables.
