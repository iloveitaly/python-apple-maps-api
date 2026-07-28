---
layout: landing
---

:::{container}
:name: home-head

<div class="title-with-logo">
   <div class="brand-text">APPLE MAPS API</div>
</div>
:::

<p class="lead" style="text-align: center; font-size: 1.25rem; color: var(--sy-c-text-muted); margin-bottom: 2rem;">
A modern, type-safe Python client for the Apple Maps Server API.
</p>

:::{container} buttons wrap
<a href="getting-started.html" class="btn-no-wrap">Get Started</a>
:::

::::{grid} 1 1 2 2
:gutter: 3

:::{grid-item-card} {octicon}`key` Automatic JWT Management
Handles signing and periodic refresh of Apple's ES256 tokens so you can focus on queries.
:::

:::{grid-item-card} {octicon}`code` Type-Safe Models
Pydantic models for every API response, with excellent IDE support and resilient retries.
:::
::::

```{toctree}
:maxdepth: 2
:hidden:

Getting Started <getting-started>
Examples <examples>
API Reference <autoapi/index>
Changelog <changelog>
```
