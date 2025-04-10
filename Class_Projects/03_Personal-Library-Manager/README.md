# Personal Library Manager

The Personal Library Manager is an application designed to help users manage their personal book collections. It provides features for adding, viewing, and organizing books.

## Project Structure

- **src/**: Contains the main application code.
  - `main.py`: The main script to run the application.
  - **assets/**: Directory for storing static assets like images or icons.

- **storage/**: Contains data storage files.
  - `books.json`: A JSON file for storing book data.
  - **temp/**: Temporary files directory.
  - **data/**: Additional data storage.

- **.venv/**: Virtual environment for managing project dependencies.

## Run the App

### Using uv

Run as a desktop app:

```bash
uv run flet run
```

Run as a web app:

```bash
uv run flet run --web
```

### Using Poetry

Install dependencies from `pyproject.toml`:

```bash
poetry install
```

Run as a desktop app:

```bash
poetry run flet run
```

Run as a web app:

```bash
poetry run flet run --web
```

For more details on running the app, refer to the [Getting Started Guide](https://flet.dev/docs/getting-started/).

## Build the App

### Android

```bash
flet build apk -v
```

For more details on building and signing `.apk` or `.aab`, refer to the [Android Packaging Guide](https://flet.dev/docs/publish/android/).

### iOS

```bash
flet build ipa -v
```

For more details on building and signing `.ipa`, refer to the [iOS Packaging Guide](https://flet.dev/docs/publish/ios/).

### macOS

```bash
flet build macos -v
```

For more details on building macOS package, refer to the [macOS Packaging Guide](https://flet.dev/docs/publish/macos/).

### Linux

```bash
flet build linux -v
```

For more details on building Linux package, refer to the [Linux Packaging Guide](https://flet.dev/docs/publish/linux/).

### Windows

```bash
flet build windows -v
```

For more details on building Windows package, refer to the [Windows Packaging Guide](https://flet.dev/docs/publish/windows/).
