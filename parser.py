import sys


def main():
    log_file = open(sys.argv[1])
    logs = []
    for log in log_file:

        fields = log.split(',')

        num             = fields[0]
        date_time       = fields[1]
        user_id         = fields[2]
        username        = fields[3]
        position        = fields[4]
        terminal_id     = fields[5]
        terminal_name   = fields[6]
        auth_type       = fields[7]
        auth_result     = fields[8]
        function_key_no = fields[9]

        date_time = date_time.split(' ')
        date = date_time[0]
        time = date_time[1]
        merediem = date_time[2]

        # time = time.split(":")
        date = date.split('/')

        year  = date[2]
        month = date[0]
        day   = date[1]

        # date = year + "-" + month + "-" + day
        date = year + "-" + month + "-" + day

        # store in a list

        e = [num,
            month,
            day,
            year,
            time,
            merediem,
            user_id,
            username,
            position,
            terminal_id,
            terminal_name,
            auth_type,
            auth_result,
            function_key_no,
            ]

        # append to logs
        logs.append(e)

    # data input
    usr_id = input('Search User ID: ')

    # empty clean log
    clean_log = []

    # loop thru logs
    for item in logs:
        if usr_id == item[6]:
            first = clean_log[0:7] = item[0:7]
            last = clean_log[9:13] = item[9:13]
            clean = first + last
            print(clean)

# run by condition
if __name__ == '__main__':
    main()
