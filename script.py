# Create Patient class
class Patient:
  def __init__(self, patient_data):
    self.name = patient_data[0]
    self.age = patient_data[1]
    # add more parameters here
    self.sex = patient_data[2]
    self.bmi = patient_data[3]
    self.num_of_children = patient_data[4]
    self.smoker = patient_data[5]

  # Create the estimated_insurance_cost() method
  def estimated_insurance_cost(self):
    estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
    print("{}'s estimated insurance costs is {} dollars.".format(self.name, estimated_cost))
  
  # Create an update_age() method
  def update_age(self, new_age):
    self.age = new_age
    print("{} is now {} years old.".format(self.name, self.age))
    self.estimated_insurance_cost()

  # Define the update_num_children method
  def update_num_children(self, new_num_children):
    self.num_of_children = new_num_children 
    if new_num_children == 1:
      print("{} has {} child.".format(self.name, self.num_of_children))
    elif new_num_children > 1:
      print("{} has {} children.".format(self.name, self.num_of_children))
    elif new_num_children < 0:
      print("Your input is not valid")
    else:
      print("{} has no child.".format(self.name))
    self.estimated_insurance_cost()

  # Define a method called patient_profile()
  def patient_profile(self):
    patient_information = dict()
    patient_information.update({
      "Name": self.name,
      "Age": self.age,
      "Sex": self.sex,
      "BMI": self.bmi,
      "Number of Children": self.num_of_children,
      "Smoker": self.smoker
    })
    return patient_information

  # Define an update_bmi() method
  def update_bmi(self, new_bmi):
    self.bmi = new_bmi
    print("{}'s BMI is {}.".format(self.name, self.bmi))
    self.estimated_insurance_cost()

  # Create a method called update_smoking_status()
  def update_smoking_status(self, new_smoker):
    self.smoker = new_smoker
    if new_smoker == 0:
      print("{} does not smoke.".format(self.name))
      self.estimated_insurance_cost()
    elif new_smoker == 1:
      print("{} is a smoker.".format(self.name))
      self.estimated_insurance_cost()
    else:
      print("Your input is not valid.\nPlease enter 1 for smoker and 0 for non-smoker")

# Create an instance variable called patient1
try:
  patient1 = Patient(["John Doe", 25, 1, 22.2, 0, 0])
except Exception as e:
  print("Error: ", e)

# Display patient1's information
print(patient1.name)  # <-- patient1's name
print(patient1.age)   # <-- patient1's age
print(patient1.sex)   # <-- patient1's sex
print(patient1.bmi)   # <-- patient1's bmi
print(patient1.num_of_children)   # <-- patient1's children
print(patient1.smoker)    # <-- patient1's smoking status

# Display patient1's estimated cost
try:
  patient1.estimated_insurance_cost()
except Exception as e:
  print("Error: ", e)

# Display a new line
print("\n")

# Display patient1's new age and estimated insurance cost
try:
  patient1.update_age(26)
except Exception as e:
  print("Error: ", e)

# Display a new line
print("\n")

# Display patient1's number of children and estimated insurance cost
try:
  patient1.update_num_children(1)
except Exception as e:
  print("Error: ", e)

# Display a new line
print("\n")

# Display patient1's information in a dictionary
try:
  print(patient1.patient_profile())
except Exception as e:
  print("Error: ", e)

# Display a new line
print("\n")

# Display patient1's new BMI and estimated insurance cost
try:
  patient1.update_bmi(18.5)
except Exception as e:
  print("Error: ", e)

# Display a new line
print("\n")

# Display patient1's new smoking status and estimated insurance cost
try:
  patient1.update_smoking_status(0)
except Exception as e:
  print("Your input is not valid. \nPlease enter 1 for smoker and 0 for non-smoker: ", e)