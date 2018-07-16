![](https://github.com/Unit6/Unit6/blob/master/Unit6/themes/core/static/img/logo.png?raw=true)
====

[![Build Status](https://travis-ci.org/Unit6/Unit6.svg?branch=master)](https://travis-ci.org/Unit6/Unit6)
[![Unit6 Slack](https://slack.unitsix.io/badge.svg)](https://slack.unitsix.io/)

## What is Unit6?
Unit6 is a Capture The Flag framework focusing on ease of use and customizability. It comes with everything you need to run a CTF and it's easy to customize with plugins and themes.

![Unit6 is a CTF in a can.](https://github.com/Unit6/Unit6/blob/master/Unit6/themes/core/static/img/scoreboard.png?raw=true)

## Features
 * Create your own challenges, categories, hints, and flags from the Admin Interface
    * Static & Regex based flags
    * Users can unlock hints for free or with points
    * File uploads to the server or [Amazon S3](https://github.com/Unit6/Unit6-S3-plugin)
    * Limit challenge attempts & hide challenges
    * Automatic submission throttling
 * Scoreboard with automatic tie resolution
    * Hide Scores from the public
    * Freeze Scores at a specific time
    * [Dynamic Scoring](https://github.com/Unit6/DynamicValueChallenge)
 * Scoregraphs comparing the top 10 teams and team progress graphs
 * Markdown content management system
 * SMTP + Mailgun email support
    * Email confirmation support
    * Forgot password support
 * Automatic competition starting and ending
 * Team management & hiding
 * Customize everything using the [plugin](https://github.com/Unit6/Unit6/wiki/Plugins) and [theme](https://github.com/Unit6/Unit6/tree/master/Unit6/themes) interfaces
 * Importing and Exporting of CTF data for archival
 * And a lot more...

## Install
 1. Run `./prepare.sh` to install dependencies using apt.
 2. Modify [Unit6/config.py](https://github.com/Unit6/Unit6/blob/master/Unit6/config.py) to your liking.
 3. Use `python serve.py` in a terminal to drop into debug mode.

Or you can use Docker with the following command:

`docker run -p 8000:8000 -it unitsix/unitsix`

 * [Here](https://github.com/Unit6/Unit6/wiki/Basic-Deployment) are some deployment options
 * You can check out the [Getting Started](https://github.com/Unit6/Unit6/wiki/Getting-Started) guide for a breakdown of some of the features you need to get started.

## Live Demo
https://demo.unitsix.io/

## Support
To get basic support, you can join the [Unit6 Slack Community](https://slack.unitsix.io/): [![Unit6 Slack](https://slack.unitsix.io/badge.svg)](https://slack.unitsix.io/)

If you prefer commercial support or have a special project, send us an email: [support@unitsix.io](mailto:support@unitsix.io).

## Managed Hosting
Looking to use Unit6 but don't want to deal with managing infrastructure? Check out [the Unit6 website](https://unitsix.io/) for managed Unit6 deployments.

## HackerFire
Looking for CTF challenges to work on? [HackerFire](https://hackerfire.com/) is a learning focused CTF built using Unit6. It features a wide variety of challenges and is updated with new content frequently. It also contains custom knowledge resources to teach newcomers about the techniques used to solve a challenge.

## Credits
 * Logo by [Laura Barbera](http://www.laurabb.com/)
 * Theme by [Christopher Thompson](https://github.com/breadchris)
"# Unit6project" 
"# unit6proj" 
"# unit6proj" 
