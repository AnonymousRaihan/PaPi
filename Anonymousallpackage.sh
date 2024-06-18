#!/bin/bash
# Defining arrays
pkg=("bash" "zsh" "fish" "exa" "bat" "fd" "zoxide" "wget" "curl" "git" "openssh" "python" "python2" "file" "tokei" "qpdf" "tree" "util-linux" "findutils" "coreutils" "diffutils" "ncurses-utils" "nmap" "openvpn" "whois" "tar" "zip" "unzip" "gzip" "rar" "nano" "vim" "micro" "net-tools" "gdb" "tmux" "tmate" "htop")
dev_pkg=("clang" "python" "python2" "pip" "php" "golang" "ruby" "perl" "openjdk-17" "dart" "nodejs" "nodejs-lts" "openssl" "nodejs" "php-apache" "nginx" "apache2" "phpmyadmin" "postgresql" "mariadb" "sqlite" "docker" "docker-compose" "kotlin" "rust" "swift")
sec_pkg=("nmap" "hashcat" "hydra" "john" "nikto" "sqlmap" "yara" "dnsrecon" "whois" "fierce" "dirb" "gobuster" "onesixtyone" "linkchecker" "crunch" "cupp" "gdb" "ffuf" "whatweb" "httrack" "recon-ng" "steghide" "netmask" "dnsenum" "dnsmap" "dnswalk" "proxychains" "openvpn" "hashid" "smbclient" "wig" "dirsearch" "urlextractor" "exif" "hashdeep" "weevely" "yersinia" "patator" "cewl" "searx")
editors=("nano" "vim" "neovim" "micro" "codiad web ide" "emacs" "joe" "hexcurse" "ired" "radare2" "dcraw" "gifsicle" "gmic" "graphicsmagick" "imagemagick" "netpbm" "optipng" "ffmpeg")
cool_pkg=("cmatrix" "hollywood" "neofetch" "figlet" "toilet" "cowsay" "fortune" "lolcat" "sl" "moon-buggy" "nyancat" "ninvaders" "nudoko" "nsnake")

# Function to install selected pkg
install_pkg() {
    local pkg_manager="apt" 

    for pkg_to_install in "${@}"; do
        echo -e "\e[1;92mInstalling $pkg_to_install..."
        yes | "$pkg_manager" install "$pkg_to_install"  # Automatically answer "yes" to prompts
        echo " "
        echo -e "\e[1;92mPackage $pkg_to_install installed."
        echo " "
    done
    # Press Enter to continue
    read -p "Ꭾ𝚁𝙴𝚂𝚂 Ꭼ𝙽𝚃𝙴𝚁 Ꭲ𝙾 Ꮯ𝙾𝙽𝚃𝙸𝙽𝚄𝙴..."
}

# Main menu
while true; do
    clear

#ANSI color codes
green="\e[32m"
reset="\e[0m"
# Green colored text art
art="${green}
╔════╗╔═══╗╔═══╗╔═╗╔═╗╔╗─╔╗╔═╗╔═╗────╔═══╗╔╗───╔╗─── 
║╔╗╔╗║║╔══╝║╔═╗║║║╚╝║║║║─║║╚╗╚╝╔╝────║╔═╗║║║───║║─── 
╚╝║║╚╝║╚══╗║╚═╝║║╔╗╔╗║║║─║║─╚╗╔╝─────║║─║║║║───║║─── 
──║║──║╔══╝║╔╗╔╝║║║║║║║║─║║─╔╝╚╗─────║╚═╝║║║─╔╗║║─╔╗ 
──║║──║╚══╗║║║╚╗║║║║║║║╚═╝║╔╝╔╗╚╗────║╔═╗║║╚═╝║║╚═╝║ 
──╚╝──╚═══╝╚╝╚═╝╚╝╚╝╚╝╚═══╝╚═╝╚═╝────╚╝─╚╝╚═══╝╚═══╝ 
╔═══╗╔═══╗╔═══╗╔╗╔═╗╔═══╗╔═══╗╔═══╗ 
║╔═╗║║╔═╗║║╔═╗║║║║╔╝║╔═╗║║╔═╗║║╔══╝ 
║╚═╝║║║─║║║║─╚╝║╚╝╝─║║─║║║║─╚╝║╚══╗ 
║╔══╝║╚═╝║║║─╔╗║╔╗║─║╚═╝║║║╔═╗║╔══╝ 
║║───║╔═╗║║╚═╝║║║║╚╗║╔═╗║║╚╩═║║╚══╗ 
╚╝───╚╝─╚╝╚═══╝╚╝╚═╝╚╝─╚╝╚═══╝╚═══╝ 
${reset}"

