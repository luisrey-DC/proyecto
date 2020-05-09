# -*- coding: utf-8 -*-
"""
Created on Mon May  4 11:59:13 2020

@author: luisr
"""

import pandas as pd
import matplotlib.pyplot as plt

"1- Compute the five-number summary, the boxplot, the mean, and the standard deviation for the annual salary per gender."
def salario_genero(df):
    filter_nan=df.dropna(subset=['Gender','ConvertedComp']) #Nuevo documento sin Nan en Genero y Salario
    outs=pd.unique(filter_nan['Gender']) #crea lista de tipos de genero
    ing = ';'.join(outs) #une la lista en una cadena agregando ";" entre valores 
    outs=ing.split(';') #crea una lista separando los valores de una cadena por ";"
    outs=(list(set(outs))) #elimina los valores repetidos en la cadena
    for i in range(len(outs)): #recorre todos los tipos de genero que exiten
        salary=filter_nan[filter_nan.Gender.str.contains(outs[i])] #filtra los datos donde aparesca el genero seleccionado
        print('\n\n\nSalario anual de '+outs[i]) #Muestra el salario del genero que se esta evaluando
        print('\nDatos') #muestra donde se encuentran los datos
        print(salary['ConvertedComp'].describe()) #muestra los datos del genero
        fig, ax = plt.subplots() #crea una figura para mostrar el diagrama de caja
        ax.set_title('Boxplot de '+outs[i],color='red',fontsize='xx-large') #titulo del diagrama 
        ax.set_ylabel('Salario', color='blue',fontsize='xx-large')
        ax.boxplot(salary['ConvertedComp'],showfliers=False) #crea el diagrama sin outlayears
        plt.show() #Muestra el diagrama
        
        
"2- Compute the five-number summary, the boxplot, the mean, and the standard deviation for the annual salary per ethnicity."
def salario_etnia(df):
    filter_nan=df.dropna(subset=['Ethnicity','ConvertedComp'])#Nuevo documento sin Nan en Etnia y Salario
    print(filter_nan)
    outs=pd.unique(filter_nan['Ethnicity']) #crea lista de tipos de etnia
    ing = ';'.join(outs) #une la lista en una cadena agregando ";" entre valores 
    outs=ing.split(';') #crea una lista separando los valores de una cadena por ";"
    outs=(list(set(outs))) #elimina los valores repetidos en la cadena
    for i in range(len(outs)):#recorre todos los tipos de etnias que exiten
        salary=filter_nan[filter_nan.Ethnicity.str.contains(outs[i])] #filtra los datos donde aparesca la etnia seleccionado
        print('\n\n\nSalario anual de '+outs[i]+'\n') #Muestra el salario de la etnia que se esta evaluando
        print('\nDatos\n') #muestra donde se encuentran los datos
        print(salary['ConvertedComp'].describe()) #muestra los datos de la etnia
        fig, ax = plt.subplots() #crea una figura para mostrar el diagrama de caja
        ax.set_title('Boxplot de '+outs[i],color='red',fontsize='xx-large') #titulo del diagrama 
        ax.set_ylabel('Salario', color='blue',fontsize='xx-large')
        ax.boxplot(salary['ConvertedComp'],showfliers=False) #crea el diagrama sin outlayears
        plt.show() #Muestra el diagrama
        

"3- Compute the five-number summary, the boxplot, the mean, and the standard deviation for the annual salary per developer type."
def salario_desarrollador(df):
    filter_nan=df.dropna(subset=['DevType','ConvertedComp'])#Nuevo documento sin Nan en lenguajes y Salario
    outs=pd.unique(filter_nan['DevType']) #crea lista de tipos de lenguajes
    ing = ';'.join(outs) #une la lista en una cadena agregando ";" entre valores 
    outs=ing.split(';') #crea una lista separando los valores de una cadena por ";"
    outs=(list(set(outs))) #elimina los valores repetidos en la cadena
    for i in range(len(outs)): #recorre todos los tipos de lenguajes que exiten
        salary=filter_nan[filter_nan.DevType.str.contains(outs[i])] #filtra los datos donde aparesca el lenguaje seleccionado
        print('\n\n\nSalario anual de '+outs[i]+'\n') #Muestra el salario del lenguaje que se esta evaluando
        print('\nDatos\n') #muestra donde se encuentran los datos
        print(salary['ConvertedComp'].describe()) #muestra los datos del lenguaje
        fig, ax = plt.subplots() #crea una figura para mostrar el diagrama de caja
        ax.set_title('Boxplot de '+outs[i],color='red',fontsize='xx-large') #titulo del diagrama 
        ax.set_ylabel('Salario', color='blue',fontsize='xx-large')
        ax.boxplot(salary['ConvertedComp'],showfliers=False) #crea el diagrama sin outlayears
        plt.show() #Muestra el diagrama
        
        
