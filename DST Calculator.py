#DISTANCE,TIME AND SPEED FINDER. NOTE: OPERATES ON KILOMETRES AND HOUR ONLY.

A = print("A. Distance finder")
B = print("B. Speed finder")
C = print("C. Time finder")
option = input("Choose any option(A,B,C):")

if option == "A":
    speed = int(input("Enter the Speed of the agent: "))
    time = int(input("Enter the Time taken: "))
    distance =(speed * time )
    print(f"The distance covered is {distance} km ")

elif option == "B":
    distance = int(input("Enter the Distance covered: "))
    time = int(input("Enter the Time taken: "))
    speed =(distance / time )
    print(f"The speed is {speed} km/h ")

elif option == "C":
    distance = int(input("Enter the Distance covered: "))
    speed = int(input("Enter the Speed of the agent: "))
    time =(distance / speed )
    print(f"The time taken is {time} h ")

else:
    print("Invalid input!")



