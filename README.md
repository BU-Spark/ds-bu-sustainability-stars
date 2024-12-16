# BU-stainablity STARS
## Getting Started
the algorithm, web scraper are in notebook(.ipynb) format, the webpage is in .py and .html format need editor that allow to run them. The kernel for notebook should be avaibly for python more than 3.1
# Introduction and desciption
This document serves as a comprehensive guide for using the Paper Algorithm and Web Scraper developed for retrieving and analyzing research publications. The purpose of these tools is to streamline the process of collecting metadata such as titles, abstracts, and publication years, specifically for sustainability-related research. It is important to mention what sustainability is. Here is the definition of sustainability, as stated in the project description: \n
*Sustainability Challenge – An issue or situation that threatens or undermines ecological integrity, racial equity and social justice, or the ability of future generations to meet their needs (e.g., biodiversity loss, poverty and inequality, and climate change), OR a goal or objective that contributes to there solution of such an issue or situation (e.g., ecosystem health, universal human rights, and renewable energy generation). To identify sustainability challenges, it may be helpful to reference the targets embedded in the Sustainable Development Goals (SDGs), the principles outlined in the Earth Charter, and/or the Doughnut of social and planetary boundaries。
## projectcheck list:
-Web Scraper for openbu\
-web scaper for google scholar\
-model detect sustainablity related papers\
-webpage allow filter by department; year; or name and download filtered data.

### Proposed Solution:
### code this semester are all under folder /24fall;
### Web Scraper
#### google scholar:
Designed to retrieve publication data from Google Scholar using the Python library scholarly.\
Filters and categorizes publications based on predefined sustainability-related keywords.\
Facilitates large-scale data collection while handling input files in manageable chunks.\

#### openbu
Automates interaction with the OpenBU discovery platform to extract publication data such as titles and abstracts.\
Uses Selenium to simulate user interactions for authors listed in an input file.


#### Model
-use tf-idf to vectorize all the abstact and title of the data for training and prediction.
-use logistic regression to train the model and adjust the parameters for better predictions


## Other Folders:
#### the detail of how to use the code are under each subfolders.
./OpenBu\
the code for scraping openBU data, in .ipynb format\
./googlescholar\
the code for scraping google scholar data, in .ipynb format, do **not** use google colab to run\
./model_prediction\
the code for training model and the do the training, in .ipynb format\
./webpage\
the code to open a webpage locally\

### refer to each folder for usage of code
