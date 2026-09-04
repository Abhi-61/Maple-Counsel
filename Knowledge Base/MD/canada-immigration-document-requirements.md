---
title: Canada Immigration Programs — Required Documents Master Reference
document_type: master_reference
compiled_date: 2026-08-24
primary_sources: IRCC (canada.ca), Gouvernement du Québec / MIFI (quebec.ca), Immigration and Refugee Board (irb-cisr.gc.ca)
scope: Federal economic, family, business, refugee/protected persons, temporary resident, regional pilot, humanitarian, and citizenship programs
excludes: Stream-by-stream Provincial Nominee Program document lists (60+ streams across 11 jurisdictions); Quebec business/investor streams; minor-specific citizenship variants
volatility_warning: Several programs covered here changed status (opened, paused, or closed) within the last 12 months. Status flags and form numbers must be re-verified against live IRCC/MIFI pages before this is treated as ground truth in a production retrieval system.
---

# Canada Immigration Programs — Required Documents Master Reference

This document maps required and commonly-requested supporting documents to each major Canadian immigration program, compiled from IRCC/canada.ca, Government of Québec, and IRB primary sources as of **August 2026**.

**Scope decision:** The Provincial Nominee Program is treated as one category rather than 60+ individual streams. Each PNP stream (e.g., Alberta Opportunity Stream, Ontario Human Capital Priorities) has its own provincial-stage document requirements that this document does not enumerate — see the note in Section 2. The same logic applies to Quebec business/investor programs.

**Read this before ingesting:** 2025–2026 saw an unusually high number of program status changes — closures, pauses, and reopenings — driven by IRCC's reduced immigration levels plan. A "Status" field is included for every program precisely because "what documents are required" is meaningless for a program that isn't currently accepting applications. Section 12 (Maintenance Notes) has a suggested recheck cadence per category.

---

## Program Status at a Glance (August 2026)

| Program | Status |
|---|---|
| Express Entry (FSWP / FSTP / CEC) | Open |
| Provincial Nominee Program (PNP) | Open (varies by province/stream) |
| Quebec PSTQ (skilled workers) | Open, via Arrima |
| Quebec PEQ | **Temporarily reopened** July 2 – Oct 31, 2026 (pre-Nov 19, 2025 eligibility only) |
| Spousal / Common-law / Conjugal Sponsorship | Open |
| Parents and Grandparents Program (PGP) | Open, invitation-only |
| Start-up Visa Program | **Closed** to new applicants (Dec 31, 2025) |
| Self-Employed Persons Program | **Intake paused**, indefinite |
| Home Care Worker Immigration Pilots (caregivers) | **Intake paused** (Dec 19, 2025) |
| In-Canada Asylum Claims | Open |
| GAR / PSR / BVOR Refugee Resettlement | Open |
| Study Permit | Open |
| Work Permits (LMIA and LMIA-exempt) | Open |
| Visitor Visa (TRV) / Super Visa | Open |
| Atlantic Immigration Program (AIP) | Open |
| Rural Community Immigration Pilot (RCIP) | Open |
| Francophone Community Immigration Pilot (FCIP) | Open |
| Agri-Food Immigration Pilot | **Closed** to new applicants (cap reached, 2025) |
| Economic Mobility Pathways Pilot (EMPP) | **Concluded** (end of 2025) |
| Humanitarian & Compassionate (H&C) / TRP | Open |
| Citizenship (Grant / Proof) | Open |

---

## 1. Cross-Program Requirements

These recur across nearly every program below and are referenced by shorthand rather than repeated in full each time.

**Identity & travel documents**
- Valid *regular* passport (diplomatic, official, service, and public affairs passports are not accepted for immigration purposes)
- All passport/travel document pages showing personal data, stamps, and visas, for the applicant and every accompanying family member

**Photos**
- Digital photos meeting IRCC's photograph specifications (uniform lighting, plain white background, taken within the last 6 months); requirements differ slightly for citizenship vs. immigration photos

**Biometrics**
- Fingerprints and a photo at a Visa Application Centre (VAC) or Service Canada location; valid for 10 years; required for most permanent and temporary resident applications, with some exemptions by age and citizenship

