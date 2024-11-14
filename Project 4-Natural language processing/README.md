This was a group project for a Subjects In Natural Language Processing course for my computer science degree.
The goal of this subject was to use the sklearn library to be able to predict the role of Binyan Hitpael in the sentence, based on the syntax and morphological context in the
sentence.
Out of two datasets (one containing syntax and morphologic analysis for sentences in modern Hebrew and one containing analysis to the whole Bible), we picked around 500 samples from each that contain a verb in Hitpael, then classified them to groups according to two linguistic methods and wrote a classification guide. We then converted each analyzed example
into a vector based on the syntax and morphology of the one or two words before and after that verb and then used 10-fold cross validation to find the best prediction rules.
The files:
1. TanakhDictaTEI.rar-the entire dataset for the Bible
2. ModernHebrew.zip-the entire dataset for modern Hebrew
3. text.xml-the classified examples from the Bible
4. modern_hebrew.conllu.txt-the classified examples for Modern Hebrew
5. classification guide.docx-the guide on how to classify each sentence according to the Glinert and Blau methods
6. vector structure.txt-the structure of the vector and the linguistic role of each element of it
7. parse-window1.py and parse-window2.py-the files that convert the classified examples into vectors, split them into a test group and a training group and make the prediction
   rules.
8. report.pdf-a more detailed explanation about our working process, and some statistics about the data.

To execute, make sure you have numpy, conllu and sklearn installed-if not, execute the following command in command prompt without the quotation marks: "pip install numpy" (or the names of the other packages). Then, simply execute either parse-window1.py or parse-window2.py (depending on the size of the window around the verb you want to examine-more information can be found in report.pdf).
