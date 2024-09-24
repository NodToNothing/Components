import streamlit as st
from streamlit_extras.mandatory_date_range import date_range_picker
from streamlit_extras.stoggle import stoggle
from streamlit_extras.badges import badge
from streamlit_extras.let_it_rain import rain
from streamlit_extras.markdownlit import mdlit

result = date_range_picker("Select a date range...")
st.write("Result:", result)

stoggle("Click me!", """Surprise, additional stuff""")

def example():
    rain(
        emoji="🎈",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )

def example2():
    rain(
        emoji="🤠",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )

example()
example2()

def example_link_and_colors():
    mdlit(
        """Tired from [default links](https://extras.streamlit.app)?
    Me too! Discover Markdownlit's `@()` operator. Just insert a link and it
    will figure a nice icon and label for you!
    Example: @(https://extras.streamlit.app)... better, right? You can
    also @(🍐)(manually set the label if you want)(https://extras.streamlit.app)
    btw, and play with a [red]beautiful[/red] [blue]set[/blue] [orange]of[/orange]
    [violet]colors[/violet]. Another perk is those beautiful arrows -> <-
    """
    )

example_link_and_colors()

def example_pypi():
    badge(type="pypi", name="plost")
    badge(type="pypi", name="streamlit")

def example_streamlit():
    badge(type="streamlit", url="https://plost.streamlitapp.com")

def example_github():
    badge(type="github", name="streamlit/streamlit")    

example_pypi()
example_streamlit()
example_github()


#https://streamlit.io/components
#https://extras.streamlit.app/
