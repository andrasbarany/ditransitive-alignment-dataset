#!/usr/bin/env python3
# coding=utf8
import argparse
import re

import pandas

parser = argparse.ArgumentParser(description='Print examples from \
                            ditransitives database.')
parser.add_argument('language', metavar='language', type=str,
                    help='language')
parser.add_argument('exno', nargs='*', metavar='exno', type=int,
                    help='example number to print')
parser.add_argument('--style', nargs='?', metavar='style', type=str,
                    help='leipzig-style glosses or small caps')


args = parser.parse_args()
language = vars(args)['language'].capitalize()
languages = pandas.read_csv('languages.csv', sep=';')
data = languages.loc[languages['Language'] == language]


def format_ex(nmbr):
    output = 'Example (' + str(nmbr) + '), ' + \
             language + ', ' + \
             data['Type'][nmbr] + \
             ' (' + \
             data['Source'][nmbr].replace('(', '').replace(')', '') + \
             ')' + \
             '\n' + \
             data['Original'][nmbr] + '\n' + \
             data['Gloss'][nmbr] + '\n' + \
             data['Translation'][nmbr]
    return output


# LaTeX output
def latex_ex(style):
    examples = ''
    if len(vars(args)['exno']) > 1:
        sep = '\n'
    else:
        sep = ''
    for nmbr in vars(args)['exno']:
        output = '\\ex\\label{ex:' + vars(args)['language'] + \
                 '-' + str(nmbr) + '}' + \
                 '\n    \\begingl\n' + \
                 '        \\glpreamble ' + language + ', ' + \
                 data['Type'][nmbr] + ', ' + \
                 '\\parencite[' + str(data['Page'][nmbr]) + ']{' + \
                 str(data['Citekey'][nmbr]) + '}//\n' + \
                 '        \\gla ' + data['Original'][nmbr] + '//\n' + \
                 '        \\glb ' + glossify(data['Gloss'][nmbr],
                                             style) + '//\n' + \
                 '        \\glft `' + data['Translation'][nmbr] + "'//\n" + \
                 '    \\endgl\n\\xe' + sep
        examples = examples + sep + output
    return examples.strip('\n')


def glossify(string, style='expex'):
    if style == 'expex':
        string = re.sub(r'(\.|-|>)([A-Za-z]{1,5})',
                        lambda m: m.group(1) + '\\' +
                        m.group(2).title() + '{}',
                        string)
        string = re.sub(r'( |^)([A-Z]{1,5})(\.|-)',
                        lambda m: m.group(1) + '\\' +
                        m.group(2).title() + '{}' +
                        m.group(3),
                        string)
        string = re.sub(r'1(SG|PL|DU)',
                        lambda m: r'\F' + m.group(1).lower(),
                        string)
        string = re.sub(r'2(SG|PL|DU)',
                        lambda m: r'\S' + m.group(1).lower(),
                        string)
        string = re.sub(r'3(SG|PL|DU)',
                        lambda m: r'\T' + m.group(1).lower() + '{}',
                        string)
        string = re.sub(r'3(\.|-|>)', r'\\Third\1', string)
    elif style == 'smallcaps':
        string = re.sub(r'(\.|-|>)([0-9]?[A-Za-z]{1,5})',
                        lambda m: m.group(1) + '\\textsc{' +
                        m.group(2).lower() + '}',
                        string)
    return string


def print_exx():
    print(*[format_ex(nmbr) for nmbr in data.index],
          sep='\n\n')


def print_exno(nmbr):
    if nmbr >= len(data['Original']):
        try:
            data['Original'][nmbr]
        except (KeyError, ValueError) as err:
            print('Sorry, "' + str(err) + '" is not a valid example number.')
    else:
        pass  # return format_ex(nmbr)


def print_lang(language):
    if type(language) != list:
        langs = [language]
    else:
        langs = language
    return [languages[languages['Language'] == language.capitalize()] for
            language in langs]


if len(vars(args)['exno']) > 0:
    if vars(args)['style'] == 'smallcaps':
        print(latex_ex('smallcaps'))
    else:
        print(latex_ex('expex'))
else:
    print_exx()
