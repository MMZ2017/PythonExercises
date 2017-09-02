if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
  
    query_name = raw_input()
    for k, v in student_marks.items():
        if k == query_name:
            average = float(sum(v))/float(len(v))
            average = format(average, '.2f')
            
    print average
            
