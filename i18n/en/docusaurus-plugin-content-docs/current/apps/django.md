---
title: Django
slug: /django
tags:
  - Python
  - Development Framework
---

import Meta from './_include/django.md';

<Meta name="meta" />

## Getting started{#guide}

## Configuration options{#configs}

- Architecture
  ![Python production environment architecture](./assets/django-arch-websoft9.jpg)

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

#### Error reported executing django startup command?

Description: You have 18 unapplied migrations. Your project may not run properly until you apply migrations for the following applications: admin, auth, contenttypes, sessions.Run "python manage.py migrate" to apply the migrations.    
Reason: unknown  
Solution: Run the following command before starting the project    
  ```
  python manage.py migrate
  ```