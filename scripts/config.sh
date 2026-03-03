#!/bin/bash

menu() {
    clear
    echo "REVERSE SHELL"
    echo "-------------------"
    echo "1. Instalar requisitos"
    echo "2. Configurar reverse shell"
    echo "3. Salir"
    echo "-------------------"
    read -p "Seleccione una opcion: " choice

    case $choice in
        1)
            echo "Instalando requisitos..."
            pip install pyinstaller
            pip install auto-py-to-exe
            echo "Requisitos instalados correctamente."
            read -p "Presione Enter para continuar..."
            menu
            ;;
        2)
            echo "Abriendo Visual Studio Code..."
            code &
            read -p "Presione Enter para continuar..."
            auto-py-to-exe
            menu
            ;;
        3)
            echo "Saliendo..."
            exit 0
            ;;
        *)
            echo "Opción no válida. Por favor, seleccione una opción válida."
            read -p "Presione Enter para continuar..."
            menu
            ;;
    esac
}

menu
