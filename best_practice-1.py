import os
import time
import pickle
import operator

studentsOfSaps = {}

#os.path.exists()
class Student:
	# constructor 
	def __init__(self): 
		self.rollNumber=0
		self.className=""
		self.name=""
		self.father=""
		self.mother=""
		self.englishMark=0
		self.hindiMark=0
		self.mathsMark=0
		self.computerMark=0
		self.totalMarks=0
	
	def setRollNumber(self,studentRollNumber):
		self.rollNumber=studentRollNumber
	
	def setName(self,studentName):
		self.name=studentName

	def setClassName(self,className):
		self.className=className
		
	def setFather(self,fatherName):
		self.father=fatherName
	
	def setMother(self,motherName):
		self.mother=motherName

	def setEnglish(self,englishMark):
		self.englishMark=englishMark
		self.totalMarks += englishMark
		
	def setHindi(self,hindiMark):
		self.hindiMark=hindiMark
		self.totalMarks += hindiMark

	def setMaths(self,mathsMark):
		self.mathsMark=mathsMark
		self.totalMarks += mathsMark
		
	def setComputer(self,computerMark):
		self.computerMark=computerMark
		self.totalMarks += computerMark

	def setTotalMarks(self, totalMarks):
		self.totalMarks=totalMarks
		
	def getRollNumber(self):
		return self.rollNumber
	
	def getName(self):
		return self.name

	def getClassName(self):
		return self.className
		
	def getFather(self):
		return self.father
	
	def getMother(self):
		return self.mother

	def getEnglish(self):
		return self.englishMark
		
	def getHindi(self):
		return self.hindiMark

	def getMaths(self):
		return self.mathsMark
		
	def getComputer(self):
		return self.computerMark
		
	def getTotalMarks(self):
		return self.totalMarks

def clearScreen():
    os.system('cls' if os.name=='nt' else 'clear')

def saveDetailsToFile():
	with open("saps.dat", "wb") as destinationFile:
		pickle.dump(studentsOfSaps, destinationFile)

def loadDetailsFromFile():
	global studentsOfSaps
	
	with open("saps.dat", "rb") as destinationFile:
		studentsOfSaps = pickle.load(destinationFile)

def selectStudentClass():
	className = ""
	
	while True:
	
		clearScreen()
		print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#\n")
		print("Select the class\n\n")
		print("1. X11-A\n")
		print("2. X11-B\n")
		print("3. X11-C\n")
		print("4. Exit\n")
		
		selectedClassOption = input('Give your option: ').title()
		
		if selectedClassOption == "1":
			className = "X11-A"
			break
		elif selectedClassOption == "2":
			className = "X11-B"
			break
		elif selectedClassOption == "3":
			className = "X11-C"
			break
		elif selectedClassOption == "4":
			className = ""
			break
		else:
			print("\n\n ==>>> Invalid option. Kindly select proper value  <<==")
			print("\n\n ")			
			input('Press any key to continue... ')
	
	return className

def readAndValidateUserInput(inputMessage):
	markValue=0
	readSubjectMark = input(inputMessage)
			
	if not readSubjectMark.isnumeric():
		print("Invalid mark given. Setting to default 0. Modify later by updating the student record.")
	else:
		markValue = int(readSubjectMark)
	
	return markValue
	
def createStudent():
	global studentsOfSaps
	
	clearScreen()
	
	className = selectStudentClass()
		
	#student details cannot be created without selecting class name
	if className == "":
		return
	
	clearScreen()
	print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#\n")
	print("Give the details for adding student to "+className+"\n\n")
			
	studentObject = Student()
	
	studentObject.setRollNumber(input('RollNumber: '))
	studentObject.setName(input('Name: ').title())
	studentObject.setClassName(className)
	studentObject.setFather(input('Father\'s Name: ').title())
	studentObject.setMother(input('Mother\'s Name: ').title())
	studentObject.setEnglish(readAndValidateUserInput('Mark for English: '))
	studentObject.setHindi(readAndValidateUserInput('Mark for Hindi: '))
	studentObject.setMaths(readAndValidateUserInput('Mark for Maths: '))
	studentObject.setComputer(readAndValidateUserInput('Mark for Computer: '))
	
	#add to global variable
	if studentObject.getClassName() not in studentsOfSaps:
		studentsOfSaps[studentObject.getClassName()] = {}
	
	if studentObject.getRollNumber() not in studentsOfSaps[studentObject.getClassName()]:
		studentsOfSaps[studentObject.getClassName()][studentObject.getRollNumber()] = studentObject
		
		#save to file
		saveDetailsToFile()

		print("\n\n #### student record created successfully ####")
	
	else:
		print("\n\n ==>>> Failed to add student record with roll number "+studentObject.getRollNumber()+". Duplicate record exists  <<==")
	
	print("\n\n ")			
	input('Press any key to continue... ')
		
