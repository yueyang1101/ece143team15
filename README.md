# ece143team15: Analysis On Global Warming

The src folder contains all the python scripts (DataProcessing, Plots). The Original Data folder contains all the data needed for the processing.

Steps:
 1. Data Processing:
     
   a)processTrade.py
      
           -> location: src/DataProcessing/processTrade.py
           
           -> run command: python src/DataProcessing/processTrade.py
           
           -> description: The file reads in the data from data/OriginalData/production-vs-consumption-co2-emissions.csv, and generate the data with the net CO2 emission


  b)processFeatureTemp.py 
      
           -> location: src/DataProcessing/processTrade.py
           
           -> run command: python src/DataProcessing/processTrade.py
           
           -> description: The file reads in the data from data/OriginalData/forcings.csv and data/OriginalData/fobserved.csv , and generate a newdataframe with all the feaure info stored
           
           -> data generated: data generated is stored in data/FinalData
    
 2. Plotting
   
   a)Feature VS ObservedTemp
     
     -> location: src/plots/FeatureVSObservedTemp.py 
     
     -> run command: python src/plots/FeatureVSObservedTemp.py 
     
     -> description: The file reads in the data from data/FinalData/TempFeature.csv folder and plots graph comparing the selected feature vs the observed earth temp. 
   
   b) Plot_Trade_CO2_Heatmap.py 
      
      -> location: src/plots/Plot_Trade_CO2_Heatmap.py 
     
     -> run command: python src/plots/HealthyVsUnhealthy.py
     
     -> description: The file reads in the data from "data/FinalData" folder and plots the heatmap of selected country and selcted feauture
    
