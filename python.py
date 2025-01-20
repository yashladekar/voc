
# import sys
# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # Set page configuration
# st.set_page_config(
#     page_title="VOC αlpha - JLR",
#     layout='wide',
#     initial_sidebar_state='expanded',
#     page_icon="JLR_Blue_Logo.svg"
# )

# # Load custom CSS
# def load_css():
#     try:
#         with open('style.css') as f:
#             st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
#     except FileNotFoundError:
#         st.warning("CSS file not found. Proceeding without custom styling.")

# # Sidebar components
# def render_sidebar(pages):
#     with st.sidebar:
#         st.markdown('<div class="title-container"><h1>Jaguar Land Rover VoC αlpha</h1></div>', unsafe_allow_html=True)

#         if 'selected_page' not in st.session_state:
#             st.session_state.selected_page = "Security Dashboard"

#         st.session_state.selected_page = st.selectbox(
#             "Navigate to",
#             list(pages.keys()),
#             index=list(pages.keys()).index(st.session_state.selected_page),
#             label_visibility="collapsed"
#         )

#         st.divider()
#         st.header("Action Center")
#         with st.container():
#             col1, col2 = st.columns(2)
#             with col1:
#                 if st.button("EVA25", use_container_width=True):
#                     st.session_state.selected_page = "Security Dashboard"
#             with col2:
#                 if st.button("SDV", use_container_width=True):
#                     st.session_state.selected_page = "SDV"

#         st.sidebar.markdown('---')
#         st.sidebar.markdown('''
#         Created by Cyber Security Team
#         ---
#         ''')
#         st.sidebar.markdown("""
#             <div class="sidebar-footer">
#                 <p class="footer-text">© 2024 <i>Jaguar Land Rover</i>  <br> <i>Confidential & Internal</i></p>
#                 <div class="footer-links">
#                     <a href="https://www.jaguarlandrover.com/privacy">Privacy</a>
#                     <a href="https://www.jaguarlandrover.com/terms-and-conditions">Terms</a>
#                     <a href="https://www.jaguarlandrover.com/contact-us">Support</a>
#                 </div>
#             </div>
#         """, unsafe_allow_html=True)

# # Main page function
# def main():
#     pages = {
#         "Security Dashboard": Events_Dashboard,
#         "Diagnostic Search": Search_Page,
#         "SDV": SDV_Page
#     }

#     render_sidebar(pages)

#     page_function = pages[st.session_state.selected_page]
#     page_function()

#     st.markdown('---')

# # Events Dashboard Page
# def Events_Dashboard():
#     st.title("Analysis Dashboard")

#     # IDS Analysis Section
#     st.header("IDS Analysis")
#     uploaded_ids_file = st.file_uploader("Upload IDS CSV file", type="csv", key="ids_file")
#     if uploaded_ids_file:
#         handle_ids_csv(uploaded_ids_file)
#     else:
#         st.info("Please upload an IDS CSV file to proceed.")

#     st.markdown('---')

#     # VCDP Analysis Section
#     st.header("VCDP Analysis")
#     uploaded_vcdp_file = st.file_uploader("Upload VCDP CSV file", type="csv", key="vcdp_file")
#     if uploaded_vcdp_file:
#         handle_vcdp_csv(uploaded_vcdp_file)
#     else:
#         st.info("Please upload a VCDP CSV file to proceed.")

# # Handle IDS CSV Upload
# def handle_ids_csv(uploaded_file):
#     try:
#         df = pd.read_csv(uploaded_file)

#         # Ensure required columns are present
#         required_columns = ['timestamp', 'severity', 'severity_level']
#         if not all(col in df.columns for col in required_columns):
#             st.error(f"The uploaded file must contain the following columns: {', '.join(required_columns)}")
#             return

#         # Data cleaning and transformation
#         df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
#         df.dropna(subset=['timestamp'], inplace=True)
#         df['severity'] = df['severity'].fillna('Unknown')

#         severity_count = df.groupby([df['timestamp'].dt.date, 'severity']).size().reset_index(name='count')
#         severity_pivot = severity_count.pivot(index='timestamp', columns='severity', values='count').fillna(0).astype(int)
#         severity_pivot['Total Count'] = severity_pivot.sum(axis=1)

#         all_dates = ['All'] + sorted(severity_pivot.index.astype(str))
#         all_severities = ['All'] + sorted(severity_count['severity'].unique())

#         # Filters
#         st.subheader("Filters")
#         col_date, col_severity = st.columns(2)
#         with col_date:
#             selected_date = st.selectbox("Select Date", all_dates, index=0)
#         with col_severity:
#             selected_severity = st.selectbox("Select Severity", all_severities, index=0)

#         filtered_df = severity_count.copy()
#         if selected_date != 'All':
#             filtered_df = filtered_df[filtered_df['timestamp'].astype(str) == selected_date]
#         if selected_severity != 'All':
#             filtered_df = filtered_df[filtered_df['severity'] == selected_severity]

#         def highlight_rows(row):
#             if (selected_date == 'All' or str(row.name) == selected_date) and (
#                 selected_severity == 'All' or selected_severity in row.index
#             ):
#                 return ['background-color: yellow' if col == selected_severity else '' for col in row.index]
#             else:
#                 return [''] * len(row)

#         st.subheader("Event Trends")
#         create_bar_chart(severity_count, 'timestamp', 'count', 'severity', 'Event Count Over Time')

