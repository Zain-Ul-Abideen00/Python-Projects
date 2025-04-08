import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import io

# Set page configuration
st.set_page_config(
    page_title="Data Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title and description
st.title("📊 Data Analytics Dashboard")
st.write("Upload your CSV file for analysis")

# File upload section
uploaded_file = st.file_uploader(
    "Upload your CSV file",
    type=['csv'],
    help="Upload a CSV file with your data"
)

# Initialize empty dataframe
df = pd.DataFrame()

if uploaded_file is not None:
    try:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)

        # Display data preview
        st.subheader("Data Preview")
        st.write(df.head())

        # Get categorical and numeric columns
        categorical_columns = df.select_dtypes(include=['object', 'category']).columns.tolist()
        numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

        # Convert date column if it exists
        if 'Date' in df.columns:
            try:
                df['Date'] = pd.to_datetime(df['Date'])
            except:
                st.warning("Could not convert 'Date' column to datetime format")

        # Create two columns for filters
        st.subheader("Data Filters")
        filter_col1, filter_col2 = st.columns(2)

        # Date filter (if Date column exists)
        if 'Date' in df.columns:
            with filter_col1:
                date_range = st.date_input(
                    "Select Date Range",
                    value=(df['Date'].min(), df['Date'].max()),
                    min_value=df['Date'].min(),
                    max_value=df['Date'].max()
                )

        # Create filters for categorical columns
        filters = {}
        with filter_col2:
            for col in categorical_columns:
                if col != 'Date':
                    unique_values = df[col].unique()
                    filters[col] = st.multiselect(
                        f"Select {col}",
                        options=unique_values,
                        default=unique_values
                    )

        # Filter data based on selections
        filtered_df = df.copy()

        if 'Date' in df.columns:
            filtered_df = filtered_df[
                (filtered_df['Date'].dt.date >= date_range[0]) &
                (filtered_df['Date'].dt.date <= date_range[1])
            ]

        for col, values in filters.items():
            if values:
                filtered_df = filtered_df[filtered_df[col].isin(values)]

        # Create metrics for numeric columns
        if numeric_columns:
            st.subheader("Key Metrics")
            metrics_cols = st.columns(min(4, len(numeric_columns)))

            for i, col in enumerate(numeric_columns[:4]):
                with metrics_cols[i]:
                    total = filtered_df[col].sum()
                    original_total = df[col].sum()
                    change = ((total / original_total) - 1) * 100 if original_total != 0 else 0

                    st.metric(
                        f"Total {col}",
                        f"{total:,.0f}",
                        f"{change:.1f}%"
                    )

        # Create tabs for different visualizations
        tab1, tab2, tab3 = st.tabs(["Data Analysis", "Visualizations", "Data Table"])

        with tab1:
            st.subheader("Data Analysis")

            # Summary statistics
            st.write("Summary Statistics")
            st.write(filtered_df[numeric_columns].describe())

            # Correlation matrix
            if len(numeric_columns) > 1:
                st.write("Correlation Matrix")
                corr_matrix = filtered_df[numeric_columns].corr()
                fig = px.imshow(
                    corr_matrix,
                    text_auto=True,
                    title="Correlation Matrix",
                    template='plotly_white'
                )
                st.plotly_chart(fig, use_container_width=True)

        with tab2:
            st.subheader("Visualizations")

            # Column selection for visualization
            viz_col1, viz_col2 = st.columns(2)

            with viz_col1:
                x_axis = st.selectbox(
                    "Select X-axis",
                    options=df.columns,
                    index=0
                )

            with viz_col2:
                y_axis = st.selectbox(
                    "Select Y-axis",
                    options=numeric_columns,
                    index=0
                )

            # Visualization type selection
            viz_type = st.selectbox(
                "Select Visualization Type",
                options=["Line Chart", "Bar Chart", "Scatter Plot", "Pie Chart"],
                index=0
            )

            # Create visualization based on selection
            if viz_type == "Line Chart":
                fig = px.line(
                    filtered_df,
                    x=x_axis,
                    y=y_axis,
                    title=f"{y_axis} by {x_axis}",
                    template='plotly_white'
                )
            elif viz_type == "Bar Chart":
                fig = px.bar(
                    filtered_df,
                    x=x_axis,
                    y=y_axis,
                    title=f"{y_axis} by {x_axis}",
                    template='plotly_white'
                )
            elif viz_type == "Scatter Plot":
                fig = px.scatter(
                    filtered_df,
                    x=x_axis,
                    y=y_axis,
                    title=f"{y_axis} vs {x_axis}",
                    template='plotly_white'
                )
            else:  # Pie Chart
                fig = px.pie(
                    filtered_df,
                    values=y_axis,
                    names=x_axis,
                    title=f"Distribution of {y_axis} by {x_axis}",
                    template='plotly_white'
                )

            st.plotly_chart(fig, use_container_width=True)

        with tab3:
            st.subheader("Data Table")

            # Display filtered data
            st.dataframe(
                filtered_df,
                use_container_width=True,
                hide_index=True
            )

            # Download button for the filtered data
            csv = filtered_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Filtered Data",
                data=csv,
                file_name="filtered_data.csv",
                mime="text/csv"
            )

    except Exception as e:
        st.error(f"Error reading file: {str(e)}")
else:
    st.info("Please upload a CSV file to begin analysis.")

# Footer
st.markdown("---")
st.markdown("### About this Dashboard")
st.markdown("""
This interactive dashboard allows you to analyze your CSV data through various visualizations and metrics.
Upload your CSV file to get started.
""")
