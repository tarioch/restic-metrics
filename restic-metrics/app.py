from prometheus_client import start_http_server, Gauge
import time

def retrieveLastBackupTime():
    return 2

if __name__ == '__main__':
    print('foo')
    timeLastBackup = Gauge('restic_backup_last_completed_time_seconds', 'Timestamp of the last backup')
    timeLastBackup.set_function(retrieveLastBackupTime)

    # Start up the server to expose the metrics.
    start_http_server(8000)

    while True:
        time.sleep(10)
