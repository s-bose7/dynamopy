
- #### REST API to store arbitrary key-value pairs, which can contain any type of data, such as text, numbers, counters, and binary data.

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"key": 12, "value": "Ab735TXZ65ghuUYk"}' \
  https://api.heisenbergdb.v1/store
```
- #### REST API to get values by their keys

```bash
curl -X GET \
  https://api.heisenbergdb.v1/get/example_key
```