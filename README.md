# pricing-lib

Library that computes prices, discounts and taxes. Other services depend on it.

## Releases

A release is a semver tag (`v1.4.0`) with a GitHub Release. Release candidates are tagged
`v1.4.0-rc.1` and published as prereleases. Urgent fixes are made on a `hotfix/1.4.1` branch
cut from the release tag, tagged `v1.4.1`, and merged back into `main`.

Publishing a GitHub Release runs `.github/workflows/release.yml`, which publishes the package.
