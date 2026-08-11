# Security Policy

## Scope

This project is intended for authorized AI safety testing, model evaluation, defensive research, and controlled experimentation.

Do not use it to test systems, models, accounts, applications, or data without permission.

## Secrets

Never commit API keys, tokens, credentials, private prompts, customer data, or confidential configuration.

Use environment variables or an appropriate secret manager for runtime credentials.

If a credential is accidentally committed:

1. Revoke or rotate it immediately at the provider.
2. Replace it with a new credential.
3. Remove the exposed value from current source.
4. Treat the old value as compromised even if Git history is later rewritten.

## Reporting a security issue

Do not open a public GitHub issue containing exploit details, credentials, private customer information, or other sensitive material.

For non-sensitive project defects, a normal GitHub issue is appropriate.

For a sensitive security report, establish contact using a high-level issue that contains no confidential details, then move the discussion to an appropriate private channel before sharing evidence.

## Responsible testing

When running red-team evaluations:

- define the target and authorization boundary first,
- avoid unrelated infrastructure,
- minimize collection of sensitive data,
- preserve evidence needed for remediation,
- stop testing if the activity leaves the agreed scope,
- document assumptions and limitations in any findings report.

## No guarantee

This project does not guarantee vulnerability discovery, security, regulatory compliance, or fitness for a specific production environment. Assessment quality depends on scope, test design, target behavior, model/provider constraints, and available evidence.
