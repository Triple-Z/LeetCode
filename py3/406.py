class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        rst = list()
        people.sort(key=lambda x: (-x[0], x[1]))

        for person in people:
            rst.insert(person[1], person)
        
        return rst