"4- Compute the median, mean and standard deviation of the annual salary per country."      
def datos_pais(df):
    filter_nan=df.dropna(subset=['Country','ConvertedComp']) #Nuevo documento sin Nan en Pais y Salario
    outs=pd.unique(filter_nan['Country']) #crea lista de tipos de paises
    ing = ';'.join(outs).replace('(Not Listed Above)','') #une la lista en una cadena agregando ";" entre valores 
    outs=ing.split(';') #crea una lista separando los valores de una cadena por ";"
    outs=(list(set(outs))) #elimina los valores repetidos en la cadena
    for i in range(len(outs)): #Recorre los paises
        salary=filter_nan[filter_nan.Country.str.contains(outs[i])] #filtra los datos donde aparesca el pais
        print('\n\n\nSalario anual de '+outs[i]) #Muestra el salario del pais que se esta evaluando
        print('\nDatos') #muestra donde se encuentran los datos
        media =salary['ConvertedComp'].mean() #media del pais
        mediana = salary['ConvertedComp'].median() #Mediana del pais
        print('Media=',media) #mostramos los datos de la media
        print('Mediana=',mediana) #muestra los datos de la mediana
        if media!=mediana: #Si la media y la mediana son igual, la desviacion estandar sera igual a 0 
            std = salary['ConvertedComp'].std()
        else:
            std=0
        print('Desviacion=',std)
    print(filter_nan)


"5- Obtain a bar plot with the frequencies of responses for each developer type."
def freq_desarrollador(df):
    filter_nan=df.dropna(subset=['DevType'])#Nuevo documento sin valores Nan en Devtype
    res_dev=pd.unique(filter_nan['DevType']) #crea lista de tipos de desarrollaodores
    type_dev=';'.join(res_dev) #une la lista en una cadena agregando ";" entre valores 
    res_dev=type_dev.split(';') #crea una lista separando los valores de una cadena por ";"
    type_dev=(list(set(res_dev))) #crea una lista de todos los tipos de desarrolladores sin repetir
    type_dev.sort() #Ordena los tipos de desarrollador por alfabeto
    frecuencia=[] #variable donde se guardaran las frecuencias
    for i in range(len(type_dev)): #Recorremos todos los tipos de desarrolladores
        freq=filter_nan[filter_nan.DevType.str.contains(type_dev[i])] #filtra los datos donde aparece el tipo de desarrollador
        frecuencia.append(freq.shape[0]) #Cuenta el numero de datos donde aparece el tipo de desarrollador
    fig = plt.figure('Gráfica de barras',figsize=(12,5)) #Crea una figura para mostrar la grafica
    ax = fig.add_subplot(111) #Posiciona la figura
    xx = range(len(frecuencia)) #tamaño de las frecuencias
    ax.bar(xx, frecuencia, width=.8, align='center') #Se crea una grafica de barras
    ax.set_xticks(xx) #Asignamos los datos de las frecuencias al eje x
    ax.set_xlabel('Tipo de desarrollador ',color='blue',fontsize='xx-large')
    ax.set_ylabel('Frecuencia', color='blue',fontsize='xx-large')
    ax.set_title('Frecuencias de tipo de desarrolladores',color='red',fontsize='xx-large')
    ax.set_xticklabels(type_dev,rotation=90,horizontalalignment='right',fontweight='light')
    plt.show()


"6- Plot histograms with 10 bins for the years of experience with coding per gender."
def exp_genero(df):
    filter_nan=df.dropna(subset=['Gender','YearsCode']) #Nuevo documento sin Nan en Genero y años de experiencia
    outs=pd.unique(filter_nan['Gender']) #crea lista de tipos de genero
    ing = ';'.join(outs) #une la lista en una cadena agregando ";" entre valores 
    outs=ing.split(';') #crea una lista separando los valores de una cadena por ";"
    outs=(list(set(outs))) #elimina los valores repetidos en la cadena
    x=[]
    filter_nan['YearsCode']=filter_nan['YearsCode'].replace(['Less than 1 year','More than 50 years'], '0') #cambia valores de strings por "0"
    for i in range(len(outs)): #Recorre los tipos de genero
        exp=filter_nan[filter_nan.Gender.str.contains(outs[i])] #filtra los datos por genero
        print(len(exp))
        exp['YearsCode']=exp['YearsCode'].astype(float) #convierte los valores en flotantes
        exp=exp.drop(exp[exp['YearsCode']==0].index) #elimina los valores de "0"
        exp=exp.sort_values('YearsCode') #Ordena los datos segun "YearsCode"
        for y in range(1,51): #Creamos una lista de los datos que pareceran en el eje x
            x.append((y))
        plt.figure('Histograma',figsize=(13,5)) #creamos una figura
        plt.title('Años de experiencia '+outs[i],color='red',fontsize='xx-large') #titulo del histograma
        plt.hist(exp['YearsCode'], bins = 10, edgecolor = 'yellow',  linewidth=2) #Crea histograma con años de experiencia 
        plt.grid(True)
        plt.ylabel('Frecuencia', color='blue',fontsize='xx-large')
        plt.xlabel('Años de experiencia', color='blue',fontsize='xx-large')
        plt.xticks(x)
        plt.show()
        plt.clf()


