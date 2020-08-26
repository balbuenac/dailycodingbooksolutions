def topologicalSortUtil(course, visited, stack, courses):
    visited[course] = True
    for neighbor in courses[course]:
        if visited[neighbor] == False:
            topologicalSortUtil(neighbor, visited, stack, courses)
    stack.insert(0, course)

def topologicalSort(courses):
    courses_list = list(courses.keys())
    visited = { c:False for c in courses_list}
    stack = []
    for course in courses_list:
        if visited[course] == False:
            topologicalSortUtil(course, visited, stack, courses)
    print(stack)

courses = { 'CSC300' : ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100' : []}
courses_failed = { 'CSC300' : ['CSC100', 'CSC400'], 'CSC400': ['CSC200'], 'CSC200': ['CSC300'], 'CSC100' : []}
topologicalSort(courses_failed)