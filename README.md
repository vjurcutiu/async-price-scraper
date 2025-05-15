# Demo Script: async-price-scraper/demo.py

This README covers running the standalone `demo.py` script, which showcases asynchronous scraping, retries, caching, and report generation.

## Prerequisites

* Python 3.9 or newer
* Packages listed in `requirements.txt`:

  * `aiohttp`
  * `async-timeout`
  * `pandas` (optional for extended reporting)

## Setup

1. **Clone the repo (if not already)**

   ```bash
   git clone https://github.com/your-username/async-price-scraper.git
   cd async-price-scraper
   ```

2. **Create a virtual environment (recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

The demo script uses a simple file-based cache under `cache/`. You can modify these variables at the top of `demo.py`:

```python
CACHE_DIR = 'cache'         # Directory for cached responses
RETRY_ATTEMPTS = 3          # Number of retries per URL
TIMEOUT_SECONDS = 10        # Request timeout
BACKOFF_BASE = 2            # Exponential backoff base
```

## Running the Demo

1. **Prepare URLs**

   * Edit the list in `demo.py` under `if __name__ == '__main__':` to include your target URLs.

2. **Run the script**

   ```bash
   python demo.py
   ```

3. **View the report**

   * After execution, a `report.json` file is created in the project root.
   * It contains a `summary` section (total, failures) and full `details` of each fetch.

## Extending the Demo

* **Switch cache backend**: Replace the file cache logic with Redis or another store.
* **Database integration**: Instead of writing JSON, insert results into your database.
* **Alerting**: Add email or Slack notifications in `generate_report()`.

---

Enjoy exploring the demo script! Feel free to customize it for your use case.
