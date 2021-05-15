"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp_dict = {}
        query = [id]

        for employee in employees:
            emp_dict[employee.id] = [employee.importance, employee.subordinates]

        res = 0
        while query:
            num = query.pop(0)
            res += emp_dict[num][0]
            query += emp_dict[num][1]
        
        return res
