import imp
import inspect
import sys

#1. fill in this class
#   it will need to provide for what happens below in the
#	main, so you will at least need a constructor that takes the values as (Brand, Price, Safety Rating),
# 	a function called showEvaluation, and an attribute carCount
class CarEvaluation:
	
	carCount = 0
	
	brandName = ""
	priceLevel = ""
	safetyRating = -1
	
	'A simple class that represents a car evaluation'
	#all your logic here
	def __init__(self, brandName = "", priceLevel = "", safetyRating = -1):
		self.brandName = brandName
		self.priceLevel = priceLevel
		self.safetyRating = safetyRating
		CarEvaluation.carCount += 1
	
	# http://stackoverflow.com/questions/4932438/how-to-create-a-custom-string-representation-for-a-class-object
	def __repr__(self):
		return '(' + self.brandName + ',' + self.priceLevel + ',' + str(self.safetyRating) + ')'

	# showEvaluation
	def showEvaluation(self):
		print("The %s has a %s price and it's safety is rated a %d" % (self.brandName, self.priceLevel, self.safetyRating))

#2. fill in this function
#   it takes a list of CarEvaluation objects for input and either "asc" or "des"
#   if it gets "asc" return a list of car names order by ascending price
# 	otherwise by descending price
def sortbyprice(the_list, asc_or_desc): #you fill in the rest
	return sorted(the_list, key=lambda x: getpricelevelnumeric(x.priceLevel), reverse=(asc_or_desc!="asc")) #return a value

#3. fill in this function
#   it takes a list for input of CarEvaluation objects and a value to search for
#	it returns true if the value is in the safety  attribute of an entry on the list,
#   otherwise false
def searchforsafety(the_list, safety_level = 0): #you fill in the rest
	return (len([x for x in the_list if x.safetyRating == safety_level]) > 0)

# helper function to define price levels numerically
def getpricelevelnumeric(low_medium_or_high):
	return ['Low', 'Med', 'High'].index(low_medium_or_high)

# This is the main of the program.  Expected outputs are in comments after the function calls.
if __name__ == "__main__":	
   eval1 = CarEvaluation("Ford", "High", 2)
   eval2 = CarEvaluation("GMC", "Med", 4)
   eval3 = CarEvaluation("Toyota", "Low", 3)

   print "Car Count = %d" % CarEvaluation.carCount # Car Count = 3

   print ""
   print "EXPECT: \n" + "The Ford has a High price and it's safety is rated a 2"
   print "RESULT:"
   # use basic introspection to call it:
   getattr(eval1, 'showEvaluation')() #The Ford has a High price and it's safety is rated a 2
   
   print ""
   print "EXPECT: \n" + "The GMC has a Med price and it's safety is rated a 4"
   print "RESULT:"
   # use basic introspection to call it:
   getattr(eval2, 'showEvaluation')() #The GMC has a Med price and it's safety is rated a 4

   print ""
   print "EXPECT: \n" + "The Toyota has a Low price and it's safety is rated a 3"
   print "RESULT:"
   # use basic introspection to call it:
   getattr(eval3, 'showEvaluation')() #The Toyota has a Low price and it's safety is rated a 3

   L = [eval1, eval2, eval3]

   print ""
   print "EXPECT: \n" + "[Toyota, GMC, Ford]"
   print sortbyprice(L, "asc"); #[Toyota, GMC, Ford]

   print ""
   print "EXPECT: \n" + "[Ford, GMC, Toyota]"
   print sortbyprice(L, "des"); #[Ford, GMC, Toyota]

   print ""
   print "EXPECT: \n" + "true"
   print searchforsafety(L, 2); #true

   print ""
   print "EXPECT: \n" + "false"
   print searchforsafety(L, 1); #false
   
