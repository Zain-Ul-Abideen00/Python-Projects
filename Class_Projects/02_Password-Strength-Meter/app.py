import streamlit as st
import plotly.graph_objects as go
from password_utils import PasswordStrengthMeter
import time
import pyperclip

# Page configuration
st.set_page_config(
    page_title="Password Strength Meter",
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    /* Input styling */
    .stTextInput > div > div > input {
        font-size: 20px;
    }

    /* Social Links Styling */
    .social-links a {
        text-decoration: none;
        padding: 8px 15px;
        margin: 5px;
        border-radius: 5px;
        transition: all 0.3s ease;
        background-color: rgba(255, 255, 255, 0.1);
        color: inherit;
        display: inline-block;
    }

    .social-links a:hover {
        background-color: rgba(255, 255, 255, 0.2);
        transform: translateY(-2px);
    }

    /* Sidebar Links Styling */
    .sidebar-links a {
        text-decoration: none;
        padding: 10px 15px;
        margin: 8px auto;
        border-radius: 8px;
        transition: all 0.3s ease;
        background-color: rgba(255, 255, 255, 0.1);
        color: inherit;
        display: block;
        width: 80%;
    }

    .sidebar-links a:hover {
        background-color: rgba(255, 255, 255, 0.2);
        transform: translateX(5px);
    }

    .dev-profile img {
        border: 3px solid rgba(255, 255, 255, 0.2);
        padding: 3px;
        transition: transform 0.3s ease;
    }

    .dev-profile img:hover {
        transform: scale(1.05);
    }

    /* Section styling */
    .password-strength {
        padding: 15px;
        border-radius: 10px;
        margin: 15px 0;
        border-left: 5px solid var(--primary-color);
    }
    .feedback-item {
        margin: 8px 0;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    /* Typography */
    .header-style {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        margin: 20px 0;
        color: var(--text-color);
    }
    .subheader-style {
        font-size: 20px;
        text-align: center;
        margin: 15px 0;
        color: var(--text-color);
    }

    /* Container styling */
    .section-title {
        color: #ffd700;
        margin-bottom: 15px;
        font-size: 1.5em;
    }

    /* Button styling */
    .stButton > button {
        width: 100%;
        padding: 0.5rem;
        font-weight: bold;
    }

    /* Slider styling */
    .stSlider > div > div > div {
        background-color: rgba(255, 255, 255, 0.2);
    }

    /* Code block styling */
    .generated-password {
        font-family: monospace;
        padding: 10px;
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 5px;
        margin: 10px 0;
    }

    /* Tooltip styling */
    .tooltip {
        position: relative;
        display: inline-block;
        cursor: help;
    }
    .tooltip .tooltiptext {
        visibility: hidden;
        background-color: rgba(0, 0, 0, 0.8);
        color: #fff;
        text-align: center;
        padding: 5px;
        border-radius: 6px;
        position: absolute;
        z-index: 1;
        bottom: 125%;
        left: 50%;
        transform: translateX(-50%);
        opacity: 0;
        transition: opacity 0.3s;
    }
    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }
</style>
""", unsafe_allow_html=True)

# About section in sidebar
with st.sidebar:
    st.markdown("<h2 style='text-align: center; margin-bottom: 20px;'>About Developer</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: center' class='dev-profile'>
        <img src="https://github.com/Zain-Ul-Abideen00.png" style="border-radius: 50%; width: 150px; margin: 10px auto; display: block;">
        <h3 style='margin: 15px 0; font-size: 1.5em;'>Zain Ul Abideen</h3>
        <p style='color: #ffd700; margin-bottom: 20px;'>Full Stack Developer</p>
        <div class='sidebar-links'>
            <a href="https://zain-ul-abideen.vercel.app/" target="_blank">
                🌐 Portfolio
            </a>
            <a href="mailto:zain.dev00@gmail.com">
                ✉️ Email
            </a>
            <a href="https://www.linkedin.com/in/zain-ul-abideen00/" target="_blank">
                👔 LinkedIn
            </a>
            <a href="https://github.com/Zain-Ul-Abideen00" target="_blank">
                💻 GitHub
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<hr style='margin: 30px 0;'>", unsafe_allow_html=True)

# Initialize the password meter
password_meter = PasswordStrengthMeter()

# Main content
st.markdown('<h1 class="header-style">🔒 Password Strength Meter</h1>', unsafe_allow_html=True)

# Password input section
st.markdown('<p class="subheader-style">Enter your password to check its strength:</p>', unsafe_allow_html=True)
password = st.text_input("", type="password", help="Type or paste your password here")

# Password generator section
st.markdown('<div class="section-title">🎲 Password Generator</div>', unsafe_allow_html=True)

# Generator controls
col1, col2 = st.columns([2, 1])
with col1:
    password_length = st.slider(
        "Password Length",
        min_value=12,
        max_value=32,
        value=16,
        step=1,
        help="Longer passwords are more secure. We recommend at least 12 characters."
    )
with col2:
    include_special = st.checkbox(
        "Special Characters",
        value=True,
        help="Include special characters (!@#$%^&*) for stronger passwords"
    )

# Generate button with loading state
if st.button("Generate Strong Password", use_container_width=True):
    with st.spinner("Generating secure password..."):
        time.sleep(0.5)  # Add slight delay for better UX
        generated_password = password_meter.generate_password(password_length, include_special)
        st.code(generated_password, language=None)
        st.success("Password generated! Click to copy and use it in the password field above.")
st.markdown('</div>', unsafe_allow_html=True)

# Password requirements section with tooltips
st.markdown('<div class="section-title">📋 Password Requirements</div>', unsafe_allow_html=True)
st.markdown("""
<div class="tooltip">Minimum 8 characters<span class="tooltiptext">Longer passwords are harder to crack</span></div>
<div class="tooltip">Mix of uppercase & lowercase<span class="tooltiptext">Using both cases increases complexity</span></div>
<div class="tooltip">At least one number<span class="tooltiptext">Numbers add another layer of security</span></div>
<div class="tooltip">Special characters (!@#$%^&*)<span class="tooltiptext">Special characters make passwords stronger</span></div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Analyze password when input is provided
if password:
    result = password_meter.check_password_strength(password)

    # Create gauge chart for password strength
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=result["score"],
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [0, 6], 'tickwidth': 1},
            'bar': {'color': password_meter.get_strength_color(result["strength"])},
            'steps': [
                {'range': [0, 2], 'color': "rgba(49, 51, 63, 0.1)"},
                {'range': [2, 4], 'color': "rgba(49, 51, 63, 0.2)"},
                {'range': [4, 6], 'color': "rgba(49, 51, 63, 0.3)"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 3
            }
        },
        title={'text': "Strength Score"}
    ))

    # Update layout for better visibility
    fig.update_layout(
        height=300,
        margin=dict(t=60, b=20, l=20, r=20),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig, use_container_width=True)

    # Display strength with appropriate color and animations
    st.markdown(f"""
    <div class='password-strength' style='border-left: 5px solid {password_meter.get_strength_color(result["strength"])}'>
        <h2 style="color: {password_meter.get_strength_color(result["strength"])}">
            Password Strength: {result["strength"]}
        </h2>
        <p><strong>Score:</strong> {result["score"]}/6</p>
        <p><strong>Entropy:</strong> {result["entropy"]:.2f} bits</p>
        <p><strong>Length:</strong> {result["length"]} characters</p>
    </div>
    """, unsafe_allow_html=True)

    # Feedback and Analysis in tabs
    tab1, tab2 = st.tabs(["📝 Feedback", "🔍 Analysis"])

    with tab1:
        if result["feedback"]:
            for item in result["feedback"]:
                st.markdown(f"""
                <div class='feedback-item'>
                    {'✅' if "Excellent" in item or "Good job" in item else '❗'} {item}
                </div>
                """, unsafe_allow_html=True)

    with tab2:
        criteria = {
            "length": "Minimum Length (8)",
            "uppercase": "Uppercase Letter",
            "lowercase": "Lowercase Letter",
            "digits": "Number",
            "special": "Special Character"
        }

        for key, label in criteria.items():
            if key in result["details"]:
                st.markdown(f"""
                <div class='feedback-item'>
                    {('✅' if result["details"][key] else '❌')} {label}
                </div>
                """, unsafe_allow_html=True)

# Footer with version and helpful links
st.markdown("---")
st.markdown("""
    <div style='text-align: center'>
        <p style='margin-bottom: 15px;'>Made with ❤️ by <a href="https://zain-ul-abideen.vercel.app/" target="_blank" style='color: #ffd700; text-decoration: none;'>Zain Ul Abideen</a></p>
        <div class='social-links' style='margin: 15px 0;'>
            <a href="mailto:zain.dev00@gmail.com">
                ✉️ Email
            </a>
            <a href="https://www.linkedin.com/in/zain-ul-abideen00/" target="_blank">
                👔 LinkedIn
            </a>
            <a href="https://github.com/Zain-Ul-Abideen00" target="_blank">
                💻 GitHub
            </a>
        </div>
        <small>Version 2.0 | <a href="https://en.wikipedia.org/wiki/Password_strength" target="_blank" style='color: #ffd700; text-decoration: none;'>Learn More</a></small>
    </div>
    """, unsafe_allow_html=True)
