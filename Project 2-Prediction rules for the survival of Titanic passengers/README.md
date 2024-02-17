This project was part of a competition in Kaggle (https://www.kaggle.com/competitions/titanic) and this submission, as of 15/2/2024, put me in the leaderboard at #826 out of 
15241 submissions (i.e. the 95th percentile).
This project implements the concept of feature engineering and uses the sklearn machine learning library.
The goal of this project is to use the training data on some passengers of the Titanic and whether or not they survived to make prediction rules about the survival of other 
passengers.

The input files are train.csv and test.csv. For each passenger the features are:
1. PassengerId
2. Survived (in train.csv only)-the lable
3. Pclass-1st, 2nd, or 3rd class
4. Name
5. Sex
6. Age
7. SibSp (number of siblings)
8. ParCh (number of children)
9. Ticket (there is no known pattern to the ticket numbers so I ignored this feature)
10. Fare (the price paid for the ticket)
11. Cabin
12. Embarked (with a letter code for each city)

I also generated the following features which I found to be important:
13. FamilySize
14. Important-whether or not the passenger has an important title, such as Colonel or Doctor
15. RealCabin-The actual cabin based on the code used in the data (ended up not being used)

I used a validation group to find the binary classification algorhithms and hyper-parameters that would have the lowest validation errors, and implemented that to classify the
test group.

The output is submission.csv which has a classification for each passenger ID in test.csv.

To run, execute all cells of the notebook file notebook2a90729d0a.ipynb. The output file submission.csv will be created as a result. Note that due to it being part of an ongoing competition, the exact results are not known to the public, but they can be evaluated as follows:
1. Go to the following link: https://www.kaggle.com/competitions/titanic/overview
2. Click on "Submit Prediction"
3. Enter the file submission.csv generated after running the notebook
4. Click on "Submit"
The evaluation of the code's predictions will be given after completing these steps.
