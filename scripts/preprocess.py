# Lucas Ondel, LISN, 2022

import argparse

# This is a mapping from the original file language code to the
# ISO 639-3 code.
# See:
#   * https://iso639-3.sil.org/code_tables/639/data
#   * https://en.wikipedia.org/wiki/ISO_639-3
language_mapping = {
    'deu': 'nld',
    'fra': 'fra',
    'ita': 'ita',
    'pol': 'pol',
    'rus': 'rus',
    'spa': 'spa'
}

# Speaker list.
speakers = {
    'Lucas_Werkmeister':     1,
    'PeterTheOne':           2,
    '0x010C':                3,
    'GrandCelinien':         4,
    'Guilhelma':             5,
    'Pamputt':               6,
    'Benoît_Prieur':         7,
    'Xenophôn':              8,
    'Exilexi':               9,
    'Happypheasant':        10,
    'Yiyi':                 11,
    'KaMan':                12,
    'Reda_Kerbouche':       13,  # Reda and Tatiana Kerbouche (Kerbush) are
    'Tatiana_Kerbush':      13,  # associated to the same ID.
    'Ahoraes':              14,
    'Anonymât':             15,
    'Eavqwiki':             16,
    'Remux':                17,
    'Rodelar':              18
}

# X-Sampa to IPA mapping.
phone_mapping = {
    '@':    'ə',
    '1':    'ɨ',
    '2':    'ø',
    '2:':   'øː',
    '6':    'ɐ',
    '9':    'œ',
    '9~':   'œ̃',
    'a':    'a',
    'a:':   'aː',
    'a~':   'ã',
    'aI':   'aI',
    'aU':   'aʊ',
    'e':    'e',
    'e:':   'eː',
    'e~':   'ẽ',
    'E':    'ɛ',
    'E:':    'ɛː',
    'i':    'i',
    'i:':   'iː',
    'I':    'I',
    'o':    'o',
    'o:':   'oː',
    'o~':   'õ',
    'O':    'ɔ',
    'OY':   'ɔY',
    'u':    'u',
    'u:':   'uː',
    'U':    'ʊ',
    'y:':   'yː',
    'Y':    'Y'
}

def find_speaker(field, speakers):
    for s in speakers:
        if s in field:
            return s
    else:
        return ""

def main(args):
    with open(args.raw_input, 'r') as f:
        # Skip the first line that contains the meta-data.
        f.readline()

        #print(f'{"lang":<4}\t{"ipa":>3}\t{"f1":>9}\t{"f2":>9}\t{"f3":>9}\t{"duration":>9}')

        for line in f:
            tokens = line.strip().split(',')
            lang = language_mapping[tokens[0]]
            ipa = phone_mapping[tokens[1]]
            f1 = float(tokens[3])
            f2 = float(tokens[4])
            f3 = float(tokens[5])
            duration = float(tokens[6])
            speaker = speakers[find_speaker(tokens[2], speakers.keys())]

            print(f'{lang}\t{speaker:3}\t{ipa}\t{f1:9.4f}\t{f2:9.4f}\t{f3:9.4f}\t{duration:9.4f}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('raw_input', help='input csv file')
    args = parser.parse_args()
    main(args)

