# LinguaLibreFormants

This is a database containing the formant frequencies (f1, f2, f3)
measured on recordings from [Lingua Libre](https://lingualibre.org/wiki/LinguaLibre:Main_Page).

This data is released under the **CC BY 4.0** licence.

## Data
The formants data is contained in the file [data/formants.tsv](https://github.com/lucasondel/LinguaLibreFormants/blob/main/data/formants.tsv).
It is a tab-separated value with 7 fields:
```
lang-id speaker-id  ipa f1 f2 f3 duration
```
where:
* `lang-id` is the [ISO 639-3](https://iso639-3.sil.org/code_tables/639/data)
  language code
* `speaker-id` is a numeric identifier (from 1 to 18) for the speaker
* `ipa` is the ipa notation of the uttered vowel
* `f1`, `f2`, `f3` frequencies for each 3 first formants
* `duration` is the vowel duration.

The recordings were time-aligned with [MAUS](https://www.bas.uni-muenchen.de/Bas/BasMAUS.html)
and the formants value were extracted with [PRAAT](https://www.fon.hum.uva.nl/praat/).

## Authors

* [Marc Allassonnière-Tang](https://www.marctang.info/)
* [Mathilde Hutin](https://mathildehutin.wordpress.com/)
* [Lucas Ondel](https://lucasondel.github.io/)

