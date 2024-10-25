import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# def set_page_style():
st.set_page_config(layout="wide")
    # st.markdown(
    #     """
    #     <style>
    #     .main {
    #         max-width: 100%;  /* Set to 100% for full width */
    #         margin: 0 auto;
    #     }
    #     </style>
    #     """,
    #     unsafe_allow_html=True
    # )

def main():
    # set_page_style()  # Apply the style to this page
    # Streamlit Dashboard
    st.title("Results")

    st.markdown("<h2 class='centered'>Performance Metrics: 21 Year Training Period</h2>", unsafe_allow_html=True)

    # Create the DataFrame
    metrics_df = pd.DataFrame(columns=['A: Underlying (SP500)', 'B: Active Monetization Put Options', 'C: Knock-in Barrier Option', 'D: VIX Index OTM Calls'])
    sharpe_ratios = {'A: Underlying (SP500)': 0.34, 'B: Active Monetization Put Options': 0.57, 'C: Knock-in Barrier Option': 0.53, 'D: VIX Index OTM Calls': 0.39}
    drawdowns = {'A: Underlying (SP500)': "55.25%", 'B: Active Monetization Put Options': "42.80%", 'C: Knock-in Barrier Option': "40.00%", 'D: VIX Index OTM Calls': "53.20%"}
    metrics_df.loc['Sharpe Ratios:', :] = sharpe_ratios
    metrics_df.loc['Max Drawdowns:', :] = drawdowns

    # Center the DataFrame
    st.markdown("<div class='centered'>", unsafe_allow_html=True)
    st.dataframe(metrics_df)
    st.markdown("</div>", unsafe_allow_html=True)

# def page_one():

#     # st.markdown("<style> .centered {text-align: center;} </style>", unsafe_allow_html=True)

#     # set_page_style()  # Apply the style to this page
#     # Select company for detailed analysis
# # st.markdown("<style> .centered {text-align: center;} </style>", unsafe_allow_html=True)

#     # Center the header and text
#     st.markdown("<h2 class='centered'>Tail-Risk Hedging Using Derivatives</h2>", unsafe_allow_html=True)

#     st.markdown("""
#     <div class='centered'>
#     <h3 style='font-size: 16px;'>
#     In an increasingly efficient financial market, predicting market crashes and achieving a completely risk-free portfolio remains elusive. While many hedge fund
#     managers resort to diversification rather than the costly protective options, this project investigated two specific derivatives-based strategies: 
#     <ul>
#     <br>
#         <li>An active put protective monetization strategy, as proposed by Bhansali (2018)</li>
#         <li>A European knock-in put option strategy, alongside volatility index option strategies for comparison.</li>
#     <br>
#     </ul>
#     Ultimately, this research supports Bhansali's conclusion that a well-monitored active monetization strategy can not only protect portfolios but also enhance overall performance.
#     <br>
#     </div>
#     </h3>
#     """, unsafe_allow_html=True)

#     # Center the performance metrics header
#     # st.markdown("<style> .centered {text-align: center;} </style>", unsafe_allow_html=True)


    
#     cola, colb = st.columns(2)
#     with cola:
#         st.header("Portfolio Values In Different Stress Periods")
#         st.markdown("<h3 style='font-size: 18px;'> By doing a K-means cluster over the dataset, we were able to identify regimes: </h3>", unsafe_allow_html=True)
        
#         image_path = f"data/clusters.png"
#         try:
#             image = Image.open(image_path)
#             new_image = image.resize((650, 450))
#             st.image(new_image, caption = "2007-2010")
#         except FileNotFoundError:
#             st.write(f"No plot found for ")
#     with colb:
#         st.subheader("")
#         st.subheader("")
#         st.subheader("")
#         st.subheader("")
#         st.markdown("""
#         <h3 style='font-size: 18px;'>
#         For the purposes of tail identification, we can break down four high-stress periods that are left-tails or right-tails:
#         <br><br>
#         i) 2007-2009, in yellow, is clearly a left-tail event, on the back of the subprime mortgage crisis.<br><br>
#         ii) 2019-2021, in yellow, is also a left-tail event, on the back of a weakened COVID economy.<br><br>
#         iii) 2011-2014 appears to capture a right-tail event/peak. <br><br>
#         iv) 2016-2018 appears to capture a right-tail event/peak.
#         </h3>
#         """, unsafe_allow_html=True)
#     col1, col2, col3, col4 = st.columns(4)

