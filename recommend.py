def get_recommendations(user_data):
    
    return

def calculate_scores(laptop_data):
    # Volume of (probably?) the largest laptop
    # https://noteb.com/?model/model.php?conf=11553357781760999424_5877&ex=USD
    max_volume = 18.9*23.5*36.0
    max_ram_mb = 32000 # 32 GB
    max_battery_life = 20
    max_resolution = 3840*2400 
    max_screen_size = 17.3
    cpu_rating      = float(laptop_data["cpu"]["rating"]) / 100
    gpu_rating      = float(laptop_data["gpu"]["rating"]) / 100
    ram_amount      = float(laptop_data["memory_size"]) / max_ram_mb
    battery_life    = float(laptop_data["battery_life_raw"]) / max_battery_life
    resolution      = int(laptop_data["display"]["horizontal_resolution"]) * \
                          int(laptop_data["display"]["vertical_resolution"]) / max_resolution
    srgb            = float(laptop_data["display"]["srgb"]) / 100
    screen_size     = float(laptop_data["display"]["size"]) / max_screen_size
    volume          = float(laptop_data["height_cm"]) * \
                          float(laptop_data["depth_cm"]) * \
                          float(laptop_data["width_cm"]) / max_volume
    overall         = float(laptop_data["config_score"]) / 100

    # TODO Values based on PassMark:
    # https://forums.passmark.com/performancetest/4599-formula-cpu-mark-memory-mark-and-disk-mark?4490-Formula-CPU-mark-memory-mark-and-disk-mark=  
    performance     = 0.5 * cpu_rating + 0.4 * gpu_rating + 0.1 * ram_amount
    portability     = 0.8 * volume + 0.2 * overall
    battery_qual    = battery_life
    screen_qual     = 0.85 * resolution + 0.1 * screen_size + 0.05 * srgb

