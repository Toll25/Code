#!/bin/bash

# function to perform recursive DNS queries
recursive_dns() {
    local domain=$1
    local nameserver=$2

    # perform the DNS query and extract the authoritative nameserver
    local ns=$(dig +noall +authority $domain @$nameserver | awk '/^'"$domain"'/ { print $5 }')

    # if there is no authoritative nameserver, exit
    if [ -z "$ns" ]; then
        return 1
    fi

    # perform the same query on the authoritative nameserver
    recursive_dns $domain $ns
}

# main function
main() {
    local domain=$1

    # get the root nameservers
    local roots=$(dig . NS +noall +answer | awk '{ print $5 }')

    # iterate over the root nameservers and perform recursive DNS queries
    for ns in $roots; do
        recursive_dns $domain $ns
    done
}

# run the script with a domain name as an argument
main $1
