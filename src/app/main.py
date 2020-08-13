import sys
import os

sys.path.extend('../../src')

from src.business.route_calculator import RouteCalculator

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
route_calculator = RouteCalculator()


def get_option_list():
    return {
        1: show_all_routes,
        2: get_distance,
        3: show_minimal_path,
        4: get_numbers_of_trip,
    }


def show_all_routes():
    route_calculator.show_routes()
    input()
    clear()


def get_distance():
    initial_point = (input('Please enter your initial point: '))
    final_point = (input('Please enter your destination: '))

    print('Total distance: ', route_calculator.find_minimal_distance(initial_point.upper(), final_point.upper()))
    input()
    clear()


def show_minimal_path():
    initial_point = (input('Please enter your initial point: '))
    final_point = (input('Please enter your destination: '))

    route_calculator.show_minimal_path(initial_point.upper(), final_point.upper())
    input()
    clear()


def get_numbers_of_trip():
    initial_point = (input('Please enter your initial point: '))
    final_point = (input('Please enter your destination: '))

    print('Total numbers of trips: ', len(route_calculator.find_path(initial_point.upper(), final_point.upper())))
    input()
    clear()


def init():
    print('Welcome to Router Provider.')
    while True:
        print('Choose Your Options : '
              '\n1 - Show all routes '
              '\n2 - Get distance '
              '\n3 - Get shortest path '
              '\n4 - Get number of trips '
              '\n5 - Exit\n')
        option = int(input())

        if option == 5:
            break
        else:
            option_execution = get_option_list().get(option, lambda: print('Invalid Option'))
            option_execution()


init()
