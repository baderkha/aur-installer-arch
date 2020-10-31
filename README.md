# aur-installer-arch
---
Quick and dirty Arch linux aur installer , because i'm lazy

What's Aur ? 
RTFM , jk , but seriously her's the manual https://wiki.archlinux.org/index.php/AUR_helpers

## Usage
The normal way to use it
```bash
$: aurer <<git-repo>>
 ```
example 
 ```bash
$: aurer https://aur.archlinux.org/slack-desktop.git
 ```
or if you're lazier
```bash
$: aurer
```
it will then ask you 

```bash
$: Enter the Aur Git Repository : 
```

## Installation 

```bash
$: git clone https://github.com/baderkha/aur-installer-arch && cd aur-installer-arch && make install;
```

## Requirements
- makepkg https://wiki.archlinux.org/index.php/makepkg
- python 3.8
- git , you should have this
