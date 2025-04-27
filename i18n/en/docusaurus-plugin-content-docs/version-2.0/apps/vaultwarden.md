---
title: Vaultwarden
slug: /vaultwarden
tags:
  - Password Security
  - Password Management
  - vaultwarden
---

import Meta from './\_include/vaultwarden.md';

<Meta name="meta" />

## Getting Started {#guide}

1. **Set up HTTPS**:
   - Log in to the Websoft9 Console, go to **Gateway** in the left menu, and follow the steps to configure HTTPS for Vaultwarden (**Required**).

2. **Application Overview**:
   - After completing the installation of Vaultwarden in the Websoft9 Console, retrieve the application's **Overview** and **Access** information from **My Apps**.

3. **Registration and Login**:
   - Follow the wizard to complete the registration and login process.

### Setting up the administration page 

Websoft9 has set up plaintext `ADMIN_TOKEN` by default, which can be used normally. If you want to set the secret text of argon2 as TOKEN, the steps are as follows: 

1. Use the command to generate the secret text of argon2 

 ``` 
 $ echo -n "MySecretPassword123" | argon2 "$(openssl rand -base64 32)" -e -id -k 65540 -t 3 -p 4 
 $ argon2id$v=19$m=65540,t=3,p=4$UTVtVDgyUkJLYkwrVjF6T3k3NjBnblk4M2JMZ3RYRW5BdUlHTXZhOVY3RT0$4uUKMzLRZHSPK0Fo3WmTdDI3suCdNGDi3F+ IrZ8AQys 
 ``` 

2. **My Apps > Compose > Go to Edit repository**, edit the .env file and set the value of `ADMIN_TOKEN` to cipher 

3. Rebuild the application 

4. Browser access to https://URL/admin and enter the plaintext password corresponding to the ciphertext to use it

## Configuration Options {#configs}

- **Multilingual Support (×)**: Vaultwarden does not support multiple languages.
- **CLI Access (✅)**: Vaultwarden can be managed using the Command Line Interface (CLI) for advanced configurations.
- **Two-Factor Authentication (2FA)**: Enable 2FA through the settings for enhanced account security.

## Administration {#administrator}

## Troubleshooting {#troubleshooting}
