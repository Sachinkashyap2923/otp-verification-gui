# OTP Verification GUI (Demo)

This is a simple demo application that implements OTP generation and verification
with a graphical user interface using Tkinter (Python).

**Important:** This demo *does not* send real SMS or emails. The OTP is shown
in a popup for testing purposes. To use with real SMS/email providers, replace
the `send_otp_to_recipient()` function in `main.py` with calls to an API such as:
- Twilio (SMS)
- AWS SNS (SMS)
- SendGrid / SMTP (email)

## Files
- `main.py` – The Tkinter GUI application.
- `README.md` – This file.
- `run.bat` – Windows double-click launcher.
- `run.sh` – Unix shell launcher.

## Requirements
- Python 3.7+
- Tkinter (usually included with standard Python installations)

## Run (Windows)
Double-click `run.bat` or run:
```
python main.py
```

## Run (Linux / macOS)
Make `run.sh` executable and run:
```
chmod +x run.sh
./run.sh
```

## Notes
- OTPs expire after 120 seconds (2 minutes).
- Resend is disabled for 30 seconds to simulate a basic rate limit.
- Replace the demo sending function with your preferred provider to deliver real OTPs.
