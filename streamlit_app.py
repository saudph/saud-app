import streamlit as st
import pandas as pd

st.title('Data Cleaning')
st.subheader('Upload a CSV file to get started')
# Load data
data = st.sidebar.file_uploader('Upload a CSV file', type=['csv'])

if data is not None:
    df = pd.read_csv(data)
    st.dataframe(df.head())

    # Show column names
    if st.checkbox('Show column names'):
        st.write(df.columns)

    # Show column data types
    if st.checkbox('Show column data types'):
        st.write(df.dtypes)

    # Show missing values
    if st.checkbox('Show missing values'):
        st.write(df.isnull().sum())

    # Show summary statistics
    if st.checkbox('Show summary statistics'):
        st.write(df.describe())

    # Show value counts
    if st.checkbox('Show value counts'):
        column = st.selectbox('Select a column', df.columns)
        st.write(df[column].value_counts())

    # Show correlation
    if st.checkbox('Show correlation'):
        st.write(df.corr())

    # Show heatmap
    if st.checkbox('Show heatmap'):
        st.heatmap(df.corr())

    # Show scatter plot
    if st.checkbox('Show scatter plot'):
        x = st.selectbox('Select x-axis', df.columns)
        y = st.selectbox('Select y-axis', df.columns)
        st.write(df.plot.scatter(x=x, y=y))

    # Show histogram
    if st.checkbox('Show histogram'):
        column = st.selectbox('Select a column', df.columns)
        st.write(df[column].plot.hist())

    # Show box plot
    if st.checkbox('Show box plot'):
        column = st.selectbox('Select a column', df.columns)
        st.write(df[column].plot.box())

    # Show line plot
    if st.checkbox('Show line plot'):
        column = st.selectbox('Select a column', df.columns)
        st.write(df[column].plot.line())

    # Show bar plot

    if st.checkbox('Show bar plot'):
        column = st.selectbox('Select a column', df.columns)
        st.write(df[column].value_counts().plot.bar())

    # Show pie chart
    if st.checkbox('Show pie chart'):
        column = st.selectbox('Select a column', df.columns)
        st.write(df[column].value_counts().plot.pie())

    # Show scatter matrix
    if st.checkbox('Show scatter matrix'):
        st.write(pd.plotting.scatter_matrix(df))

    # clean empty columns
    if st.checkbox('Clean empty columns'):
        df = df.dropna(axis=1, how='all')
        st.write(df)






