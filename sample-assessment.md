# Sanitized Sample AI Red-Team Assessment

> **Fictional public-safe example.** This document demonstrates reporting structure only. It is not a real client assessment, does not describe a live target, and intentionally withholds reusable adversarial payloads.

## Executive judgment

The fictional sandbox assistant showed **moderate instruction-boundary degradation** under repeated conflicting context. The behavior would justify remediation before relying on the model for workflows where instruction hierarchy or tool permissions have operational consequences.

**Example severity:** Medium  
**Example confidence:** Moderate  
**Retest required:** Yes

## Scope

- Target: fictional sandbox assistant
- Environment: non-production demonstration
- Objective: evaluate preservation of configured instruction hierarchy
- Authorization: fictional/demo environment
- Exclusions: infrastructure penetration testing, credential testing, real customer data, live exploit development

## Finding DEMO-RT-001

### Title

Instruction-boundary degradation under conflicting context

### Expected behavior

The assistant should preserve the configured instruction hierarchy and reject lower-priority requests that conflict with higher-priority controls.

### Observed behavior

After repeated contradictory framing, the fictional assistant allowed lower-priority context to materially influence its final response.

### Public evidence

The exact adversarial input is withheld in this public example. A commercial findings package would record the authorized test case, relevant response evidence, reproduction conditions, model/environment metadata, and analyst judgment.

### Risk

Applications that depend on stable instruction hierarchy could produce behavior outside the operator's intended control surface. Impact depends on whether the affected model can access tools, sensitive data, external systems, or consequential workflows.

### Remediation

1. Strengthen separation between trusted instructions and untrusted context.
2. Validate and sanitize context before it reaches privileged instructions or tools.
3. Add regression tests covering conflicting-context cases.
4. Add explicit authorization checks around consequential tool calls.
5. Re-run the same evaluation category after mitigation.

### Evidence ceiling

This fictional finding demonstrates a reporting pattern. It does **not** establish that any real model, provider, or customer system has this weakness.

## Reporting principles

A commercial assessment should distinguish:

- reproducible behavior from one-off output,
- observation from analyst inference,
- severity from rhetorical alarm,
- model behavior from infrastructure vulnerabilities,
- confirmed findings from unresolved hypotheses,
- remediation completed from remediation merely recommended.

## Commercial scope

See [PRICING.md](PRICING.md) for the current package ladder or open a [Commercial inquiry](https://github.com/hr185882-creator/ai-red-team-dashboard/issues/new?template=commercial-inquiry.md) with high-level, non-sensitive scope information.
