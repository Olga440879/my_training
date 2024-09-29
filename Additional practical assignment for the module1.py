grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_score = [(sum(grades[0])) / len([5, 3, 3, 5, 4]), (sum(grades[1])) / len([2, 2, 2, 3]),
      (sum(grades[2])) / len([4, 5, 5, 2]), (sum(grades[3])) / len([4, 4, 3]),
      (sum(grades[4])) / len([5, 5, 5, 4, 5])]
print(average_score)
students_ = sorted(list({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}))
print(students_)
dictionary = dict(zip(students_, average_score))
print(dictionary)

