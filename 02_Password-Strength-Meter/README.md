# 🔒 Password Strength Meter

A modern, feature-rich password strength analyzer and generator built with Python and Streamlit. This application helps users create and evaluate secure passwords with real-time feedback and detailed analysis.

## 🌐 Live Demo

Try it out here: [Password Strength Meter](https://password-meter.streamlit.app/)

## 🌟 Features

### Password Analysis
- ✨ Real-time password strength evaluation
- 📊 Interactive strength gauge with color indicators
- 🔍 Detailed entropy calculation
- ⚡ Instant feedback on password requirements
- ❌ Common password detection and warnings

### Password Generation
- 🎲 Secure password generator
- 🔧 Customizable password length (12-32 characters)
- ⚙️ Optional special characters
- 📋 One-click copy functionality

### User Interface
- 🎨 Modern, responsive design
- 🌓 Dark/Light mode support
- 💫 Smooth animations and transitions
- 🎯 Interactive tooltips
- 📱 Mobile-friendly layout

### Security Features
- 🛡️ Advanced scoring algorithm
- 📝 Multiple criteria evaluation
- 🚫 Common password blacklist
- 🔐 Pattern detection and analysis
- 📈 Entropy-based strength calculation

## 🛠️ Technical Stack

- **Python 3.8+**
- **Streamlit** - For the web interface
- **Plotly** - For interactive gauge visualization
- **Custom Password Analysis Engine** - For comprehensive password evaluation

## 📋 Requirements

```bash
streamlit>=1.42.0
plotly
```

## 🚀 Quick Start

1. **Clone the repository**
```bash
git clone <repository-url>
cd password-strength-meter
```

2. **Set up virtual environment**
```bash
# Using venv
python -m venv venv
source venv/bin/activate  # On Unix/MacOS
venv\\Scripts\\activate   # On Windows

# Or using uv (recommended)
uv venv
.venv/bin/activate       # On Unix/MacOS
.venv\\Scripts\\activate # On Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
# Or using uv
uv pip install -r requirements.txt
```

4. **Run the application**
```bash
streamlit run app.py
```

## 🔍 Password Strength Criteria

The application evaluates passwords based on multiple factors:

### Core Criteria
- Minimum length (8 characters)
- Character composition:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special characters (!@#$%^&*)

### Advanced Analysis
- Entropy calculation
- Pattern detection
- Common password checking
- Character repetition analysis
- Sequential character detection

### Scoring System
- **Very Weak** (Score: 0-2): Fails basic security requirements
- **Weak** (Score: 2-3): Meets minimal requirements
- **Moderate** (Score: 3-4): Satisfactory strength
- **Strong** (Score: 4-5): Good security level
- **Very Strong** (Score: 5-6): Excellent security

## 🎯 Use Cases

- Personal password security
- Enterprise password policy compliance
- Security awareness training
- Password policy enforcement

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and enhancement requests.

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 👨‍💻 Developer

### Zain Ul Abideen
Full Stack Developer passionate about creating secure and user-friendly applications.

#### Connect With Me
[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=About.me&logoColor=white)](https://zain-ul-abideen.vercel.app/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Zain-Ul-Abideen00)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/zain-ul-abideen00/)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:zain.dev00@gmail.com)

#### Projects
- 🌐 [Password Strength Meter](https://password-meter.streamlit.app/)
- 👨‍💻 More projects on my [portfolio](https://zain-ul-abideen.vercel.app/)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Password security best practices from NIST guidelines
- Streamlit community for the amazing framework
- All contributors and users of this project
