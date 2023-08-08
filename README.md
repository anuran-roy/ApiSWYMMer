# ApiSWYMmer

<p align="center"><img src="./assets/apiswymmer-logo.png" />

Swim through APIs with ease!
</p>

## What is API SWYMmer?

Have you seen the movie "Finding Nemo"? If you have, you might remember the scene where Nemo and his friends are trying to escape from the fish tank. They are trying to swim through the pipes to get to the ocean. But, they don't know which pipe to take. So, they ask the fish in the tank to help them. The fish in the tank tell them to take the pipe that says "Sydney". But, Nemo and his friends don't know which pipe says "Sydney".

APIs are like that, aren't they?

Documenting the APIs is like putting labels on the pipes. But, it is a tedious task. And, it is not easy to keep the documentation up-to-date. So, we decided to automate the process of documenting APIs. We call it **ApiSWYMmer**.

## Features

1. **Portable**: Generate documentation from Swagger Specs on the fly - no installation required.
2. **Easy integrations**: The build command is just a function - it can be easily integrated with CI/CD pipelines.
3. **Super-hackable**: The small codebase ensures that you can turn every knob you can think of.
4. **Multi-branching**: The build folder can contain multiple builds. So if you are working on multiple branches, you can generate documentation for all of them with a [**single command**](#builder_command).
5. **Superfast**: The build command is fast. It takes less than a second to generate the documentation for a 1000+ line Swagger Spec.
6. **Plugin Support** (under development): You can write your own plugins to extend the functionality of ApiSWYMmer. You can also use plugins written by others. Also, some delicious plugins are on their way! :wink:

## Getting Started

There is no installation of ApiSWYMmer required (except the dependencies ofcourse.)

### Setup

```bash
bash setup.sh
```

That's all you need to do!

### Usage

#### CLI-based Builder

<div id="builder_command" />

```bash
python3 cli.py samples/sample_openapi.json boo/new2.html
```

Just give this a try!