"7- Plot histograms with 10 bins for the average number of working hours per week, per developer type."
def horas_desarrollador(df):
    filter_nan=df.dropna(subset=['DevType','WorkWeekHrs']) #Nuevo documento sin Nan en Genero y Salario
    outs=pd.unique(filter_nan['DevType']) #crea lista de tipos de genero
    ing = ';'.join(outs) #une la lista en una cadena agregando ";" entre valores 
    outs=ing.split(';') #crea una lista separando los valores de una cadena por ";"
    outs=(list(set(outs))) #elimina los valores repetidos en la cadena
    for i in range(len(outs)): #recorre todos los tipos de desarrollador
        hr=filter_nan[filter_nan.DevType.str.contains(outs[i])]#filtra los datos por el tipo de desarrollador
        hr=hr.sort_values('WorkWeekHrs') #organiza de menor a mañor las horas de trabajo
        plt.figure('Histograma',figsize=(10,5)) #Crea una figura
        plt.title('Horas de trabajo de desarrolladores '+outs[i],color='red',fontsize='xx-large')
        plt.hist(hr['WorkWeekHrs'], bins = 10, edgecolor = 'yellow',  linewidth=2)
        plt.grid(True)
        plt.ylabel('Frecuencia', color='blue',fontsize='xx-large')
        plt.xlabel('Horas de trabajo a la semana', color='blue',fontsize='xx-large')
        plt.show()
        plt.clf()  
    

"8- Plot histograms with 10 bins for the age per gender."
def edad_genero(df):
    filter_nan=df.dropna(subset=['Gender','Age']) #Nuevo documento sin Nan en Genero y Salario
    outs=pd.unique(filter_nan['Gender']) #crea lista de tipos de genero
    ing = ';'.join(outs) #une la lista en una cadena agregando ";" entre valores 
    outs=ing.split(';') #crea una lista separando los valores de una cadena por ";"
    outs=(list(set(outs))) #elimina los valores repetidos en la cadena
    for i in range(len(outs)):
        age=filter_nan[filter_nan.Gender.str.contains(outs[i])]
        age=age.sort_values('Age')
        plt.figure('Histograma',figsize=(13,5))
        plt.title('Edades de '+outs[i],color='red',fontsize='xx-large')
        plt.hist(age['Age'], bins = 10, edgecolor = 'yellow',  linewidth=2)
        plt.ylabel('Frecuencia', color='blue',fontsize='xx-large')
        plt.xlabel('Edad', color='blue',fontsize='xx-large')
        plt.grid(True)
        plt.show()
        plt.clf()



"9- Compute the median, mean and standard deviation of the age per programming language."
def datos_age(df):
    filter_nan=df.dropna(subset=['Age','LanguageWorkedWith']) #Nuevo documento sin Nan en Genero y Salario
    outs=pd.unique(filter_nan['LanguageWorkedWith']) #crea lista de tipos de genero
    ing = ';'.join(outs).replace('C++','C+').replace('(s):','') #une la lista en una cadena agregando ";" entre valores 
    outs=ing.split(';') #crea una lista separando los valores de una cadena por ";"
    outs=(list(set(outs))) #elimina los valores repetidos en la cadena
    for i in range(len(outs)):
        age=filter_nan[filter_nan.LanguageWorkedWith.str.contains(outs[i])] #Nuevo documento donde aparece genero
        print(len(age))
        print('\n\n\nEdad de programadores en '+outs[i])
        print('\nDatos')
        media =age['Age'].mean()
        mediana = age['Age'].median()
        print('Media=',media)
        print('Mediana=',mediana)
        if media!=mediana:
            std = age['Age'].std()
        else:
            std=0
        print('Desviacion=',std)
    print(filter_nan)

