import csv
import os
import os.path
from pandas import DataFrame
import random



def main():
  print("test")
  mentor_data= read_excel("mentor_input.csv")
  mentee_data= read_excel("mentee_input.csv")
  print (DataFrame(mentee_data))
  print (DataFrame(mentor_data))
  output= matching(mentee_data, mentor_data)
  write_excel(output)
  print(DataFrame(output))
  #write_excel()

  #matching()

  return 0

def read_excel(excel_name):
      with open(excel_name, newline= '') as csvfile:
        inputreader = csv.reader(csvfile, delimiter =';', quotechar= '|')
        ncol= len(next(inputreader))
        csvfile.seek(0)
        print(ncol)
        list_of_rows = list(inputreader)
        return list_of_rows

def write_excel(matching_output):
  # Columns: Name, Email, Uni, Studiengang, Semester, Promotion/Studium, #Semester in der Stiftung, Will gleichen Studiengang,

  # file_exists = os.path.isfile("mentee_input.csv") 
  # print(file_exists)


  # write to csv
  # with open('mentee_input.csv', 'a', newline='') as csvfile:
  #   mentoring_data_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  #   if not file_exists:
  #     mentoring_data_writer.writerow(['Name', 'Email', 'Uni', 'Studiengang', 'Semester', 'Promotion/Studium, Semester_in_der_Stiftung'])
  #   mentoring_data_writer.writerow(["test0", "test1", "test2", "test3", "test4", "test5"])

  # file_exists = os.path.isfile("mentor_input.csv") 
  # print(file_exists)

  # write to csv
  # with open('mentor_input.csv', 'a', newline='') as csvfile:
  #   mentoring_data_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  #   if not file_exists:
  #     mentoring_data_writer.writerow(['Name', 'Email', 'Uni', 'Studiengang', 'Semester', 'Promotion/Studium, Semester_in_der_Stiftung'])
  #   mentoring_data_writer.writerow(["test0", "test1", "test2", "test3", "test4", "test5"])

  with open('matching_output.csv', 'w', newline='') as csvfile:
    mentoring_data_writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in matching_output:
      mentoring_data_writer.writerow(row)

  return


def matching(mentee_data, mentor_data):
  # Matching Algorithmus ausdenken

  matching_output= []
  test= mentor_data[0] + mentee_data[0]
  matching_output.append(test)
  
  i= 0
  for headline in mentee_data[0]:
        if headline == "Mentee_Promotion/Studium":
          mentee_promotion = i
        if headline == "Mentee gleiches geschlecht?":
              geschlechterfrage = i
        if headline == "Mentee_Geschlecht":
              mentee_geschlecht = i
        i= i+1

  a= 0
  for headline in mentor_data[0]:
        if headline == "Mentor_Promotion/Studium":
          mentor_promotion = a
        if headline == "Mentor_Geschlecht":
              mentor_geschlecht = a
        a = a+1

  mentee_data.pop(0)
  mentor_data.pop(0)


  random.shuffle(mentee_data)
  random.shuffle(mentor_data)

      
  for mentee in mentee_data:
        for mentor in mentor_data:
              if mentee[mentee_promotion] == mentor[mentor_promotion]:
                    match = mentor + mentee   
                    matching_output.append(match)  
                    # mentee_data.remove(mentee)
                    # mentor_data.remove(mentor)
       # if mentee[geschlechterfrage] = "ja":
              #geschlecht_match =


  return matching_output


if __name__ == '__main__':
  main()
