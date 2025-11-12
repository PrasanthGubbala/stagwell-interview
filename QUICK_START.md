# Quick Start Guide

## For Candidates

**You only need Docker installed!**

**Note:** No `.env` file needed - everything is pre-configured!

1. **Start the project:**
   ```bash
   docker-compose up --build
   ```

2. **Wait for the server to start** (you'll see "Starting development server at http://0.0.0.0:8000/")

3. **The API is ready at:** `http://localhost:8008/`

4. **Run tests:**
   ```bash
   docker-compose exec web pytest
   ```

That's it! All dependencies are installed in the container. Your code changes will be reflected immediately.

## For Interviewers

After the candidate completes the exercise, run:

```bash
docker-compose exec web python check_quality.py
```

This will generate a `quality_report.json` file with detailed scores.

