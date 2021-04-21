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
    if headline == "Möchtest du, dass dein zukünftiger Mentor oder Mentorin dasselbe studiert wie du?":
      studienfachfrage = i
    if headline == "Welches Fach studierst du? (Es tut uns leid, wenn wir nicht alle Fächer aufgelistet haben. Falls euer Fach nicht dabei ist, ordnet euch bitte dem inhaltlich engsten Fach zu, Bspw. wenn ihr Cello studiert, ordnet euch bitte zu *Instrumenten (divers)* zu).":
      mentee_studienfach = i
    if headline == "An welcher Universität bzw. Hochschule studierst du?":
      mentee_uni = i
    i= i+1

  a= 0
  for headline in mentor_data[0]:
        if headline == "Bist du Promotionsstipendiat*in oder regulärer Stipendiat*in? in der Studienstiftung (WICHTIG, z.B. Mediziner*innen die neben dem Studium promovieren aber trotzdem durch die reguläre Förderung gefördert werden, geben bitte Reguläre Förderung an!)":
          mentor_promotion = a
        if headline == "Mit welchem Geschlecht identifizierst du dich? ":
          mentor_geschlecht = a
        if headline == "Hast du ein Kind/mehrere Kinder?":
          mentor_kind = a
        if headline == "Welches Fach studierst du? (Es tut uns leid, wenn wir nicht alle Fächer aufgelistet haben. Falls euer Fach nicht dabei ist, ordnet euch bitte dem inhaltlich engsten Fach zu, Bspw. wenn ihr Cello studiert, ordnet euch bitte zu *Instrumenten (divers)* zu).":
          mentor_studienfach = a
        if headline == "An welcher Universität bzw. Hochschule studierst du?":
          mentor_uni = a


        a = a+1

  mentee_data.pop(0)
  mentor_data.pop(0)


  #random.shuffle(mentee_data)
  #random.shuffle(mentor_data)

  deleted = []
  for i in range(len(mentee_data[0])):
        deleted.append("deleted")


  # print("len mentee_data:", len(mentee_data))
  # print("len  mentor_data:", len(mentor_data))
  # print("len  deldtd:", len(deleted))
  i=0
  while i < len(mentee_data):
    j=0
    while j < len(mentor_data):
      print("vergleiche mentee:", i, "mentor:", j)
      print("mentee", i, "studienfach:", mentee_data[i][mentee_studienfach],"uni:", mentee_data[i][mentee_uni] ,"geschlecht", mentee_data[i][mentee_geschlecht], "kind:" ,mentee_data[i][mentee_kind], "promotion", mentee_data[i][mentee_promotion]) 
      print("mentor", j, "studienfach:", mentor_data[j][mentor_studienfach],"uni:", mentor_data[j][mentor_uni] ,"geschlecht", mentor_data[j][mentor_geschlecht], "kind:" ,mentor_data[j][mentor_kind], "promotion", mentor_data[j][mentor_promotion]) 
      print("")

      #hier wird gematcht, wenn jemand sowohl jmd mit dem gleich Fach, mit dem gleichen Geschlecht als auch jmd mit Kindern

      if mentee_data[i][kindfrage] == "Ja, das wäre gut." and mentee_data[i][geschlechterfrage] == "Ja" and mentee_data[i][studienfachfrage] == "Ja, wenn das ginge wäre das super.": 
          if mentee_data[i][mentee_promotion]== mentor_data[j][mentor_promotion] and mentee_data[i][mentee_kind] == mentor_data[j][mentor_kind] and mentee_data[i][mentee_geschlecht] == mentor_data[j][mentor_geschlecht] and mentee_data[i][mentee_uni] == mentor_data[j][mentor_uni] and mentee_data[i][mentee_studienfach] == mentor_data[j][mentor_studienfach]:
            match= mentor_data[j] + mentee_data[i]
            matching_output.append(match)
            mentor_data[j]= deleted
            mentee_data[i]= deleted
            print("kind+geschlecht+fach hat nen match gefunden mentee:", i,"mentor:", j)
            break
      j= j+1
    i= i+1

  i= 0
  while i < len(mentee_data):
    j=0
    while j < len(mentor_data):
      #hier werden leute gemacht, die sowohl Kinder Mentor haben wollen als auch jmd mit dem gleich Geschlecht
      if mentee_data[i][kindfrage] == "Ja, das wäre gut." and mentee_data[i][geschlechterfrage] == "Ja"  and mentee_data[i][0] != "deleted" and mentor_data[j][0] != "deleted":
          if mentee_data[i][mentee_promotion]== mentor_data[j][mentor_promotion] and mentee_data[i][mentee_kind] == mentor_data[j][mentor_kind] and mentee_data[i][mentee_geschlecht] == mentor_data[j][mentor_geschlecht]:
            match= mentor_data[j] + mentee_data[i]
            matching_output.append(match)
            mentor_data[j]= deleted
            mentee_data[i]= deleted
            print("kind+geschlecht hat nen match gefunden mentee:", i,"mentor:", j)
            break
      j= j+1
    i = i+1   
      
  i=0
  while i < len(mentee_data):
    j=0
    while j < len(mentor_data):
    #hier werden leute gemacht, die sowohl jmd mit dem selben Fach wollen als auch jmd mit dem gleich Geschlecht
      if mentee_data[i][studienfachfrage] == "Ja, wenn das ginge wäre das super." and mentee_data[i][geschlechterfrage] == "Ja" and  mentee_data[i][0] != "deleted" and mentor_data[j][0] != "deleted":
          if mentee_data[i][mentee_promotion]== mentor_data[j][mentor_promotion] and mentee_data[i][mentee_geschlecht] == mentor_data[j][mentor_geschlecht] and mentee_data[i][mentee_uni] == mentor_data[j][mentor_uni] and mentee_data[i][mentee_studienfach] == mentor_data[j][mentor_studienfach]:
            match= mentor_data[j] + mentee_data[i]
            matching_output.append(match)
            mentor_data[j]= deleted
            mentee_data[i]= deleted
            print("fach+geschlecht hat nen match gefunden mentee:", i,"mentor:", j)
            break
      j= j+1
    i = i+1 
    
  i=0
  while i < len(mentee_data):
    j=0
    while j < len(mentor_data):
    #hier werden leute gemacht, die sowohl jemanden mit Kindern haben wollen als auch jmd mit dem gleichen Fach
      if mentee_data[i][kindfrage] == "Ja, das wäre gut." and mentee_data[i][studienfachfrage] == "Ja, wenn das ginge wäre das super."  and  mentee_data[i][0] != "deleted" and mentor_data[j][0] != "deleted": 
          if mentee_data[i][mentee_promotion]== mentor_data[j][mentor_promotion] and mentee_data[i][mentee_kind] == mentor_data[j][mentor_kind] and mentee_data[i][mentee_uni] == mentor_data[j][mentor_uni] and mentee_data[i][mentee_studienfach] == mentor_data[j][mentor_studienfach]:
            match= mentor_data[j] + mentee_data[i]
            matching_output.append(match)
            mentor_data[j]= deleted
            mentee_data[i]= deleted
            print("kind+ fach hat nen match gefunden mentee:", i,"mentor:", j)
            break
      j= j+1
    i = i+1 

  i=0
  while i < len(mentee_data):
    j=0
    while j < len(mentor_data):
      #hier werden geschlechter gemacht, sofern dies gewünscht (bzw mit "Ja") beantwortet wurde
      if mentee_data[i][geschlechterfrage] == "Ja" and mentee_data[i][0] != "deleted" and mentor_data[j][0] != "deleted":
          if mentee_data[i][mentee_promotion]== mentor_data[j][mentor_promotion] and mentee_data[i][mentee_geschlecht] == mentor_data[j][mentor_geschlecht]:
            match= mentor_data[j] + mentee_data[i]
            matching_output.append(match)
            mentor_data[j]= deleted
            mentee_data[i]= deleted
            print("geschlecht hat nen match gefunden mentee:", i,"mentor:", j)
            break
      j= j+1
    i = i+1


  i=0
  while i < len(mentee_data):
    j=0
    while j < len(mentor_data):        
      #hier wird gemacht, wenn jemand einen Mentor mit Kindern haben möchte
      if mentee_data[i][kindfrage] == "Ja, das wäre gut." and mentee_data[i][0] != "deleted" and mentor_data[j][0] != "deleted":
          if mentee_data[i][mentee_promotion]== mentor_data[j][mentor_promotion] and mentee_data[i][mentee_kind] == mentor_data[j][mentor_kind]:
            match= mentor_data[j] + mentee_data[i]
            matching_output.append(match)
            mentor_data[j]= deleted
            mentee_data[i]= deleted
            print("kind hat nen match gefunden mentee:", i,"mentor:", j)
            break
      j= j+1
    i = i+1 

  i=0
  while i < len(mentee_data):
    j=0
    while j < len(mentor_data):
      #hier wird das Studienfach (abhängig von der Uni) gematcht
      if mentee_data[i][studienfachfrage] == "Ja, wenn das ginge wäre das super." and mentee_data[i][0] != "deleted" and mentor_data[j][0] != "deleted": #in der nächste zeile uni und studienfach matchen
            if mentee_data[i][mentee_uni] == mentor_data[j][mentor_uni] and mentee_data[i][mentee_studienfach] == mentor_data[j][mentor_studienfach] and mentee_data[i][mentee_promotion]== mentor_data[j][mentor_promotion]:  
                match = mentor_data[j] + mentee_data[i]
                matching_output.append(match)
                mentor_data[j]= deleted
                mentee_data[i]= deleted
                print("fach inkl.Uni hat nen match gefunden mentee:", i,"mentor:", j)
                break
      j= j+1
    i = i+1 


  i=0
  while i < len(mentee_data):
    j=0
    while j < len(mentor_data):
      #hier wird nur das Studienfach (unabhängig von der Uni) gematcht
      if mentee_data[i][studienfachfrage] == "Ja, wenn das ginge wäre das super."  and mentee_data[i][0] != "deleted" and mentor_data[j][0] != "deleted":
            if mentee_data[i][mentee_studienfach] == mentor_data[j][mentor_studienfach] and mentee_data[i][mentee_promotion]== mentor_data[j][mentor_promotion] :  
                match = mentor_data[j] + mentee_data[i]
                matching_output.append(match)
                mentor_data[j]= deleted
                mentee_data[i]= deleted
                print("fach ohne uni hat nen match gefunden mentee:", i,"mentor:", j)
                break
      j= j+1
    i = i+1 


  i=0
  while i < len(mentee_data):
    j=0
    while j < len(mentor_data):
      #hier werden promotionsstiftis bzw reguläre stiftis gematcht
      print("--> ich checke promotion", mentee_data[i][mentee_promotion], "vs.", mentor_data[j][mentor_promotion])
      if mentee_data[i][mentee_promotion]== mentor_data[j][mentor_promotion] and  mentee_data[i][0] != "deleted" and mentor_data[j][0] != "deleted":
            print("promotion erfolgreich")
            match= mentor_data[j] + mentee_data[i]
            matching_output.append(match)
            mentor_data[j]= deleted
            mentee_data[i]= deleted
            print("promotionsstiftis hat nen match gefunden mentee:", i,"mentor:", j)
            break

    
                      
      j=j+1
    i=i+1


  
  i=0
  while i < len(mentee_data):
    j=0
    while j < len(mentor_data):
      print("random vergleiche mentee:", i, "mentor:", j)
      print("mentee", i, "studienfach:", mentee_data[i][mentee_studienfach],"uni:", mentee_data[i][mentee_uni] ,"geschlecht", mentee_data[i][mentee_geschlecht], "kind:" ,mentee_data[i][mentee_kind], "promotion", mentee_data[i][mentee_promotion]) 
      print("mentor", j, "studienfach:", mentor_data[j][mentor_studienfach],"uni:", mentor_data[j][mentor_uni] ,"geschlecht", mentor_data[j][mentor_geschlecht], "kind:" ,mentor_data[j][mentor_kind], "promotion", mentor_data[j][mentor_promotion]) 
      print("")
      if mentee_data[i][0] != "deleted" and mentor_data[j][0] != "deleted":
            match= mentor_data[j] + mentee_data[i]
            matching_output.append(match)
            mentor_data[j]= deleted
            mentee_data[i]= deleted
            print("random hat nen match gefunden mentee:", i,"mentor:", j)
            break
      j=j+1
    i=i+1



  return matching_output


if __name__ == '__main__':
  main()
