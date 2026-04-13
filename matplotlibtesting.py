import matplotlib.pyplot as plt

scores=[45,50,55,60,65,70,75,80,200]

plt.hist(scores)
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.title("Distribution of Exam Scores")
plt.show()