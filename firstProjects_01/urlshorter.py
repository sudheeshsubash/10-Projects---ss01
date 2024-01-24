
import pyshorteners as ps


def shortener(url):
    s = ps.Shortener()
    return s.tinyurl.short(url)