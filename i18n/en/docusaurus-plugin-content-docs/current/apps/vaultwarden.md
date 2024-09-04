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

## Configuration Options {#configs}

- **Multilingual Support (×)**: Vaultwarden does not support multiple languages.
- **CLI Access (✅)**: Vaultwarden can be managed using the Command Line Interface (CLI) for advanced configurations.
- **Two-Factor Authentication (2FA)**: Enable 2FA through the settings for enhanced account security.

## Administration {#administrator}

1. **Backup and Restore**:

   - **Backup**: Schedule regular backups through the Websoft9 Console to protect your Vaultwarden data. Backups are essential in case of data corruption or accidental deletion.
   - **Restore**: If needed, use the Websoft9 Console to restore data from previous backups.

2. **User and Role Management**:

   - Admins can add, remove, and manage users within Vaultwarden. Roles and permissions can also be configured to ensure users only access the necessary data.

3. **Security Configuration**:
   - Enable **Two-Factor Authentication (2FA)** in Vaultwarden to enhance account security.
   - Ensure that HTTPS is always enabled to protect sensitive data during transmission.

## Troubleshooting {#troubleshooting}

### Common Issues

1. **Connection Problems**:

   - **Symptom**: Vaultwarden is unreachable or not responding.
   - **Solution**: Check the container status via the Websoft9 Console and restart it if necessary using `docker restart <container_name>`.

2. **Login Failures**:

   - **Symptom**: Users are unable to log in or encounter "incorrect password" errors.
   - **Solution**: Use the Vaultwarden admin interface to reset user passwords.

3. **SSL/TLS Configuration Errors**:
   - **Symptom**: SSL/TLS configuration issues prevent access to Vaultwarden over HTTPS.
   - **Solution**: Review the HTTPS settings in the Websoft9 Console and verify that the correct certificates are applied.
