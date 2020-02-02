# import pytz
import datetime
import csv, sys
import codecs

input_path = sys.argv[1]
output_path = sys.argv[2]

# To run in commandline, the program expects
# python3 app.py "input_file_path" "output_file_path"
if len(sys.argv) > 2:
    def format_datetime_to_iso(timestamp):
        return datetime.datetime.strptime(timestamp, "%m/%d/%y %I:%M:%S %p").isoformat()


    # TODO: Get clarity on expected result when the incoming zip length is > 5
    # i.e should it return zip[:5] when len(zip) > 5?
    def format_zipcode(zip):
        return zip.zfill(5)


    def calc_total_seconds(time):
        # HH:MM:SS.MS --> SS.MS
        timeList = time.split(':')
        hours_to_seconds = int(timeList[0]) * 3600
        minutes_to_seconds = int(timeList[1]) * 60
        seconds = float(timeList[2])
        return hours_to_seconds + minutes_to_seconds + seconds


    def format_fullname(fullname):
        return fullname.upper()

    # TODO: Add a timezone converter utility function

    
    try:
        with codecs.open(input_path, encoding='utf-8', errors='replace') as in_file:
            reader = csv.reader(in_file)
            header = next(reader)

            data = []
            for row in reader:
                timestamps = row[0]
                addresses = row[1]
                zipcodes = row[2]
                fullnames = row[3]
                fooDurations = row[4]
                barDurations = row[5]
                totalDurations = row[6]
                notes = row[7]
                data.append(
                    [timestamps, addresses, zipcodes, fullnames, fooDurations, barDurations, totalDurations, notes])
    except FileNotFoundError:
        in_file = None
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(in_file, reader.line_num, e))
    # TODO: Add additional error cases

    with codecs.open(output_path, 'w', encoding='utf-8', errors='replace') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(header)

        for data_item in data:
            writer.writerow([format_datetime_to_iso(data_item[0]),
                             data_item[1],
                             format_zipcode(data_item[2]),
                             format_fullname(data_item[3]),
                             calc_total_seconds(data_item[4]),
                             calc_total_seconds(data_item[5]),
                             sum([float(calc_total_seconds(data_item[4])), float(calc_total_seconds(data_item[5]))]),
                             data_item[7]
                             ])
    # TODO: Add additional error cases





