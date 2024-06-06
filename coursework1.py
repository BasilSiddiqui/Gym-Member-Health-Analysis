#Coursework1 blahiguhrgorur ga

#Welcome message
message_1 = '''
**********************************************************************************

Welcome to the Fitness Member Analysis System!
We're dedicated to providing personalized insights to ensure every member embarks on the most effective fitness journey.
Let's get started by understanding your members better!

**********************************************************************************
'''

print (message_1) 

#Lists of members' data
members_names = []
members_weight = []
members_height = []
members_resting_heartrate = []
members_bmi = []
bmi_category = []
member_fitness = []
workout_preference = []

number_of_gym_members = int(input("Enter the number of gym members to be analyzed: ")) #Number of members input

for i in range (number_of_gym_members): 
    member_name = input("Enter member name: ") #Name data input
    members_names.append(member_name)
    while True :
        member_weight =(eval(input("Enter member's weight (kg): "))) #Weight data input
        if member_weight < 20 or member_weight > 200:
            print ("Please enter a valid weight (20kg to 200kg).")
            continue 
        members_weight.append(member_weight)
        break
    while True:
        member_height = (eval(input("Enter member's height (cm): "))) #Height data input
        if member_height < 50 or member_height > 250:
            print ("Please enter a valid height (50cm to 250cm).")
            continue
        members_height.append(member_height)
        break
    while True:
        global member_resting_heartrate 
        member_resting_heartrate = (eval(input("Enter member's resting heartrate (bpm): "))) #Heartrate data input
        if member_resting_heartrate < 30 or member_resting_heartrate > 200:
            print ("Please enter a valid heart rate (30 to 200 bpm).")
            continue
        members_resting_heartrate.append(member_resting_heartrate)
        break

while True:
    
    message_2 = ''' 
Thank you for the input. The next options available are: 
1) Print summary of all members fitness details and workout recommendations.
2) List members who require physician approval before starting the recommended workout.
3) Print specific member details.
4) Exit program. 
    '''         #Thank the trainer for his input and ask him about what to do next      
    print (message_2)
    
    display_data = int(input("Choose a number to execute the command (1/2/3/4): "))
    
    if display_data == 1: #Option 1
        print("| Name  | W  |  H  | BP |")
        for i in range (number_of_gym_members):
            print("|", members_names[i], "|", members_weight[i], "|", members_height[i], "|", members_resting_heartrate[i], "|")
            
        
    if display_data == 2 : #Option 2
        print ("Members who require physician approval before starting the recommended workout: ")
        for i in range(number_of_gym_members):
            if members_resting_heartrate[i] > 84:
                print (members_names[i])
            else:
                print ("No member requires physician approval.")
                
    if display_data == 3: #Option 3
        inp_mem = input("Which member's details do you want?: " )
        if inp_mem not in members_names:
            print ("Member does not exist.")
        else:
           x = members_names.index(inp_mem)
           print ("N:", members_names[x], "W:", members_weight[x], "H:", members_height[x], "BP:", members_resting_heartrate[x])
            
    if display_data == 4: #Option 4
        message_3 = '''
We hope you found our analysis insightful and our recommendations beneficial.
Here's to empowering workouts and fostering a community of fit members.
Thank you!
'''
        print (message_3) #Thanking them finally
        break

def bmi_call(): #Calculating bmi through height and weight
    for i in range (number_of_gym_members):   
        member_weight = members_weight[i]
        member_height = members_height[i]
        member_bmi = round(((member_weight / member_height**2)*10000),2)
        members_bmi.append(member_bmi)
        if member_bmi > 0 and member_bmi <18.5:
            bmi_category.append("Underweight")
        elif member_bmi >= 18.5 and member_bmi <24.9:
            bmi_category.append("Healthy")
        elif member_bmi >= 24.9 and member_bmi <29.9:
            bmi_category.append("Overweight")
        elif member_bmi >= 29.9:
            bmi_category.append("Obese")
    
bmi_call()

def bp_call(): #Checking fitness through resting heartrate
    for i in range (number_of_gym_members):
        member_resting_heartrate = members_resting_heartrate[i]
        if member_resting_heartrate < 60:
            member_fitness.append("Athlete")
        elif member_resting_heartrate >= 60 and member_resting_heartrate < 73:
            member_fitness.append("Good")
        elif member_resting_heartrate >= 73 and member_resting_heartrate < 84:
            member_fitness.append("Acceptable")
        elif member_resting_heartrate >= 84:
            member_fitness.append("Needs improvement")
            
bp_call()

def program_recommendation(): #Recommending workouts based on bmi and fitness
    for i in range (number_of_gym_members):
        member_resting_heartrate = members_resting_heartrate[i]
        member_weight = members_weight[i]
        if (bmi_category == "Underweight" or bmi_category == "Obese") and member_fitness == "Needs improvement":
            workout_preference.append("Mixed workout with cardio emphasis")
        elif member_fitness == "Athlete" and bmi_category == "Healthy":
            workout_preference.append("Strength training emphasis")
        elif member_fitness == "Acceptable":
            workout_preference.append("Balanced workouts")
            
program_recommendation()
