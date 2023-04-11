class hash_map:
    def __init__(self, hash_func=hash, max_load_factor=2.0):
        self.hash_func = hash_func
        self.max_load_factor = max_load_factor
        self.num_elements = 0
        self.num_buckets = 8
        self.buckets = [[] for _ in range(self.num_buckets)]

    def __len__(self):
        return self.num_elements

    def __contains__(self, key):
        bucket = self.buckets[self.hash_func(key) % self.num_buckets]
        return any(k == key for k, v in bucket)

    def __getitem__(self, key):
        bucket = self.buckets[self.hash_func(key) % self.num_buckets]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(key)

    def __setitem__(self, key, value):
        bucket = self.buckets[self.hash_func(key) % self.num_buckets]
        for i, kv in enumerate(bucket):
            if kv[0] == key:
                bucket[i] = (key, value)
                break
        else:
            bucket.append((key, value))
            self.num_elements += 1
            if self.num_elements > self.max_load_factor * self.num_buckets:
                self._resize()

    def __delitem__(self, key):
        bucket = self.buckets[self.hash_func(key) % self.num_buckets]
        for i, kv in enumerate(bucket):
            if kv[0] == key:
                del bucket[i]
                self.num_elements -= 1
                return
        raise KeyError(key)

    def _resize(self):
        self.num_buckets *= 2
        new_buckets = [[] for _ in range(self.num_buckets)]
        for bucket in self.buckets:
            for k, v in bucket:
                new_buckets[self.hash_func(k) % self.num_buckets].append((k, v))
        self.buckets = new_buckets

    def clear(self):
        self.buckets = [[] for _ in range(self.num_buckets)]
        self.num_elements = 0

    def load_factor(self):
        return self.num_elements / self.num_buckets

    def rehash(self):
        new_buckets = [[] for _ in range(self.num_buckets)]
        for bucket in self.buckets:
            for k, v in bucket:
                new_buckets[self.hash_func(k) % self.num_buckets].append((k, v))
        self.buckets = new_buckets

    def keys(self):
        return [k for bucket in self.buckets for k, v in bucket]

    def values(self):
        return [v for bucket in self.buckets for k, v in bucket]

    def items(self):
        return [(k, v) for bucket in self.buckets for k, v in bucket]