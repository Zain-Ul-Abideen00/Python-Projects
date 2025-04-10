# 🔒 Secure Data Encryption System

A Streamlit-based application for secure data storage and retrieval using advanced encryption techniques.

## Features

- 🔐 **Secure Data Encryption**
  - Uses Fernet encryption for data security
  - PBKDF2 key derivation for passkey hashing
  - Secure salt storage and management

- 🔑 **Authentication System**
  - Passkey-based authentication
  - Account lockout after 3 failed attempts
  - 5-minute lockout period for security

- 📊 **Data Management**
  - Store encrypted data with metadata
  - Retrieve data using Entry ID and passkey
  - Manage and delete stored entries
  - Copy Entry ID to clipboard functionality

- 💾 **Data Persistence**
  - JSON-based storage system
  - Automatic data loading and saving
  - Secure key and salt file management

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd secure-data-encryption
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
streamlit run main.py
```

2. Navigate through the tabs:
   - **Home**: Overview of features and security measures
   - **Store Data**: Encrypt and store new data
   - **Retrieve Data**: Decrypt and view stored data
   - **Manage Data**: View and manage all stored entries
   - **Login**: Authentication system

### Storing Data

1. Navigate to the "Store Data" tab
2. Enter your data in the text area
3. Create a secure passkey
4. (Optional) Add metadata:
   - Title
   - Tags
   - Expiration date
5. Click "Encrypt & Save"
6. Copy and save the generated Entry ID

### Retrieving Data

1. Navigate to the "Retrieve Data" tab
2. Enter the Entry ID
3. Enter your passkey
4. Click "Decrypt" to view your data

### Managing Data

1. Navigate to the "Manage Data" tab
2. View all stored entries
3. Expand entries to see details
4. Delete entries as needed

## Security Features

- **Encryption**: Uses Fernet (symmetric encryption) for data security
- **Key Derivation**: PBKDF2 with SHA256 for secure passkey hashing
- **Salt Storage**: Secure salt generation and storage
- **Lockout System**: Prevents brute force attacks
- **Session Management**: Secure session handling

## File Structure

- `main.py`: Main application code
- `encrypted_data.json`: Stores encrypted data
- `encryption_key.key`: Stores encryption key
- `salt.key`: Stores salt for key derivation

## Requirements

- Python 3.7+
- Streamlit
- cryptography
- Other dependencies listed in requirements.txt

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Streamlit for the web framework
- cryptography library for encryption
- Python standard library for security features
