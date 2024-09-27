---
title: TensorFlow
slug: /tensorflow
tags:
  - Artificial Intelligence
  - Machine Learning
---

import Meta from './\_include/tensorflow.md';

<Meta name="meta" />

## Getting Started {#guide}

### Initial Setup {#wizard}

1. After completing the installation of TensorFlow in the **Websoft9 Console**, retrieve the application's **Overview** and **Access** information from **My Apps**.

2. Access the Jupyter URL locally, and you will be prompted to enter a login token.

3. Log in to the Jupyter backend using the token or set a password.
   ![](./assets/tensorflow-jupter-websoft9.png)

### Run TensorBoard

1. In the Jupyter backend, go to **New > Python 3 (ipykernel)**.

2. Refer to [Using TensorBoard in Notebooks](https://tensorflow.google.cn/tensorboard/tensorboard_in_notebooks), and run the example programs in sequence. Add the parameter `--host 0.0.0.0` to the last command (to allow external access).

3. TensorBoard will now be displayed in the Notebook.
   ![](./assets/tensorflow-dashjupter-websoft9.png)

## Configuration Options {#configs}

- Container Ports:
  - 8888: Jupyter port
  - 6006: TensorBoard port

## Administration {#administrator}

## Troubleshooting {#troubleshooting}

#### TensorBoard Not Visible in Notebook?

- Ensure that the TensorBoard command is started with the `--host 0.0.0.0` flag.
- Ensure the host port for the container's 6006 port mapping is enabled.
