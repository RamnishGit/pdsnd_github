import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'downloads\chicago.csv',
             'washington': 'downloads\washington.csv',
            'new york city': 'downloads\new_york_city.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

	Fetch city data
	Fetch month details
	

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Enter one of following city: chicago, new york city or washington! ').lower()
        if city not in CITY_DATA:
            print('Please enter correct city!')
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input('Enter one of the following month: january to june or all for all months: ').lower()
        if month not in ('january','february','march','april','may','june','all'):
            print('Please enter correct month!')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input('Enter one of the following day: monday,tuesday,wednesday,thrusday,friday,saturday,sunday or all for all days: ').lower()
        if day not in ('monday','tuesday','wednesday','thrusday','friday','saturday','sunday','all'):
            print('Please enter correct day!')
        else:
            break

    print('-'*40)
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

    df['month'] = df['Start Time'].dt.month

    df['day'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january','february','march','april','may','june','july']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    print('Most common month:', df['month'].mode()[0])

    # TO DO: display the most common day of week

    print('Most common day of week:', df['day'].mode()[0])

    # TO DO: display the most common start hour

    print('Most common start hour:', df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    print('Most commonly used start station:', df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station

    print('Most commonly used end station:', df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip

    print('Most frequest combination:', df['Start Station'] + '-' + df['End Station'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    print('Total travel time:', df['Trip Duration'].sum(), ' second or ',df['Trip Duration'].sum()/3600, 'hour' )


    # TO DO: display mean travel time

    print('Average travel time:', df['Trip Duration'].mean(), ' second or ',df['Trip Duration'].mean()/3600, 'hour')


    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    print('Count of user types:', df['User Type'].value_counts())


    # TO DO: Display counts of gender

    if 'Gender' in df:
        print('Count of gender:', df['Gender'].value_counts())

    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')

    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df:
        print('Earliest year of birth:', int(df['Birth Year'].min()))
        print('Most recent year of birth:', int(df['Birth Year'].max()))
        print('Most common year of birth:', int(df['Birth Year'].mode()[0]))
    else:
        print('Birth Year stats cannot be calculated because it does not appear in the dataframe')


    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)


def display_data(df):


    # display 5 row of data

    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no? ")
    start_loc = 0

    while (view_data):
        print(df.iloc[start_loc:start_loc + 5])

        pd.set_option('display.max_columns',200)

        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        if view_display == 'no':
            break
    pd.set_option('display.max_columns',200)

    return df


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
