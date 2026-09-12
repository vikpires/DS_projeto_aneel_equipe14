# Conversão de segundos em formato legível m:ss
def set_time_formatter(segundos: float) -> str:
    m, s = divmod(int(segundos), 60)
    return f"{m:02d}m:{s:02d}s"
