# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# + [code] deletable=false editable=false
# import and initialize otter
import otter
grader = otter.Notebook("p7.ipynb")

# + deletable=false editable=false
import p7_test

# +
# PLEASE FILL IN THE DETAILS
# Enter none if you don't have a project partner

# project: p7
# submitter: khamesra
# partner: svalecha@wisc.edu

# + [markdown] deletable=false editable=false
# # Project 7: Drinking Water Accessibility

# + [markdown] deletable=false editable=false
# ## Learning Objectives:
#
# In this project you will demonstrate how to:
#
# - Write programs to interpret data present in csv files,
# - Use lists and dictionaries effectively to manage data,
# - **Develop good coding styling habits (points may be deducted for bad coding styles)**

# + [markdown] deletable=false editable=false
# ## Testing your code:
#
# Along with this notebook, you must have downloaded the file `p7_test.py`. If you are curious about how we test your code, you can explore this file, and specifically the value of the variable `expected_json`, to understand the expected answers to the questions. You can have a look at [P2](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-s23-projects/-/tree/main/p2/p2.ipynb) if you have forgotten how to read the outputs of the `grader.check` function calls.

# + [markdown] deletable=false editable=false
# **Please go through [Lab-P7](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-s23-projects/-/tree/main/lab-p7) before starting this project.** The lab introduces some useful techniques necessary for this project.

# + [markdown] deletable=false editable=false
# <h2 style="color:red">Warning (Note on Academic Misconduct):</h2>
#
# Under any circumstances, **no more than two students are allowed to work together on a project** as mentioned in the course policies. If your code is flagged by our code similarity detection tools, **both partners will be responsible** for sharing/copying the code, even if the code is shared/copied by one of the partners with/from other non-partner student(s). Note that each case of plagiarism will be reported to the Dean of Students with a zero grade on the project. **If you think that someone cannot be your project partner then don’t make that student your lab partner.**

# + [markdown] deletable=false editable=false
# ## Project Description:
#
# Universal access to safe drinking water is a fundamental need and human right. Securing access for all would go a long way in reducing illness and death, especially among children. "Safely managed" drinking water services represent an ambitious new rung on the ladder used to track progress on drinking water. Since 2000, 2 billion people have gained access to safely managed services (i.e., accessible on-premises, available when needed, and free from contamination). In 2020, 5.8 billion people used safely managed services and a further 2 billion people used basic services. However, 771 million people still lacked even a basic level of service, including 282 million who used a “limited” water service (source from which water collection time exceeds 30 minutes), 367 million who used unimproved sources and 122 million who still collected drinking water directly from rivers, lakes, and other surface water sources. The data reveal pronounced disparities, with the poorest and those living in rural areas least likely to use a basic service. In most countries, the burden of water collection continues to fall mainly to women and girls.
#
# [The Unicef website](https://data.unicef.org/) states that "consistent, credible data about children’s situations are critical to the improvement of their lives – and indispensable to realizing the rights of every child." Data Scientists will play an important role in reaching this goal.
#
# For this project, you'll be analyzing data drawn from multiple sources. Our data is primarily drawn from the report titled ["Progress on Household Drinking Water, Sanitation and Hygiene"](https://washdata.org/sites/default/files/2021-07/jmp-2021-wash-households.pdf) data published by the Unicef/WHO Joint Monitoring Programme for Water Supply, Sanitation and Hygiene (2021). The original dataset can be found [here](https://data.unicef.org/topic/water-and-sanitation/drinking-water/) if you are interested in exploring the dataset yourself. Our dataset is further augmented by data from The World Bank on the [income levels of each country](https://datatopics.worldbank.org/world-development-indicators/the-world-by-income-and-region.html).

# + [markdown] deletable=false editable=false
# ## Dataset:
#
# The JMP report defines *people who have access to an [improved source of water](https://www.cdc.gov/healthywater/global/assessing.html#ImprovedDrinking) within 30 minutes round trip collection time* as having [at least basic access](https://www.cdc.gov/healthywater/global/assessing.html#DrinkingWaterSources) to water. For this project, we will focus on the **percentage of population** of each country who had **at least basic** water supply in the years **2015** and **2020**. Open `water_accessibility.csv` with Microsoft Excel or some other Spreadsheet viewer and look at the list of countries in the dataset. Data for each country appears twice, one row for the year *2015* and the other row for year *2020*. Countries which had incomplete data have been **omitted** from the dataset, and we will **ignore** those countries in this project. You do **not** have to deal with any **missing data** in the dataset.
#
# The data shows:
# - `country_code` : the unique country code that consists of three alphabet letters
# - `country_name` : the name of the country
# - `region` : the geographical location of the country (does not equal to its corresponding continents, but follows the administrative groupings from [The World Bank](https://datahelpdesk.worldbank.org/knowledgebase/articles/906519-world-bank-country-and-lending-groups))
# - `year` : the year in which it was subject to data collection
# - `income_level` : the classification of income level based on GNI per capita in US dollars ([The World Bank Atlas Method](https://datahelpdesk.worldbank.org/knowledgebase/articles/378834-how-does-the-world-bank-classify-countries))
# - `pop` : population of the country in a specific year (in thousands)
# - `urban_percent` : the percentage of population in a given country that is urban
# - `national_alb` : the percentage of a country's population that has access to at least basic water supply
# - `urban_alb` : the percentage of a country's urban population that has access to at least basic water supply

