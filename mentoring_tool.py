import csv
import os
import os.path


def main():
  print("test")

  matching()

  return 0


def matching():
  # Columns:

  file_exists = os.path.isfile("mentoring_input.csv")
  print(file_exists)

  # write to csv
  # with open('mentoring_input.csv', 'a', newline='') as csvfile:
  #   gem_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  #   if not file_exists:
  #     gem_writer.writerow(['Username', 'path', 'Datetime added', 'Relevant Filepath', 'timestamp', 'Situation', 'Comment'])
  #   # gem_writer.writerow([username, path, current_datetime, filepath.split('/')[-2:], timestamp, situation, comment])
  #   printed_path = filepath.split('/')[0:-2]
  #   seperator = '/'
  #   gem_writer.writerow([username, seperator.join(printed_path), current_datetime,
  #                        filepath.split('/')[-2:], timestamp, situation, comment])

  return


if __name__ == '__main__':
  main()
