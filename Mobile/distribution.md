# Distribution Methods

## InHouse
- distributes mobile apps builds (debug/release/prod) directly to devices within an organization, typically for internal use/test by employees or specific team
- uses an **Apple Developer Enterprise Program account** ($299/year)
- these builds are signed with an **InHouse provisioning profile**, and can be installed on devices **registered under the enterprise account**.
- the builds are hosted on platforms like Firebase, AppCenter

## AdHoc
- distributes mobile apps to a limited set of devices, typically used for external testing (e.g., beta testing with clients, external shareholders, etc.) or internal testing before a public release
- uses a **Standard Apple Developer Program account** ($99/year), limited to 100 registered devices
- the builds can be hosted on platforms like FireBase AppCenter, TestFlight

### TestFlight
- might not require you to manually register your devices's UUID. When you accept the invitation, TestFlight will automatically register your device's UUID in the Apple Developer Portal
- internal testers: up to 25
- external testers: up to 10000 (invitation via email, or public link)
- each build expires after 90 days
