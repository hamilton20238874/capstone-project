student1 = Student("Stacy", "908888888")

print(student1.student_name)

class Student():
  def __init__(self, student_name, student_contact):
    self.student_name = student_name
    self.student_contact = student_contact
  def __str__():
    "This student's name is "+ self.student_name + " and they can be reached at " + self.student_contact

class Class():
  def __init__(self, class_name, class_topic):
    self.class_name = class_name
    self.class_topic = class_topic

#class Student_Class(Class):
 # def __init__(self, s_class_level):
#    self.s_class_level = s_class_level
#    super().__init__(class_name)

class Interest():
  def __init__(self, interest_name, interest_topic):
      self.interest_name = interest_name
      self.interest_topic = interest_topic
    

    
#  schedule = []
#  for i in range(9):
#    i += 1
#    input = "schedule_user_input_" + i
#    schedule.append(input)

def compare(schedule1, schedule2, interest1, interest2):
  counter = 0
  for i in schedule1:
    if schedule1[i].class_name == schedule2[i].class_name:
      if schedule1[i].class_level == schedule2[i].class_level:
        counter += 1
    else:
      continue

  if interest1.length >= interest2.length:
    for i in interest1:
      for j in interest2:
        if interest1[i].interest_name == interest2[j]:
          counter += 3
      
  if interest2.length > interest1.length:
    for i in interest2:
      for j in interest1:
        if interest2[i].interest_name == interest1[j]:
          counter += 3

  return counter

