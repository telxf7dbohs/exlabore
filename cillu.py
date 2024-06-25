def generate_musicbrainz_disc_id(toc_entries):
    total_frames = 0
    track_offsets = []

    for entry in toc_entries:
        total_frames += entry.frames
        track_offsets.append(entry.offset)

    disc_id = total_frames % 0xFF
    for offset in track_offsets:
        disc_id = (disc_id << 8) | (offset >> 8)

    return (disc_id,)

# Example usage
toc_entries = [(100, 0, 12345), (150, 124, 23456), (200, 275, 34567)]
musicbrainz_disc_id = generate_musicbrainz_disc_id(toc_entries)
print(musicbrainz_disc_id)
