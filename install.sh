#!/usr/bin/sh

if [ -z "$INSTALL_DIR" ]; then
    INSTALL_DIR="/usr/share/albert/org.albert.extension.python/modules/Todoist"
fi

install -Dm755 "__init__.py" "$INSTALL_DIR"/__init__.py
install -Dm666 "todoist.svg" "$INSTALL_DIR"/todoist.svg
printf "" > "$INSTALL_DIR"/todoist-key.api
chmod 0666 "$INSTALL_DIR"/todoist-key.api