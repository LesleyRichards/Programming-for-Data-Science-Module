# pip install pandas

import pandas as pd
import numpy as np

# object creation

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

# Creating a DataFrame by passing a NumPy array, with a datetime index
# using date_range() and labeled columns:

dates = pd.date_range("20130101", periods=6)
print(dates)

# Creating a DataFrame by passing a dictionary of objects that can be converted into a
# series-like structure:

df2 = pd.DataFrame({
"A": 1.0,
"B": pd.Timestamp("20130102"),
"C": pd.Series(1, index=list(range(4)), dtype="float32"),
"D": np.array([3] * 4, dtype="int32"),
"E": pd.Categorical(["test", "train", "test", "train"]),
"F": "foo",
})
print(df2)

# columns have different data types
print(df2.dtypes)

# Viewing data

# Use DataFrame.head() and DataFrame.tail() to view the top and bottom rows of
# the frame respectively:

# code seems to be wrong ffs
# he has written 'df' which doesn't exist, so instead I wrote 'df2', so any 'df2' from
# here on is supposed to be 'df', unless I say otherwise
print(df2.head())
# output should be
# Out[13]:
# A B C D
# 2013-01-01 0.469112 -0.282863 -1.509059 -1.135632
# 2013-01-02 1.212112 -0.173215 0.119209 -1.044236
# 2013-01-03 -0.861849 -2.104569 -0.494929 1.071804
# 2013-01-04 0.721555 -0.706771 -1.039575 0.271860
# 2013-01-05 -0.424972 0.567020 0.276232 -1.087401

print(df2.tail(3))
# output should be:
# Out[14]:
# A B C D
# 2013-01-04 0.721555 -0.706771 -1.039575 0.271860
# 2013-01-05 -0.424972 0.567020 0.276232 -1.087401
# 2013-01-06 -0.673690 0.113648 -1.478427 0.524988

# Display the DataFrame.index or DataFrame.columns:
print(df2.index)
# output should be:
# Out[15]:
# DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
# '2013-01-05', '2013-01-06'],
# dtype='datetime64[ns]', freq='D')

print(df2.columns)
# output should be:
# Out[16]: Index(['A', 'B', 'C', 'D'], dtype='object')

df2.to_numpy()
# output:
# Out[17]:
# array([[ 0.4691, -0.2829, -1.5091, -1.1356],
# [ 1.2121, -0.1732, 0.1192, -1.0442],
# [-0.8618, -2.1046, -0.4949, 1.0718],
# [ 0.7216, -0.7068, -1.0396, 0.2719],
# [-0.425 , 0.567 , 0.2762, -1.0874],
# [-0.6737, 0.1136, -1.4784, 0.525 ]])

# back to original df2

# For df2, the DataFrame with multiple dtypes, DataFrame.to_numpy() is relatively
# expensive:
df2.to_numpy()

# describe() shows a quick statistic summary of your data
# df.describe()

# output
# Out[19]:
# A B C D
# count 6.000000 6.000000 6.000000 6.000000
# mean 0.073711 -0.431125 -0.687758 -0.233103
# std 0.843157 0.922818 0.779887 0.973118
# min -0.861849 -2.104569 -1.509059 -1.135632
# 25% -0.611510 -0.600794 -1.368714 -1.076610
# 50% 0.022070 -0.228039 -0.767252 -0.386188
# 75% 0.658444 0.041933 -0.034326 0.461706
# max 1.212112 0.567020 0.276232 1.071804

# Transposing your data (flipping)
# df.T
# output:
# Out[20]:
# 2013-01-01 2013-01-02 2013-01-03 2013-01-04 2013-01-05 2013-01-06
# A 0.469112 1.212112 -0.861849 0.721555 -0.424972 -0.673690
# B -0.282863 -0.173215 -2.104569 -0.706771 0.567020 0.113648
# C -1.509059 0.119209 -0.494929 -1.039575 0.276232 -1.478427
# D -1.135632 -1.044236 1.071804 0.271860 -1.087401 0.524988

