# Data visualisation in Python
# Import matplotlib - If you have Python and PIP already installed on a system, then
# installation of Matplotlib is very easy.
# Install it using this command:
# C:\Users\Your project Name>pip install matplotlib
# Once Matplotlib is installed, import it in your applications by adding
# the import module statement:
# import matplotlib
# #Checking Matplotlib Version
# print(matplotlib.__version__)
# Most of the Matplotlib utilities lies under the pyplot submodule, and are usually
# imported under the plt alias:
# Draw a line in a diagram from position (0,0) to position (6,250):
# import matplotlib.pyplot as plt
# import numpy as np
# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])
# plt.plot(xpoints, ypoints)
# plt.show()
# Default X-Points
# If we do not specify the points on the x-axis, they will get the default values 0, 1, 2, 3
# (etc., depending on the length of the y-points.
# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10, 5, 7])
# plt.plot(ypoints)
# plt.show()
# You can use the keyword argument marker to emphasize each point with a
# specified marker:
# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, marker = 'o')
# plt.show()
# Marker Description
# 'o' Circle
# '*' Star
# '.' Point
# ',' Pixel
# 'x' X
# 'X' X (filled)
# '+' Plus
# 'P' Plus (filled)
# 's' Square
# 'D' Diamond
# 'd' Diamond (thin)
# 'p' Pentagon
# 'H' Hexagon
# 'h' Hexagon
# 'v' Triangle Down
# '^' Triangle Up
# '<' Triangle Left
# '>' Triangle Right
# '1' Tri Down
# '2' Tri Up
# '3' Tri Left
# '4' Tri Right
# '|' Vline
# '_' Hline
# Add a plot title and labels for the x- and y-axis:
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
# plt.plot(x, y)
# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
# plt.show()
# The subplot() Function
# The subplot() function takes three arguments that describes the layout of the figure.
# The layout is organized in rows and columns, which are represented by
# the first and second argument.
# The third argument represents the index of the current plot.
# plt.subplot(1, 2, 1)
# #the figure has 1 row, 2 columns, and this plot is the first plot.
# plt.subplot(1, 2, 2)
# #the figure has 1 row, 2 columns, and this plot is the second plot.
# So, if we want a figure with 2 rows an 1 column (meaning that the two plots will be
# displayed on top of each other instead of side-by-side), we can write the syntax like
# this:
# #Draw 2 plots on top of each other:
# import matplotlib.pyplot as plt
# import numpy as np
# #plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(2, 1, 1)
# plt.plot(x,y)
# You can draw as many plots you like on one figure, just descibe the number of rows,
# columns, and the index of the plot.
# # Draw 6 plots:
# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(2, 3, 1)
# plt.plot(x,y)
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(2, 3, 2)
# plt.plot(x,y)
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(2, 3, 3)
# plt.plot(x,y)
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(2, 3, 4)
# plt.plot(x,y)
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(2, 3, 5)
# plt.plot(x,y)
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(2, 3, 6)
# plt.plot(x,y)
# plt.show()
# With Pyplot, you can use the scatter() function to draw a scatter plot.
# The scatter() function plots one dot for each observation. It needs two arrays of the
# same length, one for the values of the x-axis, and one for values on the y-axis:
# You can set your own color for each scatter plot with the color or the c argument:
# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x, y, color = 'hotpink')
# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# plt.scatter(x, y, color = '#88c999')
# plt.show()
# The Matplotlib module has a number of available colormaps. You can specify the
# colormap with the keyword argument cmap with the value of the colormap, in this
# case 'viridis' which is one of the built-in colormaps available in Matplotlib.
# In addition you have to create an array with values (from 0 to 100), one value for
# each point in the scatter plot:
# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
# plt.scatter(x, y, c=colors, cmap='viridis')
# plt.colorbar()
# plt.show()
# The bar() function takes arguments that describes the layout of the bars.
# The categories and their values represented by the first and second argument as
# arrays.
# The bar() and barh() take the keyword argument color to set the color of the
# bars:
# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.bar(x, y, color = "red")
# plt.show()
# A histogram is a graph showing frequency distributions. It is a graph showing the
# number of observations within each given interval.
# Example: Say you ask for the height of 250 people, you might end up with a
# histogram like this:
# In Matplotlib, we use the hist() function to create histograms.
# The hist() function will use an array of numbers to create a histogram, the array is
# sent into the function as an argument.
# For simplicity we use NumPy to randomly generate an array with 250 values, where
# the values will concentrate around 170, and the standard deviation is 10.
# import matplotlib.pyplot as plt
# import numpy as np
# x = np.random.normal(170, 10, 250)
# plt.hist(x)
# plt.show()
# With Pyplot, you can use the pie() function to draw pie charts. By default the
# plotting of the first wedge starts from the x-axis and moves counterclockwise:
# import matplotlib.pyplot as plt
# import numpy as np
# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# plt.pie(y, labels = mylabels)
# plt.legend(title = "Four Fruits:")
# plt.show()
# Seaborn
# Seaborn is a library that uses Matplotlib underneath to plot graphs. If you
# have Python and PIP already installed on a system, install it using this command:
# C:\Users\Your Name>pip install seaborn
# import seaborn as sns
# Distplot stands for distribution plot, it takes as input an array and plots a curve
# corresponding to the distribution of points in the array.
# Normal Distribution
# The Normal Distribution is one of the most important distributions. It is also called the
# Gaussian Distribution after the German mathematician Carl Friedrich Gauss. Use
# the random.normal() method to get a Normal Data Distribution. It has three parameters:
# loc - (Mean) where the peak of the bell exists.
# scale - (Standard Deviation) how flat the graph distribution should be.
# size - The shape of the returned array.
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.distplot(random.normal(size=1000), hist=False)
# plt.show()
# # importing packages
# import seaborn as sns
# # loading dataset
# data = sns.load_dataset("iris")
# # draw lineplot
# sns.lineplot(x="sepal_length", y="sepal_width", data=data)
# Multiple plots in Seaborn can also be created using the Matplotlib as well as
# Seaborn also provides some functions for the same.
# Using subplot() method
# # importing packages
# import seaborn as sns
# import matplotlib.pyplot as plt
# # loading dataset
# data = sns.load_dataset("iris")
# def graph():
# sns.lineplot(x="sepal_length", y="sepal_width", data=data)
# # Adding the subplot at the specified
# # grid position
# plt.subplot(121)
# graph()
# # Adding the subplot at the specified
# # grid position
# plt.subplot(122)
# graph()
# plt.show()
# Using subplot2grid() method
# # importing packages
# import seaborn as sns
# import matplotlib.pyplot as plt
# # loading dataset
# data = sns.load_dataset("iris")
# def graph():
# sns.lineplot(x="sepal_length", y="sepal_width", data=data)
# # adding the subplots
# axes1 = plt.subplot2grid (
# (7, 1), (0, 0), rowspan = 2, colspan = 1)
# graph()
# axes2 = plt.subplot2grid (
# (7, 1), (2, 0), rowspan = 2, colspan = 1)
# graph()
# axes3 = plt.subplot2grid (
# (7, 1), (4, 0), rowspan = 2, colspan = 1)
# graph()
# Using FacetGrid() method, FacetGrid class helps in visualizing distribution of one
# variable as well as the relationship between multiple variables separately within
# subsets of your dataset using multiple panels.
# # importing packages
# import seaborn as sns
# import matplotlib.pyplot as plt
# # loading dataset
# data = sns.load_dataset("iris")
# plot = sns.FacetGrid(data, col="species")
# plot.map(plt.plot, "sepal_width")
# plt.show()
# Using PairGrid() method to Subplot grid for plotting pairwise relationships in a
# dataset.
# # importing packages
# import seaborn as sns
# import matplotlib.pyplot as plt
# # loading dataset
# data = sns.load_dataset("flights")
# plot = sns.PairGrid(data)
# plot.map(plt.plot)
# plt.show()
# A barplot is basically used to aggregate the categorical data according to some
# methods and by default its the mean. Categorical Plots are used where we have
# to visualize relationship between two numerical values.
# # importing packages
# import seaborn as sns
# import matplotlib.pyplot as plt
# # loading dataset
# data = sns.load_dataset("iris")
# sns.barplot(x='species', y='sepal_length', data=data)
# plt.show()
# A boxplot is sometimes known as the box and whisker plot.It shows the
# distribution of the quantitative data that represents the comparisons between
# variables. boxplot shows the quartiles of the dataset while the whiskers extend to
# show the rest of the distribution i.e. the dots indicating the presence of outliers. It is
# created using the boxplot() method.
# # importing packages
# import seaborn as sns
# import matplotlib.pyplot as plt
# # loading dataset
# data = sns.load_dataset("iris")
# sns.boxplot(x='species', y='sepal_width', data=data)
# plt.show()
# Pairplot represents pairwise relation across the entire dataframe and supports an
# additional argument called hue for categorical separation. What it does basically is
# create a jointplot between every possible numerical column and takes a while if the
# dataframe is really huge. It is plotted using the pairplot() method.
# # importing packages
# import seaborn as sns
# import matplotlib.pyplot as plt
# # loading dataset
# data = sns.load_dataset("iris")
# sns.pairplot(data=data, hue='species')
# plt.show()
# Heatmap is defined as a graphical representation of data using colors to visualize
# the value of the matrix. In this, to represent more common values or higher activities
# brighter colors basically reddish colors are used and to represent less common or
# activity values, darker colors are preferred. it can be plotted using
# the heatmap() function.
# # importing packages
# import seaborn as sns
# import matplotlib.pyplot as plt
# # loading dataset
# data = sns.load_dataset("tips")
# # correlation between the different parameters
# tc = data.corr()
# sns.heatmap(tc)
# plt.show()