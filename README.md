# Scheduling a Python Script Every 2 Minutes on macOS

This guide explains how to schedule a Python script to run every 2 minutes on a Mac using `cron`, with the Python script made executable.

---

## Step 1: Prepare Your Python Script

1. Add a shebang line at the very top of your Python script:

    ```python
    #!/usr/bin/env python3
    ```

2. Make the script executable by running:

    ```bash
    chmod +x /full/path/to/your_script.py
    ```

---

## Step 2: Verify Python Interpreter Path (Optional)

To check the Python 3 interpreter path, run:

```bash
which python3
````

Typical output:

```
/usr/bin/python3
```

---

## Step 3: Edit the Cron Table

Open your crontab editor:

```bash
crontab -e
```

Add this line to run your script every 2 minutes:

```cron
*/2 * * * * /full/path/to/your_script.py
```

**Notes:**

* `*/2` in the minutes field means "every 2 minutes".
* Use the **absolute path** for your script.
* Since your script is executable and has the shebang line, you don’t need to call `python3` explicitly.

---

## Step 4: Save and Exit

* In `nano`, press `Ctrl + O` to save and `Ctrl + X` to exit.
* Your cron job is now scheduled.

---

## Step 5: Troubleshooting Tips

* Test your script manually to ensure it works:

  ```bash
  /full/path/to/your_script.py
  ```

* To capture logs and errors, modify the cron entry to redirect output:

  ```cron
  */2 * * * * /full/path/to/your_script.py >> /tmp/myscript.log 2>&1
  ```

* Check system logs for cron activity:

  ```bash
  tail -f /var/log/system.log
  ```

---

## Summary Table

| Task                        | Command / Setting                          |
| --------------------------- | ------------------------------------------ |
| Add shebang to script       | `#!/usr/bin/env python3`                   |
| Make script executable      | `chmod +x /full/path/to/your_script.py`    |
| Edit crontab                | `crontab -e`                               |
| Cron job line (every 2 min) | `*/2 * * * * /full/path/to/your_script.py` |

---

Feel free to reach out if you need help automating this setup or debugging cron jobs!



macOS Catalina and later introduced System Integrity Protection (SIP) and stricter privacy permissions. Access to certain folders like Documents, Desktop, Downloads requires explicit permission for apps or services.

Since cron runs as a background process without GUI interaction, it likely doesn't have permission to access your Documents folder.

Move the file just under the [user] will solve the problem.

* * * * * command_to_run
| | | | |
| | | | +----- Day of the week (0 - 7) (Sunday = 0 or 7)
| | | +------- Month (1 - 12)
| | +--------- Day of the month (1 - 31)
| +----------- Hour (0 - 23)
+------------- Minute (0 - 59)


