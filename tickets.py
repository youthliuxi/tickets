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

from docopt import docopt

def cli():
    arguments = docopt(__doc__, version='Tickets 1.0')
    from_station = arguments.get('<from>')
    to_station = arguments.get('<to>')
    date = arguments.get('<date>')
    url = ('https://kyfw.12306.cn/otn/leftTicket/queryZ?'
    	'leftTicketDTO.train_date={}&'
    	'leftTicketDTO.from_station={}&'
    	'leftTicketDTO.to_station={}&'
    	'purpose_codes=ADULT').format(date,from_station,to_station)

if __name__ == '__main__':
    cli()
