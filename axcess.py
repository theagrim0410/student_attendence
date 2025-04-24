import pandas as pd
# you should add your excel file in same folder
def show(add_no):
    l1=[]
    file_path = 'datasetgcet.xlsx'
    df = pd.read_excel(file_path, sheet_name='CSE')
    
    if add_no in df['Admission_no.'].values:
        
        student_name = df.loc[df['Admission_no.'] == add_no, 'StudentName'].values
        classe = df.loc[df['Admission_no.'] == add_no, 'classes'].values
        sem = df.loc[df['Admission_no.'] == add_no, 'Sem.'].values
        rol = df.loc[df['Admission_no.'] == add_no, 'roll_no'].values

        
        l1.append(int(rol[0])) #l1[0]
        l1.append(student_name[0]) #l1[1]
        l1.append(classe[0] + " " + sem[0]) #l1[2]
        l1.append(add_no) #l1[3]
        
        return l1
    
        
    else:
        return -1

# if __name__ == "__main__":
#     roll_no = (input("Enter Roll Number: "))
#     show(roll_no)
