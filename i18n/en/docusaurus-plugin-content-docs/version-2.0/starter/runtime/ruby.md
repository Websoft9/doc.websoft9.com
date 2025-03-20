---
slug: /ruby
sidebar_position: 1.7
tags:
  - container
  - runtime
  - Ruby
---

# For Ruby App

## Configuration options{#configs}

- Get version: `ruby -v`
- App root directory:  */usr/src/app*  
- CLI: `ruby`, `gem`, `bundle`, `rake`
- Package manager: `gem` to install one package，`bundle` to install packages list
- Web framework: Rails, Sinatra, jekyll
- Ruby application server: WEBrick, [Phusion passenger](https://www.phusionpassenger.com/), Puma

## Deploy a Ruby application{#deploy}

Refer to: [App Runtime tutorials](./runtime)

## Manage runtime{#administrator}

- Change gem source URL
  ```
  gem sources --remove https://rubygems.org  && gem sources -a https://gems.ruby-china.com
  ```

- Change bundle source URL
  ```
  bundle config mirror.https://rubygems.org https://gems.ruby-china.com
  ```
## Troubleshoot

#### Gem package install error for Linux dependency?

This phenomenon is normal. Some `gem` packages depend on Linux packages (declared in `extconf.rb`). Therefore, when there is such a gem package in the `Gemfile`, there will be multi-level dependencies to the operating system.