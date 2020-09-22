#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import logging

from pathlib import Path
from urllib.parse import quote
from problem import Problem


def main():
    logging.basicConfig(level=logging.DEBUG)
    problems = {}

    # get all the files
    java_filelist = Path('.').glob('java/src/*.java')
    py3_filelist = Path('.').glob('py3/*.py')
    cpp_filelist = Path('.').glob('cpp/src/*.cpp')
    doc_filelist = Path('.').glob('docs/*.md')

    java_pattern = re.compile(r'java\/src\/(\d+)\. \w+\.java', re.ASCII)
    py3_pattern = re.compile(r'py3\/(\d+)\.py', re.ASCII)
    cpp_pattern = re.compile(r'cpp\/src\/(\d+)\.cpp', re.ASCII)
    doc_pattern = re.compile(r'docs\/(\d+)\. ([\w\d\s\(\)]+)(\s+[\u4e00-\u9fa5][\u4e00-\u9fa5\w\d\s\(\)]+)?\.md', re.ASCII)
    problem_info_pattern = re.compile(r'-\sDifficulty:\s(Easy|Medium|Hard)\s*\n-\sTopics:\s(`[`\w\d\s\,\-]+`)\s*\n-\sLink:\s((?:http|https):\/\/.*)\s*\n', re.ASCII)

    # add java files
    for java_file in java_filelist:
        # processing filename
        java_res = java_pattern.match(str(java_file))
        if java_res is None:
            logging.warning('The filename {} is invalid, ignored.'.format(java_file))
            continue
        
        number = java_res.group(1)
        logging.debug('processing {} java file'.format(number))
        
        number_problem = problems.get(number)
        if number_problem is None:
            new_problem = Problem()
            new_problem.number = number
            new_problem.java = quote(str(java_file))
            problems[number] = new_problem
        else:
            number_problem.java = quote(str(java_file))

    # add python3 files
    for py3_file in py3_filelist:
        py3_res = py3_pattern.match(str(py3_file))
        if py3_res is None:
            logging.warning('The filename {} is invalid, ignored.'.format(py3_file))
            continue
        number = py3_res.group(1)
        logging.debug('processing {} python3 file'.format(number))
        
        number_problem = problems.get(number)
        if number_problem is None:
            new_problem = Problem()
            new_problem.number = number
            new_problem.py3 = quote(str(py3_file))
            problems[number] = new_problem
        else:
            number_problem.py3 = quote(str(py3_file))

    # add cpp files
    for cpp_file in cpp_filelist:
        cpp_res = cpp_pattern.match(str(cpp_file))
        if cpp_res is None:
            logging.warning('The filename {} is invalid, ignored.'.format(cpp_file))
            continue
        number = cpp_res.group(1)
        logging.debug('processing {} cpp file'.format(number))

        number_problem = problems.get(number)
        if number_problem is None:
            new_problem = Problem()
            new_problem.number = number 
            new_problem.cpp = quote(str(cpp_file))
            problems[number] = new_problem
        else:
            number_problem.cpp = quote(str(cpp_file))

    # add docs
    for doc in doc_filelist:
        doc_res = doc_pattern.match(str(doc))
        if doc_res is None:
            logging.warning('The filename {} is invalid, ignored.'.format(doc))
            continue
        number = doc_res.group(1)
        title_en = doc_res.group(2)
        title_zh = doc_res.group(3)
        logging.debug('processing {} doc file, {}, {}'.format(number, title_en, title_zh))

        # open the doc to get problem info
        difficulty, topics, problem_link = None, None, None
        with open(str(doc), 'r') as doc_file:
            # read the first 10 lines for each doc file
            file_head = [next(doc_file) for x in range(10)]
            file_head = ''.join(file_head)
            file_res = problem_info_pattern.search(file_head)
            if file_res is None:
                logging.warning('Cannot get problem info in {} , ignored'.format(doc))
                logging.debug(file_head)
            else:
                difficulty = file_res.group(1)
                topics = file_res.group(2)
                problem_link = file_res.group(3)


        number_problem = problems.get(number)
        if number_problem is None:
            new_problem = Problem()
            new_problem.number = number
            new_problem.title_en = title_en
            new_problem.title_zh = title_zh
            new_problem.difficulty = difficulty
            new_problem.topics = topics
            new_problem.link = problem_link
            new_problem.doc = quote(str(doc))
            problems[number] = new_problem
        else:
            number_problem.title_en = title_en
            number_problem.title_zh = title_zh
            number_problem.difficulty = difficulty
            number_problem.topics = topics
            number_problem.link = problem_link
            number_problem.doc = quote(str(doc))
    
    # sort problems by its number
    problems_list = sorted(problems, key=int)

    for problem in problems_list:
        logging.debug(problems[problem])
    
    # TODO: render the README file
    

if __name__ == "__main__":
    main()
