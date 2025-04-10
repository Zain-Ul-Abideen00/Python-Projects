import streamlit as st
import hashlib
import json
import time
import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from pathlib import Path
from datetime import datetime, timedelta

# Constants
MAX_ATTEMPTS = 3
LOCKOUT_TIME = 300  # 5 minutes in seconds
DATA_FILE = "encrypted_data.json"
KEY_FILE = "encryption_key.key"
SALT_FILE = "salt.key"

# Function to generate or load encryption key
def get_encryption_key():
    if Path(KEY_FILE).exists():
        with open(KEY_FILE, "rb") as key_file:
            return key_file.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
        return key

# Function to generate or load salt
def get_salt():
    if Path(SALT_FILE).exists():
        with open(SALT_FILE, "rb") as salt_file:
            return salt_file.read()
    else:
        salt = os.urandom(16)
        with open(SALT_FILE, "wb") as salt_file:
            salt_file.write(salt)
        return salt

# Initialize encryption components
KEY = get_encryption_key()
SALT = get_salt()
cipher = Fernet(KEY)

# Initialize session state
if 'stored_data' not in st.session_state:
    st.session_state.stored_data = {}
if 'failed_attempts' not in st.session_state:
    st.session_state.failed_attempts = 0
if 'last_attempt_time' not in st.session_state:
    st.session_state.last_attempt_time = 0
if 'is_authenticated' not in st.session_state:
    st.session_state.is_authenticated = False
if 'user_data' not in st.session_state:
    st.session_state.user_data = {}

# Function to load data from file
def load_data():
    if Path(DATA_FILE).exists():
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

# Function to save data to file
def save_data():
    with open(DATA_FILE, 'w') as f:
        json.dump(st.session_state.stored_data, f)

# Enhanced PBKDF2 hashing with configurable iterations
def hash_passkey(passkey, salt=None, iterations=100000):
    if salt is None:
        salt = SALT
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations,
    )
    return base64.b64encode(kdf.derive(passkey.encode())).decode()

# Function to encrypt data with metadata
def encrypt_data(text, passkey, metadata=None):
    if metadata is None:
        metadata = {
            "timestamp": datetime.now().isoformat(),
            "encryption_type": "Fernet",
            "version": "1.0"
        }

    # Encrypt the text
    encrypted_text = cipher.encrypt(text.encode()).decode()

    # Create a unique identifier for this entry
    entry_id = hashlib.sha256(f"{encrypted_text}{time.time()}".encode()).hexdigest()

    return {
        "id": entry_id,
        "encrypted_text": encrypted_text,
        "metadata": metadata,
        "passkey_hash": hash_passkey(passkey)
    }

# Function to decrypt data with validation
def decrypt_data(entry_id, passkey):
    current_time = time.time()

    # Check if user is locked out
    if st.session_state.failed_attempts >= MAX_ATTEMPTS:
        if current_time - st.session_state.last_attempt_time < LOCKOUT_TIME:
            remaining_time = int((LOCKOUT_TIME - (current_time - st.session_state.last_attempt_time))/60)
            st.error(f"🔒 Account locked! Please try again in {remaining_time} minutes.")
            return None

    # Find the entry
    entry = st.session_state.stored_data.get(entry_id)
    if not entry:
        st.error("❌ Entry not found!")
        return None

    # Verify passkey
    if hash_passkey(passkey) != entry["passkey_hash"]:
        st.session_state.failed_attempts += 1
        st.session_state.last_attempt_time = current_time
        attempts_remaining = MAX_ATTEMPTS - st.session_state.failed_attempts
        st.error(f"❌ Incorrect passkey! Attempts remaining: {attempts_remaining}")
        return None

    # Reset failed attempts on successful decryption
    st.session_state.failed_attempts = 0

    try:
        return cipher.decrypt(entry["encrypted_text"].encode()).decode()
    except Exception as e:
        st.error(f"❌ Decryption failed: {str(e)}")
        return None

# Function to check authentication
def check_auth():
    if st.session_state.failed_attempts >= MAX_ATTEMPTS:
        if not st.session_state.is_authenticated:
            st.warning("🔒 Too many failed attempts! Please login to continue.")
            return False
    return True

# Load data on startup
st.session_state.stored_data = load_data()

# Streamlit UI
st.set_page_config(
    page_title="Secure Data Encryption System",
    page_icon="🔒",
    layout="centered"
)

# Main title
st.title("🔒 Secure Data Encryption System")

# Create tabs for navigation
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Home", "Store Data", "Retrieve Data", "Manage Data", "Login"])

