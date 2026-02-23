# Bugs Found

## Bug 1: Schema Validation - Incorrect Type for `name` field
- **File:** `schemas.py`
- **Issue:** The `name` property was defined as `"type": "integer"` but the API returns a string value (e.g., `"ranger"`).
- **Fix:** Changed `"type": "integer"` to `"type": "string"`.
- **Impact:** `test_pet_schema` was failing with `ValidationError: 'ranger' is not of type 'integer'`.

## Bug 2: Missing f-string in `findByStatus` error message
- **File:** `app.py`, line ~89
- **Issue:** The error message uses `'Invalid pet status {status}'` without the `f` prefix, so the literal text `{status}` is displayed instead of the actual status value.
- **Expected:** `f'Invalid pet status {status}'`
- **Impact:** Users see an unhelpful error message when passing an invalid status.