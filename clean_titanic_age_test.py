
def import_data(path, filename):
	file_path = os.path.join(path, filename)
	data = pd.read_csv(file_path)

	return data


def bin_ages(data):
	bins = [0,10,16,25,40,60,np.inf]
	data['age_bins'] = pd.cut(data.Age, bins, labels = False)

	return data


def estimate_masters(data):
	"""
	Looking at the Master values with ages, they are all young boys. The mean age is 4, so
	binning these into the 0-10 group.
	"""
	data.ix[(data.title == 'Master') & (data.Age.isnull() == True), 'age_bins'] = 1

	return data


def estimate_mrs(data):
	"""
	Mean age of married women on the ship is 35, so binning them into the 25-40 group.
	"""
	data.ix[(data.title == 'Mrs') & (data.Age.isnull() == True), 'age_bins'] = 4

	return data


def estimate_alone(data):
	"""
	Making an assumption that anyone traveling alone is most likely not a child. Average age
	of passengers alone is 32, so 25-40 group.
	"""
	data.ix[(data.SibSp == 0) & (data.Parch == 0) & (data.Age.isnull() == True), 'age_bins'] = 4

	return data


def estimate_children(data):
	"""
	Assuming no one on the ship is married to more than one person, those with values >1 in
	Sib-spouse and at least 1 value for parent-children have a mean age 9, so binned in 0-10.
	"""
	data.ix[(data.SibSp > 1) & (data.Parch > 0) & (data.Age.isnull() == True), 'age_bins'] = 1
	return data


def estimate_miss(data):
	"""
	Assuming anyone on the ship with a 'Miss' title and > 0 for SibSp is a child. Mean age is 15
	for this group
	"""
	data.ix[(data.title == 'Miss') & (data.SibSp > 0) & (data.Age.isnull() == True), 'age_bins'] = 2
	return data


def estimate_men_not_alone(data):
	"""
	Remaining Null Age values are Mr. titles with > 0 SibSp value. Average age for this group is 31.
	"""
	data.ix[(data.title == 'Mr') & (data.SibSp > 0) & (data.Age.isnull() == True), 'age_bins'] = 4
	return data


def reorder_cols(data):
	cols = ['PassengerId','title','age_bins','Pclass','Sex','Age','SibSp','Parch','Ticket',\
	'Fare','Cabin','Embarked']
	data = data[cols]

	return data

def write_file(path, filename, data):
	file_path = os.path.join(path, filename)
	data.to_csv(file_path, index = False)

	return


def main():
	path = '/Users/emily.dahlberg/Documents/kaggle/titanic/'
	filename = 'test_names_removed.csv'

	data = import_data(path, filename)
	data = bin_ages(data)

	data = estimate_masters(data)
	data = estimate_mrs(data)
	data = estimate_alone(data)
	data = estimate_children(data)
	data = estimate_miss(data)
	data = estimate_men_not_alone(data)

	data = reorder_cols(data)

	new_save_file = 'test_ages_binned.csv'
	write_file(path, new_save_file, data)


if __name__ == '__main__':
	import pandas as pd
	import numpy as np
	import os

	main()