import hashlib
import json
import os
import re
import secrets
from getpass import getpass
from pathlib import Path


USERS_FILE = Path("users.json")
PBKDF2_ITERATIONS = 600_000


def hash_password(password: str, salt: bytes | None = None) -> tuple[str, str]:
	password_salt = salt or secrets.token_bytes(16)
	password_hash = hashlib.pbkdf2_hmac(
		"sha256",
		password.encode("utf-8"),
		password_salt,
		PBKDF2_ITERATIONS,
	)
	return password_salt.hex(), password_hash.hex()


def load_users() -> dict[str, dict[str, str]]:
	if not USERS_FILE.exists():
		return {}

	with USERS_FILE.open("r", encoding="utf-8") as file:
		return json.load(file)


def save_users(users: dict[str, dict[str, str]]) -> None:
	temporary_file = USERS_FILE.with_suffix(".tmp")
	with temporary_file.open("w", encoding="utf-8") as file:
		json.dump(users, file, indent=2)
		file.write("\n")
	os.replace(temporary_file, USERS_FILE)


def add_user(name: str, email: str, password: str) -> None:
	if not name.strip():
		raise ValueError("Name cannot be empty.")
	if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
		raise ValueError("Enter a valid email address.")
	if len(password) < 12:
		raise ValueError("Password must contain at least 12 characters.")

	users = load_users()
	if email in users:
		raise ValueError("That email is already registered.")

	salt, password_hash = hash_password(password)
	users[email] = {
		"name": name.strip(),
		"salt": salt,
		"password_hash": password_hash,
	}
	save_users(users)


if __name__ == "__main__":
	try:
		add_user(
			input("Name: "),
			input("Email: ").strip().lower(),
			getpass("Password: "),
		)
		print(f"User saved to {USERS_FILE}.")
	except (OSError, ValueError, json.JSONDecodeError) as error:
		print(f"Could not save user: {error}")
