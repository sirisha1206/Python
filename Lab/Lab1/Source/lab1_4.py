pythonStudents = input('Enter the list of students attending python separated by space: ')
webStudents = input('Enter the list of students attending web technologies separated by space: ')
pythonStudents = pythonStudents.split()#split the space seperated values into pythonStudents list
webStudents = webStudents.split()# split the space seperated values into  webStudents list
print('****List of students who are common in both python and web****')
print(list(set(pythonStudents) & set(webStudents))) #finding the intersection of pythonStudents and webStudents
                                                #  by converting them to sets
                                                #  using '&'
print('****List of students who are not common in both the classes****')
print(list(set(pythonStudents).symmetric_difference(set(webStudents))))#finding the symmetric difference of
                                                            # pythonStudents and webStudents by converting them to sets
                                                            # using symmetric_difference function
