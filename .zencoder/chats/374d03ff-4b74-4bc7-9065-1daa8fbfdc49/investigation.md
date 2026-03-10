# Bug Investigation

## Bug Summary
Multiple issues identified in the backend authentication logic:
1. `RegisterSerializer` is not imported in `views.py`.
2. `RegisterSerilizer` (typo) is defined in `serializers.py`.
3. `basic_login` in `views.py` attempts to fetch user with raw password, which fails because Django hashes passwords.
4. `RegisterSerilizer` does not hash passwords upon user creation.

## Root Cause Analysis
- **Missing Import**: Developer forgot to import the serializer in `views.py`.
- **Typo**: Misspelling in `serializers.py`.
- **Incorrect Authentication**: Using `User.objects.get` with a raw password is not the standard or secure way to authenticate users in Django.
- **Insecure Registration**: Standard `ModelSerializer` on the `User` model doesn't automatically hash the `password` field unless explicitly handled.

## Affected Components
- `backend/backend/views.py`
- `backend/backend/serializers.py`

## Proposed Solution
1. Fix typo in `backend/backend/serializers.py` (rename `RegisterSerilizer` to `RegisterSerializer`).
2. Override `create` method in `RegisterSerializer` to use `User.objects.create_user` (which handles hashing).
3. Import `RegisterSerializer` in `backend/backend/views.py`.
4. Update `basic_login` to use Django's `authenticate` function.

## Implementation Notes
- Fixed typo in `serializers.py` and implemented `create` method using `create_user`.
- Imported `authenticate` and `RegisterSerializer` in `views.py`.
- Refactored `basic_login` to use `authenticate(username=username, password=password)`.