with tab1:
    st.header("Welcome to the Secure Data System")

    st.subheader("Features")
    st.write("""
    - 🔐 Secure data encryption using Fernet
    - 🔑 Passkey-based authentication
    - ⚠️ Account lockout after 3 failed attempts
    - 💾 Data persistence using JSON storage
    - 📊 Data management interface
    - 🕒 Time-based lockout system
    """)

    st.subheader("Security Measures")
    st.write("""
    - PBKDF2 key derivation
    - Secure salt storage
    - Encrypted key management
    - Metadata tracking
    - Entry validation
    """)

with tab2:
    st.header("Store Data Securely")

    if not check_auth():
        st.info("Please login first to store data.")
    else:
        st.write("Enter your data and a secure passkey to encrypt and store it.")

        user_data = st.text_area("Data to Encrypt:", height=200, key="store_data_text")
        passkey = st.text_input("Passkey:", type="password", key="store_passkey")

        with st.expander("Additional Options"):
            data_title = st.text_input("Title:", key="store_title")
            data_tags = st.text_input("Tags (comma-separated):", key="store_tags")
            expiration = st.date_input("Expiration Date:", key="store_expiration")

        if st.button("Encrypt & Save", key="store_button", type="primary"):
            if user_data and passkey:
                metadata = {
                    "title": data_title,
                    "tags": data_tags.split(",") if data_tags else [],
                    "expiration": expiration.isoformat() if expiration else None,
                    "timestamp": datetime.now().isoformat()
                }

                encrypted_entry = encrypt_data(user_data, passkey, metadata)
                entry_id = encrypted_entry["id"]
                st.session_state.stored_data[entry_id] = encrypted_entry
                save_data()

                st.success("Data stored securely!")
                st.code(entry_id, language="text")
                st.info("Please save this Entry ID. You'll need it to retrieve your data.")
            else:
                st.error("Data and passkey are required!")

with tab3:
    st.header("Retrieve Your Data")

    if not check_auth():
        st.info("Please login first to retrieve data.")
    else:
        st.write("Enter the Entry ID and passkey to decrypt your data.")

        entry_id = st.text_input("Entry ID:", key="retrieve_entry_id")
        passkey = st.text_input("Passkey:", type="password", key="retrieve_passkey")

        if st.button("Decrypt", key="retrieve_button", type="primary"):
            if entry_id and passkey:
                decrypted_text = decrypt_data(entry_id, passkey)

                if decrypted_text:
                    entry = st.session_state.stored_data[entry_id]
                    metadata = entry.get("metadata", {})

                    st.success("Data decrypted successfully!")
                    st.text_area("Decrypted Data:", decrypted_text, height=200, key="decrypted_data")

                    if metadata.get("title"):
                        st.write(f"**Title:** {metadata['title']}")
                    if metadata.get("tags"):
                        st.write(f"**Tags:** {', '.join(metadata['tags'])}")
                    if metadata.get("expiration"):
                        exp_date = datetime.fromisoformat(metadata["expiration"])
                        if datetime.now() > exp_date:
                            st.warning("This data has expired!")
                else:
                    if st.session_state.failed_attempts >= MAX_ATTEMPTS:
                        st.warning("Too many failed attempts! Please login to continue.")
                        st.session_state.is_authenticated = False
            else:
                st.error("Both Entry ID and passkey are required!")

with tab4:
    st.header("Manage Your Data")

    if not st.session_state.is_authenticated:
        st.warning("You must be logged in to access this page.")
        st.info("Please go to the Login tab to authenticate.")
    else:
        if st.session_state.stored_data:
            st.write(f"Total entries: {len(st.session_state.stored_data)}")

            for entry_id, entry in st.session_state.stored_data.items():
                with st.expander(f"Entry: {entry_id[:8]}..."):
                    metadata = entry.get("metadata", {})

                    st.write(f"**Created:** {metadata.get('timestamp', 'N/A')}")
                    if metadata.get("title"):
                        st.write(f"**Title:** {metadata['title']}")
                    if metadata.get("tags"):
                        st.write(f"**Tags:** {', '.join(metadata['tags'])}")

                    if st.button(f"Delete {entry_id[:8]}...", key=f"delete_{entry_id}", type="secondary"):
                        del st.session_state.stored_data[entry_id]
                        save_data()
                        st.rerun()
        else:
            st.info("No data entries found.")

with tab5:
    st.header("Authentication")

    if st.session_state.is_authenticated:
        st.success("You are already authenticated!")
        if st.button("Logout", key="logout_button", type="secondary"):
            st.session_state.is_authenticated = False
            st.session_state.failed_attempts = 0
            st.rerun()
    else:
        st.write("Enter your master password to authenticate.")
        login_pass = st.text_input("Master Password:", type="password", key="login_password")

        if st.button("Login", key="login_button", type="primary"):
            if login_pass == "admin123":  # In production, use proper authentication
                st.session_state.failed_attempts = 0
                st.session_state.is_authenticated = True
                st.success("Authenticated successfully!")
                st.rerun()
            else:
                st.error("Incorrect password!")
