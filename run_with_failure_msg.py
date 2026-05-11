import logging
from configs.auto_email import send_email

def run_with_error_handling():
    try:
        import Report.main
        Report.main.main()
    except Exception as e:
        logging.error("Automation failed with error: %s", str(e))
        print("An error occurred. Check error.log for details.")
        send_email(
        recipient="pooja.kr@example.com",
        subject="Automation Report",
        body="Hi Pooja,\n\nYour automation report is failed. Please  have a look in the script and fix it! \n\nRegards,\nAutomation Bot"
    )

