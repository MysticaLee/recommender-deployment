# LeetNode: An Adaptive Learning Software

Main project: [LeetNode](https://github.com/zhermin/LeetNode)

## Recommender Microservice

This Recommender Microservice consists of:

- Machine Learning: [pyBKT](https://github.com/CAHLR/pyBKT)

- REST API: FastAPI

- Deployment: Heroku

- Storage: Firebase Storage

- Cache: Redis

- Authorisation: OAuth2.0

- Authorisation Database: Postgres

## Setup

To get all dependencies:

```bash
pip install -r requirements.txt
```

## API Documentation

This API is available at: `http://126.0.0.1:8000/`

### 1. Add students for a SINGLE topic

Adds students with given names for a topic.

#### 1.1 URL

`/add-student/:student_id/:topic`

#### 1.2 METHOD

`POST`

#### 1.3 URL Params

```python
student_id: str # Multiple students separated by commas
topic: str # 1 topic ONLY
```

#### 1.4 Data Params

`None`

#### 1.5 Success Response

Code: `200 OK`

Content:

```json
{
  "Created": true
}
```

#### 1.6 Error Response

Code: `422 UNPROCESSABLE ENTITY`

Content:

```json
{
  "detail": "Invalid topic name"
}
```

OR

Code: `422 UNPROCESSABLE ENTITY`

Content:

```json
{
  "detail": "Data already exists"
}
```

### 2. Remove students for a SINGLE topic

Removes students with given names for a topic.

#### 2.1 URL

`/remove-student/:student_id/:topic`

#### 2.2 METHOD

`DELETE`

#### 2.3 URL Params

```python
student_id: str # Multiple students separated by commas
topic: str # 1 topic ONLY
```

#### 2.4 Data Params

`None`

#### 2.5 Success Response

Code: `200 OK`

Content:

```json
{
  "Deleted": true
}
```

#### 2.6 Error Response

Code: `422 UNPROCESSABLE ENTITY`

Content:

```json
{
  "detail": "Invalid topic name"
}
```

OR

Code: `422 UNPROCESSABLE ENTITY`

Content:

```json
{
  "detail": "Student ID ['A01', 'A02'] does NOT exists"
}
```

### 3. Remove students for ALL topics (IRREVERISBLE)

Removes student for ALL topicss.

#### 3.1 URL

`/remove-all/:student_id`

#### 3.2 METHOD

`DELETE`

#### 3.3 URL Params

```python
student_id: str # 1 student ONLY

```

#### 3.4 Data Params

`None`

#### 3.5 Success Response

Code: `200 OK`

Content:

```json
{
  "Deleted": true
}
```

#### 3.6 Error Response

`None`

### 4. Get mastery for a SINGLE topic

Fetches mastery probability for a particular student for a topic. If student does not exist, add student then fetch mastery probability.

#### 4.1 URL

`/get-mastery/:student_id/:topic`

#### 4.2 METHOD

`GET`

#### 4.3 URL Params

```python
student_id: str # 1 student ONLY
topic: str # 1 topic ONLY
```

#### 4.4 Data Params

`None`

#### 4.5 Success Response

Code: `200 OK`

Content:

```json
{
  "Mastery": 0.7930704584200629
}
```

#### 4.6 Error Response

Code: `422 UNPROCESSABLE ENTITY`

Content:

```json
{
  "detail": "Invalid topic name"
}
```

### 5. Get mastery for ALL topics

Fetches mastery probability for a particular student for ALL topic. If student does not exist for a particular topic, add student then fetch mastery probability.

#### 5.1 URL

`/get-all/:student_id`

#### 5.2 METHOD

`GET`

#### 5.3 URL Params

```python
student_id: str # 1 student ONLY
```

#### 5.4 Data Params

`None`

#### 5.5 Success Response

Code: `200 OK`

Content:

```json
{
  "Mastery": {
    "dc-motors-power-calculation": 0.992251117023947,
    "inverting-non-inverting-amplifiers-gains": 0,
    "kcl": 0.9999996519885773,
    "current-division-principle": 0.25,
    "rc-steady-state-analysis": 0.2,
    "thevenin-equivalent-circuit": 0.36175,
    "energy-stored-in-capacitors": 0.25,
    "first-order-high-pass-filters": 0.25,
    "pmdc-motors-circuit-model": 0.25,
    "node-voltage-analysis-technique": 0.44625,
    "power": 0.3825,
    "rl-steady-state-analysis": 0.345,
    "equivalent-resistance-in-series-or-parallel": 0.973694291928073,
    "first-order-low-pass-filters": 0.25,
    "ohms-law": 0.4,
    "energy-stored-in-inductors": 0.25,
    "rl-transient-analysis": 0.3225,
    "opamp-golden-rules": 0.25,
    "opamp-circuit-analysis": 0.25,
    "kvl": 0.25,
    "voltage-division-principle": 0.9615649974611777,
    "rlc-circuit-analysis": 0.25,
    "equivalent-inductance": 0.25,
    "equivalent-capacitance": 0.25,
    "torque-equation": 0.25,
    "rc-transient-analysis": 0.28875
  }
}
```

#### 5.6 Error Response

`None`

### 6. Update state for a SINGLE topic

Updates state of a particular student for a topic given one response. If student does not exist, add student then update state.

#### 6.1 URL

`/update-state/:student_id/:topic/:correct`

#### 6.2 METHOD

`PATCH`

#### 6.3 URL Params

```python
student_id: str # 1 student ONLY
topic: str # 1 topic ONLY
corrrect: str # Binary string (e.g. 1101)
```

#### 6.4 Data Params

`None`

#### 6.5 Success Response

Code: `200 OK`

Content:

```json
{
  "Updated": true
}
```

#### 6.6 Error Response

Code: `422 UNPROCESSABLE ENTITY`

Content:

```json
{
  "detail": "Invalid topic name"
}
```

OR

Code: `422 UNPROCESSABLE ENTITY`

Content:

```json
{
  "detail": "Missing / Incorrect argument. Please ensure that the last agrument is a binary string."
}
```

### 7. Update state for MULTIPLE topics

Updates state of a particular student for multiple topics with corresponding responses. If student does not exist for a particular topic, add student then update state.

#### 7.1 URL

`/update-multiple/:student_id`

#### 7.2 METHOD

`PATCH`

#### 7.3 URL Params

```python
student_id: str # 1 student ONLY
```

#### 7.4 Data Params

```json
{
  "student_id": "A01",
  "topics": {
    "dc-motors-power-calculation": "1",
    "kcl": "1111",
    "voltage-division-principle": "1",
    "equivalent-resistance-in-series-or-parallel": "1"
  }
}
```

#### 7.5 Success Response

Code: `200 OK`

Content:

```json
{
  "Updated": true
}
```

#### 7.6 Error Response

Code: `422 UNPROCESSABLE ENTITY`

Content:

```json
{
  "detail": "Invalid topic name"
}
```

OR

Code: `422 UNPROCESSABLE ENTITY`

Content:

```json
{
  "detail": "Missing / Incorrect argument. Please ensure that the last agrument is a binary string."
}
```

### 8. Reset roster (IRREVERSIBLE)

Initialise empty Roster. Removes all students.

#### 8.1 URL

`/reset-roster`

#### 8.2 METHOD

`POST`

#### 8.3 URL Params

`None`

#### 8.4 Data Params

`None`

#### 8.5 Success Response

Code: `200 OK`

Content:

```json
null
```

#### 8.6 Error Response

`None`

### 9. Save roster (Manually)

Saves the Roster model to storage. Uses Python pickles.

#### 9.1 URL

`/save-roster`

#### 9.2 METHOD

`POST`

#### 9.3 URL Params

`None`

#### 9.4 Data Params

`None`

#### 9.5 Success Response

Code: `200 OK`

Content:

```json
null
```

#### 9.6 Error Response

`None`

## For more information

Refer to [LeetNode - Recommender Microservice](https://github.com/zhermin/LeetNode/tree/main/recommender)