# + [markdown] deletable=false editable=false
# ## Project Requirements:
#
# You **may not** hardcode indices in your code, unless the question explicitly says so. If you open your `.csv` file with Excel, manually count through the rows and use this number to loop through the dataset, this is also considered as hardcoding. We'll **manually deduct** points from your autograder score on Gradescope during code review. You are **allowed** to assume that the dataset is ordered in such a way that the *even indices* (0, 2 .. etc;) corresponds to the rows with information for the year 2015, and the *odd indices* (1, 3 .. etc;) correspond to the rows with information for year 2020. Using this fact about the dataset will **not** be considered hardcoding.
#
# **Store** your final answer for each question in the **variable specified for each question**. This step is important because Otter grades your work by comparing the value of this variable against the correct answer.
#
# For some of the questions, we'll ask you to write (then use) a function to compute the answer. If you compute the answer **without** creating the function we ask you to write, we'll **manually deduct** points from your autograder score on Gradescope, even if the way you did it produced the correct answer. 
#
# Required Functions:
# - `cell`
# - `get_col_dict`
#
# In this project, you will also be required to define certain **data structures**. If you do not create these data structures exactly as specified, we'll **manually deduct** points from your autograder score on Gradescope, even if the way you did it produced the correct answer.
#
# Required Data Structures:
# - `dict_2015`
# - `dict_2020`
# - `rural_non_alb_bin_2015_dict`
# - `rural_non_alb_bin_2020_dict`
#     
# Students are only allowed to use Python commands and concepts that have been taught in the course prior to the release of p7. Therefore, **you should not use the pandas module**.  We will **manually deduct** points from your autograder score on Gradescope otherwise.
#
# For more details on what will cause you to lose points during code review and specific requirements, please take a look at the [Grading rubric](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-s23-projects/-/blob/main/p7/rubric.md).

# + [markdown] deletable=false editable=false
# ## Incremental Coding and Testing:
#
# You should always strive to do incremental coding. **Incremental coding enables you to avoid challenging bugs.** Always write a few lines of code and then test those lines of code, before proceeding to write further code. You can call the `print` function to test intermediate step outputs.
#
# We also recommend you do incremental testing: make sure to run the local tests as soon as you are done with a question. This will ensure that you haven't made a big mistake that might potentially impact the rest of your project solution. Please refrain from making multiple submissions on Gradescope for testing individual questions' answers. Instead use the local tests, to test your solution on your laptop.
#
# That said, it is **important** that you check the Gradescope test results as soon as you submit your project on Gradescope. Test results on Gradescope are typically available somewhere between 2 to 10 minutes after the submission.
#
# Also, remember to check with the [P7 rubric](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-s23-projects/-/blob/main/p7/rubric.md) to verify that you will not be losing any points during manual review.

# + [markdown] deletable=false editable=false
# ## Project Questions and Functions:

# + tags=[]
# it is considered a good coding practice to place all import statements at the top of the notebook
# please place all your import statements in this cell if you need to import any more modules for this project
import csv
import math


# + [markdown] deletable=false editable=false
# First, read the data stored in `water_accessibility.csv`. You **must** read the csv file and then get the header and rows (and store them into `csv_header` and `csv_rows` variables). You will **lose points** if you use any other names to store these variables.

# + tags=[]
# read the data stored in water_accessibility.csv
def process_csv(filename):
    example_file = open(filename, encoding="utf-8")
    example_reader = csv.reader(example_file)
    example_data = list(example_reader)
    example_file.close()
    return example_data
# read the data in "water_accessibility.csv"
csv_data = process_csv("water_accessibility.csv")

# split the header and other rows into appropriate variables
csv_header = csv_data[0]
csv_rows = csv_data[1:]

print(csv_header)
print(csv_rows[0:2])


# + [markdown] deletable=false editable=false
# ### Function 1: `cell(row_idx, col_name)` 
#
# This function must take in a row index, `row_idx` and a column name, `col_name` as its inputs, and return the value in `water_accessibility.csv` stored there. There is **no missing data** in this dataset.
#
# You **must** define the variables `csv_header` and `csv_rows` as in Lab-P7, and you **must** copy/paste your `cell` function from Lab-P7.
#
# **Important:** You **must** only use the `cell` function to extract data from the dataset. If you extract any data without explicitly using this function, you will **lose points** during manual review. Moreover, your `cell` function **must** handle typecasting all columns and multiplying the population (`pop`) by *1000*. You will **lose points** if you perform these steps outside the `cell` function.

# + tags=[]
# define the cell function here
def cell(row_idx, col_name):
    col_idx = csv_header.index(col_name)
    val = csv_rows[row_idx][col_idx]
    if col_name == "pop" :
        return int(val) * 1000
    elif col_name =='urban_alb' or col_name == "national_alb" or col_name == "urban_percent" or col_name == "year":
        return int(val)
    return val 


# + [markdown] deletable=false editable=false
# After you define the function `cell`, run the following two cells to test whether it works.

# + tags=[]
cell_test1 = cell(0, 'country_name')
cell_test2 = cell(1, 'year')
cell_test3 = cell(2, 'urban_percent')
cell_test4 = cell(3, 'urban_alb')
cell_test5 = cell(4, 'income_level')
cell_test6 = cell(5, 'pop')

# + deletable=false editable=false
grader.check("cell_test")

# + [markdown] deletable=false editable=false
# You are all set! You are now ready to start solving the questions.

