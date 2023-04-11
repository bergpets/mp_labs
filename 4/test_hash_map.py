from hash_map import hash_map
hm = hash_map()
hm['key1'] = 'value1'
hm['key2'] = 'value2'
hm['key3'] = 'value3'

assert len(hm) == 3
assert hm['key1'] == 'value1'
assert hm['key2'] == 'value2'
assert hm['key3'] == 'value3'
assert 'key4' not in hm

hm['key2'] = 'new_value2'
assert hm['key2'] == 'new_value2'

del hm['key3']
assert len(hm) == 2
assert 'key3' not in hm

hm.clear()
assert len(hm) == 0

hm['key1'] = 'value1'
hm['key2'] = 'value2'
hm['key3'] = 'value3'
hm['key4'] = 'value4'
hm['key5'] = 'value5'
hm['key6'] = 'value6'
hm['key7'] = 'value7'
hm['key8'] = 'value8'
hm['key9'] = 'value9'
hm['key10'] = 'value10'
hm['key11'] = 'value11'
hm['key12'] = 'value12'
hm['key13'] = 'value13'
hm['key14'] = 'value14'
hm['key15'] = 'value15'
hm['key16'] = 'value16'
hm['key17'] = 'value17'
hm['key18'] = 'value18'
hm['key19'] = 'value19'
hm['key20'] = 'value20'

hm.rehash()
assert hm.load_factor() == 1.25