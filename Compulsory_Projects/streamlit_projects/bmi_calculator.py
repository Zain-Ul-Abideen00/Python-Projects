import streamlit as st

def calculate_bmi(weight, height):
    # Convert height from cm to meters
    height_m = height / 100
    # Calculate BMI
    bmi = weight / (height_m ** 2)
    return bmi

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    st.set_page_config(
        page_title="BMI Calculator",
        page_icon="⚖️",
        layout="centered"
    )

    st.title("BMI Calculator")
    st.write("Calculate your Body Mass Index (BMI)")

    # Create two columns for the sliders
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Weight")
        weight = st.slider(
            "Select your weight (kg)",
            min_value=30.0,
            max_value=200.0,
            value=70.0,
            step=0.1,
            format="%.1f kg"
        )

    with col2:
        st.subheader("Height")
        height = st.slider(
            "Select your height (cm)",
            min_value=100.0,
            max_value=250.0,
            value=170.0,
            step=0.1,
            format="%.1f cm"
        )

    # Calculate BMI automatically as sliders change
    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)

    # Display results
    st.markdown("---")
    st.subheader("Results")

    # Create a metric display
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Your BMI", f"{bmi:.1f}")
    with col2:
        st.metric("Category", category)

    # Display BMI chart with visual indicator
    st.markdown("---")
    st.subheader("BMI Categories")

    # Create a visual representation of BMI categories
    categories = {
        "Underweight": (0, 18.5),
        "Normal weight": (18.5, 25),
        "Overweight": (25, 30),
        "Obese": (30, 100)
    }

    # Create a progress bar for visual representation
    progress_value = min(max((bmi - 15) / 30, 0), 1)  # Scale BMI to 0-1 for progress bar
    st.progress(progress_value)

    # Display category ranges
    for category_name, (min_val, max_val) in categories.items():
        st.write(f"- {category_name}: {min_val} - {max_val}")

if __name__ == "__main__":
    main()
