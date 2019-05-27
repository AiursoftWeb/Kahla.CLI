def second2time(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)

    return "%02d:%02d:%02d" % (h, m, s)
