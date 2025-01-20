# Example from: https://github.com/PablocFonseca/streamlit-aggrid-examples (Author of Streamlit-aggrid)
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode, GridUpdateMode
import pandas as pd
import numpy as np
import requests

url = "https://www.ag-grid.com/example-assets/master-detail-data.json"
r  = requests.get(url)
data = r.json()


df = pd.read_json(url)
AgGrid(df, key="original")
df["callRecords"] = df["callRecords"].apply(lambda x: pd.json_normalize(x))

gridOptions = {
    # MasterDetail: refers to a top level grid called a Master Grid having rows that expand
    "masterDetail": True,
    # Like we saw earlier, and enable the selection of a single column
    "rowSelection": "single",
    # the first Column is configured to use agGroupCellRenderer
    "columnDefs": [
        {
            "field": "name",
            "cellRenderer": "agGroupCellRenderer",
            "checkboxSelection": True,
        },
        {"field": "account"},
        {"field": "calls"},
        {"field": "minutes", "valueFormatter": "x.toLocaleString() + 'm'"},
    ],
    "defaultColDef": {
        "flex": 1,
    },
    # provide Detail Cell Renderer Params
    "detailCellRendererParams": {
        # provide the Grid Options to use on the Detail Grid
        "detailGridOptions": {
            "rowSelection": "multiple",
            "suppressRowClickSelection": True,
            "enableRangeSelection": True,
            "pagination": True,
            "paginationAutoPageSize": True,
            "columnDefs": [
                {"field": "callId", "checkboxSelection": True},
                {"field": "direction"},
                {"field": "number", "minWidth": 150},
                {"field": "duration", "valueFormatter": "x.toLocaleString() + 's'"},
                {"field": "switchCode", "minWidth": 150},
            ],
            "defaultColDef": {
                "sortable": True,
                "flex": 1,
            },
        },
        # get the rows for each Detail Grid
        "getDetailRowData": JsCode(
            """function (params) {
                params.successCallback(params.data.callRecords);
    }"""
        ),
        
    },
    "rowData": data
}

tabs = st.tabs(["Grid", "Underlying Data", "Grid Options", "Grid Return"])

with tabs[0]:
    r = AgGrid(
        None,
        gridOptions=gridOptions,
        allow_unsafe_jscode=True,
        enable_enterprise_modules=True,
        key="an_unique_key",
    )

with tabs[1]:
    st.write(data)

with tabs[2]:
    st.write(gridOptions)