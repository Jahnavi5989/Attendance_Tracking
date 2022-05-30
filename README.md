

![Logo](https://img.freepik.com/free-vector/emotion-detection-abstract-concept-vector-illustration-speech-emotional-state-recognition-emotion-detection-from-text-sensor-technology-machine-learning-ai-reading-face-abstract-metaphor_335657-2305.jpg?w=360)
# Attendance Tracking using Facial Recognition

This Project is Desktop based Application Developed for Microsoft Intern Engage 2022 Programme
it is an Advanced Attendance App based on face recognition technology.









## Features

- Login System for three user roles
- Admin Portal(Can Manipulate Data of everyone)
- Student Portal(Save,add,delete,Update and AddPhotos)
- Faculty Portal(Save,add,delete,Update and AddPhotos)
- Attendance with Face Recognition
- Attendance reports of both faculty and Student(Excel file/Sqlite3 database)
- Import , Export Csv files and save to database
- Help desk
- Developer Page
- Exit System

## Adavanced Attendance System


![Logo](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRX-jdoPkMRAcrzfM_t0lui8f_ejOoUSZh2oA&usqp=CAU)

## Algorithms used
Haarcascade Opencv (Object Detection)

A Haar classifier, or a Haar cascade classifier, is a machine learning object detection program that identifies objects in an image and video.

LBPH Opencv (Face Recognition)

The Local Binary Pattern Histogram (LBPH) algorithm is a face recognition algorithm based on a local binary operator, designed to recognize both the side and front face of a human. However, the recognition rate of the LBPH algorithm is limited, if the conditions, such as in the expression diversification, disorientation, and a change in the lighting performance manifest.




## Usecases

### STUDENT USECASES:

1.Cannot perfom any manipulation of the data

2.Can check their details

3.Can check their Attendance Status

4.Can train the system

5.Can Give attendance

### FACULTY USECASES:

1.Can check their details

2.Can check their attendance status

3.Can Give their attendance

4.Can take student attendance

5.Can Perform CRUD operations on student data

6.Can perform CRUD operations on Student attendance data by importing and exporting csv file and can also store csv file to database for the backup purpose

7.Can train their system

### ADMIN USECASES:

ADMIN is the one who can actually manipulate every data of everyone

*List of data that admin can manipulate

1.Faculty details

2.Faculty Attendance status by importing and exporting csv file and can also store csv file to database for the backup purpose

3.Student details

4.Student Attendance status by importing and exporting attendance.csv file and can also store their attendance.csv file to database for the backup purpose

5.Photo samples of students

6.photo samples of Faculty

8.Admin can train both student and faculty system with photosamples given by student and faculty

## Tech Stack

![Logo](https://cdn.dribbble.com/users/1787323/screenshots/11310814/media/78d925f388bdfd914f5c84a30261e239.png?compress=1&resize=400x300)

**UI/UX:** - Python GUI Tkinter

**Backend:** - Sqlite3

**Project Development:** - Scurm





## Important

- While giving ID numbers of students or faculty make sure they are in sequence i.e, 1,2,3,4,5......etc you cannot give random number as id

- You cannot take photo samples after saving Students or faculty data in a bulk

you must ensure that you have saved one student details as soon as saving you have to take photosample for that student and train the system

## Clone or Fork the project
- clone this project
- install requirements by using 

        pip install -r requirements.txt
- Just run login.py file in any ide that supports python environment like VScode or pycharm etc which is the main file of the project follow how to use this app       section
  for further instructions

## How to use this app?

- Install here : https://github.com/Jahnavi5989/Attendance_Tracking/releases
- while installing dont forget to copy the path where it is installing after clicking on Finish button go in that path your file structure will look like this
- <img width="500" alt="image" src="https://user-images.githubusercontent.com/96164649/170849661-103ac9a2-c368-45c3-acb8-e1c0d202f408.png">
- Open login file 
- Register yourself with accurate data and then login with credentials
- if you register as student you will be redirected to the student portal
  where you can see your details click on your details and click on take photo samples
  follow the instructions and give your photosamples
- click on train system
- then go take my attendance tab click on scan face it will detect your face and hit attendance in the excel file directly
- you can check your attendance once faculty save your attendance
- In the same way faculty also have to follow
- faculty can see their attendance after admin saved them
- If you registered as admin you will be redirected to Admin portal you can perform CRUD on faculty and students data based on the necessities









## Screenshots
<img width="500" alt="image" src="https://user-images.githubusercontent.com/96164649/170829493-8b8f5f62-4556-4633-bd10-ed15a68231da.png">
<img width="500" alt="image" src="https://user-images.githubusercontent.com/96164649/170829797-29c3e241-846c-4cdd-8d88-077e08fd5506.png">
<img width="500" alt="image" src="https://user-images.githubusercontent.com/96164649/170829860-537420f2-e3ee-4247-ad2d-78111ae344e3.png">
<img width="500" alt="image" src="https://user-images.githubusercontent.com/96164649/170839367-0596b4c7-978e-4559-9d6e-6648ba0b6818.jpg"> 

## Future Developement Plannings
- Trying to make it as a browser based application using 
  django framework
- Trying to  build more secured Authentication System

## Things learned 
- how to prepare a proper Documentation for project
- Scrum Methodology
- Being consistent no matter what[Based on the count of bugs that I had to face while developing this project:( ]

Finally!!! you are here Thank you for checking out my Application feel free to fork, star, or clone if you have enjoyed it
