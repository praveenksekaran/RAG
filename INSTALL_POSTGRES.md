# PostgreSQL Installation Guide

## Issue
You're encountering this error:
```
ImportError: no pq wrapper available.
Attempts made:
- couldn't import psycopg 'c' implementation: No module named 'psycopg_c'
- couldn't import psycopg 'binary' implementation: No module named 'psycopg_binary'
- couldn't import psycopg 'python' implementation: libpq library not found
```

## Solution

### Option 1: Install psycopg2-binary (Recommended)
This is the easiest solution for most users:

```bash
pip install psycopg2-binary
```

### Option 2: Install PostgreSQL Client Libraries (Alternative)

#### On Windows:
1. Download PostgreSQL from: https://www.postgresql.org/download/windows/
2. During installation, make sure to install the PostgreSQL client libraries
3. Add PostgreSQL bin directory to your PATH environment variable
4. Install psycopg2:
   ```bash
   pip install psycopg2
   ```

#### On macOS:
```bash
brew install postgresql
pip install psycopg2
```

#### On Ubuntu/Debian:
```bash
sudo apt-get install libpq-dev python3-dev
pip install psycopg2
```

### Option 3: Use psycopg3 (Modern Alternative)
```bash
pip install psycopg[binary]
```

## Updated Requirements
I've updated your `requirements.txt` to include:
- `psycopg2-binary` - Pre-compiled PostgreSQL adapter
- `langchain_postgres` - LangChain PostgreSQL integration

## Installation Steps
1. Activate your virtual environment:
   ```bash
   cd RAG
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install the updated requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Test the connection:
   ```python
   from langchain_postgres import PGVector
   # Your existing code should now work
   ```

## Troubleshooting

### If psycopg2-binary fails:
Try installing the system dependencies first, then use regular psycopg2:
```bash
pip uninstall psycopg2-binary
pip install psycopg2
```

### If you're still having issues:
Consider using an alternative vector store like ChromaDB (which you already have) or FAISS:
```python
from langchain_community.vectorstores import Chroma
# or
from langchain_community.vectorstores import FAISS
``` 