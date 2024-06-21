import streamlit as st
from data_loader import load_data
from pages import overview_page, histograms_page, bar_charts_page, pie_charts_page
from streamlit_option_menu import option_menu

# Set up Streamlit app configuration
st.set_page_config(page_title="Data Visualization App", layout="wide")

# Load the data
data = load_data()

with st.sidebar:
    st.markdown("<h2 style='margin-top: -10px;'>Menu</h2>", unsafe_allow_html=True)
    st.markdown("<hr style='margin: 0; padding: 0;'>", unsafe_allow_html=True)
    selected_page = option_menu(
        menu_title=None,
        options=["Overview", "Histograms", "Bar Charts", "Pie Charts"],
        icons=["house", "bar-chart-line", "bar-chart", "pie-chart"],
        menu_icon="cast",
        default_index=0,
        orientation='vertical',
        styles={
            "container": {"padding": "5px", "background-color": "#f0f2f6"},
            "icon": {"color": "lightcoral", "font-size": "25px", "margin-left": "-13px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "0px 0px 10px -16px",
                "--hover-color": "lightblue",
                "--hover-background-color": "lightblue"
            },
            "nav-link-selected": {"background-color": "lightblue", "color": "black"},
            "nav-link-hover": {"background-color": "lightcoral"}
        }
    )

# Define a function to handle the selected page


def main():
    if selected_page == "Overview":
        overview_page(data)
    elif selected_page == "Histograms":
        histograms_page(data)
    elif selected_page == "Bar Charts":
        bar_charts_page(data)
    elif selected_page == "Pie Charts":
        pie_charts_page(data)


if __name__ == "__main__":
    main()
