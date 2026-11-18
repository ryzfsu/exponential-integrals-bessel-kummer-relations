# Building the paper

Use pdfLaTeX and BibTeX from TeX Live 2026, including AMS-LaTeX, AMSFonts,
mathtools, mathrsfs, hyperref and the Type 1 Computer Modern and RSFS fonts.
The PDF font map must include the RSFS outlines. For example, the pdfTeX
map should contain an entry for rsfs10.pfb. Use Poppler for the PDF checks.

From a clean copy of the source directory, run:

```sh
export TZ=UTC LC_ALL=C SOURCE_DATE_EPOCH=1794873600 FORCE_SOURCE_DATE=1
pdflatex -recorder -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -recorder -interaction=nonstopmode -halt-on-error main.tex
pdflatex -recorder -interaction=nonstopmode -halt-on-error main.tex
```

Repeat the last command if cross-references have not settled. The resulting
main.log and main.blg should have no unresolved references or citations,
duplicate labels, overfull boxes or bibliography warnings. Inspect the
complete build output for bitmap-font generation. Verify the PDF with:

```sh
pdffonts main.pdf
pdfinfo main.pdf
```

There should be no Type 3 fonts; the section signs and script letters must
retain their shapes. The PDF should identify the title, author, subject and
keywords. The fixed build timestamp corresponds to the title date at
midnight UTC. The ancillary calculation is described in anc/N1-README.md.
