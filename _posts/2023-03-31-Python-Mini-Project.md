**PYTHON MINI PROJECT REFLECTION REPORT**- Me and my teammates developed a typing tester using python. It can goves a random text for user and at the end it will give elapsed time, accuracy and speed in WPM(words per minutes)

**CHALLENGES WHICH I FACED DURING THIS PROJECT**- In the typing tester project, calculating the accuracy of the user's typing can be challenging because there are several factors to consider. Here are some of the challenges that may arise:

Different lengths: The word that the user is asked to type may be shorter or longer than the user's input. This means that we need to compare each character of the word and the user's input, up to the length of the shorter string.

Typos: The user may make typos while typing, such as accidentally typing the wrong character or omitting a character. This means that we need to account for partial matches, where some but not all of the characters are the same.

Case sensitivity: The project does not specify whether the typing test is case-sensitive or not. If it is case-sensitive, we need to compare the case of each character in the word and the user's input. If it is not case-sensitive, we need to convert both strings to lowercase (or uppercase) before comparing.

To address these challenges, we can define a function (in this case, calculate_accuracy()) that takes in the word and the user's input, and counts the number of characters that are the same in both. We can use a loop to compare each character in the two strings, up to the length of the shorter string. We can also account for typos by counting partial matches, where some but not all of the characters are the same. Finally, we can convert both strings to lowercase (or uppercase) if necessary to make the comparison case-insensitive.

**SKILLS I LEARNED DURING THIS PROJECT**- Over the last few weeks i have learned various aspects and modules of python language. But while completing this project I came across the problem of calculating accuracy and speed which I solved after a lot of brainstorming with my teammate. The solution to calculate accuracy and speed is as follows

---

accuracy = round((1 - errors / len(text)) * 100)
speed = round(len(text) / elapsed_time * 60)

---
