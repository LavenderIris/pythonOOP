class Patient(object):
    def __init__(self, id, name, allergies):
        self.id=id
        self.name=name
        self.allergies=allergies
        self._bednumber=None

    def setBedNumber(self, number):
        self._bednumber=number
    
    def __repr__(self):
        return '<User object id: {}, name: {}, allergies: {}, bednumber: {}'.format(self.id, self.name, self.allergies, self._bednumber)
    
    def info(self):
    # prints out info about each patient
        print "ID:",self.id
        print "Name:",self.name
        print "Allergies:", self.allergies
        print "Bed number",self._bednumber
        return self

class Hospital(object):
    """
    Class definition for Hospital, keeps track of available beds, number of patients and capacity
    """
    def __init__(self, name, capacity):
        self.patients=[]
        self.name=name
        self.capacity=capacity
        # private variable for setting up bed numbers
        self._available_beds=range(1, capacity+1)
    
    def __repr__(self):
        return '<User object patients: {}, name: {}, capacity: {}, avail beds: {}'.format(self.patients, self.name, self.capacity, self._available_beds)
    

    def admit(self, person):
        if len(self.patients)+1 > self.capacity :
            print "Hospital is full, cannot take this patient"
        else :
            print "Admitted"
            person.setBedNumber(self._available_beds.pop(0))
            self.patients.append(person)    
            
    
        return self

    def discharge(self, person_name):
        """
            Finds and Discharges a patient, reassigns bed to available and it sets bed_number to patient as None
        """
        index = -1
        for i, person in enumerate(self.patients):
            if (person.name == person_name):
                index = i

        # we are reclaiming the bed, the person is discharged and we remove them from our list of patients
        self._available_beds.append(self.patients[index]._bednumber)
        self.patients[index]._bednumber=None        
        self.patients.pop(index)
        return self       


    def info(self):
        """
            Prints out the available beds and list of current patients
        """
        print "Available beds:", self._available_beds
        for p in self.patients:
            p.info()
        return self


if __name__ == "__main__":
    patient1 = Patient(1, "Dinosaur Rex","peanuts")
    patient2 = Patient(12, "Cat Panic","dogs")
    patient3 = Patient(8, "Old MacDonalds","lucky charms")

    hospital=Hospital("General", 10)

    hospital.admit(patient1)
    hospital.admit(patient2)
    hospital.admit(patient3)
    hospital.info()

    hospital.discharge("Dinosaur Rex")

    hospital.info()



 