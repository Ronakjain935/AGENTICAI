import streamlit as st

from youtube_analyzer import build_youtube_agent

st.set_page_config(
    page_title="AI YouTube Video Analyzer",
    page_icon="🎥",
    layout="centered",
)

st.title("🎥 AI YouTube Video Analyzer")

st.write(
    "Paste a YouTube video URL and let the AI analyze it."
)


@st.cache_resource
def get_agent():
    return build_youtube_agent()


agent = get_agent()

video_url = st.text_input(
    "Enter YouTube Video URL",
    placeholder="https://www.youtube.com/watch?v=..."
)

analyze = st.button("Analyze Video")

if analyze:

    if not video_url:

        st.warning("Please enter a YouTube URL.")

    else:

        with st.spinner("Analyzing video..."):

            try:

                response = agent.run(
                    f"""
                    Analyze this video:

                    {video_url}

                    Keep the response under 500 words.
                    Focus only on the important parts.
                    """
                )

                st.success("Analysis Completed!")

                st.markdown(response.content)

            except Exception as e:

                st.error(f"Error: {str(e)}")