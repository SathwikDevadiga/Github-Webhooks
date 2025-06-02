from datetime import datetime, timezone

def Format_Date_UTC(date):

    dt = datetime.fromisoformat(str(date))
    formatted = dt.strftime("%d %B %Y - %I:%M %p UTC")
    return formatted


def Format_Date(datetime_str):
    dt = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S%z")
    output_str = dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return output_str
