import psycopg2
from config import load_config


def get_conn():
    return psycopg2.connect(**load_config())