# Creates a question and answer of a car's brand based on the name
def brandPrompt(data):
    return "Question: what car brand made a car called " + data[1] + "? Answer: ", data[0]
# Creates a question and answer of a car's model years
def yearPrompt(data, row):
    # Since some car brands were stopped and then continued we need to make a string with all
    # the year ranges
    years = ""
    i = 0
    while(i < len(data)):
        if (data[i][0] == data[row][0] and data[i][1] == data[row][1]):
            start = data[i][3]
            end = data[i][4]
            while(i+1 < len(data) and data[i+1][0] == data[i][0] and data[i+1][1] == data[i][1]):
                if (end != "Now" and int(end)+1 >= int(data[i+1][3])):
                    end = data[i+1][4]
                else:
                    if (years == ""):
                        years = start + "-" + end
                    else:
                        years = years + ", " + start + "-" + end
                    start = data[i+1][3]
                    end = data[i+1][4]
                i += 1
            if (years == ""):
                years = start + "-" + end
            else:    
                years = years + ", " + start + "-" + end
        i += 1
    return "Question: in which model years was the " + data[row][0] + " " + data[row][1] + " made? Answer: ", years
# Creates a question and answer of a car's classification
def classPrompt(data):
    return "Question: what car classification does the " + str(data[3]) + "-" + str(data[4]) + " " + data[0] + " " + data[1] + " belong to? Answer: ", data[5]
import llm
import random
import csv
data = []
carClasses = []
with open("cars.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        data.append(row)
        if (row[5] not in carClasses):
            carClasses.append(row[5])
classesString = ""
for i in range(len(carClasses)):
    classesString = classesString + carClasses[i]
    if (i != len(carClasses)-1):
        classesString = classesString + ", "
llmmodel = llm.get_model("gpt-3.5-turbo")
conv = llmmodel.conversation()
conv.prompt("I am going to ask you questions about car brands. For each brand, please write only the answer without any additional text and without a period at the end.").text()
brandQuestions = random.sample(range(0, len(data)), 10)
for i in brandQuestions:
    question, answer = brandPrompt(data[i])
    resp = conv.prompt(question)
    print(question + resp.text())
    if (resp.text().lower() == answer.lower()):
        print("Correct!")
    else:
        print("Wrong, the answer was: ", answer)
conv.prompt("Now I will ask you about year models. Please write only in this format: startYear-endYear and if it's still being made please write the word Now instead of endYear, without a period. If there are several separate ranges write it in this format: start1-end1, start2-end2. Please do not add a period in the end, just the ranges in this format, and without any additional text.")
timeQuestions = random.sample(range(0, len(data)), 10)
for i in timeQuestions:
    question, answer = yearPrompt(data, i)
    resp = conv.prompt(question)
    print(question + resp.text())
    if (resp.text() == answer):
        print("Correct!")
    else:
        print("Wrong, the answer was: ", answer)
conv.prompt("Now I will ask you questions about classifications of car models. You are only allowed to use classes from this list: " + classesString + ", you are not allowed to reply with anything that is not in this list. Please pick the most correct option from that list according to the model and years, and only write that, exactly as it is spelled here, and without any additional text or a period in the end.")
categoryQuestions = random.sample(range(0, len(data)), 10)
for i in categoryQuestions:
    question, answer = classPrompt(data[i])
    resp = conv.prompt(question)
    print(question + resp.text())
    if (resp.text() == answer):
        print("Correct!")
    else:
        print("Wrong, the answer was: ", answer)
