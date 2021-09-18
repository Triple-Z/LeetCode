#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import argparse
import logging

from datetime import datetime
from pathlib import Path
from urllib.parse import quote
from problem import Problem
from jinja2 import FileSystemLoader, Environment


def main():
    logging.basicConfig(level=logging.INFO)
    # get root directory
    cwd = Path(__file__).parents[0]
    root_dir = cwd / '..'
    # set argprase
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-i', '--interactive', dest='is_interactive', action='store_true', default=False)

    args = parser.parse_args()
    is_interactive = args.is_interactive

    # interactive input problem info(number, title_en, title_zh, difficulty, topics, link)
    if is_interactive:
        problem_number = input('Input the problem number: ')
        
        title_en = input('Input the problem English title: ')
        title_zh = input('Input the problem Chinese title: ')
        difficulty = input('Input the problem difficulty (e:Easy, m:Medium, h:Hard): ')
        difficulty = {
            'e': 'Easy',
            'm': 'Medium',
            'h': 'Hard',
        }.get(difficulty)
        if difficulty is None:
            logging.error('The difficulty is required!')
            exit(1)
        
        topics_str = input('Input the problem topics (sep in comma): ')
        topics = topics_str.split(',')
        for i, topic in enumerate(topics):
            topics[i] = topic.strip()
        
        link = input('Input the problem link: ')
        if not (link.startswith('http://') or link.startswith('https://')):
            logging.error('The problem link must be start with `http://` or `https://`')
            exit(1)
        
        problem = Problem()
        problem.number = problem_number
        problem.title_en = title_en
        problem.title_zh = title_zh
        problem.difficulty = difficulty
        problem.topics = topics
        problem.link = link

        # using jinja2 render the README file
        loader = FileSystemLoader(root_dir / 'utils' /'templates')
        env = Environment(loader=loader)
        doc_template = env.get_template('doc.md.j2')
        doc_template.globals['now'] = datetime.utcnow
        doc_generated = doc_template.render(problem=problem)
        logging.debug(doc_generated)

        doc_filename = ''
        if title_zh == '':
            doc_filename = '{0}. {1}.md'.format(problem_number, title_en)
        elif title_en == '':
            doc_filename = '{0}. {1}.md'.format(problem_number, title_zh)
        else:
            doc_filename = '{0}. {1} {2}.md'.format(problem_number, title_en, title_zh)
        logging.debug(str(root_dir / 'docs' / doc_filename))
        with open(str(root_dir / 'docs' / doc_filename), 'w') as doc_file:
            doc_file.write(doc_generated)

        logging.info('Doc has been generated to docs/{}'.format(doc_filename))

        # create new code file
        code_option = input('''
Create code file:
    1: Java
    2. Go
    3: Python3
    4: C++
    others: No need
Type your option here: ''')
        code_path = None
        if code_option == '1': # java
            code_path = root_dir / 'java' / 'src' / '{}. {}.java'.format(problem_number.replace(' ', '_'), ''.join(title_en.replace('\'', '').replace('"', '').replace('-', '').replace('(', '').replace(')', '').replace(',', '').split()))
        elif code_option == '2': # go
            code_path = root_dir / 'go' / 'src'/ '{}.go'.format(problem_number.replace(' ', '_'))
        elif code_option == '3': # python3
            code_path = root_dir / 'py3' / '{}.py'.format(problem_number.replace(' ', '_'))
        elif code_option == '4': # C++
            code_path = root_dir / 'cpp' / 'src' / '{}.cpp'.format(problem_number.replace(' ', '_'))
        else:
            logging.info('No need to create code file, exiting...')
            exit(0)
        
        if code_path is not None:
            code_path.touch()
            logging.info('Code file created at {}'.format(str(code_path)))
        
    else:
        # TODO: input via command line
        logging.info('TODO')
        exit(0)

if __name__ == "__main__":
    main()