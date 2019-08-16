# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Khemraj)s
"""
import pandas as pd
def import_data(file_path = input("Enter File Path"),filename = input("Enter Name of csv file")):
    #import Data

    if file_path == "":
        file_path = "C:\\Users\\t3175ks\\Downloads\\2019\\Automation_Projects\\To Khemraj S\\GVW\\PT10_LP_01Mar19_concat_1\\csv"

    if filename == "":
        filename = "\\PT10_LP_01Mar19_0.csv"

    file = file_path + filename
    hd = input("Enter 1 or 0")

    if hd == '1':
        df = pd.read_csv(file, header=0)
    elif hd == '0':
        df = pd.read_csv(file, skiprows=8, index_col=0, header=None)
        df = df.iloc[:, 1:]
        cl_names = ['Analog_Clutch', 'EngineSpeed', 'GasPedalPosition', 'StopLightSts', 'ThrottlePosition',
                'VehicleSpeedVSOSig']
        df.columns = cl_names
    return df
