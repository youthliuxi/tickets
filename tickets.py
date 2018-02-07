#! python3
# -*- coding: UTF-8 -*-
"""Train tickets query ia CLI

Usage:
    ticket [-dgktzl] <from> <to> <date>

Options:
    -h --help   Show this screen
    -d          动车
    -g          高铁
    -k          快速
    -t          特快
    -z          直达
    -l          临时

"""
import requests
from docopt import docopt
import stations
from colorama import Fore
from prettytable import PrettyTable

def cli():
    arguments = docopt(__doc__, version='Tickets 1.0')
    from_station = stations.get_telecodes(arguments.get('<from>'))
    to_station = stations.get_telecodes(arguments.get('<to>'))
    date = arguments.get('<date>')
    url = ('https://kyfw.12306.cn/otn/leftTicket/queryZ?'
    	'leftTicketDTO.train_date={}&'
    	'leftTicketDTO.from_station={}&'
    	'leftTicketDTO.to_station={}&'
    	'purpose_codes=ADULT').format(date,from_station,to_station)
    r = requests.get(url,verify=False)
    raw_trains = r.json()['data']['result']
    pt = PrettyTable()
    pt._set_field_names('车次 车站 时间 历时 一等座 二等座 软卧 硬卧 软座 硬座 无座'.split())
    for raw_trains in raw_trains:
        data_list = raw_trains.split('|')
        train_no = data_list[3]
        from_station_code = data_list[6]
        to_station_code = data_list[7]
        from_station_name = ''
        to_station_name = ''
        start_time = data_list[8]
        arrive_time = data_list[9]
        time_duration = data_list[10]
        first_class_seat = data_list[31] or '--'
        second_class_seat = data_list[30] or '--'
        soft_sleep = data_list[23] or '--'
        soft_seat = data_list[24] or '--'
        hard_sleep = data_list[28] or '--'
        hard_seat = data_list[29] or '--'
        no_seat = data_list[33] or '--'
        pt.add_row([
            train_no,
            '\n'.join([Fore.GREEN + stations.get_name(from_station_code) + Fore.RESET, Fore.RED + stations.get_name(to_station_code) + Fore.RESET]),
            '\n'.join([Fore.GREEN + start_time + Fore.RESET, Fore.RED + arrive_time + Fore.RESET]),
            time_duration,
            first_class_seat,
            second_class_seat,
            soft_sleep,
            hard_sleep,
            soft_seat,
            hard_seat,
            no_seat
        ])
    print(pt)


if __name__ == '__main__':
    cli()
