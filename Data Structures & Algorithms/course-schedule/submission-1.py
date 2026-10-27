class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # USE DFS TO FIND CYCLES

        visited = set()

        # Build Hashmap of prereq relationships
        prereqMap = defaultdict(list)
        for prereq in prerequisites:
            prereqMap[prereq[0]].append(prereq[1])

        def dfs(course: int):
            if course in visited:
                return False
            elif prereqMap[course] == []:
                return True

            visited.add(course)
            for prereq in prereqMap[course]:
                if not dfs(prereq): # Call DFS on every prereq of the course
                    return False

            visited.remove(course) # Remove from visited to prevent false positive
            prereqMap[course] = [] # Mark course as already validated
            return True


        for course in range(numCourses):
            if not dfs(course): 
                return False
        return True