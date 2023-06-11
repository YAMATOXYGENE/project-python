import streamlit as st
import pandas as pd
import plotly.express as px
import requests

def set_background_image():
    page_bg_img = '''
        <style>
        body {
            background-image: url("background.gif");
            background-size: cover;
        }
        </style>
        '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

def set_background_color(color):
    """
    Function to set the background color of the page.
    """
    page_bg_css = f"""
        <style>
        body {{
            background-color: {color};
        }}
        </style>
    """
    st.markdown(page_bg_css, unsafe_allow_html=True)

def home():
    st.title("Home Page")
    # Add content for the Home page

    # Animated text
    st.markdown('<p class="rainbow-text">Welcome to the Home Page!</p>', unsafe_allow_html=True)

    # Animated image
    st.image("background.gif", use_column_width=True)


def languages_codes_news():
    st.title("Languages Codes News")
    set_background_image()
    
    st.markdown('### Donut chart')
    donut_theta = st.selectbox('Select data', ('FIRST', 'SECOND'))
    stocks = pd.read_csv('https://raw.githubusercontent.com/YAMATOXYGENE/yoyo/master/nunu')
    fig = px.pie(
        data_frame=stocks,
        names='company',
        values=donut_theta,
        color='company',
        hole=0.5,
        height=400,
        width=500
    ).update_traces(textinfo='percent+label')
    st.plotly_chart(fig)

    st.markdown('### Code Languages')
    code_languages = ['Python', 'Java', 'JavaScript', 'C++', 'Ruby']
    st.write(code_languages)

    st.markdown('### Popular Frameworks')
    frameworks = ['Django', 'Spring', 'React', 'Angular', 'Ruby on Rails']
    st.write(frameworks)


def weather_news():
    st.title("Weather News")
    set_background_image()
    st.markdown('### Metrics')
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")
    
    seattle_weather = pd.read_csv('https://raw.githubusercontent.com/YAMATOXYGENE/yoyo/main/coco')
    
    st.markdown('### Heatmap')
    time_hist_color = st.selectbox('Color by', ('temp_min', 'temp_max'))
    fig = px.histogram(
        data_frame=seattle_weather,
        x='date',
        y=time_hist_color,
        color_discrete_sequence=["#00cc96"],
        height=400
    ).update_layout(
        xaxis_title="Date",
        yaxis_title=time_hist_color.capitalize(),
        showlegend=False
    )
    st.plotly_chart(fig)

    st.markdown('### Line chart')
    plot_data = st.multiselect('Select data', ['temp_min', 'temp_max'], ['temp_min', 'temp_max'])
    plot_height = st.slider('Specify plot height', 200, 500, 400)
    st.line_chart(seattle_weather, x='date', y=plot_data, height=plot_height)


def mood_brightener():
    st.title("Helping You Make Your Mood Brighter")
    set_background_image()
    
    st.markdown('### Exercise')
    st.write('Engaging in physical exercise releases endorphins and boosts your mood. Try going for a walk, doing yoga, or dancing to your favorite music.')

    st.markdown('### Gratitude')
    st.write('Take a moment to write down three things you are grateful for. Focusing on gratitude can help shift your mindset and bring positivity.')

    st.markdown('### Mindfulness')
    st.write('Practice mindfulness or meditation to relax your mind and reduce stress. You can find guided meditation apps or videos online.')

    st.markdown('### Enjoyable Activities')
    st.write('Spend time doing activities you enjoy, such as reading a book, watching a movie, or pursuing a hobby. Engaging in pleasurable activities can uplift your mood.')

    st.markdown('### Social Connection')
    st.write('Connect with friends or loved ones. Reach out to someone you haven\'t talked to in a while or plan a virtual hangout. Social interactions can boost your mood.')

    st.markdown('### Uplifting Content')
    st.write('Expose yourself to uplifting content such as inspirational quotes, motivational videos, or success stories. Surrounding yourself with positive influences can improve your mood.')

    st.markdown('### Meme Generator')
    st.write('Create your own memes to add some humor to your day. You can use online meme generators or apps to customize and share funny memes.')

    st.markdown('### Jokes')
    st.write('Read or share jokes to lighten the mood. Laughter is a powerful mood enhancer. Look up joke websites or ask friends for their favorite jokes.')


def code_snippets():
    st.title("Code Snippets")
    set_background_color("#F2F2F2")  # Light gray background color
    # Add content for the Code Snippets page


def api_documentation():
    st.title("API Documentation")
    set_background_color("#E5F3FF")  # Light blue background color
    # Add content for the API Documentation page


def version_control():
    st.title("Version Control")
    set_background_color("#FFE5CC")  # Light orange background color
    # Add content for the Version Control page


def collaboration_tools():
    st.title("Collaboration Tools")
    set_background_color("#FFD9D9")  # Light red background color
    # Add content for the Collaboration Tools page


def project_management():
    st.title("Project Management")
    set_background_color("#FCE4D6")  # Light coral background color
    # Add content for the Project Management page


def code_analytics():
    st.title("Code Analytics")
    set_background_color("#F2D8D8")  # Light pink background color
    # Add content for the Code Analytics page


def learning_resources():
    st.title("Learning Resources")
    set_background_color("#D9EAD3")  # Pale green background color
    # Add content for the Learning Resources page


def community_forum():
    st.title("Community Forum")
    set_background_color("#E2F0CB")  # Light green background color
    # Add content for the Community Forum page


def about():
    st.title("About Page")
    set_background_color("#E9E9E9")  # Light gray background color
    # Add content for the About page


def contact():
    st.title("Contact Page")
    set_background_color("#FFEBCC")  # Light peach background color
    # Add content for the Contact page


def joke_generator():
    st.title("Joke Generator")
    set_background_color("#F8F8F8")  # Light white background color

    category = st.selectbox("Select a joke category", ["Any", "Miscellaneous", "Programming", "Pun", "Spooky", "Christmas"])

    if category == "Any":
        url = "https://v2.jokeapi.dev/joke/Any"
    else:
        url = f"https://v2.jokeapi.dev/joke/{category}"

    response = requests.get(url)
    if response.status_code == 200:
        joke_data = response.json()
        if joke_data["type"] == "single":
            st.write(joke_data["joke"])
        elif joke_data["type"] == "twopart":
            st.write(joke_data["setup"])
            st.write(joke_data["delivery"])
    else:
        st.write("Oops! Something went wrong. Please try again.")


def main():
    pages = {
        "Home": home,
        "Languages Codes News": languages_codes_news,
        "Weather News": weather_news,
        "Mood Brightener": mood_brightener,
        "Code Snippets": code_snippets,
        "API Documentation": api_documentation,
        "Version Control": version_control,
        "Collaboration Tools": collaboration_tools,
        "Project Management": project_management,
        "Code Analytics": code_analytics,
        "Learning Resources": learning_resources,
        "Community Forum": community_forum,
        "About": about,
        "Contact": contact,
        "Joke Generator": joke_generator
    }

    st.set_page_config(layout='wide', initial_sidebar_state='expanded')

    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))

    page = pages[selection]
    page()


if __name__ == "__main__":
    main()
