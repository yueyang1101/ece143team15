# ece143team15: Analysis On Global Warming

The src folder contains all the python scripts (DataProcessing, Plots). The Original Data folder contains all the data needed for the processing.

Steps:
 1. Data Processing:
     
      a)processTrade.py
      
           -> location: src/DataProcessing/processTrade.py
           
           -> run command: python src/DataProcessing/processTrade.py
           
           -> description: The file reads in the data from data/OriginalData/production-vs-consumption-co2-emissions.csv, and generate the data with the net CO2 emission and stored the data in data/FinalData/HeatmapData 


     b)processFeatureTemp.py 
      
           -> location: src/DataProcessing/processTrade.py
           
           -> run command: python src/DataProcessing/processTrade.py
           
           -> description: The file reads in the data from data/OriginalData/forcings.csv and data/OriginalData/fobserved.csv , and generate a newdataframe with all the feaure info stored as 
           
           -> data generated: data generated is stored in data/FinalData/TempFeature.csv
    
 2. Plotting
   
     a)Feature VS ObservedTemp

           -> location: src/plots/FeatureVSObservedTemp.py 
           
           -> run command: python src/plots/FeatureVSObservedTemp.py 
           
           -> description: The file reads in the data from data/FinalData/TempFeature.csv folder and plots graph comparing the selected feature vs the observed earth temp. 
     
   
     b) Plot_Trade_CO2_Heatmap.py 
           
           -> location: src/plots/Plot_Trade_CO2_Heatmap.py 
           
           -> run command: python src/plots/HealthyVsUnhealthy.py
           
           -> description: The file reads in the data from data/FinalData/HeatmapData folder and plots the heatmap of selected country and selected feauture
      b) Temperature heat map
           
           -> location: src/plots/TemperatureMap.py
           
           -> functions: 
           * get_figure(year: int): create bokeh figure object
           * save_figure(year: int, filename: str): save figure to filename
           * show_figure(year: int): show figure in ipython
           * generate_gif(plots_directory: str, file_path: str, start: int, end: int, step: int = 1, fps: int = 5): geterate gif from plots
           * show_gif(file_path): show gif in ipython
           -> description: it is a module that can be used to plot temperature heatmap and also create gif animations. It is called in the ipython file.
    
