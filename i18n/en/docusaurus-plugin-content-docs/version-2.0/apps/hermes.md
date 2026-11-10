---
title: Hermes Agent
slug: /hermes
tags:
  - Hermes Agent
  - AI Agent
  - LLM
---

import Meta from './_include/hermes.md';

<Meta name="meta" />

## Getting Started {#guide}

### Initialize {#wizard}

After installing Hermes Agent in the Websoft9 console, open the Dashboard URL from the **Access** tab and sign in with the HTTP Basic Auth credentials configured as `W9_LOGIN_USER` and `W9_LOGIN_PASSWORD`.

### Configure a model and start a conversation {#model}

Hermes Agent requires an LLM provider. Open the app's **Compose** tab and set a provider API key in `.env` (for example, `OPENROUTER_API_KEY`), save, and rebuild the app. Then select a model in the Dashboard and start a conversation.

### Use the OpenAI-compatible API {#api}

After a model provider is configured, the OpenAI-compatible API server starts on port 8642. Authenticate API requests with `W9_POWER_PASSWORD` as a Bearer token. The same variable drives the dashboard password; rebuild the app after changing it.

## Best Practices

### Persist agent state {#persistence}

Configuration, environment variables, sessions, memories, skills, and logs are stored in the persistent data volume mounted at `/opt/data`. The image itself is stateless, so keep this volume when recreating or upgrading the container.

### Secure the Dashboard {#security}

The Dashboard uses HTTP Basic Auth. Keep `HERMES_DASHBOARD_BASIC_AUTH_*` authentication configured and ensure that `W9_POWER_PASSWORD` is at least 16 characters long. Limit access to the API and admin interface to trusted users.

## Configuration {#configs}

| Setting | Description | Default / location |
|---------|-------------|--------------------|
| Dashboard | Hermes web dashboard port | 9119 |
| OpenAI-compatible API | API server port; starts after a provider key is configured | 8642 |
| Dashboard username and password | Dashboard Basic Auth credentials | `W9_LOGIN_USER` / `W9_LOGIN_PASSWORD` |
| `W9_POWER_PASSWORD` | Dashboard password and API Bearer token | At least 16 characters |
| LLM provider API key | Required to use models and start the API service | Set in `.env`, for example `OPENROUTER_API_KEY` |
| `/opt/data` | Agent configuration, sessions, memories, skills, and logs | `hermes_data` persistent volume |

## Administration {#administrator}

### Upgrade

Update `W9_VERSION` and recreate the container from the Websoft9 console. The image is stateless; keep the `/opt/data` volume to preserve agent state. The first image pull may take several minutes.

### Backup and restore

Back up and restore the persistent volume mounted at `/opt/data`. It contains the agent's runtime configuration and user data. After restoring, check Dashboard authentication, model provider configuration, and session state.

## Troubleshooting {#troubleshooting}

#### The Dashboard does not open

Confirm the Dashboard authentication variables are configured, `W9_POWER_PASSWORD` is at least 16 characters, and the health check has passed. The initial image pull may take some time.

#### The API port does not start

The API server starts only after an LLM provider API key is configured in `.env`. Save the key, rebuild the app, and check the service status.

#### The agent reports a provider error

Check that a valid LLM provider API key is set in `.env`, then retry after rebuilding the app.

## References {#references}

- [Hermes Agent Docker user guide](https://hermes-agent.nousresearch.com/docs/user-guide/docker)
- [Hermes Agent project](https://github.com/NousResearch/hermes-agent)
- [Hermes Agent releases](https://github.com/NousResearch/hermes-agent)
