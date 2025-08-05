#**********User-defined Functions**********#
#**********Practical Task**********#

#The following brogram will calculate a user's total holiday cost with feedback.
#The following input will be requested from the user:
#1. The city they are flying to, defined as variable 'city_flight'
#2. The number of nights to be spent in a hotel, defined as variable 'num_nights'
#3. The number of days that the user will rent a car, defined as variable 'rental_days'

#Following the user input, the following functions will be created:
#1. 'hotel_cost()' - using the number of nights return the total cost for the hotel stay.
#2. 'plane_cost()' - using the city that the user is flying from to calculate the flight cost, considering the return flight as well
#3. 'car_rental()' - using the rental days to calculate the total rental cost
#4. 'holiday_cost()' - using the above 3 function results to calculate the total holiday cost

#***********START**********#

#Defining the unit costs
hotel_night = 2500
car_day = 1200
flight_CapeTown = 3000
flight_Durban = 2000
flight_Gqeberha = 2500

#User Landing Message and explanation
print("The following calculator will return the total cost of your planned holiday. \n\n" \
"When promted, please supply the information regarding your planned holiday.")

#Defining which city the user will be flying to
print("To which of the below cities will you fly to for your holiday:\n\n" \
"Cape Town\n" \
"Durban\n" \
"Gqeberha\n")
city_flight = input("City flying to: ").lower()
#city_flight = city_flight.lower

#Defining the number of hotel stay nights
num_nights = int(input("How many nights will you spend at the hotel? "))

#Defining the number of rental car days
rental_days = int(input("For how many days will you rent a car? "))

#Plane cost function
def plane_cost(city_flight):
    if city_flight == "cape town":
        plane_total = flight_CapeTown
    elif city_flight == "durban":
        plane_total = flight_Durban
    elif city_flight == "gqeberha":
        plane_total = flight_Gqeberha
    else:
        print("\nHoliday destination not selected, please rerun the program and select applicable holiday destination")
    return plane_total

#Hotel cost function
def hotel_cost(num_nights):
    hotel_total = hotel_night * num_nights
    return hotel_total

#Car rental funtion
def car_rental(rental_days):
    car_total = car_day * rental_days
    return car_total

#Holiday cost funtion
def holiday_cost(num_nights, city_flight, rental_days):
    holiday_total = car_rental(rental_days) + plane_cost(city_flight) + hotel_cost(num_nights)
    return holiday_total

#Printing output
 
print("\nThe total cost for your flights to " + str(city_flight).upper() + " will be: R " +str(plane_cost(city_flight)) +".00")
print("\nThe total hotel cost for you holiday will be: R " + str(hotel_cost(num_nights)) +".00")
print("\nThe total car rental cost for your holiday will be: R " +str(car_rental(rental_days)) +".00")
print("\nYour total holiday cost will be: R " +str(holiday_cost(num_nights, city_flight, rental_days)) +".00")

#**********END**********#




