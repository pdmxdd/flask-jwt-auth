# Flask Authorization via JWT
This is a skeleton project that should get prototypes up and running very quickly. It's simply a ReSTful API with User Authorization via encrypted JSON web Toekns (JWT).

Restricted routes must be accessed by providing an encrypted JWT string as a header marked 'Authorization'.

JWTs are issued on successful user registration, and on successful user authentication.

The JWT needs to be captured by the front end, stored, and then sent back when requesting restricted content.

## Routes
### User
- /user/register --> POST; JSON Required: "email", "password", "confirm_password"
- /user/login --> POST; JSON Required: "email", "password"
- /user/account --> GET; JWT Required
- /user/account --> POST; JWT Required; JSON Required: "password", "confirm_password"

### Database
- /database/reset

## Route Decorators
- @json_required
- @jwt_required
