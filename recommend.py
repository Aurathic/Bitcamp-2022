def get_recommendations(user_data):
    pass

def calculate_scores(row):
    # TODO Values based on PassMark:
    # https://forums.passmark.com/performancetest/4599-formula-cpu-mark-memory-mark-and-disk-mark?4490-Formula-CPU-mark-memory-mark-and-disk-mark=  
    performance     = 0.5 * row["Cpu percentile"] + 0.4 * row["Gpu percentile"] + 0.1 * row["Ram percentile"]
    portability     = 0.7 * row["Weight percentile"] + 0.3 * row["Size percentile"]
    battery_qual    = 0.3 * (1-row["Gpu percentile"]) + 0.3 * (1-row["Cpu percentile"]) + 0.2 * row["Size percentile"] + 0.1 * row["Price percentile"]
    screen_qual     = 0.8 * row["Pixel percentile"] + 0.2 * row["Size percentile"]


