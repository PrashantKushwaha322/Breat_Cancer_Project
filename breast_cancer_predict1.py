#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
import tkinter
import tkinter.messagebox

#get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:

def main():
    cancer = pd.read_csv('test.csv')
    print(cancer.columns)
    
    
    # ### The dataset consists of 569 data points, with 32 features each:
    
    # In[5]:
    
    
    print("dimension of cancer data: {}".format(cancer.shape))
    
    
    """preparing data for Deployment model"""
    features_x=['radius_worst',
     'texture_worst',
     'perimeter_worst',
     'area_worst',
     'smoothness_worst',
     'compactness_worst',
     'concavity_worst',
     'concave points_worst',
     'symmetry_worst',
     'fractal_dimension_worst',
     'concavity_se',
     'area_se',
     'concave points_mean',
     'texture_mean',]
    feature_y=['diagnosis']
    
    
    x=cancer[features_x]
    y=cancer[feature_y]
    
    # ### Logistic Regression
    # 
    # One of the most common linear classification algorithms is logistic regression. Despite its name, LogisticRegression is a classification algorithm and not a regression algorithm.
    
    # In[14]:
    
    
    from sklearn.linear_model import LogisticRegression
    
    lr = LogisticRegression()
    lr.fit(x,np.array(y))
    print(lr)
    #logreg100 = LogisticRegression(C=100).fit(X_train, y_train)
    #print("Training set score: {:.3f}".format(logreg100.score(X_train, y_train)))
    #print("Test set score: {:.3f}".format(logreg100.score(X_test, y_test)))
    #
    
    # Using C=100 results in higher accuracy on both training set and test set, confirming that less regularization and a more complex model should perform better.
    
    # In[16]:
    #
    #cancer_features = [x for i,x in enumerate(cancer.columns) if i!=0]
    #
    #plt.figure(figsize=(8,6))
    #plt.plot(logreg.coef_.T, 'o', label="C=1")
    #plt.plot(logreg100.coef_.T, '^', label="C=100")
    #plt.plot(logreg001.coef_.T, 'v', label="C=0.001")
    #plt.xticks(range(cancer.shape[1]), cancer_features, rotation=90)
    #plt.hlines(0, 0, cancer.shape[1])
    #plt.ylim(-5, 5)
    #plt.xlabel("Feature")
    #plt.ylabel("Coefficient magnitude")
    #plt.legend()
    #plt.savefig('log_coef')
    
    """GUI code starts here"""
    #from tkinter import *
    #from tkinter import ttk
    #import tkinter
    #import tkinter.messagebox
    
    
        # create a GUI window
    root = Tk()
    
    # set the background colour of GUI window
    root.configure(background='light green')
    
    # set the title of GUI window
    root.title("CANCER PREDICTION")
    
    # set the configuration of GUI window
    root.geometry("400x900")
    root.minsize(width=550,height=400)
    root.maxsize(width=550,height=400)
    # create a Form label
    heading = Label(root, text="REPORT FIELD", bg="light green")
    
    # create a ID label
    l1 = Label(root, text="radius_worst", bg="light green")
    
    # create a Diagnosis label
    l2 = Label(root, text="texture_worst", bg="light green")
    
    # create a Radius Mean label
    l3 = Label(root, text="perimeter_worst", bg="light green")
    
    # create a Texture Mean lable
    l4= Label(root, text="area_worst", bg="light green")
    
    # create a Perimeter Mean label
    l5= Label(root, text="smoothness_worst", bg="light green")
    
    # create a Area Mean label
    l6 = Label(root, text="compactness_worst", bg="light green")
    
    # create a Smoothness Mean label
    l7 = Label(root, text="concavity_worst", bg="light green")
    
    # create a ID label
    l8 = Label(root, text="concave points_worst", bg="light green")
    
    # create a Diagnosis label
    l9 = Label(root, text="symmetry_worst", bg="light green")
    
    # create a Radius Mean label
    l10 = Label(root, text="fractal_dimension_worst", bg="light green")
    
    # create a Texture Mean lable
    l11= Label(root, text="concavity_se", bg="light green")
    
    # create a Perimeter Mean label
    l12= Label(root, text="area_se", bg="light green")
    
    # create a Area Mean label
    l13 = Label(root, text="concave points_mean", bg="light green")
    
    l14 = Label(root, text="texture_mean", bg="light green")
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    heading.grid(row=0, column=1)
    l1.grid(row=1, column=0)
    l2.grid(row=2, column=0)
    l3.grid(row=3, column=0)
    l4.grid(row=4, column=0)
    l5.grid(row=5, column=0)
    l6.grid(row=6, column=0)
    l7.grid(row=7, column=0)
    l8.grid(row=8, column=0)
    l9.grid(row=9, column=0)
    l10.grid(row=10, column=0)
    l11.grid(row=11, column=0)
    l12.grid(row=12, column=0)
    l13.grid(row=13, column=0)
    l14.grid(row=14, column=0)
    
    
    e1= Entry(root)
    e2 = Entry(root)
    e3 = Entry(root)
    e4 = Entry(root)
    e5 = Entry(root)
    e6 = Entry(root)
    e7 = Entry(root)
    e8= Entry(root)
    e9 = Entry(root)
    e10 = Entry(root)
    e11 = Entry(root)
    e12 = Entry(root)
    e13= Entry(root)
    e14= Entry(root)
    
    # whenever the enter key is pressed
    # then call the focus6 function
    e1.grid(row=1, column=1, ipadx="100")
    e2.grid(row=2, column=1, ipadx="100")
    e3.grid(row=3, column=1, ipadx="100")
    e4.grid(row=4, column=1, ipadx="100")
    e5.grid(row=5, column=1, ipadx="100")
    e6.grid(row=6, column=1, ipadx="100")
    e7.grid(row=7, column=1, ipadx="100")
    e8.grid(row=8, column=1, ipadx="100")
    e9.grid(row=9, column=1, ipadx="100")
    e10.grid(row=10, column=1, ipadx="100")
    e11.grid(row=11, column=1, ipadx="100")
    e12.grid(row=12, column=1, ipadx="100")
    e13.grid(row=13, column=1, ipadx="100")
    e14.grid(row=14, column=1, ipadx="100")
    def calculate():
        a1=int(e1.get())
        a2=int(e2.get())
        a3=int(e3.get())
        a4=int(e4.get())
        a5=int(e5.get())
        a6=int(e6.get())
        a7=int(e7.get())
        a8=int(e8.get())
        a9=int(e9.get())
        a10=int(e10.get())
        a11=int(e11.get())
        a12=int(e12.get())
        a13=int(e13.get())
        a14=int(e14.get())
        tmp=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14]
        tmp=np.array(tmp)
        tmp=tmp.reshape(-14,14)
        pred=lr.predict(tmp)
        prediction="Result is = if M mean Malignent else if M mean Benine"+str(pred)
        messagebox.showinfo("Prediction of Diagnosis Report",prediction)
        
    
    
    
    submit = Button(root, text="Submit", fg="Black",
                    bg="Red", command=calculate)
    submit.grid(row=16, column=1)
    
    # start the GUI
    root.mainloop()
    
    
    """GUI code ends here"""






