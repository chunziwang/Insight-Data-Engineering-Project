import csv
import re
import sys

input = sys.argv[1]
output_job = sys.argv[2]
output_state = sys.argv[3]
    
# create dictionaries to hold the count of each job and state in the dataset
job = dict()
state = dict()
    
# count the number of certified rows
count = 0
    
# read the data
with open(input,'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
        
    # put data columns into a seperate list
    fields = csv_reader.next()
        
    # find the index of targeted columns using regular expression
    r = re.compile(".*STATUS")
    cert_index = fields.index(filter(r.match,fields)[0])
    r = re.compile(".*SOC_NAME")
    job_index = fields.index(filter(r.match,fields)[0])
    r = re.compile(".*WORK.*STATE")
    state_index = fields.index(filter(r.match,fields)[0])
        
    # loop through rows to populate the dictionary
    for row in csv_reader:
        if row[cert_index] == 'CERTIFIED':
            job[row[job_index]] = job.get(row[job_index],0)+1
            state[row[state_index]] = state.get(row[state_index],0)+1
            count+=1


# find the top 10 jobs/states in the dictionary by value
if len(state) >= 10:    
    sorted_count = sorted(state.values())[-10:][::-1]
else:
    sorted_count = sorted(state.values())[::-1]
    
if len(job) >= 10:
    sorted_count2 = sorted(job.values())[-10:][::-1]
else:
    sorted_count2 = sorted(job.values())[::-1]

    
# put the selected jobs into a dataframe
fields = ['TOP_OCCUPATIONS','NUMBER_CERTIFIED_APPLICATIONS','PERCENTAGE'] 
# calculate the percentage using value/total rows count
rows = list([key,value,"{0:0.1f}%".format(value*100.0/count)] for key, value in job.iteritems() if value in sorted_count2)
# sort the rows in ascending order of name and descending order of value
rows.sort(key=lambda x:x[0])
rows.sort(key=lambda x:x[1],reverse=True)
filename = "top_10_occupations.txt"
    
# write to txt file
with open(output_job, 'w') as csv_file: 
    csv_writer = csv.writer(csv_file, delimiter=';') 
    csv_writer.writerow(fields) 
    csv_writer.writerows(rows)
    
# put the selected states into a dataframe
fields = ['TOP_STATES','NUMBER_CERTIFIED_APPLICATIONS','PERCENTAGE'] 
# calculate the percentage using value/total rows count
rows = list([key,value,"{0:0.1f}%".format(value*100.0/count)] for key, value in state.iteritems() if value in sorted_count)
# sort the rows in ascending order of name and descending order of value
rows.sort(key=lambda x:x[0])
rows.sort(key=lambda x:x[1],reverse=True)
filename = "top_10_states.txt"
    
# write to txt file
with open(output_state, 'w') as csv_file: 
    csv_writer = csv.writer(csv_file, delimiter=';') 
    csv_writer.writerow(fields) 
    csv_writer.writerows(rows)
    