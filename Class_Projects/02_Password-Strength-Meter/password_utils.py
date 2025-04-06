import re
import random
import string
import math
from typing import Dict, List, Union
import json
from pathlib import Path

class PasswordStrengthMeter:
    def __init__(self):
        # Load common passwords from file
        self.common_passwords = self._load_common_passwords()

        # Enhanced scoring weights with more granular controls
        self.weights = {
            "length": 1.5,      # Increased weight for length
            "uppercase": 1.0,   # Basic requirement
            "lowercase": 1.0,   # Basic requirement
            "digits": 1.0,      # Basic requirement
            "special": 1.2,     # Bonus for special characters
            "complexity": 1.3,  # Bonus for complexity
            "entropy": 1.2      # Bonus for randomness
        }

        # Extended complexity patterns
        self.complexity_patterns = [
            # Penalize patterns
            (r'(.)\1\1+', -0.5),  # Repeated characters
            (r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)', -0.3),  # Sequential letters
            (r'(123|234|345|456|567|678|789|890)', -0.3),  # Sequential numbers
            (r'(qwerty|asdfgh|zxcvbn)', -0.4),  # Keyboard patterns

            # Bonus patterns
            (r'(?=.*[A-Z].*[A-Z])', 0.2),  # Multiple uppercase
            (r'(?=.*[!@#$%^&*].*[!@#$%^&*])', 0.2),  # Multiple special chars
            (r'(?=.*\d.*\d.*\d)', 0.2),  # Multiple numbers
            (r'(?=.*[a-z].*[A-Z].*\d.*[!@#$%^&*])', 0.3)  # Good mix of characters
        ]

        # Special character set
        self.special_chars = "!@#$%^&*"

        # Minimum requirements
        self.min_length = 8
        self.recommended_length = 12

    def _load_common_passwords(self) -> set:
        """Load common passwords from a predefined set and optional file"""
        common_passwords = {
            "password", "123456", "qwerty", "admin", "letmein",
            "welcome", "password123", "admin123", "12345678", "abc123",
            "monkey", "dragon", "baseball", "football", "letme1n",
            "master", "hello123", "shadow", "superman", "qwerty123",
            "welcome123", "ninja", "abc123456", "123456789", "password1"
        }

        # Try to load additional passwords from file if exists
        try:
            password_file = Path(__file__).parent / "common_passwords.txt"
            if password_file.exists():
                with open(password_file, 'r') as f:
                    common_passwords.update(line.strip().lower() for line in f)
        except Exception:
            pass  # Fail silently if file operations fail

        return common_passwords

    def calculate_entropy(self, password: str) -> float:
        """Calculate password entropy (randomness) with improved accuracy"""
        if not password:
            return 0.0

        # Calculate character set size
        has_lower = bool(re.search(r'[a-z]', password))
        has_upper = bool(re.search(r'[A-Z]', password))
        has_digit = bool(re.search(r'\d', password))
        has_special = bool(re.search(f'[{re.escape(self.special_chars)}]', password))

        charset_size = 0
        if has_lower: charset_size += 26
        if has_upper: charset_size += 26
        if has_digit: charset_size += 10
        if has_special: charset_size += len(self.special_chars)

        # Calculate basic entropy
        length = len(password)
        basic_entropy = length * math.log2(max(charset_size, 1))

        # Adjust for repetition patterns
        char_freq = {}
        for char in password:
            char_freq[char] = char_freq.get(char, 0) + 1

        repetition_penalty = sum(count * math.log2(count) for count in char_freq.values() if count > 1)
        adjusted_entropy = max(0, basic_entropy - repetition_penalty/2)

        return adjusted_entropy

    def check_password_strength(self, password: str) -> Dict[str, Union[int, str, List[str], dict, float]]:
        """Enhanced password strength evaluation with detailed analysis"""
        if not password:
            return {
                "score": 0,
                "strength": "No Password",
                "feedback": ["Please enter a password."],
                "details": {},
                "entropy": 0.0,
                "length": 0
            }

        # Check against common passwords
        if password.lower() in self.common_passwords:
            return {
                "score": 1,
                "strength": "Very Weak",
                "feedback": [
                    "This is a commonly used password. Please choose a more unique password.",
                    "Common passwords are the first ones attackers try."
                ],
                "details": {},
                "entropy": self.calculate_entropy(password),
                "length": len(password)
            }

        # Initialize scoring
        score = 0
        feedback = []
        details = {}

        # Length analysis with progressive scoring
        length = len(password)
        details["length"] = length >= self.min_length
        length_score = min(2, length / self.min_length)
        score += length_score * self.weights["length"]

        if length < self.min_length:
            feedback.append(f"Password should be at least {self.min_length} characters long")
        elif length < self.recommended_length:
            feedback.append(f"Consider using at least {self.recommended_length} characters for stronger security")
        elif length >= 16:
            feedback.append("Good length! Longer passwords are harder to crack")

        # Character type analysis
        patterns = {
            "uppercase": (r'[A-Z]', "uppercase letter", "Uppercase letters (A-Z)"),
            "lowercase": (r'[a-z]', "lowercase letter", "Lowercase letters (a-z)"),
            "digits": (r'\d', "number", "Numbers (0-9)"),
            "special": (f'[{re.escape(self.special_chars)}]', "special character", f"Special characters ({self.special_chars})")
        }

        for key, (pattern, desc, full_desc) in patterns.items():
            matches = len(re.findall(pattern, password))
            details[key] = matches > 0
            if details[key]:
                score += self.weights[key]
                if matches > 2:
                    score += 0.1  # Small bonus for using more than 2 of each type
            else:
                feedback.append(f"Include at least one {desc}")

        # Complexity analysis
        complexity_score = 0
        for pattern, weight in self.complexity_patterns:
            if re.search(pattern, password):
                complexity_score += weight

        score += complexity_score * self.weights["complexity"]

        # Entropy analysis
        entropy = self.calculate_entropy(password)
        entropy_bonus = min(1, entropy / 4.0)
        score += entropy_bonus * self.weights["entropy"]

        # Determine strength level with more granular categories
        if score <= 2:
            strength = "Very Weak"
        elif score <= 3:
            strength = "Weak"
        elif score <= 4:
            strength = "Moderate"
        elif score <= 5:
            strength = "Strong"
        else:
            strength = "Very Strong"
            if not feedback:
                feedback = ["Excellent! Your password meets all security criteria."]

        # Add positive feedback for strong passwords
        if score > 4:
            if entropy > 3.5:
                feedback.append("Good job! Your password has high complexity and randomness.")
            if length >= 16:
                feedback.append("Excellent length! This makes the password much harder to crack.")

        return {
            "score": min(6, score),  # Cap score at 6
            "strength": strength,
            "feedback": feedback,
            "details": details,
            "entropy": entropy,
            "length": length
        }

    def generate_password(self, length: int = 16, include_special: bool = True) -> str:
        """Enhanced password generator with improved randomness and pattern avoidance"""
        if length < self.min_length:
            length = max(16, self.min_length)  # Use 16 or min_length, whichever is larger

        # Character sets
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        special = self.special_chars if include_special else ""

        # Ensure minimum requirements
        password = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits)
        ]

        if include_special:
            password.append(random.choice(special))

        # Fill remaining length with random characters
        all_chars = lowercase + uppercase + digits + (special if include_special else "")
        remaining_length = length - len(password)

        # Add remaining characters while avoiding patterns
        for _ in range(remaining_length):
            new_char = random.choice(all_chars)
            # Avoid three consecutive same characters and simple patterns
            while (len(password) >= 2 and
                   (new_char == password[-1] == password[-2] or
                    (len(password) >= 3 and
                     ''.join(password[-3:] + [new_char]).lower() in ['pass', 'word', '1234', 'abcd']))):
                new_char = random.choice(all_chars)
            password.append(new_char)

        # Shuffle the password multiple times for better randomness
        for _ in range(3):
            random.shuffle(password)

        return ''.join(password)

    def get_strength_color(self, strength: str) -> str:
        """Get color code for password strength with improved visibility"""
        colors = {
            "Very Weak": "#dc3545",    # Bootstrap danger red
            "Weak": "#ff4b4b",         # Lighter red
            "Moderate": "#ffc107",     # Bootstrap warning yellow
            "Strong": "#28a745",       # Bootstrap success green
            "Very Strong": "#198754"   # Darker green
        }
        return colors.get(strength, "#dc3545")  # Default to danger red
