# Data set of ditransitive alignment patterns

This repository is a data set of case and agreement alignment patterns in over
120 languages.

## Data

The data can be found in `languages.csv` in which each line represents one data
point, a ditransitive or transitive sentence. The CSV file provides the
language, source, alignment type, gloss, as well as the case and agreement
properties of the arguments for each data point.

### Structure

`languages.csv` is a CSV file (using `;` as a separator) with 24 columns.

- `Language`: Name of language
- `Original`: Original text of examples in source language
- `Gloss`: Gloss (sometimes adapted)
- `Translation`: Translation from source
- `Type`: Case and agreement alignment for ditransitives, Transitive, Intransitive, or Recipient passive
- `Remarks`: Additional remarks
- `Source`: Source of example in plain text
- `Citekey`: biblatex citekey (see [sources.bib](sources.bib))
- `Page`: Page number containing example in source
- `Exno`: Example number in source
- `AddSourceInfo`: Additional source information if available
- `Predicate`: Predicate in source language, e.g. *give*
- `SbjPrs`: Person of subject
- `SbjNbr`: Number of subject
- `SbjGen`: Gender of subject
- `SbjCase`: Case of subject
- `RPrs`: Person of recipient
- `RNbr`: Number of recipient
- `RGen`: Gender of recipient
- `RCase`: Case of recipient
- `TPrs`: Person of theme/patient
- `TNbr`: Number of theme/patient
- `TGen`: Gender of theme/patient
- `TCase`: Case of theme/patient

In the case of passives, `Type` is `Recipient passive` or `Theme passive`, the
features of the recipient and the theme are specified, and `SbjPrs`, `SbjNbr`,
`SbjGen`, `SbjCase` are left empty.

### Printing data to the console

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

Instead of using glossing commands, by adding the option `--style smallcaps`,
the output uses the LaTeX command `\textsc{}` to format grammatical morphemes
in small capitals:

```
> ./data.py gorwaa 3 --style smallcaps
\ex\label{ex:gorwaa-3}
    \begingl
        \glpreamble Gorwaa, SCSA, \parencite[176]{Harvey2018}//
        \gla mwalimú desír ng-a-∅-na kitaabú-i hariís//
        \glb teacher.\textsc{lmo} girl.\textsc{lfr} A.3-\textsc{p}.\textsc{f}-\textsc{aux}-\textsc{imprf} book.\textsc{lmo}-\textsc{lat} bring.\textsc{m}.\textsc{pst}//
        \glft `The teacher brought the girl the book.'//
    \endgl
\xe
```

### Accessing data using Python or R

The data in `languages.csv` can be used easily with Python or R etc.

The following code block loads `languages.csv` into a data frame called
`languages` using `pandas`.

```python
> import pandas
> languages = pandas.read_csv('languages.csv', sep=';')
> languages
        Language                                           Original                                              Gloss                                        Translation  ... TPrs TNbr TGen TCase
