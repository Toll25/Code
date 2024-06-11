#!/usr/bin/env bash
curl -X POST -H "Content-Type: application/lisp" -d '(:template-supplied-p t
    :template "Hello, {NAME} {*flag*}! The flag is {flag}"
    :substitutions ((:NAME . "(print *flag*)John")
                    (:flag . "*flag*")))' http://fuperfiberneticinterpolator.challs.open.ecsc2024.it/interpolate