import csv
import os
import os.path
from pandas import DataFrame
import random



def main():
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
    if headline == "Bist du Promotionsstipendiat*in oder regulärer Stipendiat*in? in der Studienstiftung (WICHTIG, z.B. Mediziner*innen die neben dem Studium promovieren aber trotzdem durch die reguläre Förderung gefördert werden, geben bitte Reguläre Förderung an!)":
      mentee_promotion = i
    if headline == "Möchtest du dass dein zukünftige Mentorin oder Mentor das gleiche Geschlecht wie du hat?":
      geschlechterfrage = i
    if headline == "Mit welchem Geschlecht identifizierst du dich? (Muss leider auch angegeben werden falls euch da Geschlecht eures Mentors/Mentorin egal ist)":
      mentee_geschlecht = i
    if headline == "Möchtest du, dass dein zukünftiger Mentor*in ebenfalls Kinder hat?":
      kindfrage = i
    if headline == "Hast du ein Kind/mehrere Kinder?":
      mentee_kind	= i
    
    i= i+1

  a= 0
  for headline in mentor_data[0]:
        if headline == "Bist du Promotionsstipendiat*in oder regulärer Stipendiat*in? in der Studienstiftung (WICHTIG, z.B. Mediziner*innen die neben dem Studium promovieren aber trotzdem durch die reguläre Förderung gefördert werden, geben bitte Reguläre Förderung an!)":
          mentor_promotion = a
        if headline == "Mit welchem Geschlecht identifizierst du dich? ":
              mentor_geschlecht = a
        if headline == "Hast du ein Kind/mehrere Kinder?":
              mentor_kind = a
        a = a+1

  mentee_data.pop(0)
  mentor_data.pop(0)


  random.shuffle(mentee_data)
  random.shuffle(mentor_data)

  deleted = []
  for i in range(len(mentor_data[0])):
        deleted.append("deleted")


  # print("len mentee_data:", len(mentee_data))
  # print("len  mentor_data:", len(mentor_data))
  # print("len  deldtd:", len(deleted))
  i=0
  while i < len(mentee_data):
        j=0
        while j < len(mentor_data):
              # print("vergleiche mentee:", i, "mentor:", j)

              if mentee_data[i][kindfrage] == "Ja, das wäre gut." and mentee_data[i][geschlechterfrage] == "Ja":
                  if mentee_data[i][mentee_promotion]== mentor_data[j][mentor_promotion] and mentee_data[i][mentee_kind] == mentor_data[j][mentor_kind] and mentee_data[i][mentee_geschlecht] == mentor_data[j][mentor_geschlecht]:
                    match= mentor_data[j] + mentee_data[i]
                    matching_output.append(match)
                    mentor_data[j]= deleted
                    mentee_data[i]= deleted
                    print("kind+geschlecht hat nen match gefunden mentee:", i,"mentor:", j)
                    break

              elif mentee_data[i][geschlechterfrage] == "Ja":
                  if mentee_data[i][mentee_promotion]== mentor_data[j][mentor_promotion] and mentee_data[i][mentee_geschlecht] == mentor_data[j][mentor_geschlecht]:
                    match= mentor_data[j] + mentee_data[i]
                    matching_output.append(match)
                    mentor_data[j]= deleted
                    mentee_data[i]= deleted
                    print("geschlecht hat nen match gefunden mentee:", i,"mentor:", j)
                    break
                  
              elif mentee_data[i][kindfrage] == "Ja, das wäre gut.":
                  if mentee_data[i][mentee_promotion]== mentor_data[j][mentor_promotion] and mentee_data[i][mentee_kind] == mentor_data[j][mentor_kind]:
                    match= mentor_data[j] + mentee_data[i]
                    matching_output.append(match)
                    mentor_data[j]= deleted
                    mentee_data[i]= deleted
                    print("kind hat nen match gefunden mentee:", i,"mentor:", j)
                    break

              elif mentee_data[i][mentee_promotion]== mentor_data[j][mentor_promotion]:
                    match= mentor_data[j] + mentee_data[i]
                    matching_output.append(match)
                    mentor_data[j]= deleted
                    mentee_data[i]= deleted
                    break
              j=j+1
        i=i+1
  
  for mentee in mentee_data:
        for mentor in mentor_data:
              if mentee[0] != "deleted" and mentor[0] != "deleted":
                    match= mentor+mentee
                    matching_output.append(match)
                    mentor= deleted
                    mentee= deleted




  return matching_output


if __name__ == '__main__':
  main()
