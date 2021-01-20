# 1. Read in the attached file
# a. Produce a list sorted by “Current Rent” in ascending order
# b. Obtain the first 5 items from the resultant list and output to the console
# 2. From the list of all mast data, create a new list of mast data with “Lease Years” = 25
# years.

# PYTHON DEVELOPER TEST

# a. Output the list to the console, including all data fields
# b. Output the total rent for all items in this list to the console
# 3. Create a dictionary containing tenant name and a count of masts for each tenant
# a. Output the dictionary to the console in a readable form
# 4. List the data for rentals with “Lease Start Date” between 1st June 1999 and 31st
# August 2007
# a. Output the data to the console with dates formatted as DD/MM/YYYY
from functools import reduce
from operator import add
import csv
from datetime import datetime


def csv_reader(doc_csv):
    new_csv = []
    with open(doc_csv) as f:
        reader = csv.reader(f, delimiter=',')
        new_csv = list(reader).copy()
        return new_csv

def read_csv(file_path):
    key = int(input('Options please enter a number from the following: (1. "Current Rent" in ascending order), (2. Obtain first 5 items of "Current Rent"), (3. Mast data with "Lease Years" = 25 years), (4. Total rent for all items in mast data = 25 years), (5. Tenant name and count of masts for each tenant), (6. Rentals with "Lease Start Date" between start of June 99 and end of August 2007), (0 to exit):\n'))
    cols = []
    if key == 0:
        return
    elif key == 1:
        new_csv = csv_reader(file_path)
        for ind, row in enumerate(new_csv):
            if ind == 0:
                cols = row
            else:
                row[-1] = float(row[-1])
        final_output = sorted(new_csv[1:], key=lambda x:x[-1])
        final_output.insert(0, cols)
        print(final_output)
        return final_output

    elif key == 2:
        new_csv = csv_reader(file_path)
        for ind, row in enumerate(new_csv):
            if ind == 0:
                cols = row
            else:
                row[-1] = float(row[-1])
        final_output = sorted(new_csv[1:], key=lambda x:x[-1])[:5]
        final_output.insert(0, cols)
        print(final_output[0:6])
        return final_output[0:6]
    
    elif key == 3:
        lease_over_25 = []
        new_csv = csv_reader(file_path)
        for ind, row in enumerate(new_csv):
            if ind == 0:
                cols = row
            else:
                if row[9] == '25':
                    lease_over_25.append(row)
        print(lease_over_25)
        return lease_over_25
    
    elif key == 4:
        total_rent_list = []
        new_csv = csv_reader(file_path)
        rent_list = [float(row[10]) for row in new_csv[1:] if row[9] == '25']
        total = reduce(add, rent_list)
        print(total)
        return total
        
       
    
    elif key == 5:
        mast_dict = {}
        tenant_set = set()

        new_csv = csv_reader(file_path)
        for ind, row in enumerate(new_csv):
            if ind == 0:
                pass
            else:
                row[6] = row[6].replace('&', ' & ').replace('.', '').replace('Uk','UK').replace('EverythingEverywhere', 'Everything Everywhere').replace('Hutchinson3G', 'Hutchinson 3G').replace('Hutchinson 3G UK', 'Hutchinson 3G UK Ltd').replace('3G Ltd', '3G UK Ltd').replace('3GUK', '3G UK').replace('  ',' ').replace('LTd', 'Ltd')

                if row[6] in tenant_set:
                    mast_dict[row[6]] += 1
                elif row[6] not in tenant_set:
                    tenant_set.add(row[6])
                    mast_dict[row[6]] = 1
                    
                    
        print(mast_dict)
        return mast_dict
    
    
    elif key == 6:
        date_list = []
        cols = []
        june = datetime.strptime('1 June 1999', '%d %B %Y')
        august = datetime.strptime('31 August 2007', '%d %B %Y')
        new_csv = csv_reader(file_path)
        for ind, row in enumerate(new_csv):
            if ind == 0:
                cols = row
            else:
                a = datetime.strptime('1 June 1999', '%d %B %Y')
                b = datetime.strptime('31 August 2007', '%d %B %Y') 
                q = datetime.strptime(row[7], '%d %b %Y')
                if  a < q < b:
                    row[7] = datetime.strptime(row[7], '%d %b %Y').strftime('%d/%m/%Y')
                    row[8] = datetime.strptime(row[8], '%d %b %Y').strftime('%d/%m/%Y')
                    date_list.append(row)
                    date_list.insert(0, cols)
        print(date_list)
        return date_list
                
                
    

    
    
 
        
if __name__ == '__main__':
    read_csv('Python Developer Test Dataset.csv')
    