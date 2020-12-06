import matplotlib.pyplot as pyplot

labels = 'Tweeter Positive', 'Tweeter Negative', 'Tweeter Neutral'

def drawGraph(tweeter_positive, tweeter_negative, tweeter_neutral, subject):
    sizes = [tweeter_positive, tweeter_negative, tweeter_neutral]
    fig1, ax1 = pyplot.subplots()
    ax1.pie(sizes, labels = labels, autopct='%1.1f%%', shadow=True, startangle=90)
    pyplot.title('Análise do assunto:'+ subject)
    pyplot.show()