"10- Compute the correlation between years of experience and annual salary."
def years_salary(df):
    filter_nan=df.dropna(subset=['ConvertedComp','YearsCode'])#Nuevo documento sin valores Nan en Devtype
    filter_nan['YearsCode'].replace(['Less than 1 year','More than 50 years'], ['0.5','55'],inplace=True)
    filter_nan['YearsCode']=filter_nan['YearsCode'].astype(float)
    print(filter_nan)
    correlation=filter_nan['ConvertedComp'].corr(filter_nan['YearsCode'],method='pearson')
    print('\n\nCorrelacion entre años de experiencia y salario\n',correlation,'\n\n\n')


"11- Compute the correlation between the age and the annual salary."
def age_salary(df):
    filter_nan=df.dropna(subset=['ConvertedComp','Age'])#Nuevo documento sin valores Nan en Devtype
    correlation=filter_nan['Age'].corr(filter_nan['ConvertedComp'],method='pearson')
    print('\n\nCorrelacion entre la edad y el salario\n',correlation,'\n\n\n')
  

"""12- Compute the correlation between educational level and annual salary. In this case,
       replace the string of the educational level by an ordinal index (e.g. Primary/elementary
       school = 1, Secondary school = 2, and so on)."""    
def edlevel_salary(df):
    filter_nan=df.dropna(subset=['ConvertedComp','EdLevel'])#Nuevo documento sin valores Nan en EdLevel y ConvertedComp
    #Asigna un valor a cada nivel educativo y sustituye por el valor
    filter_nan['EdLevel'].replace(['I never completed any formal education'
              ,'Primary/elementary school'
              ,'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)'
              ,'Associate degree','Some college/university study without earning a degree'
              ,'Bachelor’s degree (BA, BS, B.Eng., etc.)','Professional degree (JD, MD, etc.)'
              ,'Master’s degree (MA, MS, M.Eng., MBA, etc.)','Other doctoral degree (Ph.D, Ed.D., etc.)']
    , ['0','1','2','3','4','5','6','7','8'],inplace=True)
    filter_nan['EdLevel']=filter_nan['EdLevel'].astype(float)
    correlation=filter_nan['ConvertedComp'].corr(filter_nan['EdLevel'],method='pearson')
    print('\n\nCorrelacion entre nivel educativo y salario\n',correlation,'\n\n\n')   


"13- Obtain a bar plot with the frequencies of the different programming languages."
def freq_language(df):
    filter_nan=df.dropna(subset=['LanguageWorkedWith'])#Nuevo documento sin valores Nan en Devtype
    res_dev=pd.unique(filter_nan['LanguageWorkedWith']) #crea lista de tipos de desarrollaodores
    type_dev=';'.join(res_dev).replace('C++','C+').replace('(s):','') #une la lista en una cadena agregando ";" entre valores 
    res_dev=type_dev.split(';') #crea una lista separando los valores de una cadena por ";"
    type_dev=(list(set(res_dev))) #crea una lista de todos los tipos de desarrolladores sin repetir
    type_dev.sort() #Ordena los tipos de desarrollador por alfabeto
    frecuencia=[] #variable donde se guardaran las frecuencias
    for i in range(len(type_dev)): #Recorremos todos los tipos de desarrolladores
        freq=filter_nan[filter_nan.LanguageWorkedWith.str.contains(type_dev[i])]
        frecuencia.append(freq.shape[0])
    fig = plt.figure('Gráfica de barras',figsize=(12,5)) # Figure
    print(frecuencia)
    ax = fig.add_subplot(111) # Axes
    xx = range(len(frecuencia))
    ax.bar(xx, frecuencia, width=.8, align='center')
    ax.set_xticks(xx)
    ax.set_xlabel('Lenguaje',color='blue',fontsize='xx-large')
    ax.set_ylabel('Frecuencia', color='blue',fontsize='xx-large')
    ax.set_title('Frecuencia de tipos de lenguajes',color='red',fontsize='xx-large')
    ax.set_xticklabels(type_dev,rotation=45,horizontalalignment='right',fontweight='light')
    plt.show()

w_d="C:/Users/luisr/Desktop/Proyecto/"
i_f= w_d+'survey_results_public.csv'
df=pd.read_csv(i_f)

"Funciones"
#salario_genero(df)
#salario_etnia(df)
#salario_desarrollador(df)
#datos_pais(df)
#freq_desarrollador(df)
#exp_genero(df)
#horas_desarrollador(df)
#edad_genero(df)
#datos_age(df)
#years_salary(df)
#age_salary(df)
#edlevel_salary(df)
freq_language(df)
