---
slug: /runtime/ruby
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

Refer to: [App Runtime tutorials](../runtime#quick)

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