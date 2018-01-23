# Agile Data Cleaning
In this repo I describe how we could easily do basic data cleaning using:

1. Bash Commands-Shell Scripting
2. Python Scripts
3. The [Pandas](https://pandas.pydata.org) Library

My inspiration was a data cleaning proccess I implemented in order to create a data warehouse for data analysis and data mining.

## Context

* [Bash Commands](#bash_commands)
	1. [Merge multiple files to one file](#merge)
	2. [Create a table from a csv file](#create1)
	3. [Create a table with unique values of a column of a csv file](#create2)
	4. [Find duplicate ids](#duplicates)
* [Pandas Jupyter Notebooks](#pandas)
	1. [Add an id column](#add_id)
	2. [Create a Table from a specific column](#create3)
* [Python Scripts](#python)
	1. [Match Id](#match)

## <a name="bash_commands"></a>Bash Commands

### <a name="merge"></a>Merge multiple files to one file
Assume we have 20 csv files that we want to merge into one csv file. The file names are like: example_1.csv etc..

1. Create a new file with the first row (columns names) of our files:

	```bash
	head -1 example_1.csv > data.csv
	```
2. Remove the first row from all csv files:

	```bash
	for i in example_{1..20}.csv; do sed -i '' -e 1d $i; done
	```
3. Merge the files:

	```bash
	cat example_{1..20}.csv >> data
	```
4. Remove duplicates(identical rows):

	```bash
	cat data.csv > temp_data
	cat temp_data | sort -r | uniq > data.csv
	```

### <a name="create1"></a>Create a table from a csv file
Let's say we want to create a new table with the columns 2,3,5 of data.csv.

```bash
awk -F, {'OFS=",";print $2,$3,$5'} data.csv > table1.csv
```

### <a name="create2"></a>Create a table with unique values of a column of a csv file
Let's say you want to create a new table with the unique values of line 4 of data.csv.

```bash
cut -d ',' -f 4 data.csv | sort -r | uniq > table2.csv
```

### <a name="duplicates"></a>Find duplicate ids
We have a table (table3.csv) and we want to check if there are any duplicate ids (column 1).

1. To check if there are duplicates we must check if the two results are the same:

	```bash
	cut -d ',' -f 1 table3.csv | sort | uniq | wc -l
	cat table3.csv | sort | uniq | wc -l
	```
2.  If the results are the same then there aren't duplicates. If not then we use the below command to find the duplicates:

	```bash
	cut -d ',' -f 1 table3.csv | sort | uniq -c
	```

## <a name="pandas"></a>Pandas Jupyter Notebooks

### <a name="add_id"></a>Add an id column

* [add_id.ipynb](https://github.com/StefanosChaliasos/agile-data-cleaning/blob/master/jupyter-notebooks/add_id.ipynb)

### Create a Table from a specific column

* [create-date-table.ipynb](https://github.com/StefanosChaliasos/agile-data-cleaning/blob/master/jupyter-notebooks/create-date-table.ipynb)
* In our example we create a new table ([dates.csv](https://github.com/StefanosChaliasos/agile-data-cleaning/blob/master/dummy_data/dates.csv)) from the bday column of [data.csv](https://github.com/StefanosChaliasos/agile-data-cleaning/blob/master/dummy_data/data.csv). The columns of the new table are: id, month, year (we could also include a day column if we wanted to).

## <a name="python"></a>Python Scripts

### <a name="match"></a>Match

[match_ids.py](https://github.com/StefanosChaliasos/agile-data-cleaning/blob/master/python-scripts/match_ids.py)

* A python script that matches and changes the values of a column with another table's id.
* In our example we match the bday column of [data.csv](https://github.com/StefanosChaliasos/agile-data-cleaning/blob/master/dummy_data/data.csv) with a row of [dates.csv](https://github.com/StefanosChaliasos/agile-data-cleaning/blob/master/dummy_data/dates.csv) and then we update the bday column with the appropriate id.


## Contributing
* Any contribution that will enchance the current project is welcome.
* If you have any questions about this project you can open an issue.
* If you want to contribute to this project just create a pull request.

## Author
**[Stefanos Chaliasos](https://github.com/StefanosChaliasos)**

## Licence
This project is licensed under the GNU Lesser General Public License v3.0 Licence — see [LICENSE.md]() file for details.
