import os
import subprocess

""" This file defines what the update-kali script should do. """

# Determine release, and whether we are on Windows Subsystem for Linux (WSL) so that we can set
# different settings for different environments. Anything common can go outside the if statements.

release = subprocess.check_output(
    """sh -c '. /etc/os-release; echo "$NAME"'""", shell=True, universal_newlines=True
).strip()
are_we_on_wsl = os.path.exists("/mnt/c/Windows/System32/wsl.exe")


if "Kali" in release:
    # These directories will be removed from your home directory
    directories_to_remove = [
        "Documents",
        "Music",
        "Pictures",
        "Public",
        "Templates",
        "Videos",
    ]

    # These kali packages will be installed
    packages_to_install = [
        "terminator",
        "most",
        "ttf-mscorefonts-installer",
        "pydf",
        "htop",
        "gobuster",
        "amass",
        "golang",
        "exif",
        "hexedit",
        "jq",
        "python3-pip",
        "python3-venv",
        "apt-transport-https",
        "curl",
        "filezilla",
        "meld",
        "ncat",
        "net-tools",
        "bash-completion",
        "ieee-data",
        "python3-netaddr",
        "ruby-full",
        "cewl",
        "nbtscan",
        "tree",
        "upx-ucl",
        "exe2hexbat",
        "grc",
    ]

    # These kali packages will be removed
    packages_to_remove = []

    # These python packages will be installed globally
    pip_packages = []

    # These gem packages will be installed globally
    gem_packages = ["wpscan"]

    # These go tools will be installed globally. You will need to have the following settings in your
    # .bashrc already:

    # export GOROOT=/usr/lib/go
    # export GOPATH=$HOME/go
    # export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
    golang_install_directory = "/usr/lib/go/modules/"
    golang_modules_to_install = [
        "github.com/lc/gau",
        "github.com/hakluke/hakrawler",
        "github.com/hahwul/dalfox",
        "github.com/projectdiscovery/nuclei/v2/cmd/nuclei",
        "github.com/Shopify/kubeaudit",
        "github.com/tomnomnom/httprobe",
    ]

    # These git repositories will be synced to the 'external repo' directory

    external_tools_directory = "/opt"

    external_tools_directory_dns = "/opt/dns"

    ext_repositories_dns = [
        "https://github.com/aboul3la/Sublist3r",
        "https://github.com/darkoperator/dnsrecon",
        "https://github.com/vortexau/dnsvalidator",
        "https://github.com/guelfoweb/knock",
        "https://github.com/d3mondev/puredns",
        "https://github.com/a6avind/spoofcheck",
        "https://github.com/RevoltSecurities/Subdominator",
    ]

    external_tools_directory_infra = "/opt/infra"

    ext_repositories_infra = [
        "https://github.com/danielbohannon/Invoke-Obfuscation",
        "https://github.com/SpiderLabs/Responder",
        "https://github.com/chipik/SAP_RECON",
        "https://github.com/Octoberfest7/TeamsPhisher",
        "https://github.com/BishopFox/bigip-scanner",
        "https://github.com/PowerShellMafia/PowerSploit",
        "https://github.com/fortra/impacket",
        "https://github.com/samratashok/nishang",
        "https://github.com/kh4sh3i/exchange-penetration-testing",
        "https://github.com/SecurityRiskAdvisors/msspray",
        "https://github.com/gremwell/o365enum",
        "https://github.com/airbus-seclab/ilo4_toolbox",
        "https://github.com/peass-ng/PEASS-ng",
        "https://github.com/RUB-NDS/PRET",
        "https://github.com/Anon-Exploiter/SUID3NUM",
        "https://github.com/Pepelux/sippts",
        "https://github.com/jtesta/ssh-audit",
        "https://github.com/nullt3r/udpx",
        "https://github.com/trustedsec/unicorn",
        "https://github.com/c3c/ADExplorerSnapshot.py",
        "https://github.com/samratashok/ADModule",
        "https://github.com/r3motecontrol/Ghostpack-CompiledBinaries",
        "https://github.com/Kevin-Robertson/Inveigh",
        "https://github.com/netwrix/pingcastle",
        "https://github.com/itm4n/PrivescCheck",
        "https://github.com/GhostPack/Rubeus",
        "https://github.com/FalconForceTeam/SOAPHound",
        "https://github.com/S3cur3Th1sSh1t/WinPwn",
        "https://github.com/bitsadmin/wesng",
        "https://github.com/sensepost/ruler",
        "https://github.com/ShawnDEvans/smbmap",
        "https://github.com/GoSecure/WSuspicious",
        "https://github.com/outflanknl/PrintNightmare",
    ]

    external_tools_directory_mobile = "/opt/mobile"

    ext_repositories_mobile = [
        "https://github.com/dwisiswant0/apkleaks",
        "https://github.com/skylot/jadx",
    ]

    external_tools_directory_osint = "/opt/osint"

    ext_repositories_osint = [
        "https://github.com/jobroche/InSpy",
        "https://github.com/GiJ03/Infoga",
        "https://github.com/SimplySecurity/SimplyEmail",
        "https://github.com/sse-secure-systems/TeamsEnum",
        "https://github.com/Ekultek/WhatBreach",
        "https://github.com/m8sec/CrossLinked",
        "https://github.com/alpkeskin/mosint",
        "https://github.com/sundowndev/phoneinfoga",
        "https://github.com/smicallef/spiderfoot",
    ]

    external_tools_directory_utility = "/opt/utility"

    ext_repositories_utility = [
        "https://github.com/swisskyrepo/PayloadsAllTheThings",
        "https://github.com/danielmiessler/SecLists",
        "https://github.com/gchq/CyberChef",
        "https://github.com/Hoplite-Consulting/EPSS-CLI",
        "https://github.com/sean-t-smith/Extreme_Breach_Masks",
        "https://github.com/fkie-cad/FACT_core",
        "https://github.com/internetwache/GitTools",
        "https://github.com/securityjoes/MasterParser",
        "https://github.com/stealthsploit/OneRuleToRuleThemStill",
        "https://github.com/PercussiveElbow/docker-escape-tool",
        "https://github.com/vinitkumar/json2xml",
        "https://github.com/radareorg/radare2",
        "https://github.com/cycurity/wister",
    ]

    external_tools_directory_web = "/opt/web"

    ext_repositories_web = [
        "https://github.com/yunemse48/403bypasser",
        "https://github.com/s0md3v/Arjun",
        "https://github.com/clr2of8/GatherContacts",
        "https://github.com/PortSwigger/autorize",
        "https://github.com/dionach/CMSmap",
        "https://github.com/chenjj/CORScanner",
        "https://github.com/digininja/CeWL",
        "https://github.com/s0md3v/Corsy",
        "https://github.com/Santandersecurityresearch/DrHeader",
        "https://github.com/shivsahni/FireBaseScanner",
        "https://github.com/PalindromeLabs/STEWS",
        "https://github.com/a0xnirudh/WebXploiter",
        "https://github.com/urbanadventurer/WhatWeb",
        "https://github.com/tunetheweb/wappalyzer",
        "https://github.com/iosiro/baserunner",
        "https://github.com/SamJoan/droopescan",
        "https://github.com/immunIT/drupwn",
        "https://github.com/securebinary/firebaseExploiter",
        "https://github.com/0xbigshaq/firepwn-tool",
        "https://github.com/carlospolop/fuzzhttpbypass",
        "https://github.com/ozguralp/gmapsapiscanner",
        "https://github.com/dolevf/graphw00f",
        "https://github.com/mozilla/http-observatory",
        "https://github.com/simplylu/jpeg_polyglot_xss",
        "https://github.com/callforpapers-source/jshole",
        "https://github.com/ticarpi/jwt_tool",
        "https://github.com/steverobbins/magescan",
        "https://github.com/inc0d3/moodlescan",
        "https://github.com/mozilla/observatory-cli",
        "https://github.com/sqlmapproject/sqlmap",
        "https://github.com/drwetter/testssl.sh",
        "https://github.com/epinna/tplmap",
        "https://github.com/EnableSecurity/wafw00f",
        "https://github.com/Lissy93/web-check",
        "https://github.com/xmendez/wfuzz",
        "https://github.com/wpscanteam/wpscan",
        "https://github.com/vavkamil/xss2png",
        "https://github.com/Grunny/zap-cli",
    ]

    # Next, take a look in the /scripts directory. Every script ending in .sh or .py will be run,
    # provided it's # executable. For example, the current scripts install VS Code, Google Chrome and
    # Typora. Any script that goes in this directory should be written so it can run multiple times
    # without causing problems.

    zshrc_configuration = [
        "alias c='clear'",
        "alias opt='cd /opt && ls",
        "alias profile='sudo nano ~/.zshrc",
        "alias save='source ~/.zshrc",
        "export GOROOT=/usr/lib/go",
        "export GOPATH=$HOME/go",
    ]

