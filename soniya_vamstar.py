import json
class Data:
	def loadData(self):
		input_file = open ('person.json')
		json_array = json.load(input_file)
		return (json_array)
			
	def calculateHealthStatus(self,json_array):
		Overweight_people=0
		for person in json_array:
			BMI=person['WeightKg']/(person['HeightCm']/100)
			if(BMI<=18.4):
				BMICategory="Underweight"
				HealthRisk="Malnutrition risk"
			elif(BMI >=18.5 and BMI<=24.9):
				BMICategory="Normal weight"
				HealthRisk="Low risk"
			elif(BMI>=25 and BMI<=29.9):
				BMICategory="Overweight"
				HealthRisk="Enhanced risk"
			elif(BMI>=30 and BMI<=34.9):
				BMICategory="Moderately obese"
				HealthRisk="Medium risk"
			elif(BMI>=35 and BMI<=39.9):
				BMICategory="Severely obese"
				HealthRisk="High risk"
			elif(BMI>=40):
				BMICategory="Very severely obese"
				HealthRisk="Very high risk"
			person.update({'BMICategory':BMICategory})
			person.update({'HealthRisk':HealthRisk})
			print (json.dumps(person))
			if(BMICategory=="Overweight" or BMICategory=="Moderately obese" or BMICategory=="Severely obese" or BMICategory=="Very severely obese"):
				Overweight_people=Overweight_people+1
		print('Overweight people:',+Overweight_people)
		
if __name__ == '__main__': 
	data = Data()
	json_array=data.loadData()
	data.calculateHealthStatus(json_array)