# + [markdown] deletable=false editable=false
# **Question 1:** Which country had the highest population (`pop`) in *2020*?

# + tags=[]
# compute and store the answer in the variable 'highest_pop_country', then display it
value = 0
pop = 0
for value in range(len(csv_rows)):
    count_name = cell(value , "country_name")
    high_pop = cell(value, "pop")
    year_pop = cell(value , "year")
    if year_pop == 2020 and high_pop > pop :
        pop = high_pop
        highest_pop_country = count_name
    else :
        continue

highest_pop_country       



# + deletable=false editable=false
grader.check("q1")

# + [markdown] deletable=false editable=false
# **Question 2:** Which country had the highest population (`pop`) **increase** between *2015* and *2020*?
#
# There is a **unique** country in this dataset whose population increased the most. You **do not** have to worry about ties.
#
# **Hint:** Recall how to loop through the dataset and extract data from each year from [Lab-P7](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-s23-projects/-/tree/main/lab-p7).

# + tags=[]
# compute and store the answer in the variable 'highest_pop_inc_country', then display it
highest_pop = 0
for value in range(0, len(csv_rows), 2):
    value_2015 = value
    value_2020 = value + 1
    increase_pop = (cell(value_2020 , "pop") - cell(value_2015, "pop"))
    count_name = cell(value , "country_name")
    if increase_pop > highest_pop :
        highest_pop = increase_pop
        highest_pop_inc_country = count_name
    else :
        continue
highest_pop_inc_country


# + deletable=false editable=false
grader.check("q2")

# + [markdown] deletable=false editable=false
# **Question 3:** Which country had the highest **increase** in at least basic (`national_alb`) water supply between the years of *2015* and *2020*? 
#
# There is a **unique** country in this dataset whose `national_alb` value increased the most. You **do not** have to worry about ties.
#
# **Hint:** Take a look at q7 in Lab-P7 to see how to compute the change in `national_alb` between *2015* and *2020* for each country.

# + tags=[]
# compute and store the answer in the variable 'highest_nat_alb_inc_country', then display it
highest_alb = 0
for value in range(0, len(csv_rows), 2):
    value_2015 = value
    value_2020 = value + 1
    increase_alb = (cell(value_2020 , "national_alb") - cell(value_2015, "national_alb"))
    count_name = cell(value , "country_name")
    if increase_alb > highest_alb :
        highest_alb = increase_alb
        highest_nat_alb_inc_country = count_name
    else :
        continue
highest_nat_alb_inc_country

# + deletable=false editable=false
grader.check("q3")

# + [markdown] deletable=false editable=false
# **Question 4:** What was the `income_level` in *2020* of the country with the highest increase in at least basic (`national_alb`) water supply between *2015* and *2020*?
#
# You **must** not repeat your computation here. Instead modify your code for q3 to extract the correct index, and use that to answer this question.

# + tags=[]
# compute and store the answer in the variable 'highest_alb_inc_income_level', then display it
highest_alb = 0
for value in range(0, len(csv_rows), 2):
    value_2015 = value
    value_2020 = value + 1
    increase_alb = (cell(value_2020 , "national_alb") - cell(value_2015, "national_alb"))
    income_value = cell(value , "income_level")
    if increase_alb > highest_alb :
        highest_alb = increase_alb
        highest_alb_inc_income_level = income_value
        
    else :
        continue
highest_alb_inc_income_level

# + deletable=false editable=false
grader.check("q4")

# + [markdown] deletable=false editable=false
# **Question 5:** What is the **total** population (`pop`) of **all** the countries (in the dataset) in the `year` *2015*?
#
# The `pop` column stores the population in thousands. Your `cell` function already multiplies the value in this column by *1000*, so you can directly use the value returned by `cell` as the population of the country.

# + tags=[]
# compute and store the answer in the variable 'total_pop_2015', then display it
total_pop = 0
for value in range(len(csv_rows)):
    year_value = cell(value, "year")
    if year_value == 2015:
        pop_value = cell(value, "pop")
        total_pop += pop_value
total_pop_2015 = total_pop
total_pop_2015

# + deletable=false editable=false
grader.check("q5")
# -



# + [markdown] deletable=false editable=false
# **Question 6:** What was the global **percentage** of urban population (`urban_percent`) across **all** countries (in the dataset) in the `year` *2015*?
#
# You need to find the **total** urban population by *multiplying* the `pop` and `urban_percent` columns of each country and *adding* this up (the urban population). Then you need to *divide* by the **total** population to get the percentage of urban population across all the countries.
#
# Your output **must** be an **int**. You **must** use the `round` function to round your answer to the nearest integer.

# + tags=[]
# compute and store the answer in the variable 'urban_pop_percent_2015', then display it
total_pop = 0 
urban_pop = 0
urban_pop_percent_2015 = 0
for value in range(len(csv_rows)):
    year_value = cell(value , "year")
    if year_value == 2015 :
        pop_value = cell(value, "pop")
        urban_value = cell(value , "urban_percent")
        total_pop += pop_value
        urban_pop += pop_value * urban_value
    
urban_pop_percent_2015 = round(urban_pop/total_pop)
urban_pop_percent_2015   

# + deletable=false editable=false
grader.check("q6")

# + [markdown] deletable=false editable=false
# **Question 7:** What was the **total** population (`pop`) of countries that were in the *High income* group (`income_level`) in the `year` *2020*?
#
# Your output **must** be an **int**.