def viewStudent():
	
	className = selectStudentClass()
		
	#student details cannot be created without selecting class name
	if className == "":
		return
		
	print("\n\n")
	rollNumberToSearch = input('Enter the student rollnumber: ').title()
	
	if className in studentsOfSaps:
		if rollNumberToSearch in studentsOfSaps[className]:
			
			studentObject = studentsOfSaps[className][rollNumberToSearch]
			
			print("\n\n")
			print("\n RollNumber: "+studentObject.getRollNumber())
			print("\n Name: "+studentObject.getName())
			print("\n Class: "+studentObject.getClassName())
			print("\n Father's Name: "+studentObject.getFather())
			print("\n Mother's Name: "+studentObject.getMother())
			print("\n Mark for English: "+str(studentObject.getEnglish()))
			print("\n Mark for Hindi: "+str(studentObject.getHindi()))
			print("\n Mark for Maths: "+str(studentObject.getMaths()))
			print("\n Mark for Computer: "+str(studentObject.getComputer()))
			print("\n Total Marks: "+str(studentObject.getTotalMarks()))
		
		else:
			print("\n\n ==>>> Unable to find any student record with roll number - "+rollNumberToSearch+" <<==")			
	else:
		print("\n\n ==>>> No student records are enrolled in class - "+className+" <<==")
	
	print("\n\n ")			
	input('Press any key to continue...')
	
def updateStudent():
	global studentsOfSaps
	
	className = selectStudentClass()
		
	#student details cannot be created without selecting class name
	if className == "":
		return
		
	print("\n\n")
	rollNumberToSearch = input('Enter the student rollnumber: ').title()
	
	if className in studentsOfSaps:
		if rollNumberToSearch in studentsOfSaps[className]:
			
			print("\n\n")
			
			studentObject = studentsOfSaps[className][rollNumberToSearch]
			studentObject.setTotalMarks(0)
			studentObject.setName(input('Name: ').title())
			studentObject.setFather(input('Father\'s Name: ').title())
			studentObject.setMother(input('Mother\'s Name: ').title())
			studentObject.setEnglish(readAndValidateUserInput('Mark for English: '))				
			studentObject.setHindi(readAndValidateUserInput('Mark for Hindi: '))
			studentObject.setMaths(readAndValidateUserInput('Mark for Maths: '))
			studentObject.setComputer(readAndValidateUserInput('Mark for Computer: '))
		
			studentsOfSaps[studentObject.getClassName()][studentObject.getRollNumber()] = studentObject
			
			#save to file
			saveDetailsToFile()
			
			print("\n\n **** student record updated successfully ****")
			
		else:
			print("\n\n ==>>> Unable to find any student record with roll number - "+rollNumberToSearch+" <<==")
			
	else:
		print("\n\n ==>>> No student records are enrolled in class - "+className+" <<==")
	
	print("\n\n ")			
	input('Press any key to continue...')

def prettySpacing(inputValue,maxCharacters):
	inputValue = str(inputValue)
	missingChars = maxCharacters - len(inputValue)
	
	while missingChars > 0:
		inputValue += " "
		missingChars -=1
	
	return inputValue
	
def displayRanklist():
	
	clearScreen()
	
	className = selectStudentClass()
		
	#student details cannot be created without selecting class name
	if className == "":
		return
	
	clearScreen()
	
	if className in studentsOfSaps:
		classDetails = studentsOfSaps[className]
		rankCounter=1
		
		#header
		print("_________________________________________________________________________________________")
		print("| Rank | Name                 | RollNumber | English | Hindi | Maths | Computer | Total |")
		print("-----------------------------------------------------------------------------------------")
		
		for student in (sorted(classDetails.values(), key=operator.attrgetter('totalMarks'),reverse=True)):
			#second argument in prettySpacing() is the header character count (including space) between '|' 
			
			print("| "+ prettySpacing(rankCounter,4) +" | " + prettySpacing(student.name,20) + " | " + prettySpacing(student.rollNumber,10) + " | " + prettySpacing(student.englishMark,7) +" | " + prettySpacing(student.hindiMark,5) +" | " + prettySpacing(student.mathsMark,5) +" | " + prettySpacing(student.computerMark,8) +" | " + prettySpacing(student.totalMarks,5) + " |")
			
			rankCounter +=1
	else:
		print("\n\n ==>>> No student records available in class - "+className+" <<==")
		
	print("\n\n ")			
	input('Press any key to continue...')
	
def main_menu():
	isFileLoaded = False
	
	while True:
		studentDetails={}
		clearScreen()
		
		if not os.path.exists("saps.dat"):
			print("#####################################################\n")
			print("This is a fresh implementation. So add records first\n")
			print("#####################################################\n\n\n")
			print("Loading...")
			
			time.sleep(10)
			createStudent()
					
		else:
			
			if not isFileLoaded:
				loadDetailsFromFile()
				isFileLoaded = True
			
			print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#\n")
			print("Welcome to SAPS student details \n\n")
			print("1. Add Student\n")
			print("2. View Student\n")
			print("3. Update Student\n")
			print("4. Display Ranklist\n")
			print("5. Exit\n")
			
			selectedOption = input('Give your option: ').title()
		
			if selectedOption == "1":
				createStudent()
			elif selectedOption == "2":
				viewStudent()
			elif selectedOption == "3":
				updateStudent()
			elif selectedOption == "4":
				displayRanklist()
			elif selectedOption == "5":
				break
			else:
				print("\n\n ==>>> Invalid menu option. Kindly select proper value  <<==")
				print("\n\n ")			
				input('Press any key to continue... ')
								

#Start the program
main_menu()	