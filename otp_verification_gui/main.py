import tkinter as tk
from tkinter import messagebox
import random
import threading
import time

class OTPApp:
    def __init__(self, root):
        self.root = root
        root.title("OTP Verification - Demo")
        root.geometry("420x300")
        root.resizable(False, False)

        self.otp = None
        self.otp_valid_until = 0

        tk.Label(root, text="Recipient (phone or email):").pack(pady=(12,0))
        self.recipient_entry = tk.Entry(root, width=40)
        self.recipient_entry.pack(pady=6)

        send_frame = tk.Frame(root)
        send_frame.pack(pady=6)
        self.send_btn = tk.Button(send_frame, text="Send OTP (Demo)", command=self.send_otp)
        self.send_btn.pack(side="left", padx=6)
        self.resend_lbl = tk.Label(send_frame, text="")
        self.resend_lbl.pack(side="left", padx=6)

        tk.Label(root, text="Enter OTP:").pack(pady=(12,0))
        self.otp_entry = tk.Entry(root, width=20)
        self.otp_entry.pack(pady=6)

        verify_frame = tk.Frame(root)
        verify_frame.pack(pady=6)
        self.verify_btn = tk.Button(verify_frame, text="Verify OTP", command=self.verify_otp)
        self.verify_btn.pack(side="left", padx=6)
        self.clear_btn = tk.Button(verify_frame, text="Clear", command=self.clear_inputs)
        self.clear_btn.pack(side="left", padx=6)

        self.status_label = tk.Label(root, text="", wraplength=380)
        self.status_label.pack(pady=12)

        # Info
        info = ("This is a demo OTP generator/validator.\n"
                "It simulates sending an OTP and displays it for testing.\n"
                "To make this send real SMS/email, replace the send_otp_to_recipient() function.")
        tk.Label(root, text=info, justify="left", fg="gray").pack(side="bottom", pady=6)

    def send_otp(self):
        recipient = self.recipient_entry.get().strip()
        if not recipient:
            messagebox.showwarning("Missing recipient", "Please enter a recipient (phone or email).")
            return

        # disable send button briefly to avoid spam
        self.send_btn.config(state="disabled")
        self.resend_lbl.config(text="Please wait 30s to resend")
        threading.Thread(target=self._send_otp_background, args=(recipient,), daemon=True).start()

    def _send_otp_background(self, recipient):
        # Create OTP
        self.otp = f"{random.randint(0, 999999):06d}"
        # set expiry in 2 minutes
        self.otp_valid_until = time.time() + 120

        # --- Replace this function with actual sending (SMS/Email) ---
        self.send_otp_to_recipient(recipient, self.otp)
        # -------------------------------------------------------------

        # Update UI
        self.status_label.config(text=f"OTP sent to {recipient}. (Demo shows it in a popup)\nOTP expires in 120 seconds.")
        # re-enable send after 30 seconds
        for i in range(30, 0, -1):
            self.resend_lbl.config(text=f"Resend available in {i}s")
            time.sleep(1)
        self.send_btn.config(state="normal")
        self.resend_lbl.config(text="")

    def send_otp_to_recipient(self, recipient, otp):
        # DEMO sending: show the OTP in a popup (for development/testing).
        # In production replace this with an API call to SMS or email provider.
        message = f"(DEMO) OTP for {recipient}: {otp}"
        # Using after to ensure it runs on main thread
        self.root.after(0, lambda: messagebox.showinfo("Demo: OTP Sent", message))

    def verify_otp(self):
        entered = self.otp_entry.get().strip()
        if not entered:
            messagebox.showwarning("Missing OTP", "Please enter the OTP you received.")
            return
        if self.otp is None:
            messagebox.showerror("No OTP Sent", "Please request an OTP first.")
            return
        if time.time() > self.otp_valid_until:
            messagebox.showerror("OTP Expired", "The OTP has expired. Please request a new one.")
            return
        if entered == self.otp:
            messagebox.showinfo("Success", "OTP verified successfully!")
            self.status_label.config(text="OTP verified successfully.")
            # clear after success
            self.otp = None
            self.otp_entry.delete(0, 'end')
        else:
            messagebox.showerror("Failed", "Incorrect OTP. Please try again.")

    def clear_inputs(self):
        self.recipient_entry.delete(0, 'end')
        self.otp_entry.delete(0, 'end')
        self.status_label.config(text="")

if __name__ == '__main__':
    root = tk.Tk()
    app = OTPApp(root)
    root.mainloop()
