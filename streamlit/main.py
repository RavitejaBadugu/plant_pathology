import streamlit as st
from multipage import MultiPage
import uploads
import entrance




from multipage import MultiPage

app = MultiPage()


# Add all your applications (pages) here
app.add_page('entrance page',entrance.app)
app.add_page("Upload Data", uploads.app)


# The main app
app.run()


