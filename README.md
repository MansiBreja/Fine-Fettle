# Fine-Fettle

## Abstract

This clinical intervention aims to provide a feasible solution to the existing problems in the Health Care sector.

The objective is to provide a hassle-free and user-friendly application which would help both doctors as well as patients to save time and resources. There are several problems in the medical sector of our economy, some of which we managed to discover as an upshot of our trek to a nearby hospital. Our interaction with a number of patients and doctors steered our focus to one specific problem which seemed quite general and unresolvable, the long OPD queues which seem ceaseless for hours altogether. 

## Introduction and Motivation

There are several medical disorders whose severity cannot be interpreted or perceived by common people. Most of the times, people presume that they don’t require any medical treatment and end up taking their medical conditions too lightly. The major reason for this is the trouble they have to face while waiting in long OPD queues. They prefer taking some common antipyretic tablets in case of high fever for instance, rather than consulting a doctor.

There are many cases reported every year which show that a timely treatment could have prevented worse conditions and the ailments could have easily been cured in earlier stages.

There are several parameters such as blood pressure, body temperature, BMI, pulse rate and respiratory rate which are easy to measure and can be really helpful in the detection of the level of severity for medical conditions such as Flu, Typhoid and road accidents. Although the parameters are well known and easy to measure, several people lack the knowledge and resources required for diagnosis.

## The solution

We came up with the idea of a WEB APP which can solve the problem identified to a very large extent and that too, in a fairly simple way.

This app provides an absolutely easy to use and convenient platform that can help in predicting the condition of the user. The app would suggest the user whether he/she should be visiting a doctor or not.

This app would take as inputs, the health parameters of the user like Blood Pressure (BP), Temperature(T), Respiratory Rate(RR), Pulse rate and Body Mass Index(BMI). BP and temperature can be determined by using digital thermometers and sphygmomanometers which are generally available in several households. The app will also provide information to the user on how to calculate parameters like Respiratory Rate, BMI and Pulse Rate manually. 

This app would then predict whether or not the user needs to visit a doctor. This can be achieved by developing a “Logistic Regression Model” which will predict the seriousness of the condition based upon the fed dataset.

The idea is to save the most important resource, “time” and that too in the most effortless and elementary way possible. By setting up a separate table outside the OPD counter to diagnose people who cannot afford such equipments at home or lack any sort of skills to measure the specified parameters, the queue can be simply split into two categories:

--people with serious medical conditions who need admission urgently.

--people who simply need to be prescribed medicines.

This would help save the time of both the above categories of people as well as the doctors to a very large extent. The OPD doctors would have to deal with a lesser number of patients now. The second category of people would find shorter OPD queues in comparison to earlier cases. And most importantly, the people having serious medical conditions wouldn’t have to bear the trouble of undergoing 2 clinical trials, first in the OPD and then in the ward where they are admitted later.

## Installation requirements

```
Framework : Django, Version : 1.11.8
Language : Python, Version : 3.6.3

To run it, we have to install some packages and libraries
Bootstrap 3
numpy
pandas
matplotlib
sklearn
bcrypt
django[argon]

To install it, write this on command line terminal:
"pip install package-name"
```

## To run

```
Clone this repo
cd into this repo
Enter the command: "python manage.py runserver"
Copy the url and paste it in your favourite browser window.
```

This project was made by collectively by [Kavita Maurya](https://github.com/Kavita309), [Mansi Breja](https://github.com/MansiBreja) and [Karan](https://github.com/karans785) as a part of the Hackeam Hackathon, NSIT, Delhi. 
