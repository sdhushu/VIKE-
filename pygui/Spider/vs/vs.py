import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib
def vsgo(classvs):
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['font.family']='sans-serif'
    labels = ['turnover', 'spending', 'income', 'transactions', 'spending']
    # men_means = [20, 34, 30, 35, 27]
    #women_means = [25, 32, 34, 20, 25]
    men_means=classvs
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x, men_means, width, label='Men')
    ax.set_ylabel('Pay treasure')
    ax.set_title('2019 Revenue Visualization')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()


    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')


    plt.savefig('xxx.png')
    plt.close()
