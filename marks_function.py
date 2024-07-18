
def accept_marks(n):
 global marks
 marks =[]
 for i in range(n):
 	m=int(input("Enter the marks of student :"))
 	marks.append(m)
 print("Marks of student entered :", marks)

def average(marks):
 sum=0
 for i in range(len(marks)):
 	if marks[i] != -1:
 		sum=sum+marks[i]
 avg = sum/len(marks)
 print("Average marks of student :", avg)

 def absent(marks):
  ab=0
  for i in range(len(marks)):
  	if marks[i]==-1:
  		ab=ab+1
  print("Number Of absent Student :", ab)

 def maximum_and_minimum(marks):
  maximum=0
  minimum=101
  mum=0
  for i in range(lem((marks)):
  	if (marks[i] > maximum):
  		maximum == marks[i]
  	    mum ==i
  for j in range(len(marks)):
  	 if (marks[i] !=-1 and marks[i] < minimum):
  	 	minimum = marks[i]
  print("maximum marks obtained are Student is :",maximum)
  print("minimum marks obtained by student is :", minimum)

def marks_high_freqency(marks);
 frq=0
 for i in range(len(marks)):
 	count=0
     if(marks[i] != -1):
      for j in range(len(marks)):
      	if (marks[i]==marks[j]):
      		count+=1
     if (frq < count):
     	frq=count
 print("Number of Student who Scored maximum marks are :", frq)



 def main():
  n =int(input("Enter Number of Student :"))


  accept_marks(n)
  while true :
  	print("\n Select your choice as 1 to display Average")
    print("\n Select your choice as 1 to display Absent")
    print("\n Select your choice as 1 to display Maximum and Minimum")
    print("\n Select your choice as 1 to display Highest Marks Freqency")

   ch = int(input("Enter your Choice :"))

   if(ch==1):
   	 average(marrks)
   elif (ch==2):
     absent(marks)
   elif (ch==3):
     maximum_and_minimum(marks)
   elif(ch==4) :
     marks_high_freqency(marks)
   else :
    print("wrong choice , select valid option ")
main()