# + tags=[]
# compute and store the answer in the variable 'high_income_pop', then display it
high_income_pop = 0 
for value in range(len(csv_rows)):
    income_value = cell(value , "income_level")
    year_value = cell(value , "year")
    if income_value == 'High income' and year_value == 2020 :
        pop_value = cell(value,"pop")
        high_income_pop += pop_value
high_income_pop

# + deletable=false editable=false
grader.check("q7")

# + [markdown] deletable=false editable=false
# **Question 8:** Which *income group* (`income_level`) had the **least** population (`pop`) in the `year` *2015*?
#
# You must find the **total** population (`pop`) for each `income_level`, and find the `income_level` which has the **least** total population.
#
# **Hint:** There are several ways to solve this problem efficiently (including using `dicts`). You can try to solve this problem using dicts if you want to. However, another approach that you might already be familiar with from p6 is to first create a *list* of all the **unique** income levels, and then loop through the entire dataset for **each** income level to find the total population of that income level, before comparing these numbers to find the income level with the least population.

# + tags=[]
# compute and store the answer in the variable 'least_pop_income_group', then display it
list_income_level = []
value_min = 0
lowest_pop = 0
total_pop = 0 
for value in range(len(csv_rows)):
    year_value = cell(value,'year')
    if year_value == 2015:
        income_value = cell(value,'income_level')
        list_income_level.append(income_value)
        total_pop += cell(value,"pop")
        if total_pop > lowest_pop:
            lowest_pop = total_pop
            value_min = value
    
least_pop_income_group = cell(value_min , "income_level")
least_pop_income_group

# + deletable=false editable=false
grader.check("q8")

# + [markdown] deletable=false editable=false
# **Question 9:** Create a **list** of the names (`country_name`) of all countries in the *North America* `region` that **tied** for the **maximum** `national_alb` in *2015* (in *North America*).
#
# You need to first find the **maximum** value of `national_alb` among all countries in the `region` *North America*, and then make a `list` of **all** the countries in this region having this `national_alb` value. **Multiple** countries from *North America* have the same maximum `national_alb` value, so your output **must** be a `list` of **all** those countries.

# + tags=[]
# compute and store the answer in the variable 'na_max_alb_countries', then display it
names_of_country = []
max_value = 0
max_alb = 0
na_max_alb_countries = []
for value in range(len(csv_rows)):
    region_value = cell(value,'region')
    year_value = cell(value,'year')
    if region_value == 'North America' and year_value == 2015:
        name_value = cell(value, 'country_name')
        names_of_country.append(name_value)
        nat_alb_value = cell(value,'national_alb')
        if nat_alb_value > max_alb:
            nat_alb_value = max_alb
            max_value = value
            na_max_alb_countries.append(cell(max_value, "country_name"))
na_max_alb_countries

# + deletable=false editable=false
grader.check("q9")


# + [markdown] deletable=false editable=false
# ### Function 2: `get_col_dict(col_name, year)` 
#
# This function should take in a column `col_name` and a `year` (*2015* or *2020*) as its inputs, and return a `dict` where each key is a `country_code` and the corresponding value is the value under the given `col_name` for the country with the said `country_code` in the given `year`.
#
# For example, the value returned by `get_col_dict('country_name', 2015)` should be something like the following:
# ```python
# {'AFG': 'Afghanistan',
#  'ALB': 'Albania',
#  'DZA': 'Algeria',
#  'AND': 'Andorra',
#  'AGO': 'Angola',
#  'ARM': 'Armenia',
#  'AUS': 'Australia',
#  'AUT': 'Austria',
#  'AZE': 'Azerbaijan',
#  'BGD': 'Bangladesh',
#  ...
# }
# ```
#
# and the value returned by `get_col_dict('pop', 2020)` should be something like the following:
# ```python
# {'AFG': 38928000,
#  'ALB': 2878000,
#  'DZA': 43851000,
#  'AND': 77000,
#  'AGO': 32866000,
#  'ARM': 2963000,
#  'AUS': 25500000,
#  'AUT': 9006000,
#  'AZE': 10139000,
#  'BGD': 164689000,
#  ...
# }
# ```
#
# Start with the following code snippet and complete the function.

# + tags=[]
# replace the ... with your code

def get_col_dict(col_name, year):
    col_dict = {}
    if year == 2015:
        for idx in range (0, len(csv_rows), 2):
            col_dict[cell(idx, "country_code")] =  cell(idx, col_name)
    elif year == 2020:
        for idx in range (1, len(csv_rows), 2):
            col_dict[cell(idx, "country_code")] = cell(idx, col_name)
    return col_dict


# + [markdown] deletable=false editable=false
# After you define the function `get_col_dict`, run the following two cells to test whether it works.

# + tags=[]
get_col_dict_test1 = get_col_dict('region', 2020)
get_col_dict_test2 = get_col_dict('national_alb', 2015)
get_col_dict_test3 = get_col_dict('pop', 2020)

# + deletable=false editable=false
grader.check("get_col_dict")

