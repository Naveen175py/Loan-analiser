from django.http import HttpResponse
from django.shortcuts import render
import joblib
import random
import numpy as np
def home(request):
    return render(request,"home.html")
def result(request):
    return render(request,"result.html")
def result(request):
    cls=joblib.load('finalized_model.sav')
    lis=[]
    #lis.append(int(request.GET['Loan_ID']))
    if  request.GET['Gender']=='male':
        lis.append(1)
    if request.GET['Gender']=='female':
        lis.append(0)
    if request.GET['Married']=='yes':
        lis.append(1)
    if request.GET['Married']=='no':
        lis.append(0)
    if request.GET['Dependents']=='yes':
        lis.append(1)
    if request.GET['Dependents']=='no':
        lis.append(0)
    if request.GET['Education']=='yes':
        lis.append(1)
    if request.GET['Education']=='no':
        lis.append(0)
    if request.GET['Self_Employed']=='yes':
        lis.append(1)
    if request.GET['Self_Employed']=='no':
        lis.append(0)
    lis.append(int(request.GET['ApplicantIncome']))
    lis.append(int(request.GET['CoapplicantIncome']))
    lis.append(int(request.GET['LoanAmount']))
    lis.append(int(request.GET['Loan_Amount_Term']))
    lis.append(int(request.GET['Credit_History']))
    lis.append(int(request.GET['Property_Area']))
    
   
    arr=np.array(lis)
    ans=cls.predict(arr.reshape(1,-1))
    if ans==[0]:
        return render(request,"result.html",{'ans':'Sorry!Requirments are not satisfied.'})
    elif ans==[1]:
        return render(request,"result.html",{'ans':'Congratulations!Your Loan requirements are approved.'})
    
    
