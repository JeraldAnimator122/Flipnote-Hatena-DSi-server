# --- 1. SET YOUR ACTUAL DOMAIN HERE ---
MY_SERVER_URL = "jeraldmemo.neocities.org"
FSID = "(X-Dsi-ID)"

def get_universal_fillers(fsid, user_stats):
    """
    This is the master list. 
    The left side is the {TAG} in your HTML.
    The right side is the data we want to put there.
    """
    return {
        "{DOMAIN}": MY_SERVER_URL,  # <-- This links to the setting above
        "{FSID}": FSID,
        "{THEME}": user_stats.get("theme", "default"),
        "{USERNAME}": user_stats.get("username", "Jeraldmemo User"),
        
        # Star Counts from the .data file
        "{STAR_GREEN_COUNT}": user_stats.get("stars_green", "0"),
        "{STAR_RED_COUNT}": user_stats.get("stars_red", "0"),
        "{STAR_GOLD_COUNT}": user_stats.get("stars_gold", "0"),
        
        # Supporter Badge Logic
        # If they are a supporter, {BADGE} becomes a star icon. If not, it's empty.
        "{BADGE}": "★" if user_stats.get("is_supporter") == "true" else ""
    }
