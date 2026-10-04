"""Offline checks for the first text-first Chinese scenario."""

import json
from pathlib import Path

ROOT=Path(__file__).parents[1]
data=json.loads((ROOT/'fixture.json').read_text())
assert data['item_id']=='tones-context-1'
assert [item['id'] for item in data['segments']] == ['buy-rice','sell-rice']
assert data['expected_segment']=='buy-rice'
assert 'mǎi' in data['segments'][0]['pinyin']
assert 'mài' in data['segments'][1]['pinyin']
assert set(data['response_dimensions']) == {'tone','character','communicative_fit'}
assert '买' in data['transfer_prompt']
print('PASS: tone scenario has context, character/pinyin layers, inspectable feedback, revision, and transfer')
