grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
aa = grades
ss = students
sss = sorted(ss) # list
print(sss)
aa0 = sum(aa[0]) / len(aa[0])
aa1 = sum(aa[1]) / len(aa[1])
aa2 = sum(aa[2]) / len(aa[2])
aa3 = sum(aa[3]) / len(aa[3])
aa4 = sum(aa[4]) / len(aa[4])
ax = (aa0, aa1, aa2, aa3, aa4)
print(ax)
dd = zip(sss, ax) # Соединение
ddd = dict(dd) # Преобразование
print(ddd)

