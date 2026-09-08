# Native/mobile OAuth

Use authorization code with PKCE S256 through the system browser or platform authentication session. Native applications are public clients: an embedded client secret is not confidential. Avoid collecting provider credentials in an embedded webview.

Register the platform-appropriate redirect: claimed HTTPS/universal/app links when supported, a registered custom scheme where appropriate, or a loopback redirect for supported desktop clients. Validate the callback and bind state to the initiating flow. The native-app loopback exception is different from a general permission to use HTTP remotely.

Store refresh/access credentials with Keychain, Keystore or an appropriate platform wrapper; consider backup, device migration and logout behavior. Do not log codes/tokens. Handle cancellation, duplicate callbacks, expired state, app suspension and a revoked refresh token.

Source: [RFC 8252](https://www.rfc-editor.org/rfc/rfc8252.html). Follow the selected provider's platform SDK and redirect requirements.
