"""Date parsing and staleness helpers for as_of / last_reviewed fields."""

from datetime import date, datetime
from typing import Optional, Union

DateLike = Union[str, date, datetime, None]


def parse_partial_date(value: DateLike) -> Optional[date]:
    """Parse YYYY-MM or YYYY-MM-DD (or date/datetime) into a date.

    Month-only values use the first day of the month so age is conservative.
    """
    if value is None:
        return None
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    text = str(value).strip()
    if not text:
        return None
    if len(text) == 7 and text[4] == "-":
        try:
            year = int(text[:4])
            month = int(text[5:7])
            return date(year, month, 1)
        except ValueError:
            return None
    if len(text) >= 10 and text[4] == "-" and text[7] == "-":
        try:
            return date.fromisoformat(text[:10])
        except ValueError:
            return None
    return None


def age_days(value: DateLike, today: Optional[date] = None) -> Optional[int]:
    """Days between a parsed date and today. None if the value cannot be parsed."""
    parsed = parse_partial_date(value)
    if parsed is None:
        return None
    if today is None:
        today = date.today()
    return (today - parsed).days


def iso_today(today: Optional[date] = None) -> str:
    if today is None:
        today = date.today()
    return today.isoformat()


def year_month(today: Optional[date] = None) -> str:
    if today is None:
        today = date.today()
    return today.strftime("%Y-%m")
