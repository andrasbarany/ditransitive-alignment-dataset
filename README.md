# Data set of ditransitive alignment patterns

This repository is a data set of case and agreement alignment patterns in over
120 languages.

## Data

The data can be found in `languages.csv` in which each line represents one data
point, a ditransitive or transitive sentence. The CSV file provides the
language, source, alignment type, gloss, as well as the case and agreement
properties of the arguments for each data point.

The script `data.py` provides a few simple ways of accessing the data. The
script needs the name of a language in the database as an argument (and
optionally takes an example number). For example, running `./data.py gorwaa`
prints the two examples from Gorwaa found in the data set.

```
> ./data.py gorwaa
Example (2), Gorwaa, ICIA (Harvey 2018: 176)
mwalimú kitaabú ng-u-∅-(g)a hariís dír desír
teacher.LMo book.LMo A.3-P.M-AUX-PRF bring.M.PST to girl.LFR
The teacher brought the book to the girl.

Example (3), Gorwaa, SCSA (Harvey 2018: 176)
mwalimú desír ng-a-∅-na kitaabú-i hariís
teacher.LMo girl.LFR A.3-P.F-AUX-IMPRF book.LMo-LAT bring.M.PST
The teacher brought the girl the book.
```

Optionally, at least one example number can be provided as an argument. The
script then prints a LaTeX-formatted version of the example(s), using the
syntax of the [ExPeX](https://ctan.org/pkg/expex) package for examples and the
[leipzig](https://ctan.org/pkg/leipzig?lang=en) package for glosses.
Non-standard abbreviations follow the original authors' usage and might not be
available for `leipzig`.

```
> ./data.py gorwaa 3
\ex\label{ex:gorwaa-3}
    \begingl
        \glpreamble Gorwaa, SCSA, \parencite[176]{Harvey2018}//
        \gla mwalimú desír ng-a-∅-na kitaabú-i hariís//
        \glb teacher.\Lmo{} girl.\Lfr{} \A{}.\Third-\P{}.\F{}-\Aux{}-\Imprf{} book.\Lmo{}-\Lat{} bring.\M{}.\Pst{}//
        \glft `The teacher brought the girl the book.'//
    \endgl
\xe
```

Instead of using glossing commands, by adding the option `smallcaps`, the output
uses the LaTeX command `\textsc{}` to format grammatical morphemes in small
capitals:

```
> ./data.py gorwaa 3 smallcaps
\ex\label{ex:gorwaa-3}
    \begingl
        \glpreamble Gorwaa, SCSA, \parencite[176]{Harvey2018}//
        \gla mwalimú desír ng-a-∅-na kitaabú-i hariís//
        \glb teacher.\textsc{lmo} girl.\textsc{lfr} A.3-\textsc{p}.\textsc{f}-\textsc{aux}-\textsc{imprf} book.\textsc{lmo}-\textsc{lat} bring.\textsc{m}.\textsc{pst}//
        \glft `The teacher brought the girl the book.'//
    \endgl
\xe
```

## Sources

In addition to the data itself, the file `sources.bib` contains the
bibliographical information of the sources listed in the `citekey` column of
`languages.csv`.
