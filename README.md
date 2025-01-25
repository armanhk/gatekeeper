# Gatekeeper Discord Bot
## Overview
A script for a discord bot that assigns a role to a member of a given server, contingent upon the user sending the bot a secret message upon joining the server.

## Prerequisites
- Create a discord application and bot with appropriate permissions (ability to manage roles)
- Add discord bot to target server
- Enable server members intent for the bot
- Install the discord python module on the server

## Usage

In order to use this script, you'll need to change the following items where they appear in the script:

-  `<DISCORD BOT TOKEN>`
- `<SERVER ID>`
- `<ROLE ID>`
- `<SERVER NAME>` (optional)

You'll also need to replace the contents of `"secret phrase here (all lowercase)"` and any logging statements as desired.

## What Does it Do?
This script simply creates a bot that sends a private welcome message to users when they join target server. The bot will assign a given role to new members if they reply to the welcome message with a secret phrase.
