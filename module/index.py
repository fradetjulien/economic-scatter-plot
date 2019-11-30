'''
Scatter plot builder
'''
import os
import csv
import random
import click
import matplotlib.pyplot as plt

def display_scatter(plt):
    '''
    Display the scatter with legend, label and title
    '''
    plt.title("Scatter Plot of GDP and Currency Value")
    plt.grid(True)
    plt.xlabel('GDP')
    plt.ylabel('Currency value')
    plt.show()

def fusion_data(tarif, gdp):
    '''
    Synchronize data from both files.
    '''
    try:
        for item in gdp:
            item.append(tarif[0][len(tarif[0]) - 1])
            tarif.pop(0)
    except:
        print("Can't synchronize data from both files.")
    return gdp

def check_to_start(line):
    '''
    Check if the readed line is metadata or data
    '''
    if "Country Name" in line and "Country Code" in line:
        return False
    return True

def get_data(file):
    '''
    Open and read the CSV file, then fill a list with the readed values
    '''
    waiting = True
    data = []
    with open(file, mode='r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONE)
        try:
            for row in reader:
                if not waiting:
                    data.append(row)
                else:
                    waiting = check_to_start(row)
        except csv.Error:
            print("Failed while opening and reading file.")
        finally:
            del reader
    return data

def builder(file_1, file_2):
    '''
    Build the final scatter plot
    '''
    data = fusion_data(get_data(file_1), get_data(file_2))
    i = 0
    while i < 10:
        random_value = random.randint(1, len(data) - 1)
        plt.scatter(data[random_value][2], data[random_value][3], label=data[random_value][0])
        i = i + 1
    display_scatter(plt)

def is_csv(file):
    '''
    Check if the file received in parameter is a correct CSV file
    '''
    if not file.endswith('.csv') or os.path.getsize(file) <= 0:
        print("Insert a correct CSV file please.")
        return False
    return True

@click.group()
def cli():
    '''
    Scatter Plot Builder
    '''

@cli.command('build')
@click.argument('file_1', type=click.Path(exists=True))
@click.argument('file_2', type=click.Path(exists=True))
def build_scatter_plot(file_1, file_2):
    '''
    Build a Scatter plot combining data
    '''
    if is_csv(file_1) and is_csv(file_2):
        builder(file_1, file_2)

if __name__ == '__main__':
    cli()
