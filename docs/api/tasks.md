# Tasks
Supports CRUD operations with tasks from Todo list.

## Create a new task

**Request**:

`POST` `/tasks/`

Parameters:

Name       | Type   | Required | Description
-----------|--------|----------|------------
title      | string | Yes      | The title of the new task.
text       | string | No       | The body of the new task.
due_date   | string | No       | The tasks's expiration date.

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
201 Created

{
  "id": 3,
  "title": "Do nothing",
  "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit ...",
  "due_date": "2015-12-11T10:12:14+0000"
}
```


## Get all tasks from ToDo list

**Request**:

`GET` `/tasks/`

Parameters:

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 3,
      "title": "Do nothing",
      "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit ...",
      "due_date": "2019-12-11T10:12:14+0000"
    },
    {
      "id": 2,
      "title": "Do something",
      "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit ...",
      "due_date": "2017-10-11T10:12:14+0000"
    }
  ]
}

```


## Get a task details

**Request**:

`GET` `/tasks/:id`

Parameters:

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "id": 3,
  "title": "Do nothing",
  "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit ...",
  "due_date": "2015-12-11T10:12:14+0000"
}
```


## Update your task

**Request**:

`PUT/PATCH` `/tasks/:id`

Parameters:

Name       | Type   | Required | Description
-----------|--------|----------|------------
title      | string | Yes      | The title of the task.
text       | string | No       | The body of the task.
due_date   | string | No       | The tasks's expiration date.



*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "id": 3,
  "title": "Do nothing",
  "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit ...",
  "due_date": "2015-12-11T10:12:14+0000"
}
```

## Delete your task

**Request**:

`DELETE` `/tasks/:id`

Parameters:

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
204 No Content
```
