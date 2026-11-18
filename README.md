# Relations among exponential integrals, Bessel and Kummer functions

Ruiyi Zhang

DOI: [10.5281/zenodo.24327320](https://doi.org/10.5281/zenodo.24327320)

The paper determines the algebraic relations among finite families of special functions
built from

- exponentials `e^(λz)` and rational-exponential primitives: primitives of finite sums
  `Σ q_μ(z) e^(μz)` with `q_μ ∈ C(z)`, with arbitrary additive constants;
- iterated entire exponential integrals `Ein_k(ηz)`;
- Bessel functions of rational order;
- Kummer functions `1F1(a; 1; sz)` with `a` not an integer.

## Main results

- **Theorem 1 (relation ideal).** For a closed, normalized list of such functions over
  `T = C(z)(e^(λ_1 z), ..., e^(λ_d z))`, the transcendence degree is `ρ + τ + 3·#C`.
  Here `ρ` is the rank of the residue vectors of the first-level primitives, `τ` counts the
  higher exponential-integral levels and `#C` is the number of linkage classes of
  second-order blocks. Over `C(z)` the degree is `d + ρ + τ + 3·#C`. The prime relation
  ideal is given by explicit generators: affine residue relations, one Wronskian
  determinant per linkage class, linear linkage identities and equality graphs.
- **Theorem 2 (linkage maps).** Two second-order blocks are related by a rank-one twist
  exactly in the following cases:
  - Bessel–Bessel: `c'^2 = c^2` and the same normalized order;
  - Kummer–Kummer: `s' = s` with `a' − a ∈ Z`, or `s' = −s` with `a' + a ∈ Z`;
  - Bessel–Kummer: order `0`, `s = ±2c`, `a ∈ 1/2 + Z`.

  These equivalences are due to Gorelov (2021). The paper gives the explicit normalized
  maps between the blocks.
- **Theorem 3 (values).** Take algebraic data and a nonzero algebraic point `α`. Then the
  ideal of algebraic relations among the values is the specialization at `z = α` of the
  ideal of Theorem 1, and
  `trdeg_Q̄ Q̄(X(α)) = d + ρ^E + τ + 3·#C`.
  The same holds for several evaluation points.
- **Theorem 4 (linear independence estimate).** Put `A_* = 311040·2^24001`, `N = A_*^8`
  and `H_0 = N^N`. For integers `(a, b, c, d) ≠ 0` with `H = max(|a|, |b|, |c|, |d|) ≥ H_0`,

      |a + b e + c e^(-1) + d Ein(1)| ≥ H^(-60) / 12.

  The exponent is weaker than the classical `3 + ε`; every constant here is explicit.
- **Theorem 5 (mixed connection values).** Take `N` values from the connection values
  `E_1(x)`, `K_m(u)/I_m(u)` and `Γ(a) U(a, 1, t) / 1F1(a; 1; t)` at positive algebraic
  arguments, subject to stated exclusions. Together with Euler's constant `γ`, the
  logarithms involved and, when needed, `π`, they generate a field of transcendence
  degree at least `N` over `E = acl(Q̄(e^β : β ∈ Q̄))`, and also over a larger base field `B`
  that contains the regular values. The one-point case over `E` is classical (Shidlovskii);
  no novelty is claimed for the mixed formulation over `B`.

The qualitative results use differential Galois theory and the specialization theory of
Siegel's E-functions (Shidlovskii, André, Beukers). Twisted residues, integration and
`SL_2` factors determine the Galois group. The estimate of Theorem 4 uses integer polynomial
approximations and derivative selection. Supplementary sections at the end of `main.pdf`
give worked examples, the exact input model and comparisons with classical results.

## Contents

- `main.pdf` (44 pages, including the supplementary sections)
- `source/` - LaTeX source: `main.tex`, `macros.tex`, `sections/`, `refs.bib` and the
  generated `main.bbl`
- `source/anc/` - exact ancillary calculation for the mixed example: `n1_exact.py`, its
  complete output `n1_exact.out` and `N1-README.md`
- `BUILD.md` - build instructions and PDF checks
- `CITATION.cff`, `LICENSE.md`, `LICENSES/`, `SHA256SUMS`

## Build

TeX Live 2026 with pdfLaTeX and BibTeX (details in `BUILD.md`):

    cd source
    pdflatex main.tex
    bibtex main
    pdflatex main.tex
    pdflatex main.tex

## Checks

Python 3 with SymPy (reference output: Python 3.12.3, SymPy 1.14.0). Copy `source/anc/`
to a scratch directory and run there:

    python3 n1_exact.py > check.out
    cmp check.out n1_exact.out

The output ends with `ALL_ASSERTIONS_PASSED`. See `source/anc/N1-README.md`.

## Citation

Ruiyi Zhang, *Relations among exponential integrals, Bessel and Kummer functions*, preprint, Zenodo, 2026. https://doi.org/10.5281/zenodo.24327320

```bibtex
@misc{zhang2026einbesselkummer,
  author    = {Zhang, Ruiyi},
  title     = {Relations among exponential integrals, {Bessel} and {Kummer} functions},
  year      = {2026},
  publisher = {Zenodo},
  note      = {Preprint},
  doi       = {10.5281/zenodo.24327320},
  url       = {https://doi.org/10.5281/zenodo.24327320}
}
```

## License

The paper, its LaTeX source and the documentation: CC BY 4.0. The Python program in
`source/anc/`: Apache License 2.0. See `LICENSE.md`.
