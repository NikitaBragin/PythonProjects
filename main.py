import streamlit as st
import datetime
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from celluloid import Camera
import plotly.express as px

# streamlit run F:/PythonProjects/main.py

with st.echo(code_location='below'):
    @st.cache
    def fetch_data():
        df = pd.read_csv('avocado.csv')
        df['AveragePrice'] = df['AveragePrice'].rolling(2).mean()
        df['Total Volume'] = df['Total Volume'].rolling(2).mean()/1000
        df['Total Bags'] = df['Total Bags'].rolling(2).mean()/1000
        df['Date'] = pd.to_datetime(df['Date'])
        df['Month'] = df['Date'].dt.month
        df['Year'] = df['Date'].dt.year
        df.dropna(axis=0, inplace=True)
        return df

    @st.cache
    def parse_dates(df, start, end):
        df = df.query('`Date` >= @start and `Date` <= @end')
        return df

    @st.cache
    def choose_date_agg(df_to_copy, agg):
        df = df_to_copy.copy()
        if agg == 'weeks':
            pass
        elif agg == 'months':
            df['Date'] = pd.to_datetime(df.pop('Year').astype(str) + '-' + df.pop('Month').astype(str) + '-' + '01')
        else:
            df['Date'] = df.pop('Year').astype(str)
            del df['Month']
        prices = df.groupby(['Date', 'region', 'type']).mean()['AveragePrice'].reset_index(inplace=False)
        volAndBags = df.groupby(['Date', 'region', 'type']).sum()[['Total Volume', 'Total Bags']].reset_index(inplace=False)
        df = prices.merge(volAndBags, how='left', on=['Date', 'region', 'type'])
        return df

    @st.cache
    def cache_for_anim(df, typ, slice):
        dict_to_dash = {'Price, $US': 'AveragePrice',
                        'Volume, thousands of avocados': 'Total Volume',
                        'Number of Bags, thousands': 'Total Bags'}
        column = dict_to_dash[slice]
        dict_returned = {}
        df_two = df.query('''`type` == @typ and `region` in ['Plains', 'West','Midsouth','GreatLakes','Southeast','Northeast', 'SouthCentral', 'California']''')

        for j in sorted(np.unique(df_raw_main['Date'].dt.to_pydatetime())):
            instance = df_two.query('`Date` == @j')
            instance.sort_values(by=[column], inplace=True)
            dict_returned[j.date()] = instance
        return dict_returned

    st.title("Avocado Data in America")
    st.markdown(
        """
        <style>
        .reportview-container {
            background: #98e4d9
        }
       .sidebar.sidebar-content {
            background: #ddd48f
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    """Hello, fellow coder and avocado lover! :)"""
    """This dashboard allows you to check avocado prices, """
    """avocado volumes and bags sold for regions of USA from 2015 to 2017 year!"""
    """Also, you can pick a particular type of avocado to look at - either organic, or conventional."""
    """As well, you can pick to see weekly, monthly, or annuallized data"""
    """Feel free to compare the regions between each other, using the buttons below"""

    df_raw = fetch_data()
    start_date = st.sidebar.date_input('Start date (min: 2015-01-01)', datetime.date(2015, 1, 1))
    last_date = st.sidebar.date_input('End date (max: 2018-03-25)', datetime.date(2017, 12, 31))
    if start_date >= last_date:
        st.sidebar.error('Error: Final date must be less than the start date.')
    df_raw2 = parse_dates(df_raw, start_date, last_date)
    agg = st.sidebar.selectbox(
        'Date Level:',
        ['weeks', 'months', 'years'])
    df_raw_main = choose_date_agg(df_raw2, agg)
    pars = {'General':
                {'Region': df_raw_main['region'].unique().tolist(),
                      'Type': df_raw_main['type'].unique().tolist()
                 },
            'Slice': ['Price, $US', 'Volume, thousands of avocados', 'Number of Bags, thousands']}
    dict_to_dash = {'Price, $US': 'AveragePrice',
                    'Volume, thousands of avocados': 'Total Volume',
                    'Number of Bags, thousands': 'Total Bags'}
    slice = st.sidebar.selectbox(
        'Slice:',
        pars['Slice'])
    numbers = st.selectbox(
        'How many regions do you want to visualize?\nMaximum: 3.',
        [1, 2, 3])
    region = [str(st.selectbox(
        'Region of interest:',
        pars['General']['Region']))]
    if numbers != 1:
        region2 = str(st.selectbox(
            'Second region:',
            pars['General']['Region']))
        region.append(region2)
        if numbers > 2:
            region3 = str(st.selectbox(
                'Third region:',
                pars['General']['Region']))
            region.append(region3)
    typeo = str(st.sidebar.selectbox(
        'Type of Avocado:',
        pars['General']['Type']))
    query = '`region` in @region and `type` == @typeo'
    df = df_raw_main.query(query)
    fig = px.line(df, x="Date", y=str(dict_to_dash[slice]), color='region',
              line_group="region", hover_name="region", labels={
                     "Date": "Date, level: " + str(agg),
                     str(dict_to_dash[slice]): str(slice),
                     "region": "Region"
                 })
    fig.update_layout(
        margin=dict(l=0, r=0, t=5, b=0),
        paper_bgcolor='white',
    )
    st.plotly_chart(fig)

    """If you are interested in the animated bar chart, pick a shorter time period. Otherwise, the chart may load way too long"""

    if st.button('Animated bar plot'):
        "Let's look at the data dynamically!"
        "Here we have data aggregated by large regions of US."
        "You can check the states that are aggregated in each of the sections in Wikipedia."
        fig, ax = plt.subplots()
        fig.set_figwidth(7)
        fig.set_figheight(6)
        camera = Camera(fig)
        dict_anim = cache_for_anim(df_raw_main, typeo, slice)
        for i in dict_anim.keys():
            ax.barh(dict_anim[i]['region'], dict_anim[i][str(dict_to_dash[slice])])
            camera.snap()
        animation = camera.animate()

        components.html(animation.to_jshtml(), height=1000)