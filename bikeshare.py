import pandas as pd
import numpy as np
import time #to help with calculating  the duartions

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington dc': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Choose a city: chicago, new york city, washington dc: ").lower()
    print('\n')
    while city not in CITY_DATA.keys():
        print("Make sure to choose one city from the pervious\n")
        city = input("Choose a city: chicago, new york city, washington dc\n ")
    #lower function will make sure that letters stay small in the input

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ["january", "february", "march", "april" , "may", "june", "all"]
    while True:
            month = input("Choose a month: ").lower()
        #lower function will make sure that letters stay small in the input
            if month in months:
                break
            else:
                print('Choose a month from the following: january, february, march, april, may, june, all: \n')

        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    while True:
          day = input("Choose a day of the week: ")
        #lower function will make sure that letters stay small in the input
          if day in days:
              break 
          else:
            print('Choose a day of the week: (sunday, monday, tuesday, wednesday, thursday, friday, saturday, all): ')

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
#Load data from DATAFRAME
    df = pd.read_csv(CITY_DATA[city])

#Convert start time to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])

#Exctract month and day of the week to create new coloum
    df['month'] = df["Start Time"].dt.month
    df['day_of_week'] = df["Start Time"].dt.weekday_name
    df['start hour'] = df["Start Time"].dt.hour

#filters by month and day if applicable.
    if month != 'all':
        months = ('january', 'february', 'march', 'april', 'may', 'june')
        month = months.index(month) + 1 #+1 was added as python starts with zero.
        df = df[df['month'] == month]

    if day != 'all':
     days = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
     df =df[df['day_of_week'] == day.title()] #.tittle was added to make it match with how it is written in the sheer
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    #mode is used to extract the most repeated number (common month)
    print('most common month: {}'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    #mode is used to extract the most repeated number (common month)
    print('most common day: {}'.format(df['day_of_week'].mode()[0]))


    # TO DO: display the most common start hour
    print('most common start hour: {}'.format(df['start hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df): 
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most visited station: {}".format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print("Most common end station: {}".format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['route'] = df['Start Station'] + " " +" " + df['End Station']
    print("most frequent combination of start station and end station trip: {}".format(df['route'].mode()[0]))
      
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print("total travel time: ", total_time)
    # TO DO: display mean travel time
    average_time = df['Trip Duration'].mean()
    print("Average travel time: ", average_time)
    print('\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts().to_frame)

    # TO DO: Display counts of gender
    if city != 'washington dc':
        print(df['Gender'].value_counts().to_frame())

    # TO DO: Display earliest, most recent, and most common year of birth
        print("Earliest year of birth: ", int(df['Birth Year'].min()))
        print("Most recent year of birth: ", int(df['Birth Year'].max()))
        print("Most common year of birth: ", int(df['Birth Year'].mode()[0]))
    else:
        print("Couldn't find data")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    # ask user if he/she wants to review 4 row data
    print('\n Raw data is available\n')
    
    index = 0 
    user_input = input('If you want to review 4 row write yes if not write no: ')
    if user_input not in ['yes' , 'no']:
        print("Kindly choose yes or no")
        user_input = input('If you want to review 4 row write yes if not write no: ')
    elif user_input != 'yes':
        print("thanks")
    
    else:
        while index+4 < df.shape[0]:
            print(df.iloc[index:index+4])
            index += 4
            user_input = input('If you want to review 4 row write yes if not write no: ')
            if user_input != "yes":
                print('thanks')
                break

def main():
    while True:
            city, month, day = get_filters()
            df = load_data(city, month, day)

        #time_stats(df)
            time_stats(df)                        
        #station_stats(df)
            station_stats(df)                         
        #trip_duration_stats(df)
            trip_duration_stats(df)                         
        #user_stats(df)
            user_stats(df,city)
            display_data(df) 
                                 
            restart = input('\nWould you like to restart from the beginning? Enter yes if not choose no.\n').lower()
            if restart.lower() != 'yes':
                print("Thanks for your effort")
                break
if __name__ == "__main__":
	main()
