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
    # logging.basicConfig(level=logging.DEBUG)
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
    go_filelist = Path(root_dir).glob('go/src/*.go')
    py3_filelist = Path(root_dir).glob('py3/*.py')
    cpp_filelist = Path(root_dir).glob('cpp/src/*.cpp')
    doc_filelist = Path(root_dir).glob('docs/*.md')

    java_pattern = re.compile(r'java\/src\/([\d\w\_\-\u4e00-\u9fa5|\u3002|\uff1f|\uff01|\uff0c|\u3001|\uff1b|\uff1a|\u201c|\u201d|\u2018|\u2019|\uff08|\uff09|\u300a|\u300b|\u3008|\u3009|\u3010|\u3011|\u300e|\u300f|\u300c|\u300d|\ufe43|\ufe44|\u3014|\u3015|\u2026|\u2014|\uff5e|\ufe4f|\uffe5]+)\.?\s?[\w\-]*\.java', re.ASCII)
    go_pattern = re.compile(r'go\/src\/([\d\w\_\-\u4e00-\u9fa5|\u3002|\uff1f|\uff01|\uff0c|\u3001|\uff1b|\uff1a|\u201c|\u201d|\u2018|\u2019|\uff08|\uff09|\u300a|\u300b|\u3008|\u3009|\u3010|\u3011|\u300e|\u300f|\u300c|\u300d|\ufe43|\ufe44|\u3014|\u3015|\u2026|\u2014|\uff5e|\ufe4f|\uffe5]+)\.go', re.ASCII)
    py3_pattern = re.compile(r'py3\/([\d\w\_\-\u4e00-\u9fa5|\u3002|\uff1f|\uff01|\uff0c|\u3001|\uff1b|\uff1a|\u201c|\u201d|\u2018|\u2019|\uff08|\uff09|\u300a|\u300b|\u3008|\u3009|\u3010|\u3011|\u300e|\u300f|\u300c|\u300d|\ufe43|\ufe44|\u3014|\u3015|\u2026|\u2014|\uff5e|\ufe4f|\uffe5]+)\.py', re.ASCII)
    cpp_pattern = re.compile(r'cpp\/src\/([\d\w\_\-\u4e00-\u9fa5|\u3002|\uff1f|\uff01|\uff0c|\u3001|\uff1b|\uff1a|\u201c|\u201d|\u2018|\u2019|\uff08|\uff09|\u300a|\u300b|\u3008|\u3009|\u3010|\u3011|\u300e|\u300f|\u300c|\u300d|\ufe43|\ufe44|\u3014|\u3015|\u2026|\u2014|\uff5e|\ufe4f|\uffe5]+)\.cpp', re.ASCII)
    doc_pattern = re.compile(r'docs\/([\d\w\s\_\-\u4e00-\u9fa5|\u3002|\uff1f|\uff01|\uff0c|\u3001|\uff1b|\uff1a|\u201c|\u201d|\u2018|\u2019|\uff08|\uff09|\u300a|\u300b|\u3008|\u3009|\u3010|\u3011|\u300e|\u300f|\u300c|\u300d|\ufe43|\ufe44|\u3014|\u3015|\u2026|\u2014|\uff5e|\ufe4f|\uffe5]+)\. ([\w\d\s\'\"\(\)\-\,\.]+)?(\s?[\uFF00-\uFFFF|\u4e00-\u9fa5|\u3002|\uff1f|\uff01|\uff0c|\u3001|\uff1b|\uff1a|\u201c|\u201d|\u2018|\u2019|\uff08|\uff09|\u300a|\u300b|\u3008|\u3009|\u3010|\u3011|\u300e|\u300f|\u300c|\u300d|\ufe43|\ufe44|\u3014|\u3015|\u2026|\u2014|\uff5e|\ufe4f|\uffe5|\w\d\s\_\-\(\)\,\.\+]+)?\.md', re.ASCII)
    problem_info_pattern = re.compile(r'-\sDifficulty:\s(Easy|Medium|Hard)\s*\n-\sTopics:\s(`[`\w\d\s\,\-]+`)\s*\n-\sLink:\s((?:http|https):\/\/.*)\s*\n', re.ASCII)

    # add java files
    for java_file in java_filelist:
        # processing filename
        java_res = java_pattern.search(str(java_file))
        if java_res is None:
            logging.warning('The filename {} is invalid, ignored.'.format(java_file))
            continue
        
        number = java_res.group(1).replace("_", " ")
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

    # add go files
    for go_file in go_filelist:
        go_res = go_pattern.search(str(go_file))
        if go_res is None:
            logging.warning('The filename {} is invalid, ignored.'.format(go_file))
            continue
        number = go_res.group(1).replace("_", " ")
        logging.debug('processing {} go file'.format(number))

        number_problem = problems.get(number)
        rel_go_file = go_file.relative_to(root_dir)
        if number_problem is None:
            new_problem = Problem()
            new_problem.number = number
            new_problem.is_solved = True
            new_problem.go = quote(str(rel_go_file))
            problems[number] = new_problem
        else:
            number_problem.go = quote(str(rel_go_file))
            number_problem.is_solved = True
    
    # add python3 files
    for py3_file in py3_filelist:
        py3_res = py3_pattern.search(str(py3_file))
        if py3_res is None:
            logging.warning('The filename {} is invalid, ignored.'.format(py3_file))
            continue
        number = py3_res.group(1).replace("_", " ")
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
        number = cpp_res.group(1).replace("_", " ")
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
        if title_en == "":
            title_en = None
        
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
    def cmp(o: str):
        if o.isdigit():
            return int(o)
        elif o.startswith("剑指"):
            if len(o.split()) > 5:
                # 剑指 Offer XX - II
                return 10000 + int(o.split()[2]) * 10 + len(o.split()[4])
            return 10000 + int(o.split()[2]) * 10
    problems_number_list = sorted(problems, key=cmp)

    problems_list = []
    for problem in problems_number_list:
        problems_list.append(problems[problem])
    # logging.debug(problems_list)

    # get jinja2 template loader
    loader = FileSystemLoader(root_dir / 'utils' /'templates')
    env = Environment(loader=loader)

    ### Generate topics
    topics_map = {}
    for problem in problems_list:
        if problem.topics is None:
            continue

        problem_raw_topics = problem.topics.split('`')
        problem_topics = []
        for t in problem_raw_topics:
            if len(t) > 0 and "," not in t:
                # valid topic
                problem_topics.append(t)
        
        for topic in problem_topics:
            if topics_map.get(topic) is None:
                topics_map[topic] = []
            topics_map[topic].append(problem)

    topics = list(topics_map.keys())
    topics.sort()
    # render each {TOPIC}.md
    topic_template = env.get_template('TOPIC.md.j2')
    for topic in topics:
        topic_generated = topic_template.render(topic=topic, problems_list=topics_map[topic])
        # logging.debug(topic_generated)
        with open(str(root_dir / 'docs' / 'topics' / '{}.md'.format(topic)), 'w') as topic_file:
            topic_file.write(topic_generated)
        logging.debug("{} topic file is generated.".format(topic))

    # using jinja2 render the README file
    readme_template = env.get_template('README.md.j2')
    readme_template.globals['now'] = datetime.utcnow
    readme_generated = readme_template.render(problems_list=problems_list, topics=topics)
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
