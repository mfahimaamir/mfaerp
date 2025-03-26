#https://discuss.streamlit.io/t/toggle-hide-show-sidebar-from-python/5805/5
#https://blog.streamlit.io/session-state-for-streamlit/

import streamlit as st
st.header("Muhammad Is the Best in all over the uiverses")

# Initialize a session state variable that tracks the sidebar state (either 'expanded' or 'collapsed').
if 'sidebar_state' not in st.session_state:
    st.session_state.sidebar_state = 'collapsed'
#    st.session_state.sidebar_state = 'expanded'

# Streamlit set_page_config method has a 'initial_sidebar_state' argument that controls sidebar state.
st.set_page_config(initial_sidebar_state=st.session_state.sidebar_state)

# Show title and description of the app.
st.title('Example: Controlling sidebar programmatically')
st.sidebar.markdown('This is an example Streamlit app to show how to expand and collapse the sidebar programmatically.')

# Toggle sidebar state between 'expanded' and 'collapsed'.
if st.button('Click to toggle sidebar state'):
    #st.session_state.sidebar_state = 'expanded'
    if st.session_state.sidebar_state == 'collapsed' :
        st.session_state.sidebar_state = 'expanded'
    #    st.session_state.sidebar_state = 'expanded'
    #else st.session_state.sidebar_state == 'expanded':
    
    #st.session_state.sidebar_state = 'expanded' if st.session_state.sidebar_state == 'collapsed' else 'collapsed'
    #st.session_state.sidebar_state = 'expanded' if st.session_state.sidebar_state == 'collapsed' else 'collapsed'
    #st.session_state.sidebar_state = 'collapsed' if st.session_state.sidebar_state == 'expanded' else 'expanded'
    # Force an app rerun after switching the sidebar state.
    #st.experimental_rerun()