import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')

    """
    TO DO: get user input for city (chicago, new york city, washington).
    HINT: Use a while loop to handle invalid inputs
    """

    city = input('Which city do you want to explore Chicago, New York City or Washington? \n ').lower()

    while city not in (CITY_DATA.keys()):
        print("Please enter a valied city name")
        city = input('Which city do you want to explore Chicago, New York or Washington? \n').lower()

    user_choise = input('Would you like to filter by   Month   ,  Day  ,  Both  ,  None \n').lower()
    while user_choise not in (['month', 'day', 'both', 'none']):
        print("please provid a vailed filter")
        user_choise = input('Would you like to filter by Month   ,  Day  ,  Both  ,  None \n').lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    if user_choise == 'month' or user_choise == 'both':
        month = input("Which one ? \n [January  ,  February ,  March ,  April ,  May ,  June ] \n").lower()
        while month not in months:   #Note: while loop inside if statment
            print("Please enter a valied month")
            month = input("Which one ? \n [January  ,  February ,  March ,  April ,  May ,  June ] \n").lower()
    else:
        month = 'all'

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if user_choise == 'day' or user_choise == 'both':
        day = input("Which one ? \n [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday , Sunday] \n").lower()

        while day not in days:
            print("Please enter a valied day")
            day = input("Which one ? \n [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday , Sunday] \n").lower()
    else:
        day = 'all'

    print('-' * 40)

    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])


    df['Start Time'] = pd.to_datetime(df['Start Time'])


    df['selected_month'] = df['Start Time'].dt.month
    df['selected_Day'] = df['Start Time'].dt.day_name()


    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['selected_month'] == month]


    if day != 'all':
        df = df[df['selected_Day'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    months = ['january', 'february', 'march', 'april', 'may', 'june']
    
    month = df['selected_month'].mode()[0] ;  print(f'The most common month is: {months[month-1]}')

    day = df['selected_Day'].mode()[0]     ;  print(f'The most common day of week is: {day}')

    df['hour'] = df['Start Time'].dt.hour
    
    popular_hour = df['hour'].mode()[0]    ; print(f'The most common start hour is: {popular_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most popular start station is: {}'.format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most popular end station is: {}'.format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    popular_trip = df['Start Station'] + ' to ' + df['End Station']
    print('The most popular trip is: from {}'.format(popular_trip.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_duration = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).sum()
    days =  total_travel_duration.days
    hours = total_travel_duration.seconds // (60*60)
    minutes = total_travel_duration.seconds % (60*60) // 60
    seconds = total_travel_duration.seconds % (60*60) % 60
    print('Total travel time is: {} days {} hours {} minutes {} seconds'.format(days,hours,minutes,seconds))

    # TO DO: display mean travel time
    average_travel_duration = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).mean()
    days =  average_travel_duration.days
    hours = average_travel_duration.seconds // (60*60)
    minutes = average_travel_duration.seconds % (60*60) // 60
    seconds = average_travel_duration.seconds % (60*60) % 60
    print('Average travel time is: {} days {} hours {} minutes {} seconds'.format(days,hours,minutes,seconds))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())  ;    print('\n\n')
    # TO DO: Display counts of gender
    if 'Gender' in(df.columns):
        print(df['Gender'].value_counts()) ;      print('\n\n')

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]
        print(f'Earliest birth  is: {earliest_birth:.0f}\n')
        print(f'Most recent birth is: {most_recent_birth:.0f}\n')
        print(f'Most common birth  is: {most_common_birth:.0f}\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):

    raw = input('\nWould you like to diplay raw data?\nEnter yes or no.\n')
    if raw.lower() == 'yes':
        count = 0
        while True:
            print(df.iloc[count: count+5])
            count += 5
            ask = input('Next 5 raws? \nEnter yes or no.\n')
            if ask.lower() != 'yes':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        restart = input('\nWould you like to restart? \nEnter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

    
    
# This is some of my helping resourses
"""
https://stackoverflow.com/questions/50866850/ask-user-to-continue-viewing-the-next-5-lines-of-data/50866928
https://github.com/beingjainparas/Udacity-Explore_US_Bikeshare_Data
https://stackoverflow.com/questions/52938818/how-to-display-increment-raw-data-using-iloc-depending-on-user-input
https://stackoverflow.com/questions/35523635/extract-values-in-pandas-value-counts/35523820

"""
    
