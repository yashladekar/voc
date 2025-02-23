# # Example from: https://github.com/PablocFonseca/streamlit-aggrid-examples (Author of Streamlit-aggrid)
# import streamlit as st
# from st_aggrid import AgGrid, GridOptionsBuilder, JsCode, GridUpdateMode
# import pandas as pd
# import numpy as np
# import requests

# url = "https://www.ag-grid.com/example-assets/master-detail-data.json"
# r  = requests.get(url)
# data = r.json()


# df = pd.read_json(url)
# AgGrid(df, key="original")
# df["callRecords"] = df["callRecords"].apply(lambda x: pd.json_normalize(x))

# gridOptions = {
#     # MasterDetail: refers to a top level grid called a Master Grid having rows that expand
#     "masterDetail": True,
#     # Like we saw earlier, and enable the selection of a single column
#     "rowSelection": "single",
#     # the first Column is configured to use agGroupCellRenderer
#     "columnDefs": [
#         {
#             "field": "name",
#             "cellRenderer": "agGroupCellRenderer",
#             "checkboxSelection": True,
#         },
#         {"field": "account"},
#         {"field": "calls"},
#         {"field": "minutes", "valueFormatter": "x.toLocaleString() + 'm'"},
#     ],
#     "defaultColDef": {
#         "flex": 1,
#     },
#     # provide Detail Cell Renderer Params
#     "detailCellRendererParams": {
#         # provide the Grid Options to use on the Detail Grid
#         "detailGridOptions": {
#             "rowSelection": "multiple",
#             "suppressRowClickSelection": True,
#             "enableRangeSelection": True,
#             "pagination": True,
#             "paginationAutoPageSize": True,
#             "columnDefs": [
#                 {"field": "callId", "checkboxSelection": True},
#                 {"field": "direction"},
#                 {"field": "number", "minWidth": 150},
#                 {"field": "duration", "valueFormatter": "x.toLocaleString() + 's'"},
#                 {"field": "switchCode", "minWidth": 150},
#             ],
#             "defaultColDef": {
#                 "sortable": True,
#                 "flex": 1,
#             },
#         },
#         # get the rows for each Detail Grid
#         "getDetailRowData": JsCode(
#             """function (params) {
#                 params.successCallback(params.data.callRecords);
#     }"""
#         ),
        
#     },
#     "rowData": data
# }

# tabs = st.tabs(["Grid", "Underlying Data", "Grid Options", "Grid Return"])

# with tabs[0]:
#     r = AgGrid(
#         None,
#         gridOptions=gridOptions,
#         allow_unsafe_jscode=True,
#         enable_enterprise_modules=True,
#         key="an_unique_key",
#     )

# with tabs[1]:
#     st.write(data)

# with tabs[2]:
#     st.write(gridOptions)


import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode, GridUpdateMode
import pandas as pd
import numpy as np

