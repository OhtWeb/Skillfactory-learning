def format_date(date, format="dmy"):
   year, month, day = date.split("-")
   if format == "dmy":
       return f"{day}{month}{year}"
   elif format == "mdy":
       return f"{month}{day}{year}"
   elif format == "ymd":
       return f"{year}{month}{day}"
   else:
       return date