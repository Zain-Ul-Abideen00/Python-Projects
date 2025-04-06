# Modern Unit Converter

A sophisticated, feature-rich unit converter application built with Python and Streamlit. This modern web application provides an intuitive interface for converting between different units of measurement, inspired by Google's unit converter but with additional features and improvements.

## 🌟 Key Features

- **Multiple Conversion Categories**
  - Length (m, km, cm, mm, mile, yard, foot, inch)
  - Mass/Weight (kg, g, mg, ton, lb, oz)
  - Temperature (Celsius, Fahrenheit, Kelvin)
  - Area (m², km², mi², yd², ft², in², hectare, acre)
  - Volume (m³, L, mL, gal, qt, pt, cup)
  - Speed (m/s, km/h, mph, knots, ft/s)
  - Time (second, minute, hour, day, week, month, year)
  - Digital Storage (byte, KB, MB, GB, TB)

- **User-Friendly Interface**
  - Clean, modern design with intuitive layout
  - Real-time conversion updates
  - Category icons for better visualization
  - Mobile-responsive design

- **Advanced Features**
  - Quick conversion presets for common conversions
  - Conversion history tracking with timestamp
  - Export history to CSV
  - Favorite conversions system
  - Copy results to clipboard
  - Conversion formula display
  - Comprehensive help section

## 🚀 Setup Instructions

1. **Prerequisites**
   - Python 3.8 or higher
   - pip or uv package manager

2. **Installation**

   Using pip:
   ```bash
   pip install -r requirements.txt
   ```

   Or using uv (recommended):
   ```bash
   pip install uv
   uv pip install -r requirements.txt
   ```

3. **Running the Application**
   ```bash
   streamlit run main.py
   ```

## 📦 Dependencies

- streamlit==1.42.2
- pandas==2.2.3
- numpy==2.2.3

## 💡 Usage Tips

1. **Basic Usage**
   - Select a measurement category from the dropdown
   - Choose the units to convert from/to
   - Enter your value
   - See results instantly

2. **Advanced Features**
   - Use quick conversion buttons for common conversions
   - Save frequently used conversions as favorites
   - View conversion history in the sidebar
   - Export conversion history as CSV
   - View conversion formulas for each category

3. **Keyboard Shortcuts**
   - `Enter`: Submit value
   - `Tab`: Navigate between fields
   - `Space`: Toggle expanders

## 🔧 Features in Detail

### Conversion History
- Tracks recent conversions with timestamps
- Displays last 5 conversions in sidebar
- Export complete history to CSV
- Clear history option

### Quick Conversions
- Preset conversions for common use cases
- Category-specific quick conversion buttons
- Instant results display

### Favorites System
- Save frequently used conversions
- Quick access to saved conversions
- Delete favorites as needed

### Formula Display
- View conversion formulas for each category
- Temperature conversion formulas
- Base unit conversion explanations

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements you'd like to add. Some areas for potential enhancement:
- Additional unit categories
- More conversion presets
- Enhanced visualization features
- Offline mode support
- Unit conversion API integration

## 📄 License

This project is open source and available under the MIT License.
