# API Test Cases

| ID | Scenario | Method | Expected |
|---|---|---|---|
| API-001 | Retrieve an existing post | GET | 200 and valid JSON object |
| API-002 | Retrieve a non-existing post | GET | 404 response |
| API-003 | Create a post with valid data | POST | Successful response containing submitted fields |
| API-004 | Create a post with missing title | POST | Behavior documented and response validated |
| API-005 | Update an existing post | PUT | Successful response containing updated data |
| API-006 | Delete an existing post | DELETE | Successful deletion response |
| API-007 | Validate response content type | GET/POST | JSON response is returned |
| API-008 | Validate response schema | GET | Expected fields are present |

Execution results should be recorded after running the collection in Postman.