# sorting by axis
# df.sort_index(axis=1, ascending=False)
# output
# Out[21]:
# D C B A
# 2013-01-01 -1.135632 -1.509059 -0.282863 0.469112
# 2013-01-02 -1.044236 0.119209 -0.173215 1.212112
# 2013-01-03 1.071804 -0.494929 -2.104569 -0.861849
# 2013-01-04 0.271860 -1.039575 -0.706771 0.721555
# 2013-01-05 -1.087401 0.276232 0.567020 -0.424972
# 2013-01-06 0.524988 -1.478427 0.113648 -0.673690





# since the data doesn't work im gonna copy everything and sort it later lol




#  sorts by values:
# df.sort_values(by="B")
# Out[22]:
# A B C D
# 2013-01-03 -0.861849 -2.104569 -0.494929 1.071804
# 2013-01-04 0.721555 -0.706771 -1.039575 0.271860
# 2013-01-01 0.469112 -0.282863 -1.509059 -1.135632
# 2013-01-02 1.212112 -0.173215 0.119209 -1.044236
# 2013-01-06 -0.673690 0.113648 -1.478427 0.524988
# 2013-01-05 -0.424972 0.567020 0.276232 -1.087401
# Selecting a single column, which yields a Series, equivalent to df.A:
# Programming for Data Science
# pandas.pydata.org, 2023
# df["A"]
# Out[23]:
# 2013-01-01 0.469112
# 2013-01-02 1.212112
# 2013-01-03 -0.861849
# 2013-01-04 0.721555
# 2013-01-05 -0.424972
# 2013-01-06 -0.673690
# Freq: D, Name: A, dtype: float64
# Selecting via [] (__getitem__), which slices the rows:
# df[0:3]
# Out[24]:
# A B C D
# 2013-01-01 0.469112 -0.282863 -1.509059 -1.135632
# 2013-01-02 1.212112 -0.173215 0.119209 -1.044236
# 2013-01-03 -0.861849 -2.104569 -0.494929 1.071804
# df["20130102":"20130104"]
# Out[25]:
# A B C D
# 2013-01-02 1.212112 -0.173215 0.119209 -1.044236
# 2013-01-03 -0.861849 -2.104569 -0.494929 1.071804
# 2013-01-04 0.721555 -0.706771 -1.039575 0.271860
# Selection by label
# For getting a cross section using a label:
# df.loc[dates[0]]
# Out[26]:
# A 0.469112
# B -0.282863
# C -1.509059
# D -1.135632
# Name: 2013-01-01 00:00:00, dtype: float64
# Selecting on a multi-axis by label:
# df.loc[:, ["A", "B"]]
# Out[27]:
# A B
# 2013-01-01 0.469112 -0.282863
# 2013-01-02 1.212112 -0.173215
# 2013-01-03 -0.861849 -2.104569
# 2013-01-04 0.721555 -0.706771
# 2013-01-05 -0.424972 0.567020
# 2013-01-06 -0.673690 0.113648
# Programming for Data Science
# pandas.pydata.org, 2023
# Showing label slicing, both endpoints are included:
# df.loc["20130102":"20130104", ["A", "B"]]
# Out[28]:
# A B
# 2013-01-02 1.212112 -0.173215
# 2013-01-03 -0.861849 -2.104569
# 2013-01-04 0.721555 -0.706771
# Reduction in the dimensions of the returned object:
# df.loc["20130102", ["A", "B"]]
# Out[29]:
# A 1.212112
# B -0.173215
# Name: 2013-01-02 00:00:00, dtype: float64
# For getting a scalar value:
# df.loc[dates[0], "A"]
# Out[30]: 0.4691122999071863
# For getting fast access to a scalar (equivalent to the prior method):
# df.at[dates[0], "A"]
# Out[31]: 0.4691122999071863
# Selection by position
# See more in Selection by Position using DataFrame.iloc() or DataFrame.at().
# Select via the position of the passed integers:
# df.iloc[3]
# Out[32]:
# A 0.721555
# B -0.706771
# C -1.039575
# D 0.271860
# Name: 2013-01-04 00:00:00, dtype: float64
# By integer slices, acting similar to NumPy/Python:
# df.iloc[3:5, 0:2]
# Out[33]:
# A B
# 2013-01-04 0.721555 -0.706771
# 2013-01-05 -0.424972 0.567020
# Programming for Data Science
# pandas.pydata.org, 2023
# By lists of integer position locations, similar to the NumPy/Python style:
# df.iloc[[1, 2, 4], [0, 2]]
# Out[34]:
# A C
# 2013-01-02 1.212112 0.119209
# 2013-01-03 -0.861849 -0.494929
# 2013-01-05 -0.424972 0.276232
# For slicing rows explicitly:
# df.iloc[1:3, :]
# Out[35]:
# A B C D
# 2013-01-02 1.212112 -0.173215 0.119209 -1.044236
# 2013-01-03 -0.861849 -2.104569 -0.494929 1.071804
# For slicing columns explicitly:
# df.iloc[:, 1:3]
# Out[36]:
# B C
# 2013-01-01 -0.282863 -1.509059
# 2013-01-02 -0.173215 0.119209
# 2013-01-03 -2.104569 -0.494929
# 2013-01-04 -0.706771 -1.039575
# 2013-01-05 0.567020 0.276232
# 2013-01-06 0.113648 -1.478427
# For getting a value explicitly:
# df.iloc[1, 1]
# Out[37]: -0.17321464905330858
# For getting fast access to a scalar (equivalent to the prior method):
# df.iat[1, 1]
# Out[38]: -0.17321464905330858
# Boolean indexing
# df[df["A"] > 0]
# Out[39]:
# Programming for Data Science
# pandas.pydata.org, 2023
# A B C D
# 2013-01-01 0.469112 -0.282863 -1.509059 -1.135632
# 2013-01-02 1.212112 -0.173215 0.119209 -1.044236
# 2013-01-04 0.721555 -0.706771 -1.039575 0.271860
# Selecting values from a DataFrame where a boolean condition is met:
# df[df > 0]
# Out[40]:
# A B C D
# 2013-01-01 0.469112 NaN NaN NaN
# 2013-01-02 1.212112 NaN 0.119209 NaN
# 2013-01-03 NaN NaN NaN 1.071804
# 2013-01-04 0.721555 NaN NaN 0.271860
# 2013-01-05 NaN 0.567020 0.276232 NaN
# 2013-01-06 NaN 0.113648 NaN 0.524988
# Using the isin() method for filtering:
# df2 = df.copy()
# df2["E"] = ["one", "one", "two", "three", "four", "three"]
# df2
# Out[43]:
# A B C D E
# 2013-01-01 0.469112 -0.282863 -1.509059 -1.135632 one
# 2013-01-02 1.212112 -0.173215 0.119209 -1.044236 one
# 2013-01-03 -0.861849 -2.104569 -0.494929 1.071804 two
# 2013-01-04 0.721555 -0.706771 -1.039575 0.271860 three
# 2013-01-05 -0.424972 0.567020 0.276232 -1.087401 four
# 2013-01-06 -0.673690 0.113648 -1.478427 0.524988 three
# df2[df2["E"].isin(["two", "four"])]
# Out[44]:
# A B C D E
# 2013-01-03 -0.861849 -2.104569 -0.494929 1.071804 two
# 2013-01-05 -0.424972 0.567020 0.276232 -1.087401 four
# Setting
# Setting a new column automatically aligns the data by the indexes:
# s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))
# In [46]: s1
# Out[46]:
# 2013-01-02 1
# 2013-01-03 2
# Programming for Data Science
# pandas.pydata.org, 2023
# 2013-01-04 3
# 2013-01-05 4
# 2013-01-06 5
# 2013-01-07 6
# Freq: D, dtype: int64
# df["F"] = s1
# Setting values by label:
# df.at[dates[0], "A"] = 0
# Setting values by position:
# df.iat[0, 1] = 0
# Setting by assigning with a NumPy array:
# df.loc[:, "D"] = np.array([5] * len(df))
# The result of the prior setting operations:
# df
# Out[51]:
# A B C D F
# 2013-01-01 0.000000 0.000000 -1.509059 5 NaN
# 2013-01-02 1.212112 -0.173215 0.119209 5 1.0
# 2013-01-03 -0.861849 -2.104569 -0.494929 5 2.0
# 2013-01-04 0.721555 -0.706771 -1.039575 5 3.0
# 2013-01-05 -0.424972 0.567020 0.276232 5 4.0
# 2013-01-06 -0.673690 0.113648 -1.478427 5 5.0
# A where operation with setting:
# df2 = df.copy()
# df2[df2 > 0] = -df2
# df2
# Out[54]:
# A B C D F
# 2013-01-01 0.000000 0.000000 -1.509059 -5 NaN
# 2013-01-02 -1.212112 -0.173215 -0.119209 -5 -1.0
# 2013-01-03 -0.861849 -2.104569 -0.494929 -5 -2.0
# 2013-01-04 -0.721555 -0.706771 -1.039575 -5 -3.0
# 2013-01-05 -0.424972 -0.567020 -0.276232 -5 -4.0
# Programming for Data Science
# pandas.pydata.org, 2023
# 2013-01-06 -0.673690 -0.113648 -1.478427 -5 -5.0
# String Methods
# Series is equipped with a set of string processing methods in the str attribute that make it
# easy to operate on each element of the array, as in the code snippet below. Note that
# pattern-matching in str generally uses regular expressions by default (and in some cases
# always uses them). See more at Vectorized String Methods.
# s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])
# s.str.lower()
# Out[72]:
# 0 a
# 1 b
# 2 c
# 3 aaba
# 4 baca
# 5 NaN
# 6 caba
# 7 dog
# 8 cat
# dtype: object
# Time series
# pandas has simple, powerful, and efficient functionality for performing resampling
# operations during frequency conversion (e.g., converting secondly data into 5-minutely
# data). This is extremely common in, but not limited to, financial applications. See
# the Time Series section.
# rng = pd.date_range("1/1/2012", periods=100, freq="S")
# ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
# ts.resample("5Min").sum()
# Out[106]:
# 2012-01-01 24182
# Freq: 5T, dtype: int64
# Series.tz_localize() localizes a time series to a time zone:
# rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D")
# ts = pd.Series(np.random.randn(len(rng)), rng)
# Programming for Data Science
# pandas.pydata.org, 2023
# ts
# Out[109]:
# 2012-03-06 1.857704
# 2012-03-07 -1.193545
# 2012-03-08 0.677510
# 2012-03-09 -0.153931
# 2012-03-10 0.520091
# Freq: D, dtype: float64
# ts_utc = ts.tz_localize("UTC")
# ts_utc
# Out[111]:
# 2012-03-06 00:00:00+00:00 1.857704
# 2012-03-07 00:00:00+00:00 -1.193545
# 2012-03-08 00:00:00+00:00 0.677510
# 2012-03-09 00:00:00+00:00 -0.153931
# 2012-03-10 00:00:00+00:00 0.520091
# Freq: D, dtype: float64
# Series.tz_convert() converts a timezones aware time series to another time zone
# ts_utc.tz_convert("US/Eastern")
# Out[112]:
# 2012-03-05 19:00:00-05:00 1.857704
# 2012-03-06 19:00:00-05:00 -1.193545
# 2012-03-07 19:00:00-05:00 0.677510
# 2012-03-08 19:00:00-05:00 -0.153931
# 2012-03-09 19:00:00-05:00 0.520091
# Freq: D, dtype: float64