**Police certificates**
- General rule: a certificate from every country/jurisdiction where the applicant (18+) lived for 6+ consecutive months
- **Timing varies by program** — several economic/family streams require certificates upfront; PGP explicitly tells applicants *not* to submit them until IRCC requests them later in processing

**Medical exams**
- Must be completed by an IRCC-designated panel physician (not a regular doctor); results go directly to IRCC; valid 12 months
- Timing also varies: most Express Entry/PNP applicants do this upfront post-ITA; PGP again defers this until requested

**Certified translations**
- Any document not in English or French requires a certified translation plus an affidavit, unless the translator is a member in good standing of a provincial/territorial translators' association

**Recurring forms**
- **IMM 5669** — Schedule A: Background/Declaration (near-universal on PR applications)
- **IMM 5406** — Additional Family Information
- **IMM 5476 / IMM 5475** — Use of a Representative / Authority to Release Personal Information (only if a rep is used)
- **IMM 5409** — Statutory Declaration of Common-law Union (if applicable)
- **IMM 0008** — Generic Application Form for Canada (backbone of most non-Express-Entry PR applications)

---

## 2. Provincial Nominee Program (PNP)

**Status:** Open — varies by province/stream (60+ streams across 11 jurisdictions)
**Jurisdictions with a PNP:** Alberta, British Columbia, Manitoba, New Brunswick, Newfoundland and Labrador, Nova Scotia, Ontario, Prince Edward Island, Saskatchewan, Northwest Territories, Yukon. *(Quebec and Nunavut do not operate a PNP.)*

**Federal-stage documents (common to nearly all PNP streams, submitted to IRCC after nomination):**
- **IMM 0199** — Document Checklist: Provincial Nominee Class (non-Express Entry route) or **IMM 5690** (Express Entry-aligned PNP route)
- Confirmation/certificate of nomination from the nominating province or territory
- **Schedule 4** — Economic Classes: Provincial Nominees (and **Schedule 4A** if nominated under a business/entrepreneur stream)
- Standard identity, language test, education (+ ECA if applicable), proof of funds (stream-dependent — many PNP streams waive this with a qualifying job offer), police certificates, medical exam, photos, biometrics (see Section 1)
- Language test is mandatory for NOC TEER 4/5-equivalent (formerly skill level C/D) nominees regardless of stream

**Provincial-stage documents (vary by province and stream — not enumerated here):**
Expression of interest / application forms, business plans, net worth statements, intent-to-reside declarations, job offer letters, and settlement funds proof are all province- and stream-specific. Given the volume (60+ streams), treating each PNP as its own ingestion source with its own refresh cadence is likely more maintainable than trying to represent all of them in this master document — flagging for your ingestion manifest.

---

## 3. Quebec-Selected Immigration

Quebec independently selects its own economic immigrants under the Canada–Québec Accord; selected candidates still complete a federal permanent residence application afterward.

### 3.1 Programme de sélection des travailleurs qualifiés (PSTQ)
**Status:** Open (replaced the PRTQ; reopened June 2025 after an 8-month suspension)

**Stage 1 — Provincial selection (Arrima / Mon projet Québec):**
- Declaration of Interest in the Arrima portal (education, work history, language scores, family info, intended region)
- Following an invitation: language test results (TEF/TCF for French, or IELTS/TOEFL iBT for English), work reference letters (last 10 years, on letterhead with duties/hours/dates), proof of funds, validated Quebec job offer and LMIA-exemption confirmation (if applicable)

**Stage 2 — Federal permanent residence:**
- Certificat de sélection du Québec (CSQ)
- **IMM 5690** (Quebec Skilled Worker section)
- **Schedule 5** — Economic Classes: Declaration of Intent to Reside in Quebec
- Standard identity, police certificate, medical exam, biometrics (Section 1)

