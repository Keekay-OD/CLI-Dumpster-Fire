# Linux Terminal Alias Configuration Guide

A guide for managing command aliases in Linux/Ubuntu terminals.

## Installation

No additional installation required - uses built-in shell configuration.

## Usage

### Adding New Aliases

1. Open `.bashrc`:
```bash
nano ~/.bashrc
```

2. Add alias at the bottom:
```bash
alias custom_name='command_to_run'
```

3. Apply changes:
```bash
source ~/.bashrc
```

### Common Examples

```bash
# Media player shortcut
alias media='vlc'

# Quick directory navigation
alias projects='cd ~/projects'

# Enhanced commands
alias ll='ls -la'
```

### Managing Aliases

Remove temporary alias:
```bash
unalias alias_name
```

List all aliases:
```bash
alias
```

## Troubleshooting

- Aliases not working after adding: Run `source ~/.bashrc`
- Alias conflicts: Check existing aliases with `alias` command
- Permanent vs. temporary: Changes in `.bashrc` are permanent, `unalias` is temporary

## Notes

- Aliases are shell-specific (bash/zsh)
- Use quotes for commands with spaces/special characters
- Aliases can include arguments and pipes

## License

MIT License