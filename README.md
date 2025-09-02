# Advanced Selenium Demo

This repository contains the code for a demo application and its corresponding Selenium test automation framework. It's designed to showcase advanced techniques and best practices.

The project demonstrates:

* A component-based Page Object Model (POM)
* Robust waiting strategies (Explicit and Fluent Waits)
* Best practices for locators

---

## Getting Started

### Prerequisites

You need to have Python and `pip` installed on your machine. We recommend using a virtual environment to manage dependencies.

```bash
# Clone the repository
git clone https://github.com/tarunsinghofficial/selenium-test-bp.git
cd selenium-test-bp
```

---

### Installation

1. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use .\venv\Scripts\activate
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

### Running the Demo App

To run the web application for testing:

```bash
python serve_app.py
```

The app will be accessible at `http://localhost:8000`. Make sure you keep running the application.

---

### Running the Tests

Make sure the demo app is running in a separate terminal.

```bash
# Run all tests
pytest tests/
```

Run tests in **parallel with Grid**:

1. Start Selenium Grid (standalone)

```bash
java -jar selenium-server-4.35.0.jar standalone
```

2. Run tests

```bash
.\cross_browser_test.bat test-local
```

Run tests with **cross-browser implementation**:

```bash
.\cross_browser_test.bat test-local
```

---

## Reference

For more details on the code and the advanced concepts, please refer to the accompanying blog post.
