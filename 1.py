import math

x1 = math.sqrt(92) # Точне число х1
x2 = (16/7) # Точне число х2
x1_approx = 9.59 # Наближене число x1
x2_approx = 2.28 # Наближене число x2

def find_more_accurate_equality(x1, x1_approx, x2, x2_approx):
 marginal_absolute_error_x1 = abs(x1 - x1_approx)
 marginal_absolute_error_x2 = abs(x2 - x2_approx)

 marginal_relative_error_x1 = marginal_absolute_error_x1 / x1
 marginal_relative_error_x2 = marginal_absolute_error_x2 / x2

 if marginal_relative_error_x1 < marginal_relative_error_x2:
  print("Перша рівність точнішa з відносною похибкою:", marginal_relative_error_x1)
 elif marginal_relative_error_x2 < marginal_relative_error_x1:
  print("Друга рівність точнішa з відносною похибкою:", marginal_relative_error_x2)
 else:
  print("Обидві рівності мають однакову точність з відносними похибками:", marginal_relative_error_x2)

find_more_accurate_equality(x1, x1_approx, x2, x2_approx)