# + [markdown] deletable=false editable=false
# ### Data Structures 1: `dict_2015`
#
# You must now create a data structure named `dict_2015`. This data structure must be a **dict**. Each key must be a `country_code`, and the corresponding value must be another **dict**. As for the inner dictionary, the keys must be the various column names, and the values must be the values under the column name for `country_code` in the `year` *2015*.
#
# The keys for each of the *inner* dictionary are the column names:
# - `'country_name'`
# - `'region'`
# - `'income_level'`
# - `'year'`
# - `'pop'`
# - `'urban_percent'`
# - `'national_alb'`
# - `'urban_alb'`
#
# You are **allowed** to *hardcode* the **names** of all these columns (i.e., the keys of the *inner* dictionaries).
#
# The data structure `dict_2015` should look something like this:
# ```python
# {'AFG': {'country_name': 'Afghanistan',
#   'region': 'South Asia',
#   'income_level': 'Low income',
#   'year': 2015,
#   'pop': 34414000,
#   'urban_percent': 25,
#   'national_alb': 61,
#   'urban_alb': 87},
#  'ALB': {'country_name': 'Albania',
#   'region': 'Europe & Central Asia',
#   'income_level': 'Upper middle income',
#   'year': 2015,
#   'pop': 2891000,
#   'urban_percent': 57,
#   'national_alb': 93,
#   'urban_alb': 95},
#   ...
# }
# ```

# + tags=[]
# define the variable 'dict_2015' here as described above
# you may display the variable for testing purposes while you define it,
# BUT you MUST remove the line displaying 'dict_2015' before submission as the output will be too large to display

# initialize as an empty dictionary
dict_2015 = {}
country_dict = get_col_dict('country_name', 2015)
region_dict = get_col_dict('region', 2015)
income_level_dict = get_col_dict('income_level', 2015)
year_dict = get_col_dict('year', 2015)
pop_dict = get_col_dict('pop', 2015)
urban_percent_dict = get_col_dict('urban_percent', 2015)
national_alb_dict = get_col_dict('national_alb', 2015)
urban_alb_dict = get_col_dict('urban_alb', 2015)

# call get_col_dict for other columns
for value in range(len(csv_rows)):
    country_code = cell(value, "country_code")
    dict_2015[country_code] = {}
    dict_2015[country_code]["country_name"] = country_dict[country_code]
    dict_2015[country_code]["region"] = region_dict[country_code]
    dict_2015[country_code]["income_level"] = income_level_dict[country_code]
    dict_2015[country_code]["year"] = year_dict[country_code]
    dict_2015[country_code]["pop"] = pop_dict[country_code]
    dict_2015[country_code]["urban_percent"] = urban_percent_dict[country_code]
    dict_2015[country_code]["national_alb"] = national_alb_dict[country_code]
    dict_2015[country_code]["urban_alb"] = urban_alb_dict[country_code]
    
# add data from all these dicts to dict_2015

# + [markdown] deletable=false editable=false
# After you define the data structure `dict_2015`, run the following cell to test whether you have defined it properly.

# + deletable=false editable=false
grader.check("dict_2015")

# + [markdown] deletable=false editable=false
# ### Data Structures 2: `dict_2020`
#
# You must now create a data structure named `dict_2020`. This data structure must be a **dict**. Each key must be a `country_code`, and the corresponding value must be another **dict**. As for the inner dictionary, the keys must be the various column names, and the values must be the values under the column name for `country_code` in the `year` *2020*.
#
# The keys for each of the *inner* dictionary are the column names:
# - `'country_name'`
# - `'region'`
# - `'income_level'`
# - `'year'`
# - `'pop'`
# - `'urban_percent'`
# - `'national_alb'`
# - `'urban_alb'`
#
# You are **allowed** to *hardcode* the **names** of all these columns (i.e., the keys of the *inner* dictionaries).

# + tags=[]
# define the variable 'dict_2020' here as described above
# you may display the variable for testing purposes while you define it,
# BUT you MUST remove the line displaying 'dict_2020' before submission as the output will be too large to display
dict_2020 = {}

country_dict = get_col_dict('country_name', 2020)
region_dict = get_col_dict('region', 2020)
income_level_dict = get_col_dict('income_level', 2020)
year_dict = get_col_dict('year', 2020)
pop_dict = get_col_dict('pop', 2020)
urban_percent_dict = get_col_dict('urban_percent', 2020)
national_alb_dict = get_col_dict('national_alb', 2020)
urban_alb_dict = get_col_dict('urban_alb', 2020)
for value in range(len(csv_rows)):
    country_code = cell(value, "country_code")
    dict_2020[country_code] = {}
    dict_2020[country_code]["country_name"] = country_dict[country_code]
    dict_2020[country_code]["region"] = region_dict[country_code]
    dict_2020[country_code]["income_level"] = income_level_dict[country_code]
    dict_2020[country_code]["year"] = year_dict[country_code]
    dict_2020[country_code]["pop"] = pop_dict[country_code]
    dict_2020[country_code]["urban_percent"] = urban_percent_dict[country_code]
    dict_2020[country_code]["national_alb"] = national_alb_dict[country_code]
    dict_2020[country_code]["urban_alb"] = urban_alb_dict[country_code]

# + [markdown] deletable=false editable=false
# After you define the data structure `dict_2020`, run the following cell to test whether you have defined it properly.

# + deletable=false editable=false
grader.check("dict_2020")

# + [markdown] deletable=false editable=false
# #### From this point onwards, you are only allowed to access data from `water_accessibility.csv` by querying from the **dicts** `dict_2015` and `dict_2020`. You will **lose points** during manual review if you access the data through any other means (inlcuding calling the `cell` function).

