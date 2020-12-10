#!/usr/bin/env python
# coding: utf-8

# In[436]:



import hvplot.pandas
import panel as pn
import plotly.express as px
import pandas as pd
import holoviews as hv


# In[437]:


def add_season(df):
    Season = []
    
    df.index = pd.to_datetime(df.index)
    
    for i in range(len(df)):
        if df.index.month[i] in [12,1,2]:
            Season.append('Winter')
        elif df.index.month[i] in [3,4,5]:
            Season.append('Spring')
        elif df.index.month[i] in [6,7,8]: 
            Season.append('Summer')
        else:
            Season.append('Fall')
            
    
    df['Season'] = Season
    df['Year'] = df.index.year
    df['Month'] = df.index.month
    
    return df


# In[438]:


corn_df = pd.read_csv('../Resources/corn_belt_weather20201130.csv')
corn_df = corn_df.set_index('date')


# In[439]:


precip_df = corn_df[['PRCP_Illinois','PRCP_Indiana','PRCP_Nebraska','PRCP_Ohio','PRCP_Iowa']].copy()
temp_df = corn_df[['TMIN_Illinois','TMIN_Indiana','TMIN_Nebraska',
                   'TMIN_Ohio','TMIN_Iowa','TMAX_Illinois','TMAX_Indiana',
                   'TMAX_Nebraska','TMAX_Ohio','TMAX_Iowa']].copy()


# In[440]:


precip_graph = add_season(precip_df)
temp_graph = add_season(temp_df)



# In[442]:


def weather_map():
    state_df = pd.read_csv('../Resources/station_dataset.csv',
                       parse_dates=True,
                       infer_datetime_format=True,
                       names=['elevation','mindate','maxdate',
                              'latitude','name','datacoverage',
                              'id','elevationUnit','longitude',
                              'State','Location_ID'])

    fig = px.scatter_mapbox(state_df, lat="latitude", lon="longitude", color="State", size="datacoverage",
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=4,
                  mapbox_style="carto-positron", title='Distribution of Weather Stations')
    
    return fig


# In[443]:


## Weather Station Tab

weather_station_text = pn.pane.Markdown('Ten weather stations were selected at random from each of the five states. <br> Daily minimum/maximum temperatures and precipitation were averaged daily across each of the states to produce our dataset for machine learning.')


state_df = pd.read_csv('../Resources/station_dataset.csv',
                       parse_dates=True,
                       infer_datetime_format=True,
                       names=['elevation','mindate','maxdate',
                              'latitude','name','datacoverage',
                              'id','elevationUnit','longitude',
                              'State','Location_ID'])

state_table = state_df.hvplot.table(columns=['elevation','mindate','maxdate',
                              'latitude','name','datacoverage',
                              'id','elevationUnit','longitude',
                              'State','Location_ID'],
                          sortable=True, selectable=True)




weather_station_desc = pn.Row(pn.Column(weather_map(),state_table),pn.Column(weather_station_text))


# In[444]:


# Annual Seasonal Precipitation
def rain_20_long(state):
    
    df = precip_graph.groupby(['Year','Season']).sum().copy()
    
    return df[f'PRCP_{state}'].hvplot.bar(ylabel='Precipitation',
                        width=800,
                        height=400,
                        rot=90,
                #color='blue',
                title=f'{state}',
                                  alpha=0.3
                                          ).opts(shared_axes=False)
annual_seasonal_title = "## Annual Seasonal Precipitation over 20 Years"
precip_20_long = pn.Column(
    pn.Row(
        pn.Column(annual_seasonal_title, rain_20_long('Iowa'))
    ),
    pn.Row(
        pn.Column(rain_20_long('Illinois'))
    ),
    pn.Row(
        pn.Column(rain_20_long('Nebraska'))
    ),
    pn.Row(
        pn.Column(rain_20_long('Indiana'))
    ),
    pn.Row(
        pn.Column(rain_20_long('Ohio'))
    )
)


# In[445]:


## Annual Monthly Precipitation
def annual_monthly1():
    title_Monthly = '## Annual Monthly Precipitation'
    
    corn_states = ['Illinois', 'Indiana', 'Nebraska','Ohio','Iowa']
    
    state = pn.widgets.Select(name='State', options=corn_states)
    years = pn.widgets.IntSlider(name='Years', value=2000, start=2000, end=2019)

    @pn.depends(state, years)
    def get_plot(state, years):
        df = precip_graph[precip_graph['Year'] == years ]
        return df.hvplot.bar('Month', f'PRCP_{state}', grid=True).opts(shared_axes=False)

    return pn.Row(
        pn.Column(title_Monthly, state, years),
        get_plot
        )
def annual_monthly2():
    title_Monthly = '## Annual Monthly Precipitation'
    
    corn_states = ['Indiana', 'Nebraska','Ohio','Iowa','Illinois']
    
    state = pn.widgets.Select(name='State', options=corn_states)
    years = pn.widgets.IntSlider(name='Years', value=2000, start=2000, end=2019)

    @pn.depends(state, years)
    def get_plot(state, years):
        df = precip_graph[precip_graph['Year'] == years ]
        return df.hvplot.bar('Month', f'PRCP_{state}', grid=True).opts(shared_axes=False)

    return pn.Row(
        pn.Column(state, years),
        get_plot
        )
