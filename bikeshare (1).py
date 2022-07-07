import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chi': 'chicago.csv',
              'nyc': 'new_york_city.csv',
              'was': 'washington.csv' }

def get_filters():
    print("Hello! Let\'s explore some US bikeshare data!")
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("which city you want to see its bikeshare data? type chi for Chicago nyc for New York City, or was for Washington: \n").lower()
    while city not in CITY_DATA.keys():
        print("entered city doesn't exist in this data")
        city = input("Please choos again a city you want to see its bikeshare data \n type chi for Chicago nyc for New York City, or was for Washington: \n").lower()
        
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all','january','february','march','april','may','june']
    month = input("To check a certain month, please enter the month name or type all to view all 6 months: \n-all\n-January\n-February\n-March\n-April\n-May\n-June\n").lower()
    while month not in months:
        print("entered month doesn't exist in this data")
        month = input("To check a certain month, please enter the month name or type all to view all 6 months: \nAll\n-January\n-February\n-March\n-April\n-May\n-June\n").lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    day = input("To check a certain day, please enter the day or type all to while wek: \n-All\n-Monday\n-Tuesday\n-Wednesday\n-Thursday\n-Friday\n-Satursday\n-Sunday\n").lower()
    while day not in days:
        print("That is incorrect, please enter day name or all for whole week")
        day = input("To check a certain day, please enter the day or type all to while wek: \n-All\n-Monday\n-Tuesday\n-Wednesday\n-Thursday\n-Friday\n-Satursday\n-Sunday\n").lower()
    print('-'*40)
    return city,month,day

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
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df  

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most common month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most common day:', popular_day)
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station :", start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print("The most commonly used end station :", end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most frequent combination of start station and end station trip : {}, {}" .format(most_frequent_start_end_station[0], most_frequent_start_end_station[1]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel Time: ",total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Average travel Time: ",mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User Types: ",user_types)

    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print("\nBike riders gender split: \n", gender_count)
    except KeyError:
        print("Gender data is not available for Washington, only for Chicago and New Zork City")
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year_of_birth = df['Birth Year'].min()
        most_recent_year_of_birth = df['Birth Year'].max()
        most_common_year_of_birth = df['Birth Year'].mode()
        print("The earliest year of birth: ", earliest_year_of_birth)
        print("The most recent year of birth: ", most_recent_year_of_birth)
        print("The most common year of birth: ", most_common_year_of_birth)
    except KeyError:
        print("Birth dates data are not available for Washington, only for Chicago and New Zork City")    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    data_display = input (" Do you want to see first 5 rows of data? yes or no \n").lower()
    loc_start=0
    while data_display != 'no':
        print (" Here they are: \n", df.iloc[loc_start:loc_start+5])
        loc_start +=5
        data_display = input (" Do you want to see another 5 rows of data? yes or no \n").lower()
         
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