import streamlit as st
import pandas as pd
from datetime import datetime
import json

# Initialize session state
if 'conversion_history' not in st.session_state:
    st.session_state.conversion_history = []
if 'favorites' not in st.session_state:
    st.session_state.favorites = []

# Category icons mapping
category_icons = {
    "Length": "📏",
    "Mass": "⚖️",
    "Temperature": "🌡️",
    "Area": "📐",
    "Volume": "🧊",
    "Speed": "🏃",
    "Time": "⏰",
    "Digital Storage": "💾"
}

# Set page configuration
st.set_page_config(
    page_title="Unit Converter",
    page_icon="🔄",
    layout="wide"
)

# Custom CSS for modern look
st.markdown("""
    <style>
    /* Main container styling */
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }

    /* Hide the default title */
    .main .block-container > div:first-child {
        display: none;
    }

    /* Card styling */
    .conversion-card {
        padding: 1.5rem;
        border-radius: 1rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
        border: 1px solid rgba(0, 0, 0, 0.05);
    }

    .conversion-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 12px rgba(0, 0, 0, 0.1);
    }

    /* History items styling */
    .history-item {
        padding: 1rem;
        margin: 0.7rem 0;
        border-radius: 0.8rem;
        border: 1px solid rgba(0, 0, 0, 0.05);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.02);
        transition: all 0.3s ease;
    }

    .history-item:hover {
        transform: translateX(5px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
        border-color: #ff4b4b;
    }

    /* Button styling */
    .stButton > button {
        width: 100%;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
        color: white;
        border: none;
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgb(245,71,68);
    }

    /* Quick convert buttons */
    .quick-convert-btn {
        border: 1px solid #ff4b4b !important;
        color: #ff4b4b !important;
        margin: 0.3rem 0;
        font-size: 0.9rem;
    }

    .quick-convert-btn:hover {
        background: #ff4b4b

 !important;
        color: white !important;
    }

    /* Input fields styling */
    .stNumberInput input, .stSelectbox select {
        border-radius: 0.5rem;
        border: 1px solid rgba(0, 0, 0, 0.1);
        padding: 0.5rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.02);
    }

    .stNumberInput input:focus, .stSelectbox select:focus {
        border-color: #ff4b4b

;
        box-shadow: 0 0 0 2px rgba(33, 147, 176, 0.2);
    }

    /* Metric display styling */
    .stMetric {

        padding: 1rem;
        border-radius: 0.8rem;
        border: 1px solid rgba(0, 0, 0, 0.05);
    }

    /* Expander styling */
    .streamlit-expanderHeader {
        border-radius: 0.8rem;
        border: 1px solid rgba(0, 0, 0, 0.05);
        padding: 0.8rem;
        margin-bottom: 0.5rem;
    }

    /* Success message styling */
    .stSuccess {
        background: linear-gradient(90deg, #ff4b4b, #a52e36);
        padding: 0.8rem;
        border-radius: 0.5rem;
    }

    /* Code block styling */
    .stCodeBlock {
        background: #2d3436;
        color: #ff4b4b;
        border-radius: 0.5rem;
        padding: 1rem;
    }

    /* Toast styling */
    .stToast {
        border-radius: 0.5rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }

    /* Responsive design */
    @media (max-width: 768px) {
        .stApp {
            padding: 0.5rem;
        }
        .main {
            padding: 0.5rem;
        }
        .conversion-card {
            padding: 1rem;
        }
        .history-item {
            padding: 0.8rem;
        }
        .stButton > button {
            padding: 0.4rem 0.8rem;
            font-size: 0.9rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Main app layout
st.markdown("""
    <div style='text-align: center; padding: 2rem 0;'>
        <h1 style='
            color: white;
            background: linear-gradient(90deg, #ff4b4b, #a52e36);
            padding: 1rem;
            border-radius: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 15px rgba(255, 75, 75, 0.3);
        '>
            ⟳ Unit Converter
        </h1>
        <p style='
            color: #666;
            font-size: 1.1rem;
            max-width: 600px;
            margin: 1rem auto;
            line-height: 1.6;
            padding: 1rem;
            border-radius: 0.5rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        '>
            Convert between different units of measurement with ease.
            Features quick conversions, favorites, and history tracking.
            Perfect for students, professionals, and everyday calculations.
        </p>
    </div>
""", unsafe_allow_html=True)

# Conversion dictionaries
CONVERSION_FACTORS = {
    "Length": {
        "Meter": 1,
        "Kilometer": 0.001,
        "Centimeter": 100,
        "Millimeter": 1000,
        "Mile": 0.000621371,
        "Yard": 1.09361,
        "Foot": 3.28084,
        "Inch": 39.3701
    },
    "Mass": {
        "Kilogram": 1,
        "Gram": 1000,
        "Milligram": 1000000,
        "Metric Ton": 0.001,
        "Pound": 2.20462,
        "Ounce": 35.274
    },
    "Temperature": {
        "Celsius": "C",
        "Fahrenheit": "F",
        "Kelvin": "K"
    },
    "Area": {
        "Square Meter": 1,
        "Square Kilometer": 0.000001,
        "Square Mile": 3.861e-7,
        "Square Yard": 1.19599,
        "Square Foot": 10.7639,
        "Square Inch": 1550,
        "Hectare": 0.0001,
        "Acre": 0.000247105
    },
    "Volume": {
        "Cubic Meter": 1,
        "Liter": 1000,
        "Milliliter": 1000000,
        "Gallon": 264.172,
        "Quart": 1056.69,
        "Pint": 2113.38,
        "Cup": 4226.75
    },
    "Speed": {
        "Meters per second": 1,
        "Kilometers per hour": 3.6,
        "Miles per hour": 2.23694,
        "Knots": 1.94384,
        "Feet per second": 3.28084
    },
    "Time": {
        "Second": 1,
        "Minute": 1/60,
        "Hour": 1/3600,
        "Day": 1/86400,
        "Week": 1/604800,
        "Month": 1/2592000,
        "Year": 1/31536000
    },
    "Digital Storage": {
        "Byte": 1,
        "Kilobyte": 1/1024,
        "Megabyte": 1/1048576,
        "Gigabyte": 1/1073741824,
        "Terabyte": 1/1099511627776
    }
}

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    # Convert to Celsius first
    if from_unit == "Fahrenheit":
        celsius = (value - 32) * 5/9
    elif from_unit == "Kelvin":
        celsius = value - 273.15
    else:
        celsius = value

    # Convert from Celsius to target unit
    if to_unit == "Fahrenheit":
        return (celsius * 9/5) + 32
    elif to_unit == "Kelvin":
        return celsius + 273.15
    return celsius

def convert_units(value, from_unit, to_unit, category):
    try:
        if not isinstance(value, (int, float)):
            raise ValueError("Input must be a number")

        if category == "Temperature":
            return convert_temperature(value, from_unit, to_unit)

        if category in CONVERSION_FACTORS:
            # Convert to base unit first
            base_value = value / CONVERSION_FACTORS[category][from_unit]
            # Convert from base unit to target unit
            result = base_value * CONVERSION_FACTORS[category][to_unit]

            if not isinstance(result, (int, float)) or not str(result).replace('.','').replace('-','').isdigit():
                raise ValueError("Invalid conversion result")

            return result
        return value
    except Exception as e:
        st.error(f"Conversion error: {str(e)}")
        return None

# Create main layout with sidebar
main_col, sidebar_col = st.columns([2, 1])

with sidebar_col:
    st.sidebar.header("📋 Recent Conversions")

    # Export history button
    if st.session_state.conversion_history:
        df = pd.DataFrame(st.session_state.conversion_history)
        csv = df.to_csv(index=False)
        st.sidebar.download_button(
            label="📥 Export History to CSV",
            data=csv,
            file_name="conversion_history.csv",
            mime="text/csv"
        )

    if st.sidebar.button("🗑️ Clear History"):
        st.session_state.conversion_history = []
        st.sidebar.success("History cleared!")

    if st.session_state.conversion_history:
        for entry in reversed(st.session_state.conversion_history[-5:]):
            st.sidebar.markdown(
                f"""<div class="history-item">
                    <small>{entry['timestamp']}</small><br>
                    <b>{category_icons.get(entry['category'], '')} {entry['category']}</b><br>
                    {entry['from_value']} {entry['from_unit']} →<br>
                    {entry['to_value']:.6g} {entry['to_unit']}
                </div>""",
                unsafe_allow_html=True
            )
    else:
        st.sidebar.info("No conversions yet!")

    # Enhanced help section
    with st.sidebar.expander("❓ How to Use"):
        st.markdown("""
            ### Basic Usage
            1. Select measurement category
            2. Choose units to convert from/to
            3. Enter value
            4. See result instantly

            ### Advanced Features
            - **Quick Conversions**: Use preset conversions
            - **Favorites**: Save frequently used conversions
            - **History**: View recent conversions
            - **Export**: Download conversion history as CSV

            ### Tips & Tricks
            - Use the copy button to copy results
            - Save common conversions as favorites
            - Clear history anytime with the clear button
            - Export history for record keeping

            ### Keyboard Shortcuts
            - `Enter`: Submit value
            - `Tab`: Navigate between fields
            - `Space`: Toggle expanders
        """)

with main_col:
    # Category selection with icons
    category = st.selectbox(
        "Select Category",
        list(CONVERSION_FACTORS.keys()),
        index=0,
        format_func=lambda x: f"{category_icons.get(x, '')} {x}"
    )

    # Quick conversion buttons
    st.markdown("### ⚡ Quick Conversions")
    quick_conversions = {
        "Length": [
            ("1 Mile → km", 1, "Mile", "Kilometer"),
            ("1 Meter → ft", 1, "Meter", "Foot")
        ],
        "Temperature": [
            ("32°F → °C", 32, "Fahrenheit", "Celsius"),
            ("100°C → °F", 100, "Celsius", "Fahrenheit")
        ],
        "Mass": [
            ("1 kg → lb", 1, "Kilogram", "Pound"),
            ("1 lb → kg", 1, "Pound", "Kilogram")
        ]
    }

    if category in quick_conversions:
        quick_cols = st.columns(len(quick_conversions[category]))
        for idx, (label, val, from_u, to_u) in enumerate(quick_conversions[category]):
            with quick_cols[idx]:
                if st.button(label):
                    quick_result = convert_units(val, from_u, to_u, category)
                    st.success(f"{quick_result:.2f} {to_u}")

    # Main conversion interface
    col1, col2 = st.columns(2)

    with col1:
        from_unit = st.selectbox(
            "From",
            list(CONVERSION_FACTORS[category].keys()),
            key="from_unit"
        )
        value = st.number_input(
            "Enter Value",
            value=1.0,
            format="%f"
        )

    with col2:
        to_unit = st.selectbox(
            "To",
            list(CONVERSION_FACTORS[category].keys()),
            key="to_unit"
        )
        result = convert_units(value, from_unit, to_unit, category)
        st.metric(
            label="Result",
            value=f"{result:.6g} {to_unit}"
        )

    # Copy result button
    if st.button("📋 Copy Result"):
        st.code(f"{value} {from_unit} = {result:.6g} {to_unit}")
        st.toast("Result copied to clipboard!", icon="✅")

    # Add to history
    if result is not None:
        history_entry = {
            'timestamp': datetime.now().strftime("%H:%M:%S"),
            'category': category,
            'from_value': value,
            'from_unit': from_unit,
            'to_value': result,
            'to_unit': to_unit
        }
        st.session_state.conversion_history.append(history_entry)

    # Formula display
    with st.expander("📖 View Conversion Formula"):
        if category == "Temperature":
            st.info("Temperature Conversion Formulas:\n"
                    "- Celsius to Fahrenheit: °F = (°C × 9/5) + 32\n"
                    "- Fahrenheit to Celsius: °C = (°F - 32) × 5/9\n"
                    "- Kelvin to Celsius: °C = K - 273.15")
        else:
            base_unit = list(CONVERSION_FACTORS[category].keys())[0]
            st.info(f"Conversion is done through {base_unit} as the base unit.")

    # Add favorite conversions feature
    with st.expander("⭐ Favorite Conversions"):
        # Add current conversion to favorites
        if st.button("Save Current Conversion as Favorite"):
            favorite = {
                'category': category,
                'from_unit': from_unit,
                'to_unit': to_unit,
                'value': value
            }
            if favorite not in st.session_state.favorites:
                st.session_state.favorites.append(favorite)
                st.success("Added to favorites!")

        # Display favorites
        if st.session_state.favorites:
            for idx, fav in enumerate(st.session_state.favorites):
                cols = st.columns([3, 1])
                with cols[0]:
                    result = convert_units(fav['value'], fav['from_unit'], fav['to_unit'], fav['category'])
                    st.markdown(f"""
                        {category_icons.get(fav['category'], '')} **{fav['category']}**:
                        {fav['value']} {fav['from_unit']} → {result:.6g} {fav['to_unit']}
                    """)
                with cols[1]:
                    if st.button("🗑️", key=f"del_fav_{idx}"):
                        st.session_state.favorites.pop(idx)
                        st.rerun()
        else:
            st.info("No favorites saved yet!")

    # Add to the quick_conversions dictionary
    quick_conversions.update({
        "Volume": [
            ("1 L → gal", 1, "Liter", "Gallon"),
            ("1 gal → L", 1, "Gallon", "Liter")
        ],
        "Digital Storage": [
            ("1 GB → MB", 1, "Gigabyte", "Megabyte"),
            ("1 TB → GB", 1, "Terabyte", "Gigabyte")
        ],
        "Speed": [
            ("60 mph → km/h", 60, "Miles per hour", "Kilometers per hour"),
            ("100 km/h → mph", 100, "Kilometers per hour", "Miles per hour")
        ]
    })
