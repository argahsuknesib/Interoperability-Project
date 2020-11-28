import csv        

data = ['text1', 'text2', 'text3', 'text4']    

with open('output.tsv', 'w', newline='') as f_output:
    tsv_output = csv.writer(f_output, delimiter='\t') #using the delimiter as '\t' gives a .tsv file.
    tsv_output.writerow(data)

'''
The output data is saved into a file named output.tsv which can be seen in the same project folder.
'''