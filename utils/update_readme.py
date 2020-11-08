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
    problems = {}
    # get root directory
    cwd = Path(__file__).parents[0]
    root_dir = cwd / '..'
    # set argprase
    parser = argparse.ArgumentParser(description='Generate Triple-Z/LeetCode README file automatically.')
    parser.add_argument('-o', '--output-file', dest='output_file_name', type=str, default='README-generated.md')

    args = parser.parse_args()
    output_file_name = args.output_file_name
    logging.debug('Output file name is: {}'.format(output_file_name))

    # get all the files
    java_filelist = Path(root_dir).glob('java/src/*.java')
    py3_filelist = Path(root_dir).glob('py3/*.py')
    cpp_filelist = Path(root_dir).glob('cpp/src/*.cpp')
    doc_filelist = Path(root_dir).glob('docs/*.md')

    java_pattern = re.compile(r'java\/src\/(\d+)\. [\w\-]+\.java', re.ASCII)
    py3_pattern = re.compile(r'py3\/(\d+)\.py', re.ASCII)
    cpp_pattern = re.compile(r'cpp\/src\/(\d+)\.cpp', re.ASCII)
    doc_pattern = re.compile(r'docs\/(\d+)\. ([\w\d\s\'\"\(\)\-]+)(\s+[\u4e00-\u9fa5\w\d\s\(\)]+)?\.md', re.ASCII)
    problem_info_pattern = re.compile(r'-\sDifficulty:\s(Easy|Medium|Hard)\s*\n-\sTopics:\s(`[`\w\d\s\,\-]+`)\s*\n-\sLink:\s((?:http|https):\/\/.*)\s*\n', re.ASCII)

    # add java files
    for java_file in java_filelist:
        # processing filename
        java_res = java_pattern.search(str(java_file))
        if java_res is None:
            logging.warning('The filename {} is invalid, ignored.'.format(java_file))
            continue
        
        number = java_res.group(1)
        logging.debug('processing {} java file'.format(number))
        
        number_problem = problems.get(number)
        rel_java_file = java_file.relative_to(root_dir)
        if number_problem is None:
            new_problem = Problem()
            new_problem.number = number
            new_problem.is_solved = True
            new_problem.java = quote(str(rel_java_file))
            problems[number] = new_problem
        else:
            number_problem.java = quote(str(rel_java_file))
            number_problem.is_solved = True

    # add python3 files
    for py3_file in py3_filelist:
        py3_res = py3_pattern.search(str(py3_file))
        if py3_res is None:
            logging.warning('The filename {} is invalid, ignored.'.format(py3_file))
            continue
        number = py3_res.group(1)
        logging.debug('processing {} python3 file'.format(number))
        
        number_problem = problems.get(number)
        rel_py3_file = py3_file.relative_to(root_dir)
        if number_problem is None:
            new_problem = Problem()
            new_problem.number = number
            new_problem.is_solved = True
            new_problem.py3 = quote(str(rel_py3_file))
            problems[number] = new_problem
        else:
            number_problem.py3 = quote(str(rel_py3_file))
            number_problem.is_solved = True

    # add cpp files
    for cpp_file in cpp_filelist:
        cpp_res = cpp_pattern.search(str(cpp_file))
        if cpp_res is None:
            logging.warning('The filename {} is invalid, ignored.'.format(cpp_file))
            continue
        number = cpp_res.group(1)
        logging.debug('processing {} cpp file'.format(number))

        number_problem = problems.get(number)
        rel_cpp_file = cpp_file.relative_to(root_dir)
        if number_problem is None:
            new_problem = Problem()
            new_problem.number = number
            new_problem.is_solved = True
            new_problem.cpp = quote(str(rel_cpp_file))
            problems[number] = new_problem
        else:
            number_problem.cpp = quote(str(rel_cpp_file))
            number_problem.is_solved = True

    # add docs
    for doc in doc_filelist:
        doc_res = doc_pattern.search(str(doc))
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
        rel_doc_file = doc.relative_to(root_dir)
        if number_problem is None:
            new_problem = Problem()
            new_problem.number = number
            new_problem.title_en = title_en
            new_problem.title_zh = title_zh
            new_problem.difficulty = difficulty
            new_problem.topics = topics
            new_problem.link = problem_link
            new_problem.doc = quote(str(rel_doc_file))
            problems[number] = new_problem
        else:
            number_problem.title_en = title_en
            number_problem.title_zh = title_zh
            number_problem.difficulty = difficulty
            number_problem.topics = topics
            number_problem.link = problem_link
            number_problem.doc = quote(str(rel_doc_file))
    
    # sort problems by its number
    problems_number_list = sorted(problems, key=int)

    problems_list = []
    for problem in problems_number_list:
        problems_list.append(problems[problem])
    
    logging.debug(problems_list)
    # using jinja2 render the README file
    loader = FileSystemLoader(root_dir / 'utils' /'templates')
    env = Environment(loader=loader)
    readme_template = env.get_template('README.md.j2')
    readme_template.globals['now'] = datetime.utcnow
    readme_generated = readme_template.render(problems_list=problems_list)
    logging.debug(readme_generated)

    # update README.md

    with open(str(root_dir / output_file_name), 'w') as readme:
        readme.write(readme_generated)
    logging.info("""

    The new README file has written to {}, go there and check it 🎉
    If you are satisfied with this generated README file, just type `make update-change`.
    """.format(output_file_name))

if __name__ == "__main__":
    main()
