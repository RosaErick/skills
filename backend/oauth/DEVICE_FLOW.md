# Device authorization flow

Use the provider's device authorization grant for input-constrained devices. Request device/user codes and display the provider's verification URI and user code accurately. Keep the device code private and do not invent a different verification destination.

Poll the token endpoint with the device grant, device code and client identification. Honor the returned interval and expiration. On `authorization_pending`, wait for the next permitted poll; on `slow_down`, increase the polling interval as specified. Stop on `access_denied`, expiry or user cancellation. A transport timeout is not a grant of access.

Store resulting tokens using the platform's appropriate protected storage and follow the provider's refresh/revocation contract. Test pending, slow-down, cancellation, denial and successful completion using a local simulation; do not hammer a real provider for a test loop.

Source: [RFC 8628](https://www.rfc-editor.org/rfc/rfc8628.html).
