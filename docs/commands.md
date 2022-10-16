<!-- Space: Projects -->
<!-- Parent: AnsibleRoleNginx -->
<!-- Title: Commands AnsibleRoleNginx -->
<!-- Label: AnsibleRoleNginx -->
<!-- Label: Project -->
<!-- Label: Commands -->
<!-- Include: disclaimer.md -->
<!-- Include: ac:toc -->

# Commands

## Pipenv

## Taskfile

### Molecule

#### Test Molecule

```bash
task molecule:test
```

#### Create Scenario

```bash
task molecule:scenario SCENARIO=name
```

### Generate Readme

```{.bash}
task readme
```

## Documentation

### Confluence

#### Sync Markdown with confluence

```{.bash}
task mark:sync
```

### Python

#### Format syntax code python with [black](https://github.com/psf/black)

```{.bash}
task python:fmt -- {{file_name or path}}
```

### Diagrams

#### Publish diagrams

```{.bash}
task diagrams:publish
```

### Mkdocs

#### Generate Website

```{.bash}
task docs:build
```

### Changelog

#### Generate Changelog Next Tag

```{.bash}
task changelog:next APP_TAG={{tag name}}
```

#### Parameters

| Name     | Description   | sample | Required |
| -------- | ------------- | ------ | :------: |
| tag name | Name next tag | 0.1.0  |   yes    |

### Version

#### Version Major

```{.bash}
task version:major
```

#### Version Minor

```{.bash}
task version:minor
```

#### Version Patch

```{.bash}
task version:patch
```
