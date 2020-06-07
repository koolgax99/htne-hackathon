from firebase import firebase
import pandas as pd

firebase = firebase.FirebaseApplication("https://htne-hackathon.firebaseio.com/", None)
result = firebase.get('/User',None)

#print(result)

temp = 90 #result['Temperature']
heartbeat = 100 #result['Heart Beat']
bp = 90 #result['Blood Pressure']
breathrate = 20 #result['Breathing Rate']
'''
file = open('data.csv','a')
file.write("%d,%d,%d,%d" %(temp,heartbeat,bp,breathrate))
file.close()
'''

#df.to_csv('my_csv.csv', mode='a', header=False)



temp = result['Temperature']
heartbeat = result['Heart Beat']
bp = result['Blood Pressure']
breathrate = result['Breathing Rate']


if(temp>100.4 and heartbeat>85 and 80<bp<120 and 12<breathrate<20): {
    print("you are symptomatic to corona. You cannot go out.")
}
else: {
    print("You can go out. ")
}