# Final_Project
My end-of-bachelor's data science project.
### Meir Joffe
### 324680461
### meir.joffe@mail.huji.ac.il

## Files Included:
  
* Code Files:
  * Models:
    * model_executor.py - a file containing functions to run (train and test) models.
    * model_helpers.py - a file containing helper functions for model preprocessing and running.
    * model_preprocessing.py - a file containing functions for model preprocessing.
    * MPLRegression.py - a file containing the class for a Multi-Layer Perceptron model.
    * RandomForestRegression.py - a file containing the class for a Random Forest Regression model.
    * SGDRegression.py - a file containing the class for a Stochastic Gradient Descent model.
  * Preprocessing:
    * preprocessing_price_data.py - a file containing functions for preprocessing the home price data.
    * preprocessing_prosperity_data.py - a file containing functions for preprocessing the prosperity data.
    * preprocessing_income_data.py - a file containing functions for preprocessing the income data.
    * preprocessing_all.py - a file containing functions for preprocessing all of the data.
  * constants.py - a file containing global constants such as data file paths, library imports and district mappings.

* Data Files:
  * Original - the home price files that came in 2 parts, files are called pp-#YEAR-part#X.csv where #X is either 1 or 
      2 and #YEAR is the year number.
  * Regular - the home price files each containing data for a whole year, files are called pp-#YEAR.csv.
  * Prosperity - the prosperity data files, in both .xls and .csv format.
  * Income_By_District - the mean and median income files, including the original files and the preprocessed mean and
      median income files.
  * Preprocessed - the preprocessed files after cleaning, organizing, aligning and combining the price, income and
      prosperity data, files are called preprocessed-#YEAR.csv.
  * Model_Prop_Bin_Preprocessed - the model preprocessed files that are ready to be used to train and test models with
      the property type column having been converted to 4 binary columns, files are called m_b-preprocessed-#YEAR.
  * Model_Prop_Bin_Train - the model preprocessed files that have been split into train and test, this is the train
      data, files are called train-b-#YEAR.csv.
  * Model_Prop_Bin_Test - the model preprocessed files that have been split into train and test, this is the test 
      data, files are called test-b-#YEAR.csv.
  * Model_Prop_Bin_Combined - the files containing the data from all the years combined and mixed (property type
      converted to binary) and separated into 20 parts, files are called m_b-preprocessed-part-#X.csv where #X is the
      part number.
  * Model_Prop_Dis_Preprocessed - the model preprocessed files that are ready to be used to train and test models with
      the property type column having been converted to discrete column, files are called m_d-preprocessed-#YEAR.csv.
  * Model_Prop_Dis_Train - the model preprocessed files that have been split into train and test, this is the train
      data, files are called train-d-#YEAR.csv.
  * Model_Prop_Dis_Test - the model preprocessed files that have been split into train and test, this is the test 
      data, files are called test-d-#YEAR.csv.
  * Model_Prop_Dis_Combined - the files containing the data from all the years combined and mixed (property type
      converted to discrete) and separated into 20 parts, files are called m_d-preprocessed-part-#X.csv where #X is 
      the part number.
  * Bootstrap - the upper and lower bounds for the bootstrap weight vector (theta) parameters (90% confidence
      intervals), files are called bootstrap_#TYPE_#YEAR.p where #TYPE is either bin (for binary), dis (for discrete)
      or all (without year) for the models for all years combined.
  * Results - contains the model results (errors) in a file called results.csv.

* Other files:
  * README - this file.
  * Pipeline Diagram.pdf - a diagram of the data pipeline from download through preprocessing through model processing.
  * Final_Project_Notebook.ipynb - a notebook containing each of the graphs in the report and the code to create them.
  * Final_Project_Notebook.pdf - same as Final_Project_Notebook.ipynb but in pdf format.
  * Data_Science_Project_Report_Meir_Joffe.docx - the project report in word format.
  * Data_Science_Project_Report_Meir_Joffe.pdf - the project report in pdf format.


## Instructions to run code:
* To run any of the code, the data path to the directory with all the data files needs to be inserted in 
    constants.py line 11.
* To run with preprocessing, take the initial files and run the commented-out code at the bottom of 
    preprocessing_price_data.py and the commented-out code at the bottom of preprocessing_income_data.py. Then, run 
    the first commented-out code section and the bottom of preprocessing_all.py. Note this will take time and will 
    create files in the process. Next, go to model_preprocessing.py and run the commented out code at the bottom 
    (depending on whether you wish to train models for both binary and discrete models or just one of them, run the 
    appropriate commands). Once this is done, to run the models see instructions for running code without 
    preprocessing. After this, if you want to run the models on all of the combined data, go to preprocessing_all.py 
    and run the second commented-out section.
* To run without preprocessing, go to model_executor.py and choose the model you with to run. Commands for running 
    each of the models, whether by year or all years combined, are commented out at the bottom of the file. 
    Additionally, there is code there to run bootstrap calculations for Stochastic Gradient Descent weight vector 
    (theta) parameters.


## Instructions to run visualizations:
* To produce the visualizations, the data path needs to be updated to the path to the directory where the data is 
    stored. Once this is done, run each of the markdown sections to produce the graphs. Note that some of the 
    sections use variables that were defined in earlier sections, thus those sections need to be run first.
