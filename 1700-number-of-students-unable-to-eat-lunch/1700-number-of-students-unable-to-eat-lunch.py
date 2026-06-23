class Solution(object):
    def countStudents(self, students, sandwiches):
        count = [0, 0]

        for s in students:
            count[s] += 1

        for i in sandwiches:
            if count[i] == 0:
                break
            count[i] -= 1

        return count[0] + count[1]