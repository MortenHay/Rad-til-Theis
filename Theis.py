# %%
from turtle import color
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


usageFrame = pd.read_csv("Forbrugsdata.csv", sep=';')

usageFrame["Fra_dato"] = pd.to_datetime(
    usageFrame["Fra_dato"], format="%d-%m-%Y %H:%M:%S")
usageFrame["Til_dato"] = pd.to_datetime(
    usageFrame["Til_dato"], format="%d-%m-%Y %H:%M:%S")

fig = plt.figure()
ax = fig.add_subplot(111)
fig2 = plt.figure()
#dx = fig2.add_subplot(111)
fig3 = plt.figure()
mx = fig3.add_subplot(111)
fig4 = plt.figure()
nx = fig4.add_subplot(111)
fig5 = plt.figure()
px = fig5.add_subplot(111)
fig6 = plt.figure()
pxx = fig6.add_subplot(111)
fig7 = plt.figure()
pxxx = fig7.add_subplot(111)

ax.plot(usageFrame["Fra_dato"], usageFrame["Maengde"])

ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%Y'))
fig.autofmt_xdate
ax.set_ylabel("kWh/dag")
ax.set_xlabel("Måned")
ax.set_title("Forbrugsdata")
plt.xticks(rotation=60)
fig.show

preUsage = usageFrame[0:11520]
# print(preUsage)
preUsage["hourOfDay"] = preUsage["Fra_dato"].dt.hour
t0 = preUsage["Fra_dato"][0]
tT = preUsage["Fra_dato"][preUsage["Fra_dato"].__len__()-1]

# for day in pd.date_range(t0, tT):
#     select = preUsage.Fra_dato.dt.date == day
#     dx.plot(preUsage.hourOfDay[select], preUsage.Maengde[select])

mx.plot(preUsage.groupby("hourOfDay").mean().index,
        preUsage.groupby("hourOfDay").mean()["Maengde"], label="Gennemsnit", color="orange")


# make dataframe with 5% 25% 50% 75% 95% quartiles
quartiles = pd.DataFrame()
quartiles["5%"] = preUsage.groupby("hourOfDay").quantile(0.05)["Maengde"]
quartiles["25%"] = preUsage.groupby("hourOfDay").quantile(0.25)["Maengde"]
quartiles["50%"] = preUsage.groupby("hourOfDay").quantile(0.50)["Maengde"]
quartiles["75%"] = preUsage.groupby("hourOfDay").quantile(0.75)["Maengde"]
quartiles["95%"] = preUsage.groupby("hourOfDay").quantile(0.95)["Maengde"]

# plot quantiles as fill with different alpha in mx
mx.fill_between(quartiles.index, quartiles["95%"], quartiles["5%"],
                alpha=0.2, color="b", label="90% percentil")
mx.fill_between(quartiles.index, quartiles["75%"], quartiles["25%"],
                alpha=0.4, color="b", label="50% percentil")

# plot median as line in mx
mx.plot(quartiles.index, quartiles["50%"], color="b", label="median")
mx.set_ylabel("kWh/dag")
mx.set_xlabel("Dagstime")
mx.set_title("Forbrugsdata")
plt.xticks(rotation=60)
fig3.show


# make legend for mx
handles, labels = mx.get_legend_handles_labels()
fig3.legend(handles, labels, loc="upper left")

# make 24 ticks on mx x axis
mx.set_xticks(np.arange(0, 24, 1))

# make postUsage dataframe that contains all data after 2021-09-01
postUsage = usageFrame[11520:]
postUsage["hourOfDay"] = postUsage["Fra_dato"].dt.hour

# plot postUsage data like preUsage data
nx.plot(postUsage.groupby("hourOfDay").mean().index,
        postUsage.groupby("hourOfDay").mean()["Maengde"], label="Gennemsnit", color="orange")

quartiles = pd.DataFrame()
quartiles["5%"] = postUsage.groupby("hourOfDay").quantile(0.05)["Maengde"]
quartiles["25%"] = postUsage.groupby("hourOfDay").quantile(0.25)["Maengde"]
quartiles["50%"] = postUsage.groupby("hourOfDay").quantile(0.50)["Maengde"]
quartiles["75%"] = postUsage.groupby("hourOfDay").quantile(0.75)["Maengde"]
quartiles["95%"] = postUsage.groupby("hourOfDay").quantile(0.95)["Maengde"]

nx.fill_between(quartiles.index, quartiles["95%"], quartiles["5%"],
                alpha=0.2, color="b", label="90% percentil")
nx.fill_between(quartiles.index, quartiles["75%"], quartiles["25%"],
                alpha=0.4, color="b", label="50% percentil")

nx.plot(quartiles.index, quartiles["50%"], color="b", label="median")
nx.set_ylabel("kWh/dag")
nx.set_xlabel("Dagstime")
nx.set_title("Forbrugsdata")
plt.xticks(rotation=60)
fig4.show

handles, labels = nx.get_legend_handles_labels()
fig4.legend(handles, labels, loc="upper left")
nx.set_xticks(np.arange(0, 24, 1))


# make dataframe from produktionsdata.csv
productionFrame = pd.read_csv("Produktionsdata.csv", sep=";")
productionFrame["Fra_dato"] = pd.to_datetime(
    productionFrame["Fra_dato"], format="%d-%m-%Y %H:%M:%S")
productionFrame["Til_dato"] = pd.to_datetime(
    productionFrame["Til_dato"], format="%d-%m-%Y %H:%M:%S")

