import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

months = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun')
y_pos = np.arange(len(months))
performance = [500,800,600,400,200,1000]

#plotando o gráfico de barras horizontais ou de colunas
plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, months)
plt.ylabel('Meses')
plt.title('Receita 1º semestre')

plt.show()