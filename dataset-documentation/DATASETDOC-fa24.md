***Project Information*** 

* What is the project name? bu-sustainability-STARS 
* What is the link to your project’s GitHub repository?  https://github.com/BU-Spark/ds-bu-sustainability-stars/tree/Algorithm
* What is the link to your project’s Google Drive folder? https://drive.google.com/drive/folders/12zry512LiiJr2xk1kGLGpKbebGZ4BGLk
* In your own words, what is this project about? What is the goal of this project?  **create database contain sustainability-related papers published by BU faculties**
* Who is the client for the project? **Gabrielle Brewer**
* What class was this project part of? **DS539**

***Dataset Information***

* What data sets did you use in your project? Please provide a link to the data sets \
  https://drive.google.com/drive/folders/1qKNaIMl3NU4J8TpbZj2saFbwAD60V1Lj \
* Please provide a link to any data dictionaries for the datasets in this project. If one does not exist, please create a data dictionary for the datasets used in this project. **https://drive.google.com/drive/folders/1qKNaIMl3NU4J8TpbZj2saFbwAD60V1Lj**   
* What keywords or tags would you attach to the data set?  
  * Domain(s) of Application: 
  * Sustainability, papers

*The following questions pertain to the datasets you used in your project.*   
*Motivation* 

* For what purpose was the dataset created? Was there a specific task in mind? Was there a specific gap that needed to be filled? Please provide a description. \
the dataset is create by finding the best way to gathering all the papers writen by BU faculties, so we use the openBU and google Scholar

*Composition*

* What do the instances that comprise the dataset represent (e.g., documents, photos, people, countries)? Are there multiple types of instances (e.g., movies, users, and ratings; people and interactions between them; nodes and edges)? What is the format of the instances (e.g., image data, text data, tabular data, audio data, video data, time series, graph data, geospatial data, multimodal (please specify), etc.)? Please provide a description. \
  **each row is a paper, contain tile, abstract, year, and author**
* How many instances are there in total (of each type, if appropriate)? \ 
  **17,000 rows, but slightly incomplete**
* Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set? If the dataset is a sample, then what is the larger set? Is the sample representative of the larger set? If so, please describe how this representativeness was validated/verified. If it is not representative of the larger set, please describe why not (e.g., to cover a more diverse range of instances, because instances were withheld or unavailable).
  **not necessary a sample from large dataset, but could be a subset of googlescholar and Whole openBU data**
* What data does each instance consist of? “Raw” data (e.g., unprocessed text or images) or features? In either case, please provide a description.
  **text data**
* Is there any information missing from individual instances? If so, please provide a description, explaining why this information is missing (e.g., because it was unavailable). This does not include intentionally removed information, but might include redacted text.
  **no** 
* Are there recommended data splits (e.g., training, development/validation, testing)? If so, please provide a description of these splits, explaining the rationale behind them
**use data splits when doing model training**
* Are there any errors, sources of noise, or redundancies in the dataset? If so, please provide a description.
  **might be repeat data from both openBU and google Scholar**
* Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g., websites, tweets, other datasets)? If it links to or relies on external resources,
  **https://scholar.google.com/** \
  **https://open.bu.edu/**
  * Are there guarantees that they will exist, and remain constant, over time;  **yes**
  * Are there official archival versions of the complete dataset (i.e., including the external resources as they existed at the time the dataset was created)?  **no**
  * Are there any restrictions (e.g., licenses, fees) associated with any of the external resources that might apply to a dataset consumer? Please provide descriptions of all external resources and any restrictions associated with them, as well as links or other access points as appropriate.   **no for openBU, google scholar need python library scholarly, and have rate restriction per day per ip address**
* Does the dataset contain data that might be considered confidential (e.g., data that is protected by legal privilege or by doctor-patient confidentiality, data that includes the content of individuals’ non-public communications)? If so, please provide a description.   **no, all open sources data**
* Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety? If so, please describe why.   **no**
* Is it possible to identify individuals (i.e., one or more natural persons), either directly or indirectly (i.e., in combination with other data) from the dataset? If so, please describe how.   **yes, contain name of the author**


| Size of dataset |  |
| :---- | :---- |
| Number of instances | 16000 |
| Number of fields  | 4 |


  
*Collection Process*

* What mechanisms or procedures were used to collect the data (e.g., API, artificially generated, crowdsourced \- paid, crowdsourced \- volunteer, scraped or crawled, survey, forms, or polls, taken from other existing datasets, provided by the client, etc)? How were these mechanisms or procedures validated?  **web scraping from google scholar and open BU**
* Over what timeframe was the data collected? Does this timeframe match the creation timeframe of the data associated with the instances (e.g., recent crawl of old news articles)? If not, please describe the timeframe in which the data associated with the instances was created. **2022-2024**

*Preprocessing/cleaning/labeling* 

* Was any preprocessing/cleaning/labeling of the data done (e.g., discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances, processing of missing values)? If so, please provide a description. If not, you may skip the remaining questions in this section.   **tokenize all the text, remove all the -ed;-es; etc.**
* Were any transformations applied to the data (e.g., cleaning mismatched values, cleaning missing values, converting data types, data aggregation, dimensionality reduction, joining input sources, redaction or anonymization, etc.)? If so, please provide a description.   **vectorize data, clean the missing value of the data**
* Was the “raw” data saved in addition to the preprocessed/cleaned/labeled data (e.g., to support unanticipated future uses)? If so, please provide a link or other access point to the “raw” data, this could be a link to a folder in your GitHub Repo, Spark\! owned Google Drive Folder for this project, or a path on the SCC, etc.  **no, the preprocessed data is not saved, but will gernate during modeling process**

*Uses* 

* What tasks has the dataset been used for so far? Please provide a description.  **seprate the sustainability related papers**
* What (other) tasks could the dataset be used for?  **analyze the paper category and quantity of papers by different department/field**
* Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses?  **tf-idf vectorize the data helps a lot for non-numerial data when modeling**

*Distribution*

* Based on discussions with the client, what access type should this dataset be given (eg., Internal (Restricted), External Open Access, Other)? **External Open Access**

*Maintenance* 

* If others want to extend/augment/build on/contribute to the dataset, is there a mechanism for them to do so? If so, please provide a description. **refer to [openBU](https://github.com/BU-Spark/ds-bu-sustainability-stars/tree/Algorithm/24fall/OpenBU) and [googlescholar](https://github.com/BU-Spark/ds-bu-sustainability-stars/tree/Algorithm/24fall/googlescholar) folder, full sequence of garthering data are provided**