# make plot of productionFrame with data
productionFrame["hourOfDay"] = productionFrame["Fra_dato"].dt.hour
px.plot(productionFrame.groupby("hourOfDay").mean().index,
        productionFrame.groupby("hourOfDay").mean()["Maengde"], label="Gennemsnit", color="orange")

Pquartiles = pd.DataFrame()
Pquartiles["5%"] = productionFrame.groupby(
    "hourOfDay").quantile(0.05)["Maengde"]
Pquartiles["25%"] = productionFrame.groupby(
    "hourOfDay").quantile(0.25)["Maengde"]
Pquartiles["50%"] = productionFrame.groupby(
    "hourOfDay").quantile(0.50)["Maengde"]
Pquartiles["75%"] = productionFrame.groupby(
    "hourOfDay").quantile(0.75)["Maengde"]
Pquartiles["95%"] = productionFrame.groupby(
    "hourOfDay").quantile(0.95)["Maengde"]

px.fill_between(Pquartiles.index, Pquartiles["95%"], Pquartiles["5%"],
                alpha=0.2, color="b", label="90% percentil")
px.fill_between(Pquartiles.index, Pquartiles["75%"], Pquartiles["25%"],
                alpha=0.4, color="b", label="50% percentil")

px.plot(Pquartiles.index, Pquartiles["50%"], color="b", label="median")
px.set_ylabel("kWh/dag")
px.set_xlabel("Dagstime")
px.set_title("Produktionsdata")
plt.xticks(rotation=60)

Phandles, Plabels = px.get_legend_handles_labels()
fig5.legend(Phandles, Plabels, loc="upper left")
px.set_xticks(np.arange(0, 24, 1))

# make dataframe from Prisdata.csv and plot like data from productionFrame in new figure
priceFrame = pd.read_csv("Prisdata.csv", sep=",")
priceFrame["HourDK"] = pd.to_datetime(
    priceFrame["HourDK"])
priceFrame["hourOfDay"] = priceFrame["HourDK"].dt.hour
pxx.plot(priceFrame.groupby("hourOfDay").mean().index,
         priceFrame.groupby("hourOfDay").mean()["SpotPriceDKK"], label="Gennemsnit", color="orange")

Pquartiles = pd.DataFrame()
Pquartiles["5%"] = priceFrame.groupby(
    "hourOfDay").quantile(0.05)["SpotPriceDKK"]
Pquartiles["25%"] = priceFrame.groupby(
    "hourOfDay").quantile(0.25)["SpotPriceDKK"]
Pquartiles["50%"] = priceFrame.groupby(
    "hourOfDay").quantile(0.50)["SpotPriceDKK"]
Pquartiles["75%"] = priceFrame.groupby(
    "hourOfDay").quantile(0.75)["SpotPriceDKK"]
Pquartiles["95%"] = priceFrame.groupby(
    "hourOfDay").quantile(0.95)["SpotPriceDKK"]

pxx.fill_between(Pquartiles.index, Pquartiles["95%"], Pquartiles["5%"],
                 alpha=0.2, color="b", label="90% percentil")
pxx.fill_between(Pquartiles.index, Pquartiles["75%"], Pquartiles["25%"],
                 alpha=0.4, color="b", label="50% percentil")

pxx.plot(Pquartiles.index, Pquartiles["50%"], color="b", label="median")
pxx.set_ylabel("Pris DKK/kWh")
pxx.set_xlabel("Dagstime")
pxx.set_title("Prisdata")
plt.xticks(rotation=60)

Phandles, Plabels = pxx.get_legend_handles_labels()
fig6.legend(Phandles, Plabels, loc="upper left")
pxx.set_xticks(np.arange(0, 24, 1))

# make dataframe from co2data.csv and plot like data from Prisdata.csv in new figure
co2Frame = pd.read_csv("co2data.csv", sep=";")
co2Frame["HourDK"] = pd.to_datetime(
    co2Frame["HourDK"])
co2Frame["hourOfDay"] = co2Frame["HourDK"].dt.hour
pxxx.plot(co2Frame.groupby("hourOfDay").mean().index,
          co2Frame.groupby("hourOfDay").mean()["CO2Emission"], label="Gennemsnit", color="orange")

Pquartiles = pd.DataFrame()
Pquartiles["5%"] = co2Frame.groupby("hourOfDay").quantile(0.05)["CO2Emission"]
Pquartiles["25%"] = co2Frame.groupby("hourOfDay").quantile(0.25)["CO2Emission"]
Pquartiles["50%"] = co2Frame.groupby("hourOfDay").quantile(0.50)["CO2Emission"]
Pquartiles["75%"] = co2Frame.groupby("hourOfDay").quantile(0.75)["CO2Emission"]
Pquartiles["95%"] = co2Frame.groupby("hourOfDay").quantile(0.95)["CO2Emission"]

pxxx.fill_between(Pquartiles.index, Pquartiles["95%"], Pquartiles["5%"],
                  alpha=0.2, color="b", label="90% percentil")
pxxx.fill_between(Pquartiles.index, Pquartiles["75%"], Pquartiles["25%"],
                  alpha=0.4, color="b", label="50% percentil")

pxxx.plot(Pquartiles.index, Pquartiles["50%"], color="b", label="median")
pxxx.set_ylabel("Udledt CO2")
pxxx.set_xlabel("Dagstime")
pxxx.set_title("CO2 udledning")
plt.xticks(rotation=60)

Phandles, Plabels = pxxx.get_legend_handles_labels()
fig7.legend(Phandles, Plabels, loc="upper left")
pxxx.set_xticks(np.arange(0, 24, 1))


plt.show(block=True)


# %%
