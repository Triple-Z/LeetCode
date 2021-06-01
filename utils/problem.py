class Problem:
    
    def __init__(self):
        self.number = None
        self.title_en = None
        self.title_zh = None
        self.difficulty = None
        self.topics = None
        self.link = None
        self.is_solved = False
        self.java = None
        self.go = None
        self.py3 = None
        self.cpp = None
        self.doc = None

    def __str__(self):
        return "{}. {} {}, Difficulty: {}, topics: {}, Java: {}, Python: {}, Cpp: {}, Doc: {}, Link: {}".format(self.number, self.title_en, self.title_zh, self.difficulty, self.topics, self.java, self.py3, self.cpp, self.doc, self.link)