# + [markdown] deletable=false editable=false
# **Question 10:** Output the data from *China* (`country_code`: *CHN*) for the `year` *2020*.
#
# Your output **must** be a **dict** mapping each column name to the value for the country *CHN* in the year *2020*. You **must** answer this by querying data from `dict_2020`.
#
# The expected output is:
# ```python
# {'country_name': 'China',
#  'region': 'East Asia & Pacific',
#  'income_level': 'Upper middle income',
#  'year': 2020,
#  'pop': 1463141000,
#  'urban_percent': 62,
#  'national_alb': 94,
#  'urban_alb': 97}
# ```

# + tags=[]
# compute and store the answer in the variable 'chn_2020_dict', then display it
chn_2020_dict = dict_2020['CHN']
chn_2020_dict

# + deletable=false editable=false
grader.check("q10")

# + [markdown] deletable=false editable=false
# **Question 11:** What is the national at least basic (`national_alb`) water supply for *Nepal* (`country_code`: *NPL*) in the `year` *2015*?

# + tags=[]
# compute and store the answer in the variable 'npl_national_alb_2015', then display it
npl_national_alb_2015 = dict_2015['NPL']['national_alb']
npl_national_alb_2015

# + deletable=false editable=false
grader.check("q11")

# + [markdown] deletable=false editable=false
# **Question 12:** How much did the population (`pop`) of *Finland* **increase** (`country_code`: *FIN*) from the `year` *2015* to *2020*?

# + tags=[]
# compute and store the answer in the variable 'population_change_fin', then display it
population_change_fin = dict_2020['FIN']["pop"] - dict_2015['FIN']['pop']
population_change_fin

# + deletable=false editable=false
grader.check("q12")

# + [markdown] deletable=false editable=false
# **Question 13:** For each `income_level`, find the **total** population (`pop`) of all countries within that `income_level` in *2020*.
#
# Your output **must** be a **dict** where each key is a `income_level`, and the corresponding value is the **sum** of populations (`pop`) of all the countries from that `income_level` in the `year` *2020*.

# + tags=[]
# compute and store the answer in the variable 'income_level_pops', then display it
income_level_pops = {}
list_of_income_level = []

for key in dict_2020: 
    income_level = dict_2020[key]["income_level"]
    if income_level not in list_of_income_level: 
        list_of_income_level.append(income_level)

for level_of_income in list_of_income_level: 
    total_population = 0 
    for key in dict_2020: 
        if dict_2020[key]['income_level'] == level_of_income: 
            total_population += dict_2020[key]['pop']
        income_level_pops[level_of_income] = total_population

income_level_pops


# + deletable=false editable=false
grader.check("q13")

# + [markdown] deletable=false editable=false
# **Question 14:** For each `income_level`, find the **total** population (`pop`) of all countries who have access to at least basic water supply within that `income_level` in *2020*.
#
# Your output **must** be a **dict** where each key is a `income_level`, and the corresponding value is the **sum** of populations (`pop`) which have access to at least basic water supply of all the countries from that `income_level` in the `year` *2020*.
#
# You **must** round the population of **each** country with access to at least basic water supply to the **nearest** integer **before** adding them up.
#
# **Hint:** For each country, the population with at least basic water supply is `pop * national_alb / 100`. 

# + tags=[]
# compute and store the answer in the variable 'income_level_alb_pops', then display it
income_level_alb_pops = {}
list_of_income_level = []

for key in dict_2020: 
    if dict_2020[key]["income_level"] not in list_of_income_level: 
        list_of_income_level.append(dict_2020[key]["income_level"])

for level_of_income in list_of_income_level: 
    total_albanian_population = 0 
    for key in dict_2020: 
        if dict_2020[key]['income_level'] == level_of_income: 
            total_albanian_population += dict_2020[key]['pop'] * dict_2020[key]['national_alb'] / 100
        income_level_alb_pops[level_of_income] = round(total_albanian_population)

income_level_alb_pops


# + deletable=false editable=false
grader.check("q14")

# + [markdown] deletable=false editable=false
# **Question 15:** For each `income_level`, find the **percentage** of population (`pop`) of all countries within that `income_level` with at least basic water supply in *2020*.
#
# Your output **must** be a **dict** where each key is a `income_level`, and the corresponding value is the **percentage** of the population (`pop`) which have access to at least basic water supply of all the countries from that `income_level` in the `year` *2020*. The percentages **must** be represented as **int**s between *0* and *100*. You **must** round each of the percentages to the **nearest** integer.
#
# **Hint:** You need to loop through the dictionary you found in Q13 (or Q14), and for each key, you need to divide the corresponding value in the Q14 dictionary by the value of the same key in the Q13 dictionary and multiply by 100. Take another look at Task 3.6 from Lab-P7, if you are not sure how to proceed here.

# + tags=[]
# compute and store the answer in the variable 'income_level_alb_percent', then display it
income_level_alb_percent = {}
for key in income_level_pops:
    if income_level_pops[key] != 0:
        percentage_albanian = (income_level_alb_pops[key] / income_level_pops[key]) * 100
        income_level_alb_percent[key] = round(percentage_albanian)
    else:
        income_level_alb_percent[key] = 0
income_level_alb_percent


# + deletable=false editable=false
grader.check("q15")

