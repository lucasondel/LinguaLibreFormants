# Lucas Ondel, LISN, 2022

import argparse

# This is a mapping from the original file language code to the
# ISO 639-3 code.
# See:
#   * https://iso639-3.sil.org/code_tables/639/data
#   * https://en.wikipedia.org/wiki/ISO_639-3
#
# NOTE: now the mapping is just identity so not very useful. I keep
# it nonetheless to facilitate the use of another mapping.
language_mapping = {
    'deu': 'deu',
    'fra': 'fra',
    'ita': 'ita',
    'pol': 'pol',
    'rus': 'rus',
    'spa': 'spa'
}

# Speaker list.
speakers = {
    'Lucas_Werkmeister':    'spk1',
    'PeterTheOne':          'spk2',
    '0x010C':               'spk3',
    'GrandCelinien':        'spk4',
    'Guilhelma':            'spk5',
    'Pamputt':              'spk6',
    'Benoît_Prieur':        'spk7',
    'Xenophôn':             'spk8',
    'Exilexi':              'spk9',
    'Happypheasant':        'spk10',
    'Yiyi':                 'spk11',
    'KaMan':                'spk12',
    'Reda_Kerbouche':       'spk13',
    'Tatiana_Kerbush':      'spk14',
    'Ahoraes':              'spk15',
    'Anonymât':             'spk16',
    'Eavqwiki':             'spk17',
    'Remux':                'spk18',
    'Rodelar':              'spk19'
}

# The speakers sex
speakers_sex = {
    'Lucas_Werkmeister':    'male',
    'PeterTheOne':          'male',
    '0x010C':               'male',
    'GrandCelinien':        'male',
    'Guilhelma':            'female',
    'Pamputt':              'male',
    'Benoît_Prieur':        'male',
    'Xenophôn':             'male',
    'Exilexi':              'female',
    'Happypheasant':        'female',
    'Yiyi':                 'male',
    'KaMan':                'male',
    'Reda_Kerbouche':       'male',
    'Tatiana_Kerbush':      'female',
    'Ahoraes':              'male',
    'Anonymât':             'male',
    'Eavqwiki':             'female',
    'Remux':                'male',
    'Rodelar':              'male'
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
            spk_name = find_speaker(tokens[2], speakers.keys())
            speaker = speakers[spk_name]
            sex = speakers_sex[spk_name]

            print(f'{lang}\t{speaker:3}\t{sex}\t{ipa}\t{f1:9.4f}\t{f2:9.4f}\t{f3:9.4f}\t{duration:9.4f}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('raw_input', help='input csv file')
    args = parser.parse_args()
    main(args)

