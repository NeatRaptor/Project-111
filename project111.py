import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff
import random
import pandas as pd

df = pd.read_csv("medium_data.csv")
data = df["claps"].tolist()

population_mean = statistics.mean(data)
print("Population mean of data: ", population_mean)


def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


mean_list = []
for i in range(0, 100):
    set_of_means = random_set_of_mean(30)
    mean_list.append(set_of_means)

mean = statistics.mean(mean_list)
std_deviation = statistics.stdev(mean_list)
print("Mean of sampling distribution: ", mean)
print("Standard deviation of sampling distribution: ", std_deviation)

first_std_deviation_end = mean + std_deviation
second_std_deviation_end = mean + (2 * std_deviation)
third_std_deviation_end = mean + (3 * std_deviation)

mean_of_sample1 = statistics.mean(data)
print("Mean of 1 sample: ", mean_of_sample1)

fig = ff.create_distplot([mean_list], ["claps"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="Mean of Sample"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines",
                         name="Standard deviation 1 end"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines",
                         name="Standard deviation 2 end"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines",
                         name="Standard deviation 3 end"))
fig.show()

z_score = (mean - mean_of_sample1) / std_deviation
print("The z score is: ", z_score)
