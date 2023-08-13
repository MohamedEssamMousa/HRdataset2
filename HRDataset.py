import pandas as pd
import streamlit as st
import plotly.express as px
import base64
from io import StringIO, BytesIO

data = pd.read_excel("C:/Users/Dell/Desktop/Test_analysis/HRDataset_v14.xlsx")

# df = data[['EmpID', 'MarriedID', 'MaritalStatusID', 'GenderID','EmpStatusID', 'DeptID', 'Salary']]
# coloration_mat = df.corr()

# fig_corr = px.imshow(coloration_mat)
# st.plotly_chart(fig_corr)

st.set_page_config(page_title="Project 1")
st.header("HR Analysis")
st.subheader("Deprtment Analysis")
# st.write("Data test")

#%% tabs
tab1, tab2 = st.tabs(["summary", "Deprtment analysis"])

#%% tab2
with tab2:
    col11, col12, col13, col14 = st.columns(4, gap = "large")
    with col11:
        department_sel = st.selectbox( "Department Select",sorted((data['Department'].unique())))
        mask1 = data["Department"] == department_sel
        filtered_data = data[data["Department"] == department_sel]
        employee_count = len(filtered_data)
        st.write("Number of employees in ", department_sel, "Department")
        st.write( employee_count)
    with col12:
        gender_sel = st.multiselect("select gender", data["Sex"].unique())
        mask2 = (data["Sex"].isin(gender_sel))
        percentage = (len(gender_sel) / len(department_sel)) * 100
        st.write(f"Percentage of selected gender: {percentage}%")
    with col13:
        postion_sel = st.selectbox( "choose postion",sorted((data['Position'].unique())))
        mask3 = data["Position"] == postion_sel
        filtered_data2 = data[data["Position"] == postion_sel]
        sum_of_salaries = filtered_data2["Salary"].sum()
        st.write(f"Sum of salaries for Position Group {postion_sel}")
        st.write(sum_of_salaries)
    # with col14:
    #     filtered_data4 = data[data['Position'].str.contains('Manager', case=False)]
    #     positions = filtered_data4['Position'].unique().tolist()
    #     selected_position = st.selectbox('Select Manger', positions)
    #     position_data = filtered_data[filtered_data['Position'] == selected_position]
#%%
    col21, col22, col23, col24 = st.columns(4, gap = "large")
    with col21:
        other_count = len(data) - employee_count
        counts = [employee_count, other_count]
        labels = [department_sel, 'Other Department']
        pie_data = pd.DataFrame({'Counts': counts, 'Labels': labels})
        fig = px.pie(pie_data, values='Counts', names='Labels')
        st.plotly_chart(fig)
    with col23:
        fig = px.histogram(data, x='PerfScoreID', nbins=12, title='Managers performance')
        st.plotly_chart(fig)