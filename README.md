# DataManager

Command-line Python script to format data for CitationDB app.

## Overview

The CitationDB relies on specially-formatted [JSON](http://www.json.org/) data in order to function. JSON is good for computers but not easy for people to edit. 

This tool converts the JSON files to a spreadsheet format called [CSV](https://en.wikipedia.org/wiki/Comma-separated_values), which stands for "comma-separated values" and then converts those files back to JSON when you're done editing the spreadsheets.

Additionally, this tool can download all four required spreadsheets from URLs contained in a specially formatted file.

## Setup

To set up this application, download this repository using:

    $ git clone this-directory-url

Then, move into the folder you just downloaded, like this:

    $ cd ./this-directory-name

Set up a virtual environment so we can install the dependencies:

    $ python3 -m venv venv
    $ ./venv/bin/activate
    $ pip install -r requirements.txt

Make the python script executable by running:

    $ chmod 755 DataManager.py

Now you can execute commands. By default, if you don't pass any arguments to DataManager, it will just print some very basic usage instructions.

    $ ./DataManager.py 
    usage: DataManager.py [-h] {csv2json,json2csv,download-csvs} ...

    Format CSV data for CitationDB

    positional arguments:
    {csv2json,json2csv,download-csvs}
                            Subcommands
        csv2json            Convert a folder of CSV files to JSON files
        json2csv            Convert a folder of JSON files to CSV files
        download-csvs       Download files from a URLs JSON file

    optional arguments:
    -h, --help            show this help message and exit

We'll go over how to use this tool for three specific use cases below: 
1. Downloading CSV files from the web.
2. Converting CSV files to JSON when you're done editing.
3. Creating CSV files from JSON files.

But first, let's describe these data files in a little more detail.

## Data files in a little more detail

The CitationDB application relies on four specially crafted JSON files. They are called: 

1. author.json
2. footnote.json
3. publication.json
4. resource.json

A folder containing all of these files contains all the data the application needs to function.

This tool can create a data folder of JSON files if you have a folder containing the same files in CSV format:

1. author.csv
2. footnote.csv
3. publication.csv
4. resource.csv

Whether you are converting from JSON to CSV, converting from CSV to JSON, or downloading these files from the Internet, you must have all four files in one place. If you are missing the "footenote.csv" file for example, the program will crash.

Now, let's describe these three use cases

## Use case 1: Download CSV files from the web

You might have copies of your CSV files on the web, for instance, if you are using a Google Sheet with four tabs, one for authors, one for footnotes, one for publications and one for resources. (We'll call these four objects "tables" regardless of what format they're in). It's fine to publish these sheets as .csv files, which makes them publicly accessible, because they do not contain any private data.

In order to download them, you need to create a urls.jdsson file that contains the url for each of the four tables. It should be a plain text file that looks like this:

    {
        "author":"https://example.com/author.csv",
        "footnote":"https:example.com/footnote.csv",
        "publication":"https://example.com/publication.csv",
        "resource":"https://example.com/resource.csv"
    }

There's a sample urls.json file, which contains links to the Google Sheets versions of each table.

*NOTE: The formatting is very important to get right for the program to be able to read this file, so be careful that you have every item surrounded by double-quotes, and that there are commas after the first three items.*

*NOTE 2: Remember, you need all four tables (author, footnote, publication and resource). If one of these items is not in your urls.json file, it won't work.*

Now that you have a *urls.json* file, you can run the following command to download them to a folder called "from-google" in the same folder as the DataManager.py file.

    $ ./DataManager.py download-csvs -u ./urls.json -o ./from-google
    
Here's what each part of that command does

* *download-csvs* - tells the program that we're going to use the download-csvs subroutine. Since this program does three things, we need to start by telling it which of the  three things to do. The other things it does are convert from csv to json ("csv2json" subroutine) and convert from JSON to CSV ("json2csv" subroutine).
* *-u ./urls.json* - tells the program that we want to load the data from URLs specified in the urls.json file. These files can be named anything, so you might want to have different urls files, like urls-google.json and urls-aws.json, to download different versions of the data files.
* *-o ./from-google* -tells the program that we want to "output" (save) the files we download in a folder called "from-google". This folder will be created if it doesn't exist already.

## Use case 2: Convertning CSV files to JSON files

Ultimately the app needs JSON files to function. You may edit the CSV files using any tool you want, including Google sheets. Once you have edited the files to your liking, put all four CSV files in a folder. In this example, we'll assume they're in a folder called "./sample-data/csv" and we want to save them in a folder called "./app-data".

Here's the command for that.

    $ ./DataManager.py csv2json -i ./sample-data/csv/ -o ./app-data

Here's what each part of that command does:

* *csv2json* - tells the program that we want to convert a folder full of CSV files to a folder full of JSON files.
* *-i ./sample-data/csv/* - tells the program that the CSV files we want to convert are already in a folder called "./sample-data/csv"
* *-o ./app-data* - tells the program that we want to "output" (save) the resulting JSON files in a folder called "app-data"

## Use case 3: Converting JSON data to CSV

If you only have JSON data but you want to edit it in a more friendly tool that edits CSV files, you can use the *json2csv* subcommand. It's basically like use case 3 in reverse.

Let's pretend we have a folder full of JSON files in called app-data, and we want to generate a folder full of CSV files called working-data. Here's the command to do that:

    $ ./DataManager.py json2csv -i ./app-data/ -o working-data

## Now what?

Now that you can convert files to CSV for editing, then convert them back to JSON so that you can feed them to the app, what do you do with the files? They need to be placed in a public folder on the web where the app knows to look for them. The location of this folder may change, so we're not going to include it in this README.

