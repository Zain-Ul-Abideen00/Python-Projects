import streamlit as st

def main():
    st.set_page_config(
        page_title="My Streamlit Website",
        page_icon="🌐",
        layout="wide"
    )

    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Go to",
        ["Home", "About", "Contact", "Projects"]
    )

    # Home page
    if page == "Home":
        st.title("Welcome to My Website! 👋")
        st.write("""
        This is a simple website created using Streamlit.
        Feel free to explore the different pages using the navigation sidebar.
        """)

        # Add some sample content
        col1, col2 = st.columns(2)

        with col1:
            st.header("Latest News")
            st.write("""
            - New project launched!
            - Website updated with new features
            - Upcoming events
            """)

        with col2:
            st.header("Quick Links")
            st.write("""
            - [Documentation](https://docs.streamlit.io)
            - [GitHub Repository](https://github.com)
            - [Contact Form](#contact)
            """)

    # About page
    elif page == "About":
        st.title("About Us")
        st.write("""
        ## Our Mission
        We are dedicated to creating innovative solutions using Python and Streamlit.

        ## Our Team
        - John Doe - Lead Developer
        - Jane Smith - UI/UX Designer
        - Mike Johnson - Project Manager
        """)

        # Add a progress bar
        st.subheader("Our Skills")
        st.write("Python Development")
        st.progress(0.9)
        st.write("Web Development")
        st.progress(0.8)
        st.write("Data Analysis")
        st.progress(0.7)

    # Contact page
    elif page == "Contact":
        st.title("Contact Us")

        # Contact form
        with st.form("contact_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            message = st.text_area("Message")
            submitted = st.form_submit_button("Submit")

            if submitted:
                st.success("Thank you for your message! We'll get back to you soon.")

    # Projects page
    elif page == "Projects":
        st.title("Our Projects")

        # Project cards
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Project 1")
            st.image("https://via.placeholder.com/300x200", caption="Project 1 Preview")
            st.write("Description of Project 1")

        with col2:
            st.subheader("Project 2")
            st.image("https://via.placeholder.com/300x200", caption="Project 2 Preview")
            st.write("Description of Project 2")

if __name__ == "__main__":
    main()
