def count_by_extension(paths: list[str]) -> dict[str, int]:
    counts = {}
    for path in paths:
        filename = path.split('/')[-1]
        
        if '.' in filename:
            ext = filename.split('.')[-1].lower()
        else:
            ext = ""
            
        counts[ext] = counts.get(ext, 0) + 1
    return counts

def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    return sorted(paths, key=lambda p: (-p.count('/'), p))[0]

def human_size(n_bytes: int) -> str:
    if n_bytes < 1024:
        return f"{n_bytes} B"
    
    units = ["KB", "MB", "GB", "TB"]
    size = n_bytes
    
    for unit in units:
        size /= 1024.0
        if size < 1024 or unit == "TB":
            return f"{size:.1f} {unit}"
