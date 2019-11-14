# Spreadsheets
A DataMade code challenge.
## Spreadsheet manipulation
Download the Sunlight Foundation’s [list of legislators in the United States](http://unitedstates.sunlightfoundation.com/legislators/legislators.csv). Write a script that reads the spreadsheet as input, filters the rows based on specific criteria, and writes two spreadsheets as output. The criteria for the two spreadsheets should be:

First spreadsheet: All Democrats who are younger than 45 years old
Second spreadsheet: All Republicans who have Twitter accounts and YouTube channels

For each row in the output, make sure to keep all of the columns from the original data source.

## How do you run it?
Clone the repo. Then `cd` into it and
```
python spreadsheets.py
```
... and in that same directory you should see two files created:
```
twitter_youtube_r.csv
under_forty_five_d.csv
```
`twitter_youtube_r.csv` is all the Republicans with both Twitter and YouTube accounts and  `under_forty_five_d.csv` is all the younger-than-forty-five Democrats.

## How'd you do it?

My approach was to use to rely on the Python `csv` module and its `DictReader` and `DictWriter` methods to read, parse and write the `.csv` data. Pretty simple and super convenient.