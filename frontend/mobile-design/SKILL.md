---
name: mobile-design
description: "Design or refine native, React Native, or Flutter mobile interactions for iOS and Android."

---

# Design for the actual mobile context

Infer platform, framework, navigation and design system from the project. Ask only when a missing platform or product decision changes the work. Read the relevant reference, not the whole collection.

| Task | Reference |
|---|---|
| Product interaction decisions | [design thinking](mobile-design-thinking.md), [decision trees](decision-trees.md) |
| Touch, gestures and navigation | [touch](touch-psychology.md), [navigation](mobile-navigation.md) |
| Platform conventions | [iOS](platform-ios.md), [Android](platform-android.md) |
| Visual readability | [typography](mobile-typography.md), [color](mobile-color-system.md) |
| Runtime responsiveness | [performance](mobile-performance.md), [debugging](mobile-debugging.md) |
| Connectivity and data | [backend integration](mobile-backend.md) |
| Validation | [testing](mobile-testing.md) |

Design reachable actions, appropriate touch targets, visible feedback and accessible labels. Account for safe areas, text scaling, keyboard, platform back behavior and interruption where relevant. Offline behavior, biometric authentication and certificate pinning depend on the product and threat model; they are not defaults for every app.

Use the platform's supported animation and list mechanisms, then measure on representative devices. Preserve established architecture and interaction conventions. Verify the changed flow and its significant failure states; [mobile_audit.py](scripts/mobile_audit.py) is a heuristic aid, not proof of usability or compliance.
