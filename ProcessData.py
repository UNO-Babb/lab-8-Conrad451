#ProcessData.py
#Name: Connor Pell
#Date: 11/2 
#Assignment: Lab 8

import csv

years = {
    'Freshman': 'FR',
    'Sophomore': 'SO',
    'Junior': 'JR',
    'Senior': 'SR'
}

def make_userid(first_name, last_name, student_id):
  first_letter = first_name[0].lower()
  last = last_name.lower()

  if len(last) < 5:
    last += 'x'

  digits = student_id[-3:]

  return f"{first_letter}{last}{digits}"


def return_year(major, year):
  letters = major[:3]

  for adj_year in years:
    if adj_year == year:
      big_year = years[adj_year]


  return f"{letters}-{big_year}"


def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')
  #headers
  outFile.write("Last name,First name,UserID,Major-Year,\n")

  #Process each line of the input file and output to the CSV file
  for line in inFile:
    linelist = line.split()
    print(linelist)
    first_name = linelist[0]
    last_name = linelist[1]
    student_id = linelist[3]
    year = linelist[5]
    major = linelist[6]

    print(year)
    user_id = make_userid(first_name, last_name, student_id)
    adjusted_major = return_year(major, year)

    outFile.write(f"{last_name},{first_name},{user_id},{adjusted_major}\n")


  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

if __name__ == '__main__':
  main()
