

import streamlit as st
import pandas as pd

html_str = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script type="text/javascript">
      function hide_row(row1, row2, row3) {
        $("#" + row1).toggle();
        $("#" + row2).toggle();
        $("#" + row3).toggle();
      }
    </script>
    <style>
      body {
        font-size: 16px;
        font-family: Arial, Helvetica, sans-serif;
      }
      h1 {
        text-align: center;
      }
      table {
        width: 700px;
      }
      table,
      td,
      th {
        border: 2px solid #000;
        border-collapse: collapse;
      }
      td,
      th {
        padding: 1px 1px;
      }
      /* Set sticky for table */
      .table.table-ontrack thead th.first_col,
      tbody th.first_col,
      tbody td.first_col {
        position: sticky;
        left: 0;
      }
      #first_col_1 {
        background-color: #4793af;
      }
      #first_col_2 {
        background-color: #000;
      }
      #first_col_3 {
        background-color: #e3f4f4;
      }
      #first_col_4 {
        background-color: #fff;
      }
      .table.table-ontrack thead tr.metric_title1 {
        font-size: 20px;
        background: #4793af;
        text-align: center;
      }
      .table.table-ontrack thead tr.metric_title1 th.metric {
        background: #dddddd;
        border-right: 2px solid #1a4d2e;
      }
      .table.table-ontrack thead tr.metric_title2 {
        text-align: center;
      }
      .table.table-ontrack thead tr.metric_title2 th.estimate {
        background: yellow;
        border-right: 2px solid #1a4d2e;
      }
      .table.table-ontrack thead tr.metric_title1 th.convert_rate {
        background: #f5eec8;
        border-right: 2px solid #1a4d2e;
      }
      .table.table-ontrack tbody tr.metric_total {
        font-size: 18px;
        background: #000;
        color: #fff;
        text-align: center;
        border-right: 2px solid #1a4d2e;
      }
      .table.table-ontrack tbody tr.owned_traffic,
      tr.owned_e2e {
        font-size: 17px;
        background: #e3f4f4;
        text-align: center;
      }
      .table.table-ontrack tbody td.first_col {
        text-align: left;
      }
      .table.table-ontrack tbody tr.traffic_sources {
        text-align: right;
      }
      .st-emotion-cache-eqffof th,
      .st-emotion-cache-eqffof td {
        padding: 1px 4px;
      }
      .table.table-ontrack tbody th.border_right_subtotal {
        border-right: 2px solid #1a4d2e;
      }
      .table.talbe-ontrack tbody th.metric_border,
      td.metric_border {
        border-right: 2px solid #1a4d2e;
      }
    </style>
  </head>
  <body>
    <table class="table table-ontrack">
      <thead>
        <tr class="metric_title1">
          <th class="first_col" id="first_col_1" rowspan="2">
            Traffic<br />Report
          </th>
          <th class="metric" colspan="6">Traffic</th>
        </tr>
        <tr class="metric_title2">
          <!-- 1. Metric Title -->
          <!-- Traffic -->
          <th>KPI</th>
          <th>Actual</th>
          <th>Last<br />month</th>
          <th>
            Period<br />
            Comparison
          </th>
          <th>GAP</th>
          <th class="estimate">Estimate</th>
        </tr>
      </thead>
      <tbody>
        <!-- Total Owned Traffic -->
        <tr onclick="hide_row('row1', 'row2', 'row3');" class="owned_traffic">
          <th class="first_col" id="first_col_3">Total</th>
          <!-- Traffic -->
          <th>500,246</th>
          <th>276,384</th>
          <th>258,051</th>
          <th>7%</th>
          <th>223,862</th>
          <th class="border_right_subtotal">84%</th>
        </tr>
        <!-- Hotline -->
        <tr class="traffic_sources" id="row1">
          <td class="first_col" id="first_col_4">Hotline</td>
          <!-- Traffic -->
          <td>7,836</td>
          <td>5,939</td>
          <td>5,234</td>
          <td>13%</td>
          <td>1,897</td>
          <td class="metric_border">76%</td>
        </tr>
        <!-- Facebook -->
        <tr class="traffic_sources" id="row2">
          <td class="first_col" id="first_col_4">Facebook</td>
          <!-- Traffic -->
          <td>6,278</td>
          <td>3,649</td>
          <td>4,260</td>
          <td>-14%</td>
          <td>2,629</td>
          <td class="metric_border">58%</td>
        </tr>
        <!-- SEO -->
        <tr class="traffic_sources" id="row3">
          <td class="first_col" id="first_col_4">SEO</td>
          <!-- Traffic -->
          <td>492,410</td>
          <td>266,796</td>
          <td>248,557</td>
          <td>4%</td>
          <td>248,557</td>
          <td class="metric_border">84%</td>
        </tr>
      </tbody>
    </table>
  </body>
</html>
...

'''
st.components.v1.html(html_str, height=200, width=800, scrolling=True)

import streamlit as st
import pandas as pd

# Sample data for the initial table
data = {
    'Item': ['Hotline', 'Facebook', 'SEO'],
    'KPI': [7836, 6278, 492410],
    'Actual': [5939, 3649, 266796],
    'Last month': [5234, 4260, 248557],
    'Period Comparison': ['13%', '-14%', '4%'],
    'GAP': [1897, 2629, 248557],
    'Estimate': ['76%', '58%', '84%']
}

# DataFrame for the main table
df = pd.DataFrame(data)

# Streamlit app
st.title("Interactive Data Table")

# Display the main table
st.dataframe(df)

# Display details of the clicked KPI
if st.button('Show details for KPI 7,836'):
    st.subheader("Details")
    details = {'Name': 'Yash', 'Age': 23}
    details_df = pd.DataFrame(details.items(), columns=['Attribute', 'Value'])
    st.table(details_df)