#         col1, col2, col3 = st.columns([3, 2, 2])

#         with col1:
#             st.subheader("Day-wise Event Count Details")
#             styled_table = severity_pivot.style.apply(highlight_rows, axis=1)
#             st.write(styled_table)

#         with col2:
#             st.subheader("Severity Distribution")
#             total_severity = severity_count.groupby('severity')['count'].sum().reset_index()
#             create_pie_chart(total_severity, 'severity', 'count', "Severity Distribution")

#         with col3:
#             st.subheader("Radar Chart: Severity Trends")
#             radar_fig = create_radar_chart(filtered_df)
#             st.plotly_chart(radar_fig, use_container_width=True)

#     except Exception as e:
#         st.error(f"An error occurred while processing the IDS file: {e}")

# def create_bar_chart(data, x_col, y_col, color_col, title):
#     try:
#         fig = px.bar(
#             data,
#             x=x_col,
#             y=y_col,
#             color=color_col,
#             title=title,
#             labels={x_col: "Timestamp", y_col: "Event Count"},
#             template='plotly_white'
#         )
#         st.plotly_chart(fig, use_container_width=True)
#     except Exception as e:
#         st.error(f"Error generating chart: {e}")

# def create_pie_chart(data, names_col, values_col, title):
#     try:
#         fig = px.pie(
#             data,
#             names=names_col,
#             values=values_col,
#             title=title,
#             template='plotly_white'
#         )
#         st.plotly_chart(fig, use_container_width=True)
#     except Exception as e:
#         st.error(f"Error generating pie chart: {e}")

# def create_radar_chart(data):
#     try:
#         fig = px.line_polar(
#             data,
#             r='count',
#             theta='severity',
#             color='severity',
#             title='Severity Trends',
#             template='plotly_white'
#         )
#         return fig
#     except Exception as e:
#         st.error(f"Error generating radar chart: {e}")
#         return None

# # Handle VCDP CSV Upload
# def handle_vcdp_csv(uploaded_file):
#     try:
#         df = pd.read_csv(uploaded_file)

#         required_columns = ['Date', 'Message']
#         if not all(col in df.columns for col in required_columns):
#             st.error(f"The uploaded file must contain the following columns: {', '.join(required_columns)}")
#             return

#         df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
#         df.dropna(subset=['Date'], inplace=True)

#         message_count = df.groupby(['Date', 'Message']).size().reset_index(name='count')
#         total_message_count = df.groupby(df['Date'].dt.date).size().reset_index(name='total_count')

#         create_bar_chart(total_message_count, 'Date', 'total_count', 'Date', 'Total Event Count Per Day')

#         col1, col2 = st.columns([2, 1])

#         with col1:
#             st.subheader("Day-wise Message Count Details")
#             st.write(message_count)

#         with col2:
#             message_distribution = df.groupby('Message').size().reset_index(name='count')
#             create_pie_chart(message_distribution, 'Message', 'count', "Message Distribution")

#     except Exception as e:
#         st.error(f"An error occurred while processing the VCDP file: {e}")

# # Diagnostic Search Page
# def Search_Page():
#     st.subheader("Diagnostic Search Page")
#     st.markdown('<style> div.block-container{padding-top:2rem;} </style>', unsafe_allow_html=True)

#     search_input = st.text_input("Enter a VIN Number to search:")
#     if st.button("Search"):
#         if search_input:
#             query = f"""
#                 SELECT *
#                 FROM VOC_DASH_DUMMY_DB.VOC_VEHICLE.VEHICLE_DETAILS_DYNAMIC
#                 WHERE VIN_NUMBER = '{search_input}'
#             """
#             vehicle_data = execute_snowflake_query(query)

#             if not vehicle_data.empty:
#                 display_info(search_input, vehicle_data)
#             else:
#                 st.warning("No data found for the given VIN number.")
#         else:
#             st.warning("Please enter a value to search.")

# # SDV Page
# def SDV_Page():
#     st.title("SDV Page")
#     st.write("This is the SDV page content.")

# if __name__ == "__main__":
#     load_css()
#     main()


import streamlit as st
import pandas as pd

# Sample data for the main table
main_data = {
    "Category": ["Fruits", "Vegetables", "Dairy"],
    "Count": [5, 8, 4]
}
main_df = pd.DataFrame(main_data)

# Nested data for each category
nested_data = {
    "Fruits": {"Name": ["Apple", "Banana", "Cherry", "Date", "Fig"], "Price": [1.2, 0.5, 2.5, 3.0, 2.0]},
    "Vegetables": {"Name": ["Carrot", "Broccoli", "Spinach", "Potato", "Onion", "Tomato", "Cucumber", "Pepper"], "Price": [0.8, 1.5, 1.2, 0.6, 0.7, 0.9, 1.0, 1.3]},
    "Dairy": {"Name": ["Milk", "Cheese", "Yogurt", "Butter"], "Price": [1.5, 3.0, 2.0, 4.0]}
}

# Display the main table
st.write("### Main Table")
st.table(main_df)

# Dropdown to select a category
selected_category = st.selectbox("Select a Category:", main_df["Category"])

# Display the nested table when a category is selected
if selected_category:
    st.write(f"### Details for {selected_category}")
    nested_df = pd.DataFrame(nested_data[selected_category])
    st.table(nested_df)
