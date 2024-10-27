#!/usr/bin/python3
#
# macgen.py script to generate a MAC address for guests on various hypervisors
#!/usr/bin/python3
#
# macgen.py
# Script to generate random MAC addresses for virtual machine guests on various hypervisors.
#
# This script allows users to generate MAC addresses with prefixes specific to popular hypervisors
# (e.g., Xen, VMware, Hyper-V, VirtualBox, and KVM/QEMU). It also supports custom MAC prefixes.
#
# Features:
# - Interactive menu to select a hypervisor-specific MAC prefix.
# - Option to generate multiple MAC addresses in a single run.
# - Ability to specify a custom MAC prefix if the hypervisor is not listed.
# - Option to save the generated MAC addresses to a file.
# - Command-line arguments for flexible, non-interactive use.
#
# Usage Examples:
# - Interactive mode:
#     ./macgen.py
# - Command-line mode (generating 5 MACs for Xen and saving to a file):
#     ./macgen.py -c 5 -s output.txt
# - Command-line mode with a custom prefix:
#     ./macgen.py --custom 52:54:00 -c 3
#
# Arguments:
# - -c, --count: Specify the number of MAC addresses to generate (default is 1).
# - -s, --save: Specify a file name to save the generated MAC addresses.
# - --custom: Provide a custom MAC prefix in the format 'XX:XX:XX'.
#
# Author: Daniel SOl
# Date: 2024
# Git: https://git.com/szolll
#
# Note:
# Ensure that the custom MAC prefix follows the format 'XX:XX:XX' with valid hexadecimal values.
# The script will validate input and handle errors for invalid choices or formats.

import random
import argparse

# Hypervisor-specific MAC prefixes with brief descriptions
MAC_PREFIXES = {
    "Xen": ([0x00, 0x16, 0x3e], "Xen virtual machine"),
    "VMware": ([0x00, 0x50, 0x56], "VMware virtual machine"),
    "Hyper-V": ([0x00, 0x15, 0x5d], "Microsoft Hyper-V virtual machine"),
    "VirtualBox": ([0x08, 0x00, 0x27], "Oracle VirtualBox virtual machine"),
    "KVM/QEMU": ([0x52, 0x54, 0x00], "KVM/QEMU virtual machine")
}

def randomMAC(prefix):
    """
    Generates a random MAC address based on a given prefix.
    The first three octets are fixed, and the last three octets are randomly generated.
    """
    mac = prefix + [
        random.randint(0x00, 0x7f),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff)
    ]
    return ':'.join(f"{x:02x}" for x in mac)

def generate_mac_addresses(prefix, count):
    """Generates a specified number of MAC addresses with a given prefix."""
    return [randomMAC(prefix) for _ in range(count)]

def main():
    parser = argparse.ArgumentParser(description="Generate MAC addresses for virtual machine guests")
    parser.add_argument("-c", "--count", type=int, default=1, help="Number of MAC addresses to generate")
    parser.add_argument("-s", "--save", type=str, help="Save output to specified file")
    parser.add_argument("--custom", type=str, help="Enter a custom MAC prefix (e.g., '52:54:00')")
    
    args = parser.parse_args()

    # Display the menu if no custom prefix is provided
    if not args.custom:
        print("\nSelect the hypervisor for which to generate a MAC address:")
        for i, (hypervisor, (prefix, description)) in enumerate(MAC_PREFIXES.items(), start=1):
            print(f"  {i}. {hypervisor} - {description}")

        choice = input("\nEnter the number of your choice: ")
        try:
            choice = int(choice)
            hypervisor = list(MAC_PREFIXES.keys())[choice - 1]
            prefix = MAC_PREFIXES[hypervisor][0]
        except (ValueError, IndexError):
            print("Invalid choice. Please select a valid number from the menu.")
            return
    else:
        try:
            prefix = [int(x, 16) for x in args.custom.split(":")]
            if len(prefix) != 3:
                raise ValueError
        except ValueError:
            print("Invalid custom prefix. Please enter a valid prefix in the format 'XX:XX:XX'.")
            return

    # Generate the specified number of MAC addresses
    mac_addresses = generate_mac_addresses(prefix, args.count)
    print("\nGenerated MAC Addresses:")
    print("========================")
    for mac in mac_addresses:
        print(f"  {mac}")

    # Save to file if specified
    if args.save:
        with open(args.save, "w") as file:
            file.write("\n".join(mac_addresses) + "\n")
        print(f"\nMAC addresses saved successfully to '{args.save}'.")

if __name__ == "__main__":
    main()