# Local JSON data
data = [
    {
        "name": "Nora Thomas",
        "account": 177000,
        "calls": 24,
        "minutes": 25.65,
        "callRecords": [
            {
                "name": "susan",
                "callId": 555,
                "duration": 72,
                "switchCode": "SW3",
                "direction": "Out",
                "number": "(00) 88542069"
            },
            {
                "name": "susan",
                "callId": 556,
                "duration": 61,
                "switchCode": "SW3",
                "direction": "In",
                "number": "(01) 7432576"
            },
            {
                "name": "susan",
                "callId": 557,
                "duration": 90,
                "switchCode": "SW5",
                "direction": "In",
                "number": "(09) 76105491"
            },
            {
                "name": "susan",
                "callId": 558,
                "duration": 83,
                "switchCode": "SW5",
                "direction": "In",
                "number": "(03) 72020613"
            },
            {
                "name": "susan",
                "callId": 559,
                "duration": 94,
                "switchCode": "SW1",
                "direction": "In",
                "number": "(04) 98295709"
            },
            {
                "name": "susan",
                "callId": 560,
                "duration": 102,
                "switchCode": "SW2",
                "direction": "Out",
                "number": "(07) 96771309"
            },
            {
                "name": "susan",
                "callId": 561,
                "duration": 22,
                "switchCode": "SW3",
                "direction": "Out",
                "number": "(08) 38428058"
            },
            {
                "name": "susan",
                "callId": 562,
                "duration": 88,
                "switchCode": "SW2",
                "direction": "Out",
                "number": "(02) 70137438"
            },
            {
                "name": "susan",
                "callId": 563,
                "duration": 77,
                "switchCode": "SW5",
                "direction": "In",
                "number": "(06) 48756154"
            },
            {
                "name": "susan",
                "callId": 564,
                "duration": 85,
                "switchCode": "SW5",
                "direction": "Out",
                "number": "(00) 11319412"
            },
            {
                "name": "susan",
                "callId": 565,
                "duration": 82,
                "switchCode": "SW1",
                "direction": "In",
                "number": "(02) 37557264"
            },
            {
                "name": "susan",
                "callId": 566,
                "duration": 75,
                "switchCode": "SW4",
                "direction": "In",
                "number": "(00) 94729563"
            },
            {
                "name": "susan",
                "callId": 567,
                "duration": 46,
                "switchCode": "SW0",
                "direction": "In",
                "number": "(09) 20489000"
            },
            {
                "name": "susan",
                "callId": 568,
                "duration": 90,
                "switchCode": "SW0",
                "direction": "In",
                "number": "(04) 90652096"
            },
            {
                "name": "susan",
                "callId": 569,
                "duration": 49,
                "switchCode": "SW2",
                "direction": "In",
                "number": "(00) 73342113"
            },
            {
                "name": "susan",
                "callId": 570,
                "duration": 40,
                "switchCode": "SW0",
                "direction": "Out",
                "number": "(01) 79831695"
            },
            {
                "name": "susan",
                "callId": 571,
                "duration": 105,
                "switchCode": "SW8",
                "direction": "In",
                "number": "(03) 28694433"
            },
            {
                "name": "susan",
                "callId": 572,
                "duration": 64,
                "switchCode": "SW9",
                "direction": "In",
                "number": "(03) 8705515"
            },
            {
                "name": "susan",
                "callId": 573,
                "duration": 44,
                "switchCode": "SW7",
                "direction": "In",
                "number": "(01) 180304"
            },
            {
                "name": "susan",
                "callId": 574,
                "duration": 24,
                "switchCode": "SW4",
                "direction": "In",
                "number": "(05) 33983060"
            },
            {
                "name": "susan",
                "callId": 575,
                "duration": 40,
                "switchCode": "SW1",
                "direction": "In",
                "number": "(02) 4129807"
            },
            {
                "name": "susan",
                "callId": 576,
                "duration": 24,
                "switchCode": "SW9",
                "direction": "Out",
                "number": "(01) 89806499"
            },
            {
                "name": "susan",
                "callId": 577,
                "duration": 36,
                "switchCode": "SW5",
                "direction": "In",
                "number": "(09) 13139104"
            },
            {
                "name": "susan",
                "callId": 578,
                "duration": 46,
                "switchCode": "SW6",
                "direction": "In",
                "number": "(06) 8486087"
            }
        ]
    },
    {
        "name": "Mila Smith",
        "account": 177001,
        "calls": 24,
        "minutes": 26.216666666666665,
        "callRecords": [
            {
                "name": "susan",
                "callId": 579,
                "duration": 23,
                "switchCode": "SW5",
                "direction": "Out",
                "number": "(02) 47485405"
            },
            {
                "name": "susan",
                "callId": 580,
                "duration": 52,
                "switchCode": "SW3",
                "direction": "In",
                "number": "(02) 32367069"
            },
            {
                "name": "susan",
                "callId": 581,
                "duration": 39,
                "switchCode": "SW7",
                "direction": "Out",
                "number": "(07) 13532649"
            },
            {
                "name": "susan",
                "callId": 582,
                "duration": 51,
                "switchCode": "SW6",
                "direction": "Out",
                "number": "(08) 45645627"
            },
            {
                "name": "susan",
                "callId": 583,
                "duration": 33,
                "switchCode": "SW3",
                "direction": "In",
                "number": "(07) 40017516"
            },
            {
                "name": "susan",
                "callId": 584,
                "duration": 22,
                "switchCode": "SW4",
                "direction": "In",
                "number": "(01) 92370908"
            },
            {
                "name": "susan",
                "callId": 585,
                "duration": 68,
                "switchCode": "SW3",
                "direction": "In",
                "number": "(05) 30156166"
            },
            {
                "name": "susan",
                "callId": 586,
                "duration": 119,
                "switchCode": "SW6",
                "direction": "In",
                "number": "(01) 52582587"
            },
            {
                "name": "susan",
                "callId": 587,
                "duration": 21,
                "switchCode": "SW8",
                "direction": "In",
                "number": "(05) 10830657"
            },
            {
                "name": "susan",
                "callId": 588,
                "duration": 109,
                "switchCode": "SW9",
                "direction": "In",
                "number": "(05) 10815312"
            },
            {
                "name": "susan",
                "callId": 589,
                "duration": 39,
                "switchCode": "SW7",
                "direction": "Out",
                "number": "(05) 89618828"
            },
            {
                "name": "susan",
                "callId": 590,
                "duration": 108,
                "switchCode": "SW3",
                "direction": "Out",
                "number": "(09) 15893215"
            },
            {
                "name": "susan",
                "callId": 591,
                "duration": 33,
                "switchCode": "SW9",
                "direction": "Out",
                "number": "(03) 24536100"
            },
            {
                "name": "susan",
                "callId": 592,
                "duration": 93,
                "switchCode": "SW9",
                "direction": "Out",
                "number": "(02) 80845157"
            },
            {
                "name": "susan",
                "callId": 593,
                "duration": 114,
                "switchCode": "SW6",
                "direction": "In",
                "number": "(03) 3221324"
            },
            {
                "name": "susan",
                "callId": 594,
                "duration": 26,
                "switchCode": "SW2",
                "direction": "Out",
                "number": "(03) 15136907"
            },
            {
                "name": "susan",
                "callId": 595,
                "duration": 109,
                "switchCode": "SW2",
                "direction": "In",
                "number": "(08) 36133013"
            },
            {
                "name": "susan",
                "callId": 596,
                "duration": 82,
                "switchCode": "SW2",
                "direction": "In",
                "number": "(09) 25025760"
            },
            {
                "name": "susan",
                "callId": 597,
                "duration": 100,
                "switchCode": "SW3",
                "direction": "Out",
                "number": "(02) 2011270"
            },
            {
                "name": "susan",
                "callId": 598,
                "duration": 49,
                "switchCode": "SW4",
                "direction": "Out",
                "number": "(09) 37470979"
            },
            {
                "name": "susan",
                "callId": 599,
                "duration": 43,
                "switchCode": "SW8",
                "direction": "In",
                "number": "(01) 56297516"
            },
            {
                "name": "susan",
                "callId": 600,
                "duration": 99,
                "switchCode": "SW2",
                "direction": "In",
                "number": "(00) 30313801"
            },
            {
                "name": "susan",
                "callId": 601,
                "duration": 95,
                "switchCode": "SW4",
                "direction": "In",
                "number": "(01) 75205393"
            },
            {
                "name": "susan",
                "callId": 602,
                "duration": 46,
                "switchCode": "SW0",
                "direction": "In",
                "number": "(09) 48865412"
            }
        ]
    },
    {
        "name": "Evelyn Taylor",
        "account": 177002,
        "calls": 25,
        "minutes": 30.633333333333333,
        "callRecords": [
            {
                "name": "susan",
                "callId": 603,
                "duration": 80,
                "switchCode": "SW8",
                "direction": "Out",
                "number": "(05) 35713044"
            },
            {
                "name": "susan",
                "callId": 604,
                "duration": 33,
                "switchCode": "SW2",
                "direction": "Out",
                "number": "(01) 66861341"
            },
            {
                "name": "susan",
                "callId": 605,
                "duration": 118,
                "switchCode": "SW4",
                "direction": "Out",
                "number": "(03) 97264924"
            },
            {
                "name": "susan",
                "callId": 606,
                "duration": 48,
                "switchCode": "SW7",
                "direction": "In",
                "number": "(06) 737384"
            },
            {
                "name": "susan",
                "callId": 607,
                "duration": 58,
                "switchCode": "SW4",
                "direction": "Out",
                "number": "(03) 64513785"
            },
            {
                "name": "susan",
                "callId": 608,
                "duration": 100,
                "switchCode": "SW3",
                "direction": "In",
                "number": "(04) 83820843"
            },
            {
                "name": "susan",
                "callId": 609,
                "duration": 32,
                "switchCode": "SW2",
                "direction": "In",
                "number": "(00) 98227161"
            },
            {
                "name": "susan",
                "callId": 610,
                "duration": 47,
                "switchCode": "SW7",
                "direction": "Out",
                "number": "(05) 79915723"
            },
            {
                "name": "susan",
                "callId": 611,
                "duration": 108,
                "switchCode": "SW1",
                "direction": "Out",
                "number": "(03) 21154598"
            },
            {
                "name": "susan",
                "callId": 612,
                "duration": 116,
                "switchCode": "SW5",
                "direction": "Out",
                "number": "(01) 59298612"
            },
            {
                "name": "susan",
                "callId": 613,
                "duration": 36,
                "switchCode": "SW7",
                "direction": "Out",
                "number": "(07) 20546944"
            },
            {
                "name": "susan",
                "callId": 614,
                "duration": 94,
                "switchCode": "SW9",
                "direction": "Out",
                "number": "(08) 86946147"
            },
            {
                "name": "susan",
                "callId": 615,
                "duration": 38,
                "switchCode": "SW2",
                "direction": "In",
                "number": "(09) 44359896"
            },
            {
                "name": "susan",
                "callId": 616,
                "duration": 63,
                "switchCode": "SW9",
                "direction": "In",
                "number": "(08) 53677055"
            },
            {
                "name": "susan",
                "callId": 617,
                "duration": 85,
                "switchCode": "SW3",
                "direction": "Out",
                "number": "(03) 93644296"
            },
            {
                "name": "susan",
                "callId": 618,
                "duration": 53,
                "switchCode": "SW1",
                "direction": "In",
                "number": "(07) 62469867"
            },
            {
                "name": "susan",
                "callId": 619,
                "duration": 55,
                "switchCode": "SW4",
                "direction": "In",
                "number": "(09) 34894361"
            },
            {
                "name": "susan",
                "callId": 620,
                "duration": 80,
                "switchCode": "SW2",
                "direction": "Out",
                "number": "(04) 73077815"
            },
            {
                "name": "susan",
                "callId": 621,
                "duration": 75,
                "switchCode": "SW5",
                "direction": "In",
                "number": "(05) 9811378"
            },
            {
                "name": "susan",
                "callId": 622,
                "duration": 100,
                "switchCode": "SW5",
                "direction": "Out",
                "number": "(09) 15120539"
            },
            {
                "name": "susan",
                "callId": 623,
                "duration": 114,
                "switchCode": "SW6",
                "direction": "In",
                "number": "(00) 95177099"
            },
            {
                "name": "susan",
                "callId": 624,
                "duration": 78,
                "switchCode": "SW7",
                "direction": "In",
                "number": "(08) 69263227"
            },
            {
                "name": "susan",
                "callId": 625,
                "duration": 71,
                "switchCode": "SW8",
                "direction": "In",
                "number": "(04) 65395799"
            },
            {
                "name": "susan",
                "callId": 626,
                "duration": 117,
                "switchCode": "SW5",
                "direction": "In",
                "number": "(02) 7721832"
            },
            {
                "name": "susan",
                "callId": 627,
                "duration": 39,
                "switchCode": "SW8",
                "direction": "In",
                "number": "(04) 83980663"
            }
        ]
    },
    {
        "name": "Harper Johnson",
        "account": 177003,
        "calls": 24,
        "minutes": 26.483333333333334,
        "callRecords": [
            {
                "name": "susan",
                "callId": 628,
                "duration": 43,
                "switchCode": "SW6",
                "direction": "In",
                "number": "(03) 99309192"
            },
            {
                "name": "susan",
                "callId": 629,
                "duration": 117,
                "switchCode": "SW5",
                "direction": "Out",
                "number": "(08) 59342105"
            },
            {
                "name": "susan",
                "callId": 630,
                "duration": 31,
                "switchCode": "SW9",
                "direction": "Out",
                "number": "(08) 12325526"
            },
            {
                "name": "susan",
                "callId": 631,
                "duration": 47,
                "switchCode": "SW3",
                "direction": "Out",
                "number": "(05) 95756786"
            },
            {
                "name": "susan",
                "callId": 632,
                "duration": 88,
                "switchCode": "SW9",
                "direction": "Out",
                "number": "(08) 57663903"
            },
            {
                "name": "susan",
                "callId": 633,
                "duration": 48,
                "switchCode": "SW9",
                "direction": "In",
                "number": "(05) 2223124"
            },
            {
                "name": "susan",
                "callId": 634,
                "duration": 87,
                "switchCode": "SW5",
                "direction": "In",
                "number": "(03) 91770582"
            },
            {
                "name": "susan",
                "callId": 635,
                "duration": 33,
                "switchCode": "SW6",
                "direction": "Out",
                "number": "(05) 18642775"
            },
            {
                "name": "susan",
                "callId": 636,
                "duration": 29,
                "switchCode": "SW8",
                "direction": "Out",
                "number": "(02) 8142481"
            },
            {
                "name": "susan",
                "callId": 637,
                "duration": 98,
                "switchCode": "SW2",
                "direction": "In",
                "number": "(02) 60222030"
            },
            {
                "name": "susan",
                "callId": 638,
                "duration": 31,
                "switchCode": "SW9",
                "direction": "Out",
                "number": "(05) 61042088"
            },
            {
                "name": "susan",
                "callId": 639,
                "duration": 54,
                "switchCode": "SW5",
                "direction": "In",
                "number": "(02) 81673712"
            },
            {
                "name": "susan",
                "callId": 640,
                "duration": 57,
                "switchCode": "SW6",
                "direction": "In",
                "number": "(05) 53777339"
            },
            {
                "name": "susan",
                "callId": 641,
                "duration": 38,
                "switchCode": "SW3",
                "direction": "In",
                "number": "(02) 19669515"
            },
            {
                "name": "susan",
                "callId": 642,
                "duration": 108,
                "switchCode": "SW7",
                "direction": "Out",
                "number": "(08) 94952980"
            },
            {
                "name": "susan",
                "callId": 643,
                "duration": 84,
                "switchCode": "SW9",
                "direction": "Out",
                "number": "(07) 27865463"
            },
            {
                "name": "susan",
                "callId": 644,
                "duration": 85,
                "switchCode": "SW7",
                "direction": "In",
                "number": "(04) 4150028"
            },
            {
                "name": "susan",
                "callId": 645,
                "duration": 41,
                "switchCode": "SW3",
                "direction": "Out",
                "number": "(00) 34497134"
            },
            {
                "name": "susan",
                "callId": 646,
                "duration": 56,
                "switchCode": "SW1",
                "direction": "In",
                "number": "(02) 14349051"
            },
            {
                "name": "susan",
                "callId": 647,
                "duration": 101,
                "switchCode": "SW3",
                "direction": "In",
                "number": "(09) 72617109"
            },
            {
                "name": "susan",
                "callId": 648,
                "duration": 90,
                "switchCode": "SW2",
                "direction": "Out",
                "number": "(04) 34028257"
            },
            {
                "name": "susan",
                "callId": 649,
                "duration": 47,
                "switchCode": "SW5",
                "direction": "In",
                "number": "(00) 585245"
            },
            {
                "name": "susan",
                "callId": 650,
                "duration": 117,
                "switchCode": "SW8",
                "direction": "Out",
                "number": "(08) 70074008"
            },
            {
                "name": "susan",
                "callId": 651,
                "duration": 59,
                "switchCode": "SW0",
                "direction": "In",
                "number": "(06) 32750750"
            }
        ]
    },
    {
        "name": "Addison Wilson",
        "account": 177004,
        "calls": 23,
        "minutes": 24.4,
        "callRecords": [
            {
                "name": "susan",
                "callId": 652,
                "duration": 32,
                "switchCode": "SW9",
                "direction": "Out",
                "number": "(04) 77524120"
            },
            {
                "name": "susan",
                "callId": 653,
                "duration": 44,
                "switchCode": "SW3",
                "direction": "Out",
                "number": "(06) 477252"
            },
            {
                "name": "susan",
                "callId": 654,
                "duration": 86,
                "switchCode": "SW1",
                "direction": "In",
                "number": "(01) 15955397"
            },
            {
                "name": "susan",
                "callId": 655,
                "duration": 85,
                "switchCode": "SW4",
                "direction": "Out",
                "number": "(07) 25298377"
            },
            {
                "name": "susan",
                "callId": 656,
                "duration": 71,
                "switchCode": "SW5",
                "direction": "In",
                "number": "(07) 63477321"
            },
            {
                "name": "susan",
                "callId": 657,
                "duration": 72,
                "switchCode": "SW6",
                "direction": "Out",
                "number": "(03) 22235015"
            },
            {
                "name": "susan",
                "callId": 658,
                "duration": 109,
                "switchCode": "SW2",
                "direction": "Out",
                "number": "(09) 82619737"
            },
            {
                "name": "susan",
                "callId": 659,
                "duration": 100,
                "switchCode": "SW1",
                "direction": "Out",
                "number": "(09) 8153754"
            },
            {
                "name": "susan",
                "callId": 660,
                "duration": 28,
                "switchCode": "SW4",
                "direction": "Out",
                "number": "(04) 25341354"
            },
            {
                "name": "susan",
                "callId": 661,
                "duration": 50,
                "switchCode": "SW2",
                "direction": "Out",
                "number": "(01) 76439655"
            },
            {
                "name": "susan",
                "callId": 662,
                "duration": 62,
                "switchCode": "SW3",
                "direction": "In",
                "number": "(09) 66176396"
            },
            {
                "name": "susan",
                "callId": 663,
                "duration": 65,
                "switchCode": "SW8",
                "direction": "In",
                "number": "(04) 90800721"
            },
            {
                "name": "susan",
                "callId": 664,
                "duration": 66,
                "switchCode": "SW9",
                "direction": "In",
                "number": "(04) 91569849"
            },
            {
                "name": "susan",
                "callId": 665,
                "duration": 63,
                "switchCode": "SW5",
                "direction": "Out",
                "number": "(07) 33873629"
            },
            {
                "name": "susan",
                "callId": 666,
                "duration": 62,
                "switchCode": "SW9",
                "direction": "In",
                "number": "(06) 66194544"
            },
            {
                "name": "susan",
                "callId": 667,
                "duration": 34,
                "switchCode": "SW8",
                "direction": "In",
                "number": "(03) 32839115"
            },
            {
                "name": "susan",
                "callId": 668,
                "duration": 106,
                "switchCode": "SW8",
                "direction": "Out",
                "number": "(01) 91033174"
            },
            {
                "name": "susan",
                "callId": 669,
                "duration": 76,
                "switchCode": "SW6",
                "direction": "Out",
                "number": "(06) 57975290"
            },
            {
                "name": "susan",
                "callId": 670,
                "duration": 44,
                "switchCode": "SW0",
                "direction": "In",
                "number": "(01) 59390834"
            },
            {
                "name": "susan",
                "callId": 671,
                "duration": 96,
                "switchCode": "SW2",
                "direction": "In",
                "number": "(07) 44947033"
            },
            {
                "name": "susan",
                "callId": 672,
                "duration": 57,
                "switchCode": "SW4",
                "direction": "In",
                "number": "(00) 71164015"
            },
            {
                "name": "susan",
                "callId": 673,
                "duration": 21,
                "switchCode": "SW4",
                "direction": "In",
                "number": "(01) 35648857"
            },
            {
                "name": "susan",
                "callId": 674,
                "duration": 35,
                "switchCode": "SW4",
                "direction": "Out",
                "number": "(06) 44609564"
            }
        ]
    }

df = pd.DataFrame(data)
AgGrid(df, key="original")

df["callRecords"] = df["callRecords"].apply(lambda x: pd.json_normalize(x))

gridOptions = {
    "masterDetail": True,
    "rowSelection": "single",
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
    "defaultColDef": {"flex": 1},
    "detailCellRendererParams": {
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
            "defaultColDef": {"sortable": True, "flex": 1},
        },
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

with tabs[3]:
    st.write(r)