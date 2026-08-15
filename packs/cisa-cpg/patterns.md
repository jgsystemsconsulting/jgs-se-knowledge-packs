# Patterns — CISA CPG 2.0

## 1. First-Mile Control Bundle
- **When:** Standing up CPGs in a resource-constrained org.
- **How:** Prioritize MFA (3.F), default-password removal (3.A), backups/restore (3.O), logging (3.Q), segmentation of critical zones (3.I), and IR plan maintenance (1.C).
- **Trade-offs:** Leaves advanced detection for later vs fastest common-threat risk cut.

## 2. 1.x → 2.0 Remap Workshop
- **When:** Existing trackers still use CPG 1.x IDs.
- **How:** Map old IDs through 2.0 consolidations/renumbering; retire OT-only duplicates; re-baseline scores.
- **Trade-offs:** Short compliance dip while remapping vs permanent false coverage.

## 3. Goal Owner + Evidence Card
- **When:** Goals are “green” with no proof.
- **How:** For each goal: owner, systems in scope, evidence artifact, review date.
- **Trade-offs:** Admin overhead vs audit-ready honesty.

## 4. MSP Trust Boundary Pack
- **When:** Providers hold admin paths into IT/OT.
- **How:** Contract for incident/vuln notice (1.D), oversight metrics (1.E), MFA on provider access, logging of privileged sessions.
- **Trade-offs:** Vendor friction vs reduced third-party blast radius.

## 5. OT-Safe Identity Rollout
- **When:** Shared/default OT credentials still exist.
- **How:** Inventory engineering accounts; stage unique creds + break-glass; avoid unsafe lockouts; segment first if auth changes are risky.
- **Trade-offs:** Longer rollout vs process-safety incidents from abrupt auth changes.

## 6. Edge Exposure Burn-Down
- **When:** Internet-facing services and remote access are poorly inventoried.
- **How:** Discover exposures; harden or remove (3.S); enforce approved remote paths; monitor logins (3.E).
- **Trade-offs:** Temporary access inconvenience vs ransomware initial access reduction.

## 7. Backup Restore Drill Tied to 6.A
- **When:** Backups exist on paper.
- **How:** Quarterly restore tests with timed recovery plan execution; fix immutability/offline gaps.
- **Trade-offs:** Ops time vs discovering unusable backups during an incident.

## 8. Board Narrative from Outcomes
- **When:** Leadership needs investment justification.
- **How:** Present CPG outcomes as risk-reduction milestones with cost-to-close and residual risk.
- **Trade-offs:** Simplification vs loss of technical nuance — keep appendix detail for practitioners.

## 9. Logging Minimum Viable Set
- **When:** Full enterprise telemetry is impossible (especially OT).
- **How:** Prioritize identity providers, VPN/remote access, firewalls, jump hosts, critical servers; define retention for investigations (3.Q).
- **Trade-offs:** Incomplete forensics vs achievable baseline.

## 10. Sector Floor then SSG Ceiling
- **When:** Sector publishes additional goals.
- **How:** Achieve cross-sector CPGs first; layer SSGs where sector risk demands.
- **Trade-offs:** Extra scope vs sector regulator/partner expectations.