0      Hungarian                            Mari lát-ja a könyv-et.              Mari see-3SG.SBJ>3SG.OBJ the book-ACC                                Mari sees the book.  ...    3   SG  NaN   ACC
1      Hungarian                       Mari neked ad-ja a könyv-et.     Mari 2SG.DAT give-3SG.SBJ>3SG.OBJ the book-ACC                           Mari gives you the book.  ...    3   SG  NaN   ACC
2         Gorwaa       mwalimú kitaabú ng-u-∅-(g)a hariís dír desír  teacher.LMo book.LMo A.3-P.M-AUX-PRF bring.M.P...          The teacher brought the book to the girl.  ...    3   SG    M   NOM
3         Gorwaa           mwalimú desír ng-a-∅-na kitaabú-i hariís  teacher.LMo girl.LFR A.3-P.F-AUX-IMPRF book.LM...             The teacher brought the girl the book.  ...    3   SG    M   LAT
4    Kapampangan         Mamye (ya)ng tela ing mestra kareng babai.                    give cloth the teacher to women          The teacher will give cloth to the women.  ...    3   SG  NaN   ABS
..           ...                                                ...                                                ...                                                ...  ...  ...  ...  ...   ...
803      Yukulta   tʸina-ŋka ṭat̪int ṭaŋka-ŋala-pakarі miyaḷṭa y...  where-PRES that+ABS man-ŋala-you+TR+PRES spear...           Where's that man who gave you the spear?  ...    3   SG  NaN   ABS
804        Yurok                               nek nahci-s-ek' ci·k                               I give-3SG-1SG money                                   I gave him money  ...    3   SG  NaN   NOM
805        Yurok                                    nek nahci-s-ek'                                     I give-3SG-1SG                                   I give it to him  ...    3   SG  NaN   NaN
806        Yurok                             nek nahci-s-ek' ku cey                               I give-3SG-1SG child                             I give it to the child  ...    3   SG  NaN   NaN
807         Zulu  uMandla u- bona [ukuthi ngi- ya- m- thanda] [u...  AUG.1Mandla 1S- see that 1SG- YA- 1O- like  wh...  Mandla sees that I like him when I give him pr...  ...    3   PL  NaN   NOM

[808 rows x 24 columns]
```

There are 139 examples with neutral case and secundative agreement alignment
(NCSA) in which the recipient's person (the agreement controller in secundative
agreement) is first person:

```python
> languages.loc[(languages['Type'] == 'NCSA') & (languages['R-Prs'] == '1')]
        Language                                           Original                                              Gloss  ... TNbr TGen TCase
0      Hungarian                            Mari lát-ja a könyv-et.              Mari see-3SG.SBJ>3SG.OBJ the book-ACC  ...   SG  NaN   ACC
1      Hungarian                       Mari neked ad-ja a könyv-et.     Mari 2SG.DAT give-3SG.SBJ>3SG.OBJ the book-ACC  ...   SG  NaN   ACC
2         Gorwaa       mwalimú kitaabú ng-u-∅-(g)a hariís dír desír  teacher.LMo book.LMo A.3-P.M-AUX-PRF bring.M.P...  ...   SG    M   NOM
3         Gorwaa           mwalimú desír ng-a-∅-na kitaabú-i hariís  teacher.LMo girl.LFR A.3-P.F-AUX-IMPRF book.LM...  ...   SG    M   LAT
4    Kapampangan         Mamye (ya)ng tela ing mestra kareng babai.                    give cloth the teacher to women  ...   SG  NaN   ABS
..           ...                                                ...                                                ...  ...  ...  ...   ...
803      Yukulta   tʸina-ŋka ṭat̪int ṭaŋka-ŋala-pakarі miyaḷṭa y...  where-PRES that+ABS man-ŋala-you+TR+PRES spear...  ...   SG   NaN   ABS
804        Yurok                               nek nahci-s-ek' ci·k                               I give-3SG-1SG money  ...   SG  NaN   NOM
805        Yurok                                    nek nahci-s-ek'                                     I give-3SG-1SG  ...   SG  NaN   NaN
806        Yurok                             nek nahci-s-ek' ku cey                               I give-3SG-1SG child  ...   SG  NaN   NaN
807         Zulu  uMandla u- bona [ukuthi ngi- ya- m- thanda] [u...  AUG.1Mandla 1S- see that 1SG- YA- 1O- like  wh...  ...   PL  NaN   NOM

[808 rows x 24 columns]
```

To get the same information in R using `tidyverse`, you can do the following:

```R
> library('tidyverse')
> languages <- read_csv2('languages.csv')
> languages %>% filter(Type == 'NCSA' & RPrs == '1')
# A tibble: 139 × 24
   Language  Original                                                   Gloss         Translation Type  Remarks Source Citekey Page  Exno  AddSourceInfo Predicate SbjPrs SbjNbr SbjGen SbjCase RPrs  RNbr  RGen  RCase TPrs  TNbr  TGen  TCase
   <chr>     <chr>                                                      <chr>         <chr>       <chr> <chr>   <chr>  <chr>   <chr> <chr> <chr>         <chr>      <dbl> <chr>  <chr>  <chr>   <chr> <chr> <chr> <chr> <chr> <chr> <chr> <chr>
 1 Movima    kɑyɬe:-kɑy--isne is lɑwɑ:jes                               give-INV-f.a… She gave m… NCSA  NA      Haude… Haude2… 404   162   {DM, Fracaso… give           3 SG     NA     NA      1     SG    NA    NA    3     SG    NA    NOM
 2 Squamish  mi-ši-t-c-ka kʷi stáqʷ!                                    come-RDR-TR-… Bring me s… NCSA  NA      Kuipe… Kiyosa… 50    47    NA            bring (i…     NA NA     NA     NA      1     SG    NA    NA    3     SG    NA    NOM
 3 Jingulu   Ngunyɑ-ɑnɑ-mi ngɑmɑniki-rni milɑkurrmi-rni, ngunyɑ-ɑnɑ-mi! give-1O-IRR … Give me th… NCSA  Pensal… Pensa… Pensal… 107   4.46k NA            give (im…     NA NA     NA     NA      1     SG    NA    NA    3     PL    NA    ABS
 4 Rembarnga tiŋʔ - yiʔ ŋinta - Ø  ŋana - pak - larayʔ - miɲ ţeɲ -  Ø   woman - ERG … The women … NCSA  NA      McKay… McKay1… 298   (3.4… NA            cook           3 PL     NA     ERG     1     SG    NA    NOM   3     SG    NA    ABS(…
 5 Ainu      A-en-kore.                                                 2HON-1SG-give You (HON) … NCSA  NA      Shiba… Shibat… 56    94c   NA            give           2 HON    NA     NA      1     SG    NA    NA    3     SG    NA    NA
 6 Ainu      Ku-cis-kor sonno en-erɑmpokinu, beko tope poronno en-kore. 1SG-cry PROG… I was cryi… NCSA  NA      Shiba… Shibat… 86    7     NA            give           3 SG     NA     NA      1     SG    NA    NA    3     SG    NA    NOM
 7 Apurinã   pu-sukɑ-no notɑ                                            2SG-give-1SG… Give away … NCSA  potent… Facun… Facund… 290   20a   NA            give (im…      2 SG     NA     NA      1     SG    NA    NOM   NA    NA    NA    NA
 8 Bagirmi   N-ád-ūm jā mɨ̀-sáà.                                         he-gave-me m… He gave me… NCSA  NA      Keega… Keegan… 17    NA    NA            give           3 SG     NA     NA      1     SG    NA    NA    3     SG    NA    NOM
 9 Bagirmi   ád-ūm jó nén kūyú.                                         give-me to o… Give me an… NCSA  NA      Keega… Keegan… 25    NA    NA            give (im…     NA NA     NA     NA      1     SG    NA    NA    3     SG    NA    NOM
10 Bagirmi   ād-ūm kāɗ-mbī kéɗē.                                        give-me spoo… Give me a … NCSA  NA      Keega… Keegan… 27    NA    NA            give (im…     NA NA     NA     NA      1     SG    NA    NA    3     SG    NA    NOM
# … with 129 more rows
```

### Empty cells

Not all cells are filled. Empty cells represent missing information from the
data points. If an argument is not expressed as a full NP, for example, but
only as an agreement marker, its value in the `Case` column is simply missing.
In contrast, for transitives, the values for the recipient (`RPrs`, `RNbr`,
`RGen`, `RCase`) are `/`.

## Sources

In addition to the data itself, the file `sources.bib` contains the
bibliographical information of the sources listed in the `citekey` column of
`languages.csv`.

## Publications using (part of) the data set

Bárány, András. 2021. [A typological gap in ditransitive constructions: No
secundative case and indirective
agreement](https://www.lingref.com/cpp/wccfl/38/abstract3549.html). In Rachel
Soo, Una Y. Chow & Sander Nederveen (eds.), *Proceedings of the 38th West Coast
Conference on Formal Linguistics*, 43–53. Somerville, MA: Cascadilla
Pro-ceedings Project.

## Using the data
