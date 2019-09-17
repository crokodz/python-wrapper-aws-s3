# pyqalx

A python wrapper for qalx

## Installation



### Requirements
python3
requests


## Usage

```python
import pyqalxapi

api = pyqalxapi.API('<your token>')

# ITEM
# get all items
response = api.get('item')
print(response)

#get item by id
response = api.get('item/<item id>')
print(response)

#get item with params
response = api.get('item', params={'limit':2, 'skip':1, 'sort':'id'})
print(response)

#save item using data
response = api.post('item', data={'test':'test value'})
print(response)

#upload file
response = api.post('item', file='../pyqalx/requirements.txt', upload=True)
print(response)

#upload file and data
response = api.post('item', data={'test':'test value'}, file='../pyqalx/requirements.txt', upload=True)
print(response)

# SET
# get sets
response = api.get('set')
print(response)

# get set by id
response = api.get('set/<set_id>')
print(response)

# get set with params
response = api.get('set', params={'limit':2, 'skip':1, 'sort':'id'})
print(response)


# save set
response = api.post('set', item_guids=['<item id 1>', '<item id 2>'])
print(response)


# GROUP
# get groups
response = api.get('group')
print(response)

# get groups by id
response = api.get('group/<group id>')
print(response)

# get groups with params
response = api.get('group', params={'limit':2, 'skip':1, 'sort':'id'})
print(response)

# save groups
response = api.post('group', set_guids=['<set id 2>', '<set id 2>'])
print(response)


# patch queues
response = api.patch('queue/494b775f-7c95-437b-9989-1c9b730ea67e', parameters={'a':'b'})
print(response)

# delete bot
response = api.delete('bot/494b775f-7c95-437b-9989-1c9b730ea67e')
print(response)
```