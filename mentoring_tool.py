import csv
import os
import os.path


def main():
  print("test")

  write_excel()

  matching()

  return 0


def write_excel():
  # Columns: Name, Email, Uni, Studiengang, Semester, Promotion/Studium, #Semester in der Stiftung, Will gleichen Studiengang,

  file_exists = os.path.isfile("mentoring_input.csv")
  print(file_exists)

  # write to csv
  with open('mentoring_input.csv', 'a', newline='') as csvfile:
    mentoring_data_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    if not file_exists:
      mentoring_data_writer.writerow(['Name', 'Email', 'Uni', 'Studiengang', 'Semester', 'Promotion/Studium, Semester_in_der_Stiftung'])
    mentoring_data_writer.writerow(["test0", "test1", "test2", "test3", "test4", "test5"])

  return


def matching():
  # Matching Algorithmus ausdenken

  return


if __name__ == '__main__':
  main()