# + [markdown] deletable=false editable=false
# ### Data Structure 3: Adding `rural_alb`  to `dict_2015` and `dict_2020`
#
# Our dataset has data on the percentage of **national** and **urban** populations with at least basic water supply. However, it is usually **rural** populations which have the greatest difficulty in getting access to water.
#
# Luckily, we are able to calculate **rural_alb** from the given data using the formula:
#
# $$
# rural_{alb} = \frac{national_{alb} - \left(urban_{alb} \times \frac{urban\_percent}{100}\right)}{\left(1 - \frac{urban\_percent}{100}\right)}
# $$
#
# *If a country has `urban_percent` equal to `100`, then the country has a negligible rural population, and the formula above is not valid. For such countries, we will assume that `rural_alb` is the **same** as `urban_alb`.*
#
# You **must** loop through each country in `dict_2015` and `dict_2020`, and add an **additional** key value pair for each country. The new key should be the string: `"rural_alb"`, and the corresponding value should be the `rural_alb` value for that country as given by the formula above. You **must** round each number to the **nearest** integer.

# + tags=[]
# add the additional key-value pair to both dicts 'dict_2015' and 'dict_2020' here
# you may display the variable for testing purposes while you define it,
# BUT you MUST remove the line displaying the dicts before submission as the output will be too large to display
for key in dict_2015:
    urban_percent = dict_2015[key]["urban_percent"]
    national_alb = dict_2015[key]["national_alb"]
    urban_alb = dict_2015[key]["urban_alb"]
    if urban_percent == 100:
        dict_2015[key]["rural_alb"] = urban_alb
    else:
        rural_alb = round((national_alb - (urban_alb * urban_percent/ 100)) / (1 - urban_percent/100))
        dict_2015[key]["rural_alb"] = rural_alb

for key in dict_2020:
    urban_percent = dict_2020[key]["urban_percent"]
    national_alb = dict_2020[key]["national_alb"]
    urban_alb = dict_2020[key]["urban_alb"]
    if urban_percent == 100:
        dict_2020[key]["rural_alb"] = urban_alb
    else: 
        rural_alb = round((national_alb - (urban_alb * urban_percent/100)) / (1- urban_percent/100))
        dict_2020[key]["rural_alb"] = rural_alb


# + [markdown] deletable=false editable=false
# Run the following cell to test whether you have correctly updated the two data structures.

# + deletable=false editable=false
grader.check("ds3")

# + [markdown] deletable=false editable=false
# **Question 16:** What's the percentage of rural population with at least basic (`rural_alb`) water supply in *Zimbabwe* (`country_code`: *ZWE*) in *2020*? 
#
# You **must** answer this question by querying data from the dict `dict_2020`.

# + tags=[]
# compute and store the answer in the variable 'zimbabwe_rural_alb_2020', then display it
zimbabwe_rural_alb_2020 = dict_2020['ZWE']['rural_alb']
zimbabwe_rural_alb_2020

# + deletable=false editable=false
grader.check("q16")

# + [markdown] deletable=false editable=false
# ### Data Structure 4: `rural_non_alb` bins
#
# We have now managed to extract the percentage of rural population with access to atleast basic water supply for each of the countries in the dataset. We can now use this information to find out the countries whose rural populations do **not** have access to at least basic water supply.
#
# You **must** create two **dict**s (one for the `year` *2015* and one for *2020*) where the keys are the integers *0*, *10*, *20*, ..., *100*. The value corresponding to the integer *0* **must** be a **list** containing the names of all the countries for which their rural population **without** access to at least basic (which we can represent as `rural_non_alb`) water supply is `0 <= rural_non_alb < 10`. Similarly, the value corresponding to the key *10* must be a **list** of all countries for which `10 <= rural_non_alb < 20`, and so on.
#
# **Hints:**
# 1. You can find `rural_non_alb` as `rural_non_alb = 100 - rural_alb`.
# 2. You can find the bin which any country falls into by using the formula:
# ```python
# rural_non_alb_bin = ((100 - rural_alb)//10) * 10
# ```
# 3. Even if a particular bin has no countries in it, you **must** still create a bin for it in your dict (with the value being an empty list). The starter code below will help you accomplish this.

# + tags=[]
# compute and store the answer in the variable 'rural_non_alb_bin_2015_dict'

# initialize as an empty dictionary
rural_non_alb_bin_2015_dict = {}

# loop through the keys we want for the dictionary - 0, 10, 20, ..., 100 (inclusive of 100)
# and add them to the dictionary as keys with the value as an empty list
for rural_non_alb_bin in range(0, 101, 10):
    rural_non_alb_bin_2015_dict[rural_non_alb_bin] = []
for key in dict_2015:
    non_rural_alb =100 - dict_2015[key]["rural_alb"]
    for idx in rural_non_alb_bin_2015_dict:
        if idx <= non_rural_alb < idx + 10:
            rural_non_alb_bin_2015_dict[idx].append(dict_2015[key]["country_name"])

# loop through each country and add to the correct bin of rural_non_alb_bin_2015_dict
rural_non_alb_bin_2015_dict


# + tags=[]
# compute and store the answer in the variable 'rural_non_alb_bin_2020_dict'
rural_non_alb_bin_2020_dict = {}

# initialize the dictionary keys with an empty list
for rural_non_alb_bin in range(0, 101, 10):
    rural_non_alb_bin_2020_dict[rural_non_alb_bin] = []