if "Ubuntu" in release and not are_we_on_wsl:
    # These directories will be removed from your home directory
    directories_to_remove = [
        "Documents",
        "Music",
        "Pictures",
        "Public",
        "Templates",
        "Videos",
    ]

    # These Ubuntu packages will be installed
    packages_to_install = [
        "most",
        "ttf-mscorefonts-installer",
        "pydf",
        "htop",
        "golang",
        "exif",
        "hexedit",
        "jq",
        "python3-pip",
        "python3-venv",
        "apt-transport-https",
        "curl",
        "filezilla",
        "meld",
        "ncat",
        "net-tools",
        "tmux",
        "bash-completion",
        "ruby-full",
        "nbtscan",
        "tree",
        "grc",
        "john",
    ]

    # These Ubuntu packages will be removed
    packages_to_remove = []

    # These python packages will be installed globally
    pip_packages = ["pipenv", "pylint", "stegcracker", "truffleHog"]

    # These gem packages will be installed globally
    gem_packages = ["wpscan"]

    # These go tools will be installed globally. You will need to have the following settings in your
    # .bashrc already:
    #
    # export GOROOT=/usr/lib/go
    # export GOPATH=$HOME/go
    # export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
    golang_modules_to_install = [
        "github.com/lc/gau",
        "github.com/hakluke/hakrawler",
        "github.com/hahwul/dalfox",
    ]

    # These git repositories will be synced to the 'external repo' directory
    external_tools_directory = "/opt"
    external_tools_directory_dns = "/opt/dns"
    external_tools_directory_infra = "/opt/infra"
    external_tools_directory_mobile = "/opt/mobile"
    external_tools_directory_osint = "/opt/osint"
    external_tools_directory_utility = "/opt/utility"
    external_tools_directory_web = "/opt/web"

    ext_repositories_to_sync = []

    # Next, take a look in the /scripts directory. Every script ending in .sh or .py will be run,
    # provided it's # executable. For example, the current scripts install VS Code, Google Chrome and
    # Typora. Any script that goes in this directory should be written so it can run multiple times
    # without causing problems.