#     with col1:
#         st.markdown("<h3 style='font-size: 18px;'>Left-Tail</h3>", unsafe_allow_html=True)
#         image_path = f"data/left_tail_event1.jpg"
#         try:
#             image = Image.open(image_path)
#             new_image = image.resize((650, 450))
#             st.image(new_image, caption = "2007-2010")
#         except FileNotFoundError:
#             st.write(f"No plot found for ")
#     with col3:
#         st.markdown("<h3 style='font-size: 18px;'>Right-Tail</h3>", unsafe_allow_html=True)
#         image_path = f"data/right_tail_event2.jpg"
#         try:
#             image = Image.open(image_path)
#             new_image = image.resize((650, 450))
#             st.image(new_image, caption = "2014-2016")
#         except FileNotFoundError:
#             st.write(f"No plot found for ")

#     with col2:
#         st.markdown("<h3 style='font-size: 18px;'>Left-Tail</h3>", unsafe_allow_html=True)
#         image_path = f"data/left_tail_event2.jpg"
#         try:
#             image = Image.open(image_path)
#             new_image = image.resize((650, 450))
#             st.image(new_image, caption = "2019-2021")
#         except FileNotFoundError:
#             st.write(f"No plot found for ")
#     with col4:
#         st.markdown("<h3 style='font-size: 18px;'>Right-Tail</h3>", unsafe_allow_html=True)
#         image_path = f"data/right_tail_event1.jpg"
#         try:
#             image = Image.open(image_path)
#             new_image = image.resize((650, 450))
#             st.image(new_image, caption = "2011-2014")
#         except FileNotFoundError:
#             st.write(f"No plot found for ")
#         # st.pyplot()  #  Replace with your actual plotting function


import pandas as pd
import streamlit as st
from PIL import Image

def page_one():
    # Set CSS for centering and improving text styles
    st.markdown("""
    <style>
        .centered { text-align: left; }
        .subheader { font-size: 18px; font-weight: bold; }
        .text { font-size: 16px; }
        .list { font-size: 16px; }
        .section-header { font-size: 22px; font-weight: bold; margin-top: 20px; }
        .image-caption { text-align: center; }
    </style>
    """, unsafe_allow_html=True)

    # Center the main header
    st.subheader("Tail-Risk Hedging Using Derivatives")

    st.markdown("""
    <div class='centered text'>
    In an increasingly efficient financial market, predicting market crashes and achieving a completely risk-free portfolio remains elusive. While many hedge fund
    managers resort to diversification rather than the costly protective options, this project investigated two specific derivatives-based strategies: 
    <ul class='list'>
        <li>An active put protective monetization strategy, as proposed by Bhansali (2018)</li>
        <li>A European knock-in put option strategy, alongside volatility index option strategies for comparison.</li>
    </ul>
    Ultimately, this research supports Bhansali's conclusion that a well-monitored active monetization strategy can not only protect portfolios but also enhance overall performance.
    </div>
    """, unsafe_allow_html=True)

    # Center the performance metrics header
    # st.markdown("<h2 class='centered section-header'>Performance Metrics: 21 Year Training Period</h2>", unsafe_allow_html=True)

    # Create the K-means cluster visualization
    st.write("")
    st.write("")
    st.write("")
    st.write("")

