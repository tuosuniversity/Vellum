import json

with open('transcript_raw.json') as f:
    data = json.load(f)

segments = []
for result in data['response']['results']:
    if 'alternatives' in result and result['alternatives']:
        transcript = result['alternatives'][0].get('transcript', '').strip()
        if transcript:
            segments.append(transcript)

# Join segments with double line breaks
clean_text = "\n\n".join(segments)

with open('clean_transcript_blocks.md', 'w') as out:
    out.write(clean_text)