# populate the dictionary with country names falling into each rural_non_alb_bin
for key in dict_2020:
    non_rural_alb = 100 - dict_2020[key]["rural_alb"]
    for rural_non_alb_bin in rural_non_alb_bin_2020_dict:
        if rural_non_alb_bin <= non_rural_alb < rural_non_alb_bin + 10:
            rural_non_alb_bin_2020_dict[rural_non_alb_bin].append(dict_2020[key]["country_name"])

rural_non_alb_bin_2020_dict


# + [markdown] deletable=false editable=false
# After you define the data structures `rural_non_alb_bin_2015_dict` and `rural_non_alb_bin_2020_dict`, run the following cell to test whether you have defined them properly.

# + deletable=false editable=false
grader.check("rural_non_alb_bins")

# + [markdown] deletable=false editable=false
# **Question 17:** List all the countries which had `rural_non_alb` value between *20* and *29* (both inclusive) in the `year` *2015*.
#
# You **must** answer this question by querying the the **dict** `rural_non_alb_bin_2015_dict`.

# + tags=[]
# compute and store the answer in the variable 'bin_20_countries', then display it
bin_20_countries = rural_non_alb_bin_2015_dict[20]
bin_20_countries

# + deletable=false editable=false
grader.check("q17")

# + [markdown] deletable=false editable=false
# **Question 18:** What are the countries in the **last** non-empty bin in the `year` *2020*?
#
# Your output **must** be a **list** of the countries in the bin with the **highest** percentage of rural population without at least basic access to water.
#
# **Hint:** You must first find the largest key of the **dict** `rural_non_alb_bin_2020_dict` with a non-empty bin, and then find the value of that key.

# + tags=[]
# compute and store the answer in the variable 'last_non_empty_bin_2020', then display it
max_key = None
for key in rural_non_alb_bin_2020_dict:
    if rural_non_alb_bin_2020_dict[key] != []:
        if max_key == None or key > max_key:
            max_key = key
            
last_non_empty_bin_2020 = rural_non_alb_bin_2020_dict[max_key]

last_non_empty_bin_2020


# + deletable=false editable=false
grader.check("q18")

# + [markdown] deletable=false editable=false
# **Question 19:** What countries have **regressed** by moving to a **higher** bin from *2015* to *2020*?
#
# Your answer **must** be a **list** of countries which have regressed by having their percentage of rural population without at least basic access to water move to a bin with a **higher** key.
#
# **Hint:** There are many ways of solving this question. Here are a few:
# 1. You could create a new dictionary by swapping the keys and values of `rural_non_alb_bin_2015_dict` (and similarly `rural_non_alb_bin_2020_dict`), and use these dictionaries to determine the countries that have regressed.
# 2. You could create a nested loop to go through all possible combinations of keys in both the dictionaries `rural_non_alb_bin_2015_dict` and `rural_non_alb_bin_2020_dict`.
# 3. You could loop through all the countries and directly query from `dict_2015` and `dict_2020` to determine which of them have regressed.

# + tags=[]
# compute and store the answer in the variable 'countries_regressed', then display it
countries_regressed = []
for key in dict_2015:
    country = dict_2015[key]["country_name"]
    in_2015 = 0
    in_2020 = 0
    for j in rural_non_alb_bin_2015_dict:
        if country in rural_non_alb_bin_2015_dict[j]:
            in_2015 = j
    for l in rural_non_alb_bin_2020_dict:
        if country in rural_non_alb_bin_2020_dict[l]:
            in_2020 = l
    if in_2020 > in_2015:
        countries_regressed.append(country)
countries_regressed

# + deletable=false editable=false
grader.check("q19")

# + [markdown] deletable=false editable=false
# **Question 20:** What countries have **improved** by moving to a **lower** bin from *2015* to *2020*?
#
# Your answer **must** be a **list** of countries which have improved by having their percentage of rural population without at least basic access to water move to a bin with a **lower** key.

# + tags=[]
# compute and store the answer in the variable 'countries_improved', then display it
countries_improved = []
for key in dict_2015:
    country = dict_2015[key]["country_name"]
    in_2015 = 0
    in_2020 = 0
    for bin_2015 in rural_non_alb_bin_2015_dict:
        if country in rural_non_alb_bin_2015_dict[bin_2015]:
            in_2015 = bin_2015
    for bin_2020 in rural_non_alb_bin_2020_dict:
        if country in rural_non_alb_bin_2020_dict[bin_2020]:
            in_2020 = bin_2020
    if in_2020 < in_2015:
        countries_improved.append(country)

countries_improved


# + deletable=false editable=false
grader.check("q20")

# + [markdown] deletable=false editable=false
# ## Submission
# It is recommended that at this stage, you Restart and Run all Cells in your notebook.
# That will automatically save your work and generate a zip file for you to submit.
#
# **SUBMISSION INSTRUCTIONS**:
# 1. **Upload** the zipfile to Gradescope.
# 2. Check **Gradescope otter** results as soon as the auto-grader execution gets completed. Don't worry about the score showing up as -/100.0. You only need to check that the test cases passed.

# + [code]
# running this cell will create a new save checkpoint for your notebook
from IPython.display import display, Javascript
display(Javascript('IPython.notebook.save_checkpoint();'))

# + [code] deletable=false editable=false
# !jupytext --to py p7.ipynb

# + [code] deletable=false editable=false
p7_test.check_file_size("p7.ipynb")
grader.export(pdf=False, run_tests=True, files=["p7.py"])

# + [markdown] deletable=false editable=false
#  