# Print the art
    echo -e "$art"
    echo -e "\e[1;94m╔════════════════════════╗"
    echo -e "\e[1;94m║Ꭲ𝙷𝙸𝚂 Ꭲ𝙾𝙾𝙻𝚂 Ꮯ𝚁𝙴𝙰𝚃𝙴 Ᏼ𝚈 Ꮧ𝙽𝙾𝙽𝚈𝙼𝙾𝚄Ꭶ║"
    echo -e "\e[1;94m╚════════════════════════╝"
    echo -e "\e[1;94m╔═════════◈❖◎❀◎❖◈═════════╗"
    echo -e "\e[1;94m［＋］ 𝙰𝚄𝚃𝙷𝙾𝚁 : Ꮧ𝙽𝙾𝙽𝚈𝙼𝙾𝚄Ꭶ.☑"
    echo -e "\e[1;94m［＋］ 𝙶𝙸𝚃𝙷𝚄𝙱 : @AnonymousRaihan.☑"
    echo -e "\e[1;94m［＋］ 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 : @Anonymous_AR_Official.☑"
    echo -e "\e[1;94m［＋］ 𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺 : Ꮧ𝙽𝙾𝙽𝚈𝙼𝙾𝚄Ꭶ.☑"
    echo -e "\e[1;94m［＋］ 𝚆𝙷𝙰𝚃𝚂𝙰𝙿𝙿 : 𝟶𝟷𝟿𝟷𝟼𝟽𝟹𝟾𝟾𝟷𝟿.☑"
    echo -e "\e[1;94m╚═════════◈❖◎❀◎❖◈═════════╝"
    echo " "
    echo "❶ Ᏼ𝙰𝚂𝙸𝙲 Ꭾ𝙰𝙲𝙺𝙰𝙶𝙴𝚂 Ꮀ𝙾𝚁 Ꭼ𝚅𝙴𝚁𝚈𝙾𝙽𝙴 (Ꭺ𝙻𝙻)"
    echo "❷ Ꭰ𝙴𝚅𝙴𝙻𝙾𝙿𝙼𝙴𝙽𝚃 Ꭾ𝙰𝙲𝙺𝙰𝙶𝙴𝚂"
    echo "❸ Ꮪ𝙴𝙲𝚄𝚁𝙸𝚃𝚈 Ꭾ𝙰𝙲𝙺𝙰𝙶𝙴𝚂 (Ꭾ𝚁𝙾𝙾𝚃-𝙳𝙸𝚂𝚃𝚁𝙾)"
    echo "❹ Ꭼ𝙳𝙸𝚃𝙾𝚁𝚂 (𝚃𝙴𝚇𝚃/𝙸𝙼𝙰𝙶𝙴/𝙷𝙴𝚇/𝙰𝚄𝙳𝙸𝙾)"
    echo "❺ Ꮯ𝙾𝙾𝙻 Ꭾ𝙰𝙲𝙺𝙰𝙶𝙴𝚂 (𝙵𝚄𝙽)"
    echo "❻ Ꮠ𝙽𝚂𝚃𝙰𝙻𝙻 Ꭺ𝙱𝙾𝚅𝙴 Ꭺ𝙻𝙻 Ꭾ𝙰𝙲𝙺𝙰𝙶𝙴𝚂 (Ꭺ𝙻𝙻)"
    echo "❼ Ꭼ𝚇𝙸𝚃"
    echo " "
    read -p "Ꮪ𝙴𝙻𝙴𝙲𝚃 Ꭺ𝙽 Ꭷ𝙿𝚃𝙸𝙾𝙽 (𝟷−𝟽): " choice

    case $choice in
    1)
        while true; do
            clear
            echo -e "\e[0;94mᏴ𝙰𝚂𝙸𝙲 Ꭾ𝙰𝙲𝙺𝙰𝙶𝙴𝚂 Ꮀ𝙾𝚁 Ꭼ𝚅𝙴𝚁𝚈𝙾𝙽𝙴"
            echo "----------------------------"
            # Display the list of basic pkgs with numbers
            for i in "${!pkg[@]}"; do
                echo "($((i+1))) ${pkg[$i]}"
            done
            echo "----------------------"
            echo "                        "
            echo "(❶ Ꮯ𝙷𝙾𝙾𝚂𝙴 Ꭾ𝙰𝙲𝙺𝙰𝙶𝙴𝚂 Ꭹ𝙾𝚄 Ꮃ𝙰𝙽𝚃 Ꭲ𝙾 Ꮠ𝙽𝚂𝚃𝙰𝙻𝙻"
            echo "❷ Ꮠ𝙽𝚂𝚃𝙰𝙻𝙻 Ꭺ𝙻𝙻 Ꭾ𝙰𝙲𝙺𝙰𝙶𝙴𝚂 Ꮮ𝙸𝚂𝚃𝙴𝙳 Ꭺ𝙱𝙾𝚅𝙴"
            echo "❸ Ᏼ𝙰𝙲𝙺"
            echo "❹ Ꭼ𝚇𝙸𝚃"
            echo "                                              "
            read -p "Ꮪ𝙴𝙻𝙴𝙲𝚃 Ꭺ𝙽 Ꭷ𝙿𝚃𝙸𝙾𝙽 (𝟷−𝟺): " basic_choice
            case $basic_choice in
            1)
                read -p "Ꭼ𝙽𝚃𝙴𝚁 Ꭾ𝙰𝙲𝙺𝙰𝙶𝙴 Ꮑ𝚄𝙼𝙱𝙴𝚁𝚂 Ꭲ𝙾 Ꮠ𝙽𝚂𝚃𝙰𝙻𝙻 (Ꭼ.Ꮐ., 𝟷 𝟸 𝟹): " selected_pkg
                selected_pkg=($selected_pkg)
                if [[ "${selected_pkg[*]}" == *"back"* ]]; then
                    break
                else
                    selected_packages=()
                    for index in "${selected_pkg[@]}"; do
                        selected_packages+=("${pkg[$((index-1))]}")
                    done
                    install_pkg "${selected_packages[@]}"
                fi
                ;;
            2)
                # Combine all the basic pkgs 
                all_basic_packages="${pkg[*]}"
                # Install all basic pkgs
                yes | install_pkg $all_basic_packages
                ;;
            3)
                break
                ;;
            4)
                exit
                ;;
            *)
                echo -e "\e[1;91mᏐ𝙽𝚅𝙰𝙻𝙸𝙳 Ꭷ𝙿𝚃𝙸𝙾𝙽"
                ;;
            esac
        done
        ;;
    2)
        while true; do
            clear
            echo -e "\e[1;91mᎠ𝙴𝚅𝙴𝙻𝙾𝙿𝙼𝙴𝙽𝚃 Ꭾ𝙰𝙲𝙺𝙰𝙶𝙴𝚂"
            echo "---------------------"
            # Display the list of dev pkgs with numbers
            for i in "${!dev_pkg[@]}"; do
                echo "($((i+1))) ${dev_pkg[$i]}"
            done
            echo "----------------------"
            echo "                        "
            echo "❶ Ꮯ𝙷𝙾𝙾𝚂𝙴 Ꭾ𝙰𝙲𝙺𝙰𝙶𝙴𝚂 Ꭹ𝙾𝚄 Ꮃ𝙰𝙽𝚃 Ꭲ𝙾 Ꮠ𝙽𝚂𝚃𝙰𝙻𝙻"
            echo "❷ Ꮠ𝙽𝚂𝚃𝙰𝙻𝙻 Ꭺ𝙻𝙻 Ꭾ𝙰𝙲𝙺𝙰𝙶𝙴𝚂 Ꮮ𝙸𝚂𝚃𝙴𝙳 Ꭺ𝙱𝙾𝚅𝙴"
            echo "❸ Ᏼ𝙰𝙲𝙺"
            echo "❹ Ꭼ𝚇𝙸𝚃"
            echo "                                              "
            read -p "Ꮪ𝙴𝙻𝙴𝙲𝚃 Ꭺ𝙽 Ꭷ𝙿𝚃𝙸𝙾𝙽 (𝟷−𝟺): " dev_choice
            case $dev_choice in
            1)
                read -p "Ꭼ𝙽𝚃𝙴𝚁 Ꭾ𝙰𝙲𝙺𝙰𝙶𝙴 Ꮑ𝚄𝙼𝙱𝙴𝚁𝚂 Ꭲ𝙾 Ꮠ𝙽𝚂𝚃𝙰𝙻𝙻 (Ꭼ.Ꮐ., 𝟷 𝟸 𝟹): " selected_dev_pkg
                selected_dev_pkg=($selected_dev_pkg)
                if [[ "${selected_dev_pkg[*]}" == *"back"* ]]; then
                    break
                else
                    selected_dev_packages=()
                    for index in "${selected_dev_pkg[@]}"; do
                        selected_dev_packages+=("${dev_pkg[$((index-1))]}")
                    done
                    install_pkg "${selected_dev_packages[@]}"
                fi
                ;;
            2)
                # Combine all the dev pkgs 
                all_dev_packages="${dev_pkg[*]}"
                # Install all dev pkgs 
                yes | install_pkg $all_dev_packages
                ;;
            3)
                break
                ;;
            4)
                exit
                ;;
            *)
                echo -e "\e[1;91mᏐ𝙽𝚅𝙰𝙻𝙸𝙳 Ꭷ𝙿𝚃𝙸𝙾𝙽"
                ;;
            esac
        done
        ;;
    3)
        while true; do
            clear
            echo -e "\e[1;92mᏚ𝙴𝙲𝚄𝚁𝙸𝚃𝚈 Ꭾ𝙰𝙲𝙺𝙰𝙶𝙴𝚂"
            echo "-----------------"
            # Display the list of sec pkgs with numbers
            for i in "${!sec_pkg[@]}"; do
                echo "($((i+1))) ${sec_pkg[$i]}"
            done
            echo "----------------------"
            echo "                        "
            echo "❶ Ꮯ𝙷𝙾𝙾𝚂𝙴 Ꭾ𝙰𝙲𝙺𝙰𝙶𝙴𝚂 Ꭹ𝙾𝚄 Ꮃ𝙰𝙽𝚃 Ꭲ𝙾 Ꮠ𝙽𝚂𝚃𝙰𝙻𝙻"
            echo "❷ Ꮠ𝙽𝚂𝚃𝙰𝙻𝙻 Ꭺ𝙻𝙻 Ꭾ𝙰𝙲𝙺𝙰𝙶𝙴𝚂 Ꮮ𝙸𝚂𝚃𝙴𝙳 Ꭺ𝙱𝙾𝚅𝙴"
            echo "❸ Ᏼ𝙰𝙲𝙺"
            echo "❹ Ꭼ𝚇𝙸𝚃"
            echo "                                              "
            read -p "Ꮪ𝙴𝙻𝙴𝙲𝚃 Ꭺ𝙽 Ꭷ𝙿𝚃𝙸𝙾𝙽 (𝟷−𝟺): " sec_choice
            case $sec_choice in
            1)
                read -p "Ꭼ𝙽𝚃𝙴𝚁 Ꭾ𝙰𝙲𝙺𝙰𝙶𝙴 Ꮑ𝚄𝙼𝙱𝙴𝚁𝚂 Ꭲ𝙾 Ꮠ𝙽𝚂𝚃𝙰𝙻𝙻 (Ꭼ.Ꮐ., 𝟷 𝟸 𝟹): " selected_sec_pkg
                selected_sec_pkg=($selected_sec_pkg)
                if [[ "${selected_sec_pkg[*]}" == *"back"* ]]; then
                    break
                else
                    selected_sec_packages=()
                    for index in "${selected_sec_pkg[@]}"; do
                        selected_sec_packages+=("${sec_pkg[$((index-1))]}")
                    done
                    install_pkg "${selected_sec_packages[@]}"
                fi
                ;;
            2)
                # Combine all the sec pkgs 
                all_sec_packages="${sec_pkg[*]}"
                # Install all sec pkgs 
                yes | install_pkg $all_sec_packages
                ;;
            3)
                break
                ;;
            4)
                exit
                ;;
            *)
                echo -e "\e[1;91mᏐ𝙽𝚅𝙰𝙻𝙸𝙳 Ꭷ𝙿𝚃𝙸𝙾𝙽"
                ;;
            esac
        done
        ;;
    4)
        while true; do
            clear
            echo -e "\e[1;95mEditors"
            echo "-------"
            # Display the list of editors with numbers
            for i in "${!editors[@]}"; do
                echo "($((i+1))) ${editors[$i]}"
            done
            echo "----------------------"
            echo "                        "
            echo "❶ Ꮯ𝙷𝙾𝙾𝚂𝙴 𝙴𝙳𝙸𝚃𝙾𝚁𝚂 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝚃𝙾 𝙸𝙽𝚂𝚃𝙰𝙻𝙻"
            echo "❷ Ꮠ𝙽𝚂𝚃𝙰𝙻𝙻 Ꭺ𝙻𝙻 Ꭼ𝙳𝙸𝚃𝙾𝚁𝚂 Ꮮ𝙸𝚂𝚃𝙴𝙳 Ꭺ𝙱𝙾𝚅𝙴"
            echo "❸ Ᏼ𝙰𝙲𝙺"
            echo "❹ Ꭼ𝚇𝙸𝚃"
            echo "                                              "
            read -p "Ꮪ𝙴𝙻𝙴𝙲𝚃 Ꭺ𝙽 Ꭷ𝙿𝚃𝙸𝙾𝙽 (𝟷−𝟺): " editors_choice
            case $editors_choice in
            1)
                read -p "Ꭼ𝙽𝚃𝙴𝚁 Ꭼ𝙳𝙸𝚃𝙾𝚁 Ꮑ𝚄𝙼𝙱𝙴𝚁𝚂 Ꭲ𝙾 Ꮠ𝙽𝚂𝚃𝙰𝙻𝙻 (Ꭼ.Ꮐ., 𝟷 𝟸 𝟹): " selected_editors
                selected_editors=($selected_editors)
                if [[ "${selected_editors[*]}" == *"back"* ]]; then
                    break
                else
                    selected_editor_packages=()
                    for index in "${selected_editors[@]}"; do
                        selected_editor_packages+=("${editors[$((index-1))]}")
                    done
                    install_pkg "${selected_editor_packages[@]}"
                fi
                ;;
            2)
                # Combine all the editor pkgs
                all_editor_packages="${editors[*]}"
                # Install all editor pkgs 
                yes | install_pkg $all_editor_packages
                ;;
            3)
                break
                ;;
            4)
                exit
                ;;
            *)
                echo -e "\e[1;91mᏐ𝙽𝚅𝙰𝙻𝙸𝙳 Ꭷ𝙿𝚃𝙸𝙾𝙽"
                ;;
            esac
        done
        ;;
    5)
        while true; do
            clear
            echo -e "\e[1;93mCool Packages"
            echo "-------------"
            # Display the list of cool pkgs with numbers
            for i in "${!cool_pkg[@]}"; do
                echo "($((i+1))) ${cool_pkg[$i]}"
            done
            echo "----------------------"
            echo "                        "
            echo "❶ Ꮯ𝙷𝙾𝙾𝚂𝙴 Ꭾ𝙰𝙲𝙺𝙰𝙶𝙴𝚂 Ꭹ𝙾𝚄 Ꮃ𝙰𝙽𝚃 Ꭲ𝙾 Ꮠ𝙽𝚂𝚃𝙰𝙻𝙻"
            echo "❷ Ꮠ𝙽𝚂𝚃𝙰𝙻𝙻 Ꭺ𝙻𝙻 Ꭾ𝙰𝙲𝙺𝙰𝙶𝙴𝚂 Ꮮ𝙸𝚂𝚃𝙴𝙳 Ꭺ𝙱𝙾𝚅𝙴"
            echo "❸ Ᏼ𝙰𝙲𝙺"
            echo "❹ Ꭼ𝚇𝙸𝚃"
            echo "                                              "
            read -p "Ꮪ𝙴𝙻𝙴𝙲𝚃 Ꭺ𝙽 Ꭷ𝙿𝚃𝙸𝙾𝙽 (𝟷−𝟺): " cool_choice
            case $cool_choice in
            1)
                read -p "Ꭼ𝙽𝚃𝙴𝚁 Ꭾ𝙰𝙲𝙺𝙰𝙶𝙴 Ꮑ𝚄𝙼𝙱𝙴𝚁𝚂 Ꭲ𝙾 Ꮠ𝙽𝚂𝚃𝙰𝙻𝙻 (Ꭼ.Ꮐ., 𝟷 𝟸 𝟹): " selected_cool_pkg
                selected_cool_pkg=($selected_cool_pkg)
                if [[ "${selected_cool_pkg[*]}" == *"back"* ]]; then
                    break
                else
                    selected_cool_packages=()
                    for index in "${selected_cool_pkg[@]}"; do
                        selected_cool_packages+=("${cool_pkg[$((index-1))]}")
                    done
                    install_pkg "${selected_cool_packages[@]}"
                fi
                ;;
            2)
                # Combine all the cool pkgs 
                all_cool_packages="${cool_pkg[*]}"
                # Install all cool pkgs 
                yes | install_pkg $all_cool_packages
                ;;
            3)
                break
                ;;
            4)
                exit
                ;;
            *)
                echo -e "\e[1;91mᏐ𝙽𝚅𝙰𝙻𝙸𝙳 Ꭷ𝙿𝚃𝙸𝙾𝙽"
                ;;
            esac
        done
        ;;
    6)
        # Install all pkgs from all given sections
        all_packages=("${pkg[@]}" "${dev_pkg[@]}" "${sec_pkg[@]}" "${editors[@]}" "${cool_pkg[@]}")
        echo " "
        yes | install_pkg "${all_packages[@]}"
        ;;
    7)
        exit
        ;;
    *)
        echo -e "\e[1;91mᏐ𝙽𝚅𝙰𝙻𝙸𝙳 Ꭷ𝙿𝚃𝙸𝙾𝙽"
        ;;
    esac
done
