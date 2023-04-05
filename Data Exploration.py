# Coded by Shivam Kumar
# PRN: 20190802073

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataExploration:
    def __init__(self,data):
        self.data=data
    def loadData(self):
        data=pd.read_csv(self)
        print('*** Selected dataset is -',self,'***\n',data.head(10))
        print('*** The detailed description of the '
              'selected dataset is given below ***\n',data.describe())
    def univariateAnalysisScatterPlot(self):
        data=pd.read_csv(self)
        feature=str(input('Enter name of feature to make graph: '))
        plt.scatter(data.index,data[feature])
        plt.title('Scatter plot graph of '+feature)
        plt.show()
    def univariateAnalysisHistogram(self):
        data=pd.read_csv(self)
        feature = str(input('Enter name of feature to make graph: '))
        plt.hist(data[feature])
        plt.title('Histogram graph of '+feature)
        plt.show()
    def univariateAnalysisDensity(self):
        data=pd.read_csv(self)
        feature = str(input('Enter name of feature to make graph: '))
        plt.figure(figsize=(5,5))
        data[feature].plot(kind='density')
        plt.title('Density graph of ' + feature)
        plt.show()
    def univariateAnalysisBoxPlot(self):
        data=pd.read_csv(self)
        feature = str(input('Enter name of feature to make graph: '))
        plt.boxplot(data[feature])
        plt.title('Box plot of ' + feature)
        plt.show()
    def univariateAnalysisViolinPlot(self):
        data=pd.read_csv(self)
        feature = str(input('Enter name of feature to make graph: '))
        plt.figure(figsize=(5,5))
        plt.violinplot(data[feature],showmeans=True)
        plt.title('Violin plot of ' + feature)
        plt.show()
    def bivariateAnalysisScatterPlot(self):
        data = pd.read_csv(self)
        feature1 = str(input('Enter name of feature 1 to make graph: '))
        feature2 = str(input('Enter name of feature 2 to make graph: '))
        plt.scatter(x=data[feature1],y=data[feature2])
        plt.title('The bivariate graph of '+feature1+" and "+feature2)
        plt.show()
    def bivariateAnalysisPairPlot(self):
        data=pd.read_csv(self)
        sns.pairplot(data)
        plt.show()

def main():
    DataExploration.loadData('haberman.csv')
    DataExploration.univariateAnalysisScatterPlot('haberman.csv')
    DataExploration.univariateAnalysisHistogram('haberman.csv')
    DataExploration.univariateAnalysisDensity('haberman.csv')
    DataExploration.univariateAnalysisBoxPlot('haberman.csv')
    DataExploration.univariateAnalysisViolinPlot('haberman.csv')
    DataExploration.bivariateAnalysisScatterPlot('haberman.csv')
    DataExploration.bivariateAnalysisPairPlot('haberman.csv')

if __name__=="__main__":
    main()