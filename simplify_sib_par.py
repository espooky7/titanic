#!/usr/bin/python

def import_data(path, filename):
	file_path = os.path.join(path, filename)
	data = pd.read_csv(file_path)

	return data


def greater_3(x):
	if x >= 3:
		x = 3

	return x


def greater_2(x):
	if x >= 2:
		x = 2

	return x


def clean_sibsp(data):
	data['SibSp_bin'] = data.SibSp
	data['SibSp_bin'] = data['SibSp_bin'].apply(greater_3)

	return data


def clean_parch(data):
	data['Parch_bin'] = data.Parch
	data['Parch_bin'] = data['Parch_bin'].apply(greater_2)

	return data


def reorder_cols(data):
	cols = ['PassengerId','title','age_bins','Pclass','Sex','Age','SibSp','SibSp_bin','Parch',\
	'Parch_bin','Ticket','Fare','Cabin','Embarked','Survived']
	data = data[cols]

	return data


def write_file(path, filename, data):
	file_path = os.path.join(path, filename)
	data.to_csv(file_path, index = False)

	return


def main():
	path = '/Users/emily.dahlberg/Documents/kaggle/titanic/'
	filename = 'train_ages_binned.csv'

	data = import_data(path, filename)

	data = clean_sibsp(data)
	data = clean_parch(data)

	data = reorder_cols(data)

	new_save_file = 'train_sibsp_binned.csv'
	write_file(path, new_save_file, data)


if __name__ == '__main__':
	import pandas as pd 
	import os

	main()