if "Ubuntu" in release and are_we_on_wsl:
    # These directories will be removed from your home directory
    directories_to_remove = []

    # These Ubuntu packages will be installed
    packages_to_install = [
        "most",
        "pydf",
        "golang",
        "exif",
        "hexedit",
        "jq",
        "python3-pip",
        "python3-venv",
        "curl",
        "net-tools",
        "tmux",
        "bash-completion",
        "ruby-full",
        "nbtscan",
        "tree",
        "grc",
    ]

    # These Ubuntu packages will be removed
    packages_to_remove = []

    # These python packages will be installed globally
    pip_packages = ["pipenv", "pylint"]

    # These gem packages will be installed globally
    gem_packages = []

    # These go tools will be installed globally. You will need to have the following settings in your
    # .bashrc already:
    #
    # export GOROOT=/usr/lib/go
    # export GOPATH=$HOME/go
    # export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
    golang_modules_to_install = []

    # These git repositories will be synced to the 'external repo' directory
    external_tools_directory = "/opt"
    ext_repositories_to_sync = []

    # Next, take a look in the /scripts directory. Every script ending in .sh or .py will be run,
    # provided it's # executable. For example, the current scripts install VS Code, Google Chrome and
    # Typora. Any script that goes in this directory should be written so it can run multiple times
    # without causing problems.