### 3.2 Programme de l'expérience québécoise (PEQ)
**Status:** Closed Nov 19, 2025; **temporarily reopened July 2 – Oct 31, 2026**, restricted to candidates who met PEQ eligibility criteria *as they stood on Nov 19, 2025*. Two streams:
- **Graduates stream:** Quebec diploma (bachelor's, master's, doctorate, DEC technique, or DEP + ASP totaling 1,800+ hours) obtained on/before Nov 19, 2025; French oral NCLC 7
- **Temporary foreign workers stream:** 24+ months full-time TEER 0–3 work experience in Quebec within the last 36 months (as of Nov 19, 2025); French oral NCLC 7

Documents: proof of diploma/training hours or work experience letters, French test results, CSQ application through Mon projet Québec, then the same federal Stage 2 documents as PSTQ.

*A possible permanent restructuring of PEQ is under discussion; this window is explicitly temporary.*

---

## 4. Family Class Sponsorship

### 4.1 Spouse, Common-Law Partner, or Conjugal Partner
**Status:** Open

- **IMM 1344** — Application to Sponsor, Sponsorship Agreement and Undertaking
- **IMM 5532** — Relationship Information and Sponsorship Evaluation
- **IMM 5533** — Document Checklist (sponsored person) / **IMM 5287** — Document Checklist (sponsor)
- Proof of sponsor's status (Canadian passport or PR card/COPR)
- Proof of relationship: marriage/civil union certificate (spouse), or 12+ months' cohabitation evidence (common-law), or a written statement explaining inability to marry/cohabit (conjugal — the most heavily scrutinized category)
- Relationship evidence: photos over time, joint financial records, lease/utility bills, communication history
- Standard identity, police certificates, medical exam, photos, biometrics (Section 1)

### 4.2 Parents and Grandparents Program (PGP)
**Status:** Open, but **invitation-based only** — full applications are accepted solely from sponsors who received an Invitation to Apply from the interest-to-sponsor pool; unsolicited applications are returned.

- **IMM 5771** — Document Checklist for Parents and Grandparents
- **IMM 1344**, **IMM 5768** (Financial Evaluation for PGP Sponsorship), **IMM 5409** (if applicable)
- Sponsor's proof of income: Notice of Assessment for the 3 most recent tax years, meeting the Minimum Necessary Income (a higher threshold applies to Quebec sponsors)
- Proof of relationship (birth/adoption certificates)
- Co-signer documents, if a co-signer is used
- **Do not submit** police certificates or a medical exam upfront — IRCC requests these later in processing for this program specifically, unlike most other PR streams

### 4.3 Dependent Children
- Birth or adoption certificate establishing the relationship
- Custody documentation and proof children may legally leave with the applicant (if divorced/separated parents)
- Standard identity, police certificate (if 18+), medical exam, photos

---

## 5. Business Immigration (Federal)

### 5.1 Start-up Visa (SUV) Program
**Status: CLOSED to new applications effective Dec 31, 2025, 11:59 p.m.** Narrow exception: holders of a valid 2025 commitment certificate who had not yet applied may still submit, with a filing deadline of June 30, 2026. The optional SUV-specific work permit is no longer available to new applicants.

Documents (for those still eligible under the transition):
- Commitment Certificate + Letter of Support from a designated venture capital fund, angel investor group, or business incubator
- Language test results (CLB 5)
- Proof of settlement funds (scaled by family size) and proof of required investment funds
- Business plan, staffing plan, proof of exploratory research, business registration/establishment documents, Business Number (BN)
- Police certificate, medical exam, biometrics

