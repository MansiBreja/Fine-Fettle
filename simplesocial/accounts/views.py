from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy,reverse
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import DiagnosisInfo
from accounts.forms import DiagnosisInfoForm
from . import forms
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

class HomePage(TemplateView):
    template_name = "index.html"

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"

class Result(TemplateView):
    template_name='accounts/result.html'

# class CreateDiagnosisView(LoginRequiredMixin,CreateView):
#     login_url = '/login/'
#     # redirect_field_name = 'accounts/result.html'
#     # get_absolute_url='result'
#     # success_url = reverse_lazy('res')
#     form_class = DiagnosisInfoForm
#     model = DiagnosisInfo
#
#     if form_class.form_valid():
#         print (form_class.cleaned_data)
#
#
#     dataset = pd.read_csv('parameter_vals.csv')
#     X = dataset.iloc[:, :-1].values
#     y = dataset.iloc[:,6].values
#     X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.1,random_state=0)
#     sc_X=StandardScaler()
#     X_train=sc_X.fit_transform(X_train)
#     X_test=sc_X.transform(X_test)
#     classifier = LogisticRegression(random_state=0)
#     classifier.fit(X_train,y_train)
#     y_pred = classifier.predict([[1,2,3,4,5,6]])
#     print(y_pred)


def diagnosis_view(request):

    if request.method == 'POST':
        form = DiagnosisInfoForm(request.POST)

        if form.is_valid():
            a=form.cleaned_data['Diastolic_Blood_Pressure']
            b=form.cleaned_data['Systolic_Blood_Pressure']
            c=form.cleaned_data['Respiratory_rate']
            d=form.cleaned_data['Pulse_rate']
            e=form.cleaned_data['Temperature']
            f=form.cleaned_data['Sore_Throat']
            dataset = pd.read_csv('2024.csv')
            X = dataset.iloc[:, :-1].values
            y = dataset.iloc[:,8].values
            X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)
            sc_X=StandardScaler()
            X_train=sc_X.fit_transform(X_train)
            X_test=sc_X.transform(X_test)
            multi_classifier = LogisticRegression(multi_class='multinomial',random_state=0,solver= 'newton-cg')
            multi_classifier.fit(X_train,y_train)
            print(a)
            print(b)
            print(c)
            print(d)
            print(e)
            print(f)
            if f=='Y':
                y_pred = multi_classifier.predict([[b,a,e,d,c,1,0,0]])
            else:
                y_pred = multi_classifier.predict([[b,a,e,d,c,0,0,0]])
            print(y_pred)
            return render(request,'accounts/result.html',{'rs':y_pred})
            # return HttpResponseRedirect(reverse('accounts:res') )

    else:
        form=DiagnosisInfoForm()

    return render(request,'accounts/diagnosisinfo_form.html',{'form':form})