# CSS for border and other styling
    st.markdown("""
        <style>
            .bordered-container {
                border: 1px solid #ccc;  /* Light gray border */
                border-radius: 1px;      /* Rounded corners */
                padding: 1px;            /* Space inside the border */
                margin-bottom: 1px;      /* Space below the container */
            }
            .subheader { font-size: 18px; font-weight: bold; }
            .list { font-size: 16px; }
        </style>
        
        """, unsafe_allow_html=True)

    # Begin bordered container
    st.markdown("<div class='bordered-container'>", unsafe_allow_html=True)

    # Create columns within the bordered container
    cola, colb = st.columns(2)

    # Left Column
    with cola:
        st.subheader("Portfolio Values In Different Stress Periods")
        st.markdown("By doing a K-means cluster over the dataset, we were able to identify regimes:", unsafe_allow_html=True)

        image_path = f"data/clusters.png"
        try:
            image = Image.open(image_path)
            new_image = image.resize((650, 350))
            st.image(new_image, caption="Clusters Identified", use_column_width=True)
        except FileNotFoundError:
            st.write("No plot found for clusters.")

    # Right Column
    with colb:
        st.subheader("")
        st.subheader("")
        st.markdown("""
        For the purposes of tail identification, we can break down four high-stress periods that are left-tails or right-tails:
        <br>
        <ul class='list'>
            <li><strong>i)</strong> 2007-2009, in yellow, is clearly a left-tail event, on the back of the subprime mortgage crisis.</li>
            <li><strong>ii)</strong> 2019-2021, in yellow, is also a left-tail event, on the back of a weakened COVID economy.</li>
            <li><strong>iii)</strong> 2011-2014 appears to capture a right-tail event/peak.</li>
            <li><strong>iv)</strong> 2016-2018 appears to capture a right-tail event/peak.</li>
        </ul>
        """, unsafe_allow_html=True)

    # End bordered container
    st.markdown("</div>", unsafe_allow_html=True)

    # Layout for images
    col1, col2, col3, col4 = st.columns(4)

    # Left-Tail Event Images
    with col1:
        st.markdown("<h3 class='subheader'>Left-Tail Event 1</h3>", unsafe_allow_html=True)
        image_path = f"data/left_tail_event1.jpg"
        try:
            image = Image.open(image_path)
            new_image = image.resize((650, 450))
            st.image(new_image, caption="2007-2010", use_column_width=True)
        except FileNotFoundError:
            st.write("No plot found for left tail event 1.")

    with col2:
        st.markdown("<h3 class='subheader'>Left-Tail Event 2</h3>", unsafe_allow_html=True)
        image_path = f"data/left_tail_event2.jpg"
        try:
            image = Image.open(image_path)
            new_image = image.resize((650, 450))
            st.image(new_image, caption="2019-2021", use_column_width=True)
        except FileNotFoundError:
            st.write("No plot found for left tail event 2.")

    # Right-Tail Event Images
    with col3:
        st.markdown("<h3 class='subheader'>Right-Tail Event 1</h3>", unsafe_allow_html=True)
        image_path = f"data/right_tail_event2.jpg"
        try:
            image = Image.open(image_path)
            new_image = image.resize((650, 450))
            st.image(new_image, caption="2014-2016", use_column_width=True)
        except FileNotFoundError:
            st.write("No plot found for right tail event 1.")

    with col4:
        st.markdown("<h3 class='subheader'>Right-Tail Event 2</h3>", unsafe_allow_html=True)
        image_path = f"data/right_tail_event1.jpg"
        try:
            image = Image.open(image_path)
            new_image = image.resize((650, 450))
            st.image(new_image, caption="2011-2014", use_column_width=True)
        except FileNotFoundError:
            st.write("No plot found for right tail event 2.")

    st.markdown("""
    The active put monetization, even after considering transaction costs, has a significant improvement
    in portfolio values, particularly on the left tail as seen in the graphs. This is one of the important results
    of the study.
    """, unsafe_allow_html=True)

# Render the selected page
st.sidebar.title("Tail-Risk Hedging With Derivatives")
page = st.sidebar.radio("Select a page:", ["Introduction/Tail Risk Scenarios", "Results: Strategy Comparisons"])

# Render the selected page
if page == "Introduction/Tail Risk Scenarios":
    page_one()
elif page == "Results: Strategy Comparisons":
    main()