### 5.2 Self-Employed Persons Program
**Status: Intake paused indefinitely** ("until further notice," per IRCC's entrepreneur measures notice)

Documents (relevant to the existing backlog being processed):
- Evidence of relevant self-employment experience (cultural activities, athletics, or farm management)
- Business/financial records demonstrating intention and ability to be self-employed in Canada
- Police certificate, medical exam, proof of funds

---

## 6. Caregivers

**Status: Intake paused.** The current Home Care Worker Immigration Pilots (HCWIP — Home Child Care Worker and Home Support Worker, launched Mar 31, 2025) paused intake as of Dec 19, 2025, and will not reopen in March 2026 as originally scheduled; IRCC continues processing applications already received. Predecessor programs (Home Child Care Provider Pilot / Home Support Worker Pilot, using **IMM 5981**/**IMM 5982**) are closed and superseded.

Documents relevant to applications already in the pipeline:
- Job offer (employer must not be a business/corporation)
- Proof of qualifying work experience or NOC-specific training
- Language test results (CLB 4)
- Education credential
- **IMM 5981** (Document Checklist) / **IMM 5982** (Schedule 19a — Education and Language Assessment) for the legacy pilots
- Standard identity, police certificate, medical exam, biometrics

---

## 7. Refugees & Protected Persons

### 7.1 In-Canada Asylum Claims
**Status:** Open (intake continues at ports of entry and inland IRCC offices, subject to Safe Third Country Agreement rules at the land border)

- **Basis of Claim (BOC) form** (Immigration and Refugee Board) — due within 15 calendar days of referral if made at a port of entry
- **IMM 0008** + **Schedule 12** (Additional Information – Refugee Claimants Inside Canada)
- **IMM 5669** — Schedule A: Background/Declaration
- Passport/travel/ID document, or a written explanation if unavailable
- **IMM 1017** — medical exam report (Panel Physician)
- Use of Representative form, if applicable
- Optional supporting evidence: country-condition documentation, proof of political/union/group membership, police or medical reports, business records, any evidence of persecution or ill-treatment

### 7.2 Government-Assisted Refugees (GAR)
**Status:** Open. Referral comes through UNHCR rather than a direct application by the refugee, so the applicant-side document burden is minimal; IRCC and IOM manage most processing. Identity documents are used where available; officers assess identity by other means (interviews, host-country records) where documentation doesn't exist, which is common for this population. Standard medical and security screening still applies.

### 7.3 Privately Sponsored Refugees (PSR) / Blended Visa Office-Referred (BVOR)
**Status:** Open

Sponsor-side forms:
- **IMM 5373** — Sponsorship Undertaking (Sponsorship Agreement Holders)
- **IMM 5440** — Settlement Plan
- **IMM 5492** — Sponsor Assessment
- Guide **5413** (SAH guide) / Guide **IMM 6000** (principal applicant guide)

Refugee-side forms/documents:
- **IMM 0008 / Schedule 2** — Refugees Outside Canada
- **IMM 5669** — Schedule A
- Refugee determination/claim documentation from the host country (narrative, decisions, appeals), with translation if applicable
- Photo, passport/travel documents where available

---

## 8. Temporary Residence

### 8.1 Study Permit
**Status:** Open

- **IMM 5483** — Document Checklist (paired with visa-office-specific instructions)
- **IMM 1294** — Application for a Study Permit
- Letter of Acceptance (LOA) from a Designated Learning Institution, including the DLI number
- **Provincial/Territorial Attestation Letter (PAL/TAL)** — mandatory for most college, undergraduate, postgraduate-certificate/diploma, and private-college-language-program applicants as of 2025–2026; master's and doctoral applicants are exempt
- Proof of funds covering tuition + living costs (a commonly-cited living-cost threshold is ~CAD $20,635 outside Quebec — this figure is updated periodically and should be verified against the current IRCC page)
- Passport, 2 photos, language test results (institution-dependent)
- Proof of ties to home country / statement of intent to leave after studies
- Medical exam and/or police certificate, where required by country of residence or program length
- Custodian declaration, for minors studying without a parent in Canada

**Note:** the Student Direct Stream (SDS) was permanently cancelled in late 2024 — all applicants now go through the regular processing stream, which has a heavier document bar than SDS did.

### 8.2 Work Permit — LMIA-based (Temporary Foreign Worker Program)
**Status:** Open

- **IMM 5488** — Document Checklist (application made outside Canada) or personalized **IMM 5556** (application from inside Canada, generated through the portal)
- **IMM 1295** — Application for a Work Permit
- Copy of the positive Labour Market Impact Assessment (LMIA) + job offer/contract from the employer
- Proof of education, work experience, language proficiency (as applicable)
- Proof of funds
- **IMM 5707** — Family Information
- Certificat d'acceptation du Québec (CAQ), if the position is in Quebec
- Police certificate and/or medical exam (occupation-dependent — e.g., healthcare, childcare)

### 8.3 Work Permit — LMIA-exempt (International Mobility Program)
**Status:** Open. Covers CUSMA/USMCA professionals, intra-company transfers, significant-benefit work, spousal open work permits, and Post-Graduation Work Permits (PGWP), among others.

- Employer-side **Offer of Employment** submission (**IMM 5802**) via the Employer Portal, generating an Offer of Employment number, plus the employer compliance fee
- Proof of eligibility for the specific exemption category (e.g., citizenship + qualifying occupation for CUSMA; qualifying corporate relationship for intra-company transfers)
- For PGWP specifically: official transcript or program-completion letter from the DLI, proof of continuous full-time study
- Passport, proof of current status (if applying from inside Canada), standard identity documents

### 8.4 Temporary Resident Visa (Visitor Visa / TRV)
**Status:** Open

- **IMM 5257** — Application for a Temporary Resident Visa
- **IMM 5484** — Document Checklist
- Passport, 2 photos
- Proof of funds for the visit
- Proof of ties to home country: employment letter confirming position/salary/approved leave dates, property, family ties, or business ownership documents
- Travel itinerary and/or letter of invitation (for family visits)
- If being hosted: the host's bank statements, employment letter, and invitation letter
- Certified translations, as needed

### 8.5 Super Visa (Parents/Grandparents Multi-Entry Visitor Visa)
**Status:** Open. In addition to the standard TRV documents above:

- Proof of relationship to the host (child/grandchild's birth or baptismal certificate, or another document naming the applicant as parent/grandparent)
- Proof of the host's status in Canada (Canadian citizenship or PR document)
- Host's financial documentation supporting the invitation
- Proof of private Canadian medical insurance valid for a minimum of 1 year from the date of entry — IRCC sets a minimum coverage amount (historically CAD $100,000) that should be verified against the current Super Visa page, since this figure is adjusted periodically
- Medical exam

---

## 9. Regional & Community Economic Pilots

### 9.1 Atlantic Immigration Program (AIP)
**Status:** Open (made permanent in 2022)

- Document checklist + **Economic Classes – Atlantic Immigration Program** form
- Offer of employment (from a designated employer) + confirmation of provincial endorsement
- Settlement plan
- Proof of education, language test results, proof of work experience (unless exempt), proof of funds (if required)
- Standard identity, civil-status certificates, police certificates

### 9.2 Rural Community Immigration Pilot (RCIP)
**Status:** Open (launched Jan 30, 2025, as the permanent successor to the Rural and Northern Immigration Pilot, which closed Aug 31, 2024; 14 participating communities)

- **IMM 0246** — Document Checklist – Rural Community Immigration Pilot
- **IMM 0247** — Offer of Employment to a Foreign National (RCIP)
- **IMM 0248** — Schedule 1 (RCIP)
- **IMM 0249** — Recommendation from the Designated Economic Development Organization (valid 6 months from issuance)
- Job offer must be full-time, non-seasonal, and indeterminate, from a community-designated employer (no LMIA involved)
- Standard identity, language, education, work experience, police certificate, medical exam

### 9.3 Francophone Community Immigration Pilot (FCIP)
**Status:** Open (launched the same day as RCIP; 6 designated Francophone communities across 4 provinces)

- Same structural documents as RCIP (community/EDO-designated job offer, full-time/non-seasonal/indeterminate, no LMIA)
- French language test results (NCLC 5 is a commonly cited minimum — confirm current threshold)
- Standard identity, education, work experience, police certificate, medical exam

### 9.4 Agri-Food Immigration Pilot
**Status: Closed to new applications** (intake cap reached in 2025); IRCC continues processing applications submitted before closure.

Documents relevant to the existing backlog:
- Job offer in an eligible sector (mushroom/greenhouse crop production, meat processing, or livestock raising), non-seasonal, full-time
- Proof of qualifying work experience gained through the Temporary Foreign Worker Program
- Language test, education credential, proof of funds (unless already legally working in Canada)
- Standard identity, police certificate, medical exam

### 9.5 Economic Mobility Pathways Pilot (EMPP)
**Status: Concluded at the end of 2025.** Included here for historical/reference completeness only — no new applications are being accepted.

---

## 10. Humanitarian & Discretionary Applications

### 10.1 Humanitarian and Compassionate (H&C) Applications
**Status:** Open

- **IMM 5283** — Document Checklist (applications made inside Canada) or **IMM 5280** (outside Canada)
- Completed application form, proof of identity
- A detailed written submission addressing the H&C grounds relied on: establishment in Canada, best interests of any child affected, and/or hardship if required to return
- Supporting evidence: employment records, language ability, community/religious involvement letters, medical/psychological reports, country-condition documentation, children's school and medical records, third-party letters of support
- Use of Representative form, if applicable

### 10.2 Temporary Resident Permit (TRP)
For otherwise inadmissible individuals with a compelling reason to enter or remain in Canada. Requires a written explanation of the inadmissibility, the compelling reason for entry/stay, and supporting evidence addressing risk (e.g., rehabilitation evidence for criminal inadmissibility). Handled case-by-case; there isn't a single standardized public checklist comparable to the PR-stream IMM forms above.

---

## 11. Citizenship

### 11.1 Grant of Citizenship — Adults (Subsection 5(1))
**Status:** Open

- **CIT 0002** — Application for Canadian Citizenship (Adults); must be a current-version form
- **CIT 0007** — Document Checklist
- Proof of permanent resident status: PR card (both sides) or Confirmation of Permanent Residence / Record of Landing
- Colour passport copies covering the full 5-year eligibility period
- Physical presence calculation printout (1,095 days within the last 5 years) — the calculation date must match the application date
- Proof of language ability (CLB 4+), required for applicants aged 18–54: approved test results (IELTS, CELPIP, TEF Canada, TCF Canada), a government-funded language program certificate (e.g., LINC/CLIC), or a qualifying high school/post-secondary transcript in English or French
- Proof of tax filing for 3 of the last 5 years, where the applicant had a tax obligation
- 2 citizenship-format photos, 2 pieces of personal ID
- Fee payment receipt
- Conditional/situational extras: Use of Representative (IMM 5476), police certificate (only if 183+ consecutive days were spent outside Canada since age 18, within the relevant period), certified translations, name/date-of-birth/gender-marker change documentation

**Note:** minors use **CIT 0003** (application) / **CIT 0008** (checklist) — not detailed here. Canadian Armed Forces members have a distinct, expedited application (**CIT 0532** / **CIT 0172**).

### 11.2 Proof of Citizenship (Citizenship Certificate)
**Status:** Open

- **CIT 0001** — Application for a Citizenship Certificate
- **CIT 0014** — Document Checklist
- Evidence of the citizenship basis: Canadian birth certificate (if born in Canada) or proof of a parent's citizenship/naturalization (if born abroad)
- Standard identity documents

---

## 12. Maintenance Notes

Given how many programs in this document changed status within a single year (Sections 3, 5, 6, 9.4, 9.5), a monthly recheck against IRCC's [forms and guides page](https://www.canada.ca/en/immigration-refugees-citizenship/services/application/application-forms-guides.html) and the Quebec MIFI site is warranted at minimum for: Start-up Visa, Self-Employed, caregiver pilots, Agri-Food, and PEQ. Weekly checks make more sense for anything Express Entry- or PNP-adjacent, since category-based draws and provincial allocations shift often. IRPA/IRPR-level document *categories* (identity, police certificates, medical exams) are far more stable and don't need this cadence — it's specific form versions, thresholds, and open/closed status that churn.

## Primary Sources Consulted

- canada.ca — IRCC forms and guides (IMM 5690, 5533, 5771, 0199, 5488, 5556, 5483, 5484, 5280/5283, 0246–0249)
- canada.ca — IRCC operational bulletins and program delivery instructions (refugee protection forms, self-employed/start-up admissibility, caregiver pilot updates)
- canada.ca — Economic Immigration transition-binder overview (2026 pilot status)
- quebec.ca — Immigration, Francisation et Intégration (PSTQ, PEQ)
- irb-cisr.gc.ca — Basis of Claim form and Claimant's Guide