def annual_monthly3():
    title_Monthly = '## Annual Monthly Precipitation'
    
    corn_states = ['Nebraska','Ohio','Iowa','Illinois', 'Indiana']
    
    state = pn.widgets.Select(name='State', options=corn_states)
    years = pn.widgets.IntSlider(name='Years', value=2000, start=2000, end=2019)

    @pn.depends(state, years)
    def get_plot(state, years):
        df = precip_graph[precip_graph['Year'] == years ]
        return df.hvplot.bar('Month', f'PRCP_{state}', grid=True).opts(shared_axes=False)

    return pn.Row(
        pn.Column(state, years),
        get_plot
        )
def annual_monthly4():
    title_Monthly = '## Annual Monthly Precipitation'
    
    corn_states = ['Ohio','Iowa','Illinois', 'Indiana', 'Nebraska']
    
    state = pn.widgets.Select(name='State', options=corn_states)
    years = pn.widgets.IntSlider(name='Years', value=2000, start=2000, end=2019)

    @pn.depends(state, years)
    def get_plot(state, years):
        df = precip_graph[precip_graph['Year'] == years ]
        return df.hvplot.bar('Month', f'PRCP_{state}', grid=True).opts(shared_axes=False)

    return pn.Row(
        pn.Column(state, years),
        get_plot
        )
def annual_monthly5():
    title_Monthly = '## Annual Monthly Precipitation'
    
    corn_states = ['Iowa','Illinois', 'Indiana', 'Nebraska','Ohio']
    
    state = pn.widgets.Select(name='State', options=corn_states)
    years = pn.widgets.IntSlider(name='Years', value=2000, start=2000, end=2019)

    @pn.depends(state, years)
    def get_plot(state, years):
        df = precip_graph[precip_graph['Year'] == years ]
        return df.hvplot.bar('Month', f'PRCP_{state}', grid=True).opts(shared_axes=False)

    return pn.Row(
        pn.Column(state, years),
        get_plot
        )


annual_monthly_precip = pn.Column(annual_monthly1,
                 annual_monthly2,
                annual_monthly3,
                annual_monthly4,
                annual_monthly5)


# In[446]:


# 20 Years Max/Min Temp
def temp_20(state):
    
    # dashed line to show corn dies above 43
    hline = hv.HLine(43)
    hline.opts(
    color='green', 
    line_dash='dashed', 
    line_width=2.0)
    
    # dashed line to show corn dies below 0
    lline = hv.HLine(0)
    lline.opts(
    color='green', 
    line_dash='dashed', 
    line_width=2.0)
    
    return temp_df.hvplot.scatter(
        width=900,
        height=400,
        y=[f'TMIN_{state}', f'TMAX_{state}'],
        title=f'{state}', 
        xlabel='Year',
        ylabel='Temperature (C)',
        groupby='Year'
    ).opts(shared_axes=False)* hline*lline

title_temp_20 = '## Minimum/Maximum Temperatures for 20 Years'

temp_20_graphs = pn.Column(
    pn.Row(
        pn.Column(title_temp_20, temp_20('Iowa'))
    ),
    pn.Row(
        pn.Column(temp_20('Illinois'))
    ),
    pn.Row(
        pn.Column(temp_20('Nebraska'))),
    pn.Row(
        pn.Column(temp_20('Indiana'))),
        pn.Row(
        pn.Column(temp_20('Ohio')))
)


# In[447]:


# Seasonal Temp
def seasonal_temp_20(state):
    
    df = temp_df.groupby(['Year','Season']).mean().copy()
    
    return df.hvplot.scatter(
        x='Season',
        by=['Year'],
        width=800,
        height=400,
        y=[f'TMIN_{state}', f'TMAX_{state}'],
        title=f'{state}', 
        xlabel='Year',
        ylabel='Temperature (C)'
    ).opts(shared_axes=False)

title_seasonal_temp = '## Seasonal Minimum/Maximum Temperatures for 20 Years'

seasonal_temp_graphs = pn.Column(
    pn.Row(
        pn.Column(title_seasonal_temp, seasonal_temp_20('Iowa'))
    ),
    pn.Row(
        pn.Column(seasonal_temp_20('Illinois'))
    ),
    pn.Row(
        pn.Column(seasonal_temp_20('Nebraska'))
    ),
    pn.Row(
        pn.Column(seasonal_temp_20('Indiana'))
    ),
        pn.Row(
        pn.Column(seasonal_temp_20('Ohio'))
        )
)




# In[448]:


dashboard = pn.Column("## Analysis of Weather Data for Top 5 Corn Producing States",
                      pn.Tabs(
                          ("Introduction", weather_station_desc),
                          ("Annual Seasonal Precipitation",precip_20_long),
                          ("Annual Monthly Precipitation",annual_monthly_precip),
                          ("20 Years Max/Min Temperatures",temp_20_graphs),
                          ("Annual Seasonal Max/Min Temperatures",seasonal_temp_graphs)
                      )
                     )


# In[450]:


dashboard.servable().show()







