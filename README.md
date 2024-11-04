# xploitheb64

is a powerful tool designed for security professionals, ethical hackers, and developers to test for vulnerabilities such as XSS, HTML injection, and other code execution flaws. With this tool, you can easily generate payloads encoded in Base64, which can be used to probe for weaknesses in web applications and services. The tool streamlines the process of creating and embedding payloads in requests, helping you identify potential security risks related to unsafe handling of image data. Whether you're conducting penetration tests or experimenting with attack vectors, XploiTheB64 offers a quick and efficient way to generate encoded payloads for your security assessments.

# Features
It's comes with several essential features designed to streamline the process of generating Base64-encoded payloads from files with custom payloads, specifically for testing vulnerabilities like XSS and HTML injection.

## File Input Option
`(-f or --file)`
This feature allows you to specify the path to the file with your custom payloads that you want to convert to a Base64-encoded payload. Making it flexible for a wide range of use cases.

## Output File Option
`(-o or --output)`
After generating the Base64 payload, this option lets you define the path where the output will be saved. You can easily direct the encoded payload to a specific file for further testing or sharing in your security assessments.

These features ensure that you can quickly encode and manage output with ease, offering a simple command-line interface that enhances productivity in vulnerability testing.

```
usage: pay_img_b64.py [-h] [-f FILE] [-o OUTPUT]

XploiTheB64

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Path to the file
  -o OUTPUT, --output OUTPUT
                        Path to save the file
```
# Usage
`python3 xploitheb64.py`

or

`python3 xploitheb64.py -f filewithpayload.txt`

or 

`python3 xploitheb64.py -f filewithpayload.txt -o output.txt`


