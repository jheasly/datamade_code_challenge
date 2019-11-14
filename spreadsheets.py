import csv
from datetime import date, datetime

def write_csv(path, payload):
    with open(path, 'w') as csvfile:
        fieldnames = list(payload[0].keys())
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for p in payload:
            writer.writerow(p)

def main():
    with open('legislators.csv', 'r') as readfile:

        under_forty_five = []
        twitter_youtube = []

        for c in csv.DictReader(readfile):
            # get birthdate string
            birthdate_str = c['birthdate']
            # convert birthdate string to date obj
            birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')
            today = date.today()
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

            if age < 45 and c['party'] == 'D':
                under_forty_five.append(c)

            if c['twitter_id'] and c['facebook_id'] and c['party'] == 'R':
                twitter_youtube.append(c)

    write_csv('under_forty_five_d.csv', under_forty_five)
    write_csv('twitter_youtube_r.csv', twitter_youtube)

if __name__ == "__main__":
    main()
