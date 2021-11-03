import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st
import random
import pandas as pd
import csv

df = pd.read_csv("c110/medium_data.csv")
data = df["reading_time"].tolist()
fig = ff.create_distplot([data], ["Math_score"], show_hist=False)
# fig.show()


def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean


mean_list = []
for i in range(0,1000):
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)
    
mean_list_mean = st.mean(mean_list)
mean_list_stdev = st.stdev(mean_list)

# print(mean_list_mean , mean_list_stdev)

mean_list_polt_graph = ff.create_distplot([mean_list], ["Math_score"], show_hist=False)
mean_list_polt_graph.add_trace(go.Scatter(x=[mean_list_mean, mean_list_mean], y=[0, 0.2], mode="lines", name="MEAN"))
# mean_list_polt_graph.show()

std1starts , std1end = mean_list_mean - mean_list_stdev , mean_list_mean+mean_list_stdev
std2starts ,std2end = mean_list_mean - (2*mean_list_stdev),mean_list_mean + (2*mean_list_stdev)
std3starts ,std3end = mean_list_mean - (3*mean_list_stdev),mean_list_mean + (3*mean_list_stdev)

df1 = pd.read_csv("c111/School_1_Sample.csv")
data1 = df1["Math_score"].to_list()
data1_mean = st.mean(data1)
fig1= ff.create_distplot([mean_list], ["Math_score 1"], show_hist=False)
fig1.add_trace(go.Scatter(x=[mean_list_mean, mean_list_mean], y=[0, 0.2], mode="lines", name="MEAN"))
fig1.add_trace(go.Scatter(x=[data1_mean, data1_mean], y=[0, 0.2], mode="lines", name="tablet"))
fig1.add_trace(go.Scatter(x=[std1end, std1end], y=[0, 0.2], mode="lines", name="std1"))
fig1.add_trace(go.Scatter(x=[std2end, std2end], y=[0, 0.2], mode="lines", name="std2"))
fig1.add_trace(go.Scatter(x=[std3end, std3end], y=[0, 0.2], mode="lines", name="std3"))
fig1.show()

zscore1 = (mean_list_mean -data1_mean)/mean_list_stdev
print(zscore1)

df2 = pd.read_csv("c111/School_2_Sample.csv")
data2 = df2["Math_score"].to_list()
data2_mean = st.mean(data2)
fig2= ff.create_distplot([mean_list], ["Math_score 2 "], show_hist=False)
fig2.add_trace(go.Scatter(x=[mean_list_mean, mean_list_mean], y=[0, 0.2], mode="lines", name="MEAN"))
fig2.add_trace(go.Scatter(x=[data2_mean, data2_mean], y=[0, 0.2], mode="lines", name="tablet"))
fig2.add_trace(go.Scatter(x=[std1end, std1end], y=[0, 0.2], mode="lines", name="std1"))
fig2.add_trace(go.Scatter(x=[std2end, std2end], y=[0, 0.2], mode="lines", name="std2"))
fig2.add_trace(go.Scatter(x=[std3end, std3end], y=[0, 0.2], mode="lines", name="std3"))
fig2.show()

zscore2= (mean_list_mean -data2_mean)/mean_list_stdev
print(zscore2)

df3 = pd.read_csv("c111/School_3_Sample.csv")
data3 = df3["Math_score"].to_list()
data3_mean = st.mean(data3)
fig3= ff.create_distplot([mean_list], ["Math_score 3"], show_hist=False)
fig3.add_trace(go.Scatter(x=[mean_list_mean, mean_list_mean], y=[0, 0.2], mode="lines", name="MEAN"))
fig3.add_trace(go.Scatter(x=[data3_mean, data3_mean], y=[0, 0.2], mode="lines", name="tablet"))
fig3.add_trace(go.Scatter(x=[std1end, std1end], y=[0, 0.2], mode="lines", name="std1"))
fig3.add_trace(go.Scatter(x=[std2end, std2end], y=[0, 0.2], mode="lines", name="std2"))
fig3.add_trace(go.Scatter(x=[std3end, std3end], y=[0, 0.2], mode="lines", name="std3"))
fig3.show()

zscore3= (mean_list_mean -data3_mean)/mean_list_stdev
print(zscore3)