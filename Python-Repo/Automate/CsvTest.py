import csv

file1 = open(r'G:\Anurag\CsvTest1.csv','w')
file2 = open(r'G:\Anurag\CsvTest2.csv','w',newline='')

writer1 = csv.writer(file1,delimiter='\t',lineterminator='\n')
writer2 = csv.writer(file2)

writer1.writerow(['anurag','sethi'])
writer1.writerow(['anuradha','sethi'])
writer1.writerow(['anurakana','sethi'])
writer1.writerow(['anurakana','sethiiiiii'])
writer1.writerow(['anurakana','pethiiiiii'])

writer2.writerow(['anurag','sethi'])
writer2.writerow(['anuradha','sethi'])
writer2.writerow(['anurakana','sethi'])
writer2.writerow(['anurakana','sethiiiiii'])
writer2.writerow(['anurakana','pethiiiiii'])

file1.close()
file2.close()

file = open(r'G:\Anurag\CsvTest1.csv','r')
reader = csv.reader(file)
for row in reader:
    print(str(reader.line_num),str(row))
file.close()


file = open(r'G:\Anurag\CsvTest2.csv','r')
reader = csv.reader(file)
for row in reader:
    print(str(reader.line_num),str(row))
file.close()

