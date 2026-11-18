# Timestamps

[OpenTimestamps](https://opentimestamps.org) proofs for the assets of release `v1`.
Each proof commits to the SHA-256 of the file below and is anchored in Bitcoin block
976350 (2026-11-18 00:29:10 UTC).

| file | SHA-256 |
|---|---|
| `exponential-integrals-bessel-kummer-relations-v1.pdf` | `e634c787bae4d6a6a42bb84cf84e32fcde480574560f6479a777a8961e2451ac` |
| `exponential-integrals-bessel-kummer-relations-v1.tar.gz` | `1f8335f3f9e389543b0c2c2d8d7dfbf665e0e85ab9279ff15ed69a1404f26765` |

To verify, download the release asset into this directory and run

    pip install opentimestamps-client
    ots verify timestamps/<file>.ots
