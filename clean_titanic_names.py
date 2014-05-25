def import_data(path, file_name):
	"""
	Import the data using a file path and file name. Path and name 
	defined in main().
	"""
	file_path = os.path.join(path, file_name)
	data = pd.read_csv(file_path)

	return data


def split_last(x):
	"""
	Specifically for titanic data - split the last name out the name column 
	"""
	split_string = x.split(',')
	last_name = split_string[0]
	last_name = last_name.strip(' ')

	return last_name


def split_title(x):
	"""
	Specifically for titanic data, split out the title from the name column.
	Will try using title in 
	"""
	remove_last = x.split(',')[1]
	title_first = remove_last.split('.')
	title = title_first[0]
	title = title.strip(' ')

	return title


def split_first(x):
	"""
	Pulls out first name (and any nicknames)
	"""
	remove_last = x.split(',')[1]
	title_first = remove_last.split('.')
	first_name = title_first[1]

	return first_name


def split_first_last(data):
	"""
	Applies the three functions above to the name column and creates
	new columns for first, last, and title. Deletes original name column
	and returns DataFrame
	"""
	#data['last_name'] = data['Name'].apply(split_last)
	data['title'] = data['Name'].apply(split_title)
	#data['first_name'] = data['Name'].apply(split_first)

	del data['Name']

	return data


def reorder_cols(data):
	cols = ['PassengerId','title','Pclass','Sex','Age','SibSp','Parch','Ticket',\
	'Fare','Cabin','Embarked','Survived']
	data = data[cols]

	return data


def write_file(data, path, filename):
	filepath = os.path.join(path, filename)
	data.to_csv(filepath, index = False)

	return


def main():
	path = '/Users/emily.dahlberg/Documents/kaggle/titanic/'
	file_name = 'train_original.csv'

	data = import_data(path, file_name)
	
	data = split_first_last(data)

	data = reorder_cols(data)

	save_new_data = 'train_names_removed.csv'
	write_file(data, path, save_new_data)


if __name__ == '__main__':
	import pandas as pd
	import os

	main()