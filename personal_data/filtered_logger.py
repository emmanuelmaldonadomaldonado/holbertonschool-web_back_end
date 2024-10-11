#!/usr/bin/env python3
"""
Filtered logger module
"""
import re
import logging
import os
import mysql.connector
from typing import List

# Tuple containing fields that are considered PII
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Obfuscates the fields in a log message"""
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formats the log record and obfuscates PII fields"""
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """Creates and configures a logger for handling user data"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))

    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Connects to the database using environment variables"""
    return mysql.connector.connect(
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        database=os.getenv("PERSONAL_DATA_DB_NAME")
    )


def main() -> None:
    """Main function to retrieve and filter users' data from the database"""
    db = get_db()
    cursor = db.cursor()

    query = "SELECT name, email, phone, ssn, password, ip, last_login, user_agent FROM users"
    cursor.execute(query)

    logger = get_logger()

    for row in cursor:
        message = f"name={row[0]};email={row[1]};phone={row[2]};ssn={row[3]};" \
            f"password={row[4]};ip={row[5]};last_login={
                row[6]};user_agent={row[7]};"
        logger.info(message)

    cursor.close()
    db.close()
