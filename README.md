# MacGen_Tool
Generate MAC addresses specifically for hypervisors.

# MAC Address Generator for Virtual Machine Guests

`macgen_tool.py` is a Python script for generating random MAC addresses for virtual machine guests on various hypervisors. The script supports prefixes specific to popular hypervisors (Xen, VMware, Hyper-V, VirtualBox, and KVM/QEMU) and allows for custom MAC prefixes.

## Features

- Interactive menu to select a hypervisor-specific MAC prefix.
- Option to generate multiple MAC addresses in a single run.
- Ability to specify a custom MAC prefix if the hypervisor is not listed.
- Option to save the generated MAC addresses to a file.
- Command-line arguments for flexible, non-interactive use.

## Requirements

- Python 3.x

## Usage

You can use the script interactively or via command-line arguments for non-interactive use.

### Interactive Mode

Simply run the script and follow the on-screen prompts:

```
./macgen_tool.py
```

## Command-Line Arguments
The script accepts the following command-line arguments:

-c, --count : Specify the number of MAC addresses to generate (default is 1).
-s, --save : Specify a file name to save the generated MAC addresses.
--custom : Provide a custom MAC prefix in the format XX:XX:XX.

### Examples
Generate 1 MAC address in interactive mode:

```
./macgen_tool.py
```

Generate 5 MAC addresses for a specific hypervisor (e.g., Xen) and save them to a file:

```
./macgen_tool.py -c 5 -s output.txt
```

Generate 3 MAC addresses with a custom prefix:

```
./macgen_tool.py --custom 52:54:00 -c 3
```
The script outputs generated MAC addresses in the format XX:XX:XX:XX:XX:XX. If saving to a file, it will save each MAC address on a new line.

## Notes
Ensure that any custom MAC prefix follows the format XX:XX:XX with valid hexadecimal values.
The script validates input and handles errors for invalid choices or formats.
