# # Coded by Shivam Kumar
# # PRN: 20190802073
#
# from scipy.stats import ttest_1samp
# import numpy as np

# class BloodPressureData:
#     def __init__(self):
#         pass
#     def populationMean(self):
#         sum=0
#         for i in self:
#             sum=sum+i
#             mean=sum/(len(self))
#         print("The population mean of given data is "+str(mean))
#         ttest,p_value=ttest_1samp(self,int(mean))
#         print('p_value:',p_value)
#         if p_value<0.05:
#             print("p_value is less than 0.05, thus null hypothesis is rejected.")
#         else:
#             print("p_value is greater than 0.05, thus null hypothesis is accepted.")
#     def sampleMean(self):
#         sum=0
#         sampleSize=10
#         sample=np.random.choice(self,sampleSize)
#         print('Samples are:',sample)
#         for i in self:
#             sum=sum+i
#             mean=sum/(len(self)-1)
#         print("The sample mean of given data is "+str(mean))
#         ttest, p_value = ttest_1samp(self, int(mean))
#         print(p_value)
#         if p_value<0.05:
#             print("p_value is less than 0.05, "
#                   "thus null hypothesis is rejected.")
#         else:
#             print("p_value is greater than 0.05, "
#                   "thus null hypothesis is accepted.")
#
# AmmoniumChloride=[13.4,10.9,11.2,11.8,14.0,15.3,14.2,12.6,17.0,16.2,16.5,15.7]
# Urea=[12,11.7,10.7,11.2,14.8,14.4,13.9,13.7,16.9,16,15.6,16]
#
# print('\n*************** Interpretation of Ammonium Chloride ***************')
# BloodPressureData.sampleMean(AmmoniumChloride)
# print('\n*************** Interpretation of Urea ***************')
# BloodPressureData.sampleMean(Urea)

# Coded by Shivam Kumar
# PRN: 20190802073

from scipy.stats import ttest_1samp
import numpy as np

class statsTest:
    def testBeforeExam(self):
        sum=0
        for i in self:
            sum=sum+i
            mean=sum/(len(self))
        print("The population mean of given data is "+str(mean))
        ttest,p_value=ttest_1samp(self,int(mean))
        print('p_value:',p_value)
        if p_value<0.05:
            print("p_value is less than 0.05, thus null hypothesis is rejected.")
        else:
            print("p_value is greater than 0.05, thus null hypothesis is accepted.")
    def testAfterExam(self):
        sum=0
        for i in self:
            sum=sum+i
            mean=sum/(len(self))
        print("The population mean of given data is "+str(mean))
        ttest,p_value=ttest_1samp(self,int(mean))
        print('p_value:',p_value)
        if p_value<0.05:
            print("p_value is less than 0.05, thus null hypothesis is rejected.")
        else:
            print("p_value is greater than 0.05, thus null hypothesis is accepted.")

marksBefore=[23, 20, 19, 21, 18, 20, 18, 17, 23, 16, 19]
marksAfter=[24, 19, 22, 18, 20, 22, 20, 20, 23, 20, 18]

print("*************** Test Result Before Exam ***************")
statsTest.testBeforeExam(marksBefore)

print("*************** Test Result After Exam ***************")
statsTest.testAfterExam(marksAfter)