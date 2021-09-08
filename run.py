from app import APP
from getStreamData import getStreamData
import threading


@APP.before_first_request
def activate_job():
    def run_job():
        getStreamData()

    thread = threading.Thread(target=run_job)
    thread.start()


if __name__ == "__main__":
    APP.run(port=8000, debug=True)

