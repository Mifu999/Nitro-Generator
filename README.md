# Discord Gift Code Generator Script

This Python script generates random Discord gift codes and sends them to a specified Discord webhook. The script continuously generates codes and posts them at regular intervals. It's perfect for testing webhooks or automating the process of sending random codes.

## Requirements

- Python 3.x
- `requests` library (can be installed via `pip install requests`)

## How to Run

1. **Clone or download** the repository to your local machine.
2. **Install dependencies** by running:
   ```bash
   pip install requests
   ```
3. **Set up your webhook URL**:
   - Go to Discord > Server Settings > Webhooks.
   - Copy the webhook URL.
   
4. **Launch the script**:
   - Run the `.bat` file to execute the Python script.

   Or you can run the Python script directly:
   ```bash
   python main.py
   ```

5. **Enter the Discord webhook URL** when prompted. The script will start generating and sending gift codes to your webhook every 3 seconds.

6. To stop the script, press `CTRL+C`.
