def rotation_arrows(arrows):
    num_arrows = set()
    for arrow in arrows:
        num_arrows.add(arrows.count(arrow))
    return len(arrows) - max(num_arrows)
