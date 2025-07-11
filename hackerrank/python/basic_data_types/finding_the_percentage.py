if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    
    def mean(list):
        x = 0
        for i in list:
            x += i
        percentage = (x/len(list))
        return "%.2f" % percentage
    query_name_percentage = mean(student_marks[query_name])
    print(query